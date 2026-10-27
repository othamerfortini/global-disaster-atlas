import unittest

from scripts.critical_impact_audit import audit
from scripts.quality_score import quality_score
from scripts.validate_canonical import validate_events


def event_with_impact(impact):
    return {
        "event_id": "test-event",
        "name": "Test event",
        "event_class": "natural_hazard",
        "hazard": {"type": "flood"},
        "time": {"start": "2025-01-01T00:00:00Z", "precision": "day"},
        "location": {"latitude": 1.0, "longitude": 2.0, "spatial_precision": "point"},
        "sources": [{"name": "Test source", "url": "https://example.com/source"}],
        "impact": impact,
    }


class EconomicImpactSchemaAlignmentTests(unittest.TestCase):
    def test_audit_counts_canonical_economic_damage(self):
        dataset = {"events": [event_with_impact({
            "economic": {"damage": {"amount": 1250000, "currency": "USD", "year": 2025, "status": "reported"}}
        })]}
        self.assertEqual(audit(dataset)["coverage"]["economic"]["covered_events"], 1)

    def test_audit_counts_canonical_reconstruction_needs(self):
        dataset = {"events": [event_with_impact({
            "economic": {"reconstruction_needs": {"amount": 400000, "currency": "EUR", "status": "estimated"}}
        })]}
        self.assertEqual(audit(dataset)["coverage"]["economic"]["covered_events"], 1)

    def test_audit_keeps_legacy_economic_loss_compatibility(self):
        dataset = {"events": [event_with_impact({
            "economic_loss": {"amount": 300000, "currency": "USD", "status": "reported"}
        })]}
        self.assertEqual(audit(dataset)["coverage"]["economic"]["covered_events"], 1)

    def test_quality_score_recognizes_canonical_economic_fields(self):
        event = event_with_impact({
            "economic": {"loss": {"amount": 50000, "currency": "EUR", "status": "reported"}}
        })
        without_economic = event_with_impact({})
        self.assertGreater(quality_score(event), quality_score(without_economic))

    def test_validator_accepts_canonical_economic_amount_with_source(self):
        event = event_with_impact({
            "economic": {"damage": {"amount": 1250000, "currency": "USD", "year": 2025, "status": "reported"}}
        })
        self.assertEqual(validate_events([event]), [])

    def test_validator_flags_known_economic_field_without_amount(self):
        event = event_with_impact({
            "economic": {"loss": {"currency": "EUR", "status": "estimated"}}
        })
        self.assertTrue(any("economic.loss status is known but amount is absent" in error
                            for error in validate_events([event])))

    def test_validator_rejects_boolean_economic_amount(self):
        event = event_with_impact({
            "economic": {"damage": {"amount": True, "currency": "USD", "status": "reported"}}
        })
        self.assertTrue(any("amount must be a finite non-negative number" in error
                            for error in validate_events([event])))

    def test_validator_rejects_negative_economic_amount(self):
        event = event_with_impact({
            "economic": {"loss": {"amount": -1, "currency": "EUR", "status": "reported"}}
        })
        self.assertTrue(any("amount must be a finite non-negative number" in error
                            for error in validate_events([event])))

    def test_validator_rejects_string_economic_amount(self):
        event = event_with_impact({
            "economic": {"combined": {"amount": "500", "currency": "EUR", "status": "reported"}}
        })
        self.assertTrue(any("amount must be a finite non-negative number" in error
                            for error in validate_events([event])))


if __name__ == "__main__":
    unittest.main()
