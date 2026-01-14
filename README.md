<div align="center">

![Cyclelytics Logo](docs/assets/Cyclelytics.png)

</div>

# Cyclelytics
Turn bike-share data into trustworthy insights with lightweight cloud pipelines and dashboards.

## What is Cyclelytics?
Cyclelytics is a data and analytics starter for bike-share systems. Inspired by public mobility analytics projects like NYC Citi Bike reports and Chicago Divvy data deep-dives, it wraps modern extract-transform-load (ETL) patterns with a clear place to stage dashboards and documentation.

## Highlights
- End-to-end flow: extract raw trip data, transform for quality and usability, and load curated tables ready for BI.
- Readable modular code: `src/extract`, `src/transform`, and `src/load` mirror the pipeline stages.
- Future dashboards: reserved gallery space for KPI snapshots, route maps, and trend visuals.
- Docs-first mindset: architecture notes and screenshots live in `docs/` to keep data decisions transparent.

## Repository Layout
- `main.py` – orchestration entrypoint for running the pipeline.
- `config.py` – central configuration for sources, destinations, and toggles.
- `src/extract/` – pull raw datasets (e.g., bike trips, station metadata).
- `src/transform/` – clean, enrich, and aggregate for reporting.
- `src/load/` – write curated outputs to your warehouse, lake, or local files.
- `docs/` – architecture notes, design decisions, and (future) screenshots.
- `docs/dashboard_images/` – placeholder folder for dashboard captures.

## Getting Started
1) **Prerequisites**: Python 3.9+ and pip.
2) **Install dependencies**: `pip install -r requirements.txt`
3) **Configure**: update `config.py` with source locations (local paths or cloud buckets) and destinations.
4) **Run the pipeline**: `python main.py`

## Pipeline Overview
- **Extract**: ingest raw trips and station reference data into a landing zone.
- **Transform**: standardize timestamps, compute trip durations, derive demand features, and build station/day aggregates.
- **Load**: publish curated tables for BI tools (CSV/parquet or warehouse tables, depending on `config.py`).

## Dashboard Showcase (coming soon)
- Add snapshots to `docs/dashboard_images/` (e.g., `dashboard_images/ridership_trends.png`).
- Reference them here once available:
	- Daily ridership trends – _pending screenshot_
	- Peak-hour utilization map – _pending screenshot_
	- Station reliability scorecard – _pending screenshot_

## Documentation Screenshots (coming soon)
- Use `docs/` for architecture diagrams, sequence charts, or modeling notes.
- Current capture:
  ![High-level architecture](docs/architecture/Cyclelytics.png)
- Add more captures like sequence diagrams or data model glossaries in `docs/` and link them here.

## Roadmap
- Add sample datasets and a reproducible demo run.
- Wire a simple warehouse target (e.g., DuckDB, Postgres, or BigQuery).
- Publish starter SQL for BI models.
- Ship a starter dashboard (Power BI, Looker, or Superset) and link images above.

## References and Inspiration
- Citi Bike public data explorations (NYC Open Data community)
- Chicago Divvy system analytics (Divvy open data community)
- Modern data stack ETL patterns from open-source mobility projects

## Contributing
Issues and pull requests are welcome. Feel free to propose new transforms, loaders, or dashboard ideas that showcase operational and rider experience insights.
