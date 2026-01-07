# Agent Notes

Basic guidance for assistants working in this repository.

## Project Snapshot

- Purpose: Dagster + dbt pipeline for TPCH data in Snowflake.
- Key dirs: `src/` (python package), `dbt/` (dbt project).
- Entry points: `src/dagster_jaffleshop/definitions.py`, `src/dagster_jaffleshop/project.py`.

## Local Development

- Sync venv: `uv sync --extra dev`
- Activate: `source .venv/bin/activate`
- Set env vars:
  - `SNOWFLAKE_PRIVATE_KEY=XXXX`
- Scaffold Dagster/dbt project:
  - `dagster-dbt project prepare-and-package --file src/dagster_jaffleshop/project.py`
- Run Dagster:
  - `dagster dev -m dagster_jaffleshop.definitions`

## Tests

- `pytest tests`

## Notes

- Deployment uses GitHub Actions workflow at `.github/workflows/deploy.yml`.
