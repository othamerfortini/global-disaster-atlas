# Licensing Policy

This project must distinguish between **accessibility** and **redistribution rights**.

## Rules

- Never commit a raw third-party dataset to this repository unless its license explicitly permits it.
- Never treat an API being publicly reachable as permission to redistribute its contents.
- Store source name, source record ID, source URL, retrieval timestamp and applicable license metadata for every imported source record.
- Keep proprietary/restricted source data outside the public repository.
- For DesInventar, verify rights at the individual database/contributor level.
- For EM-DAT, obtain and document commercial licensing before incorporating restricted data into a commercial production dataset.
- For USGS/NOAA/GDACS, verify the notice for the exact dataset/API endpoint and retain required attribution.

## Development approach

The first MVP should be capable of operating on openly reusable sources and should not depend on EM-DAT.

## Open question

Before production launch, perform a legal/license review of every source and every field that will be redistributed through the Atlas API or UI.
