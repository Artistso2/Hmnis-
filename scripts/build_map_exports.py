#!/usr/bin/env python3
"""Build KML, GeoJSON, and Google My Maps CSV from maps/locations.csv."""
from __future__ import annotations

import csv
import html
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MAPS = ROOT / "maps"
WEB_DATA = ROOT / "web" / "data"
LOCATIONS = MAPS / "locations.csv"


def has_coords(row: dict) -> bool:
    try:
        float(row.get("latitude", ""))
        float(row.get("longitude", ""))
        return True
    except ValueError:
        return False


def main() -> None:
    rows = list(csv.DictReader(LOCATIONS.open(encoding="utf-8")))
    features = []
    for row in rows:
        if not has_coords(row):
            continue
        lat = float(row["latitude"])
        lon = float(row["longitude"])
        features.append({
            "type": "Feature",
            "geometry": {"type": "Point", "coordinates": [lon, lat]},
            "properties": {k: v for k, v in row.items() if k not in {"latitude", "longitude"}}
        })

    geojson = {"type": "FeatureCollection", "features": features}
    for path in [MAPS / "locations.geojson", WEB_DATA / "locations.geojson"]:
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(json.dumps(geojson, indent=2), encoding="utf-8")

    # KML
    placemarks = []
    for row in rows:
        if not has_coords(row):
            continue
        name = html.escape(row.get("label", "Untitled"))
        description = html.escape(row.get("address_or_description", ""))
        lon = row["longitude"]
        lat = row["latitude"]
        placemarks.append(f"""
    <Placemark>
      <name>{name}</name>
      <description>{description}</description>
      <Point><coordinates>{lon},{lat},0</coordinates></Point>
    </Placemark>""")
    kml = f'''<?xml version="1.0" encoding="UTF-8"?>
<kml xmlns="http://www.opengis.net/kml/2.2">
  <Document>
    <name>HELLO, MY NAME IS STEVEN — Approved Timeline Locations</name>
    <description>Generated from author-approved locations only. No invented coordinates.</description>{''.join(placemarks)}
  </Document>
</kml>
'''
    (MAPS / "locations.kml").write_text(kml, encoding="utf-8")

    # Google My Maps CSV
    out = MAPS / "google_my_maps_import.csv"
    with out.open("w", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=[
            "Name", "Description", "Address", "Latitude", "Longitude", "Start Date", "End Date",
            "Timeline Layer", "Source ID", "Evidence Label", "Verification Status"
        ])
        writer.writeheader()
        for row in rows:
            writer.writerow({
                "Name": row.get("label", ""),
                "Description": row.get("notes", "") or row.get("address_or_description", ""),
                "Address": row.get("address_or_description", ""),
                "Latitude": row.get("latitude", ""),
                "Longitude": row.get("longitude", ""),
                "Start Date": row.get("start_date", ""),
                "End Date": row.get("end_date", ""),
                "Timeline Layer": row.get("location_type", ""),
                "Source ID": row.get("source_id", ""),
                "Evidence Label": row.get("evidence_label", ""),
                "Verification Status": row.get("verification_status", ""),
            })
    print(f"Wrote {len(features)} mapped features and {len(rows)} My Maps rows.")


if __name__ == "__main__":
    main()
