# Map System

This folder stores the geospatial roadmap for the project.

## Main Goal

Build Steven's timeline into map-ready data without inventing geography.

## Google Maps / Google My Maps Workflow

Google My Maps can import CSV, KML, KMZ, or GeoJSON-like data depending on workflow. This project generates:

```text
maps/google_my_maps_import.csv
maps/locations.kml
maps/locations.geojson
```

Use these files to import approved timeline/location points into Google My Maps.

## Important

Google Maps JavaScript API requires an API key and billing setup. We do **not** put API keys into this public repository.

Instead, this project uses:

1. map export files for Google My Maps import;
2. a static `web/map.html` page;
3. optional future map rendering from approved coordinates.

## Location Approval Rule

Only add coordinates when Steven approves the location and source.
