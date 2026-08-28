# Initial Architecture

## Principle

Keep the MVP modular but simple. The data model and provenance layer are more important than frontend complexity.

```text
Public/approved sources
        |
        v
   Source adapters
        |
        v
 Raw observations (outside repo when redistribution is restricted)
        |
        v
 Normalization + entity resolution
        |
        v
 Canonical event model
        |
        +--> provenance
        +--> uncertainty
        +--> relationships
        +--> quality score
        |
        v
 PostgreSQL + PostGIS
        |
        v
 API
        |
        v
 Next.js web application
```

## Proposed stack

- Python for ingestion and data-quality tooling.
- PostgreSQL + PostGIS for canonical storage and geospatial queries.
- Next.js + TypeScript for the web application.
- MapLibre or an equivalent map renderer for the initial map UI.

## Non-goals for Phase 0

- no microservices;
- no Kubernetes;
- no mobile application;
- no authentication/payment system;
- no predictive disaster claims;
- no large media archive;
- no proprietary dataset dependency.
