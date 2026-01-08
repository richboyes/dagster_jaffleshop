## Dagster/DBT Jaffle Shop Snowflake ❄️ Project 

[![Serverless Prod Deployment](https://github.com/richboyes/dagster_jaffleshop/actions/workflows/deploy.yml/badge.svg)](https://github.com/richboyes/dagster_jaffleshop/actions/workflows/deploy.yml)

Basic project to ingest fictional jaffle shop data from DBT and create basic data pipelines that ingests data to snowflake,
using Dagster cloud and [DBT](https://www.getdbt.com/). Information about the data the transformations can be seen in the DBT [README](./dbt/README.md)

Currently deployed Dagster Cloud at https://admiral-pioneer-poc.eu.dagster.plus/ using github actions at https://github.com/richboyes/dagster_jaffleshop/actions, also see [deploy.yml](.github/workflows/deploy.yml).

DBT documents for the project are generated at: https://richboyes.github.io/dagster_jaffleshop

On our instance of [snowflake ❄️](https://app.snowflake.com/admiralpioneer/toolbox/#/homepage) the data can be seen in the `sandbox_db.jaffle_shop` schema.

This is a test.

### Pre-requisites to run locally

- Install uv using their [official documentation](https://docs.astral.sh/uv/getting-started/installation/)
- Synchronise the virtual environment: 
  ```bash
  uv sync --extra dev
  ```
- Use the virtual environment:
  ```bash
  source .venv/bin/activate
  ```
- Create the following environment variables:
  ```bash
  export SNOWFLAKE_PRIVATE_KEY=$(cat /path/to/rsa_key.private)
  ```

### Running Dagster locally

- Scaffold the project:
  ```bash
  dagster-dbt project prepare-and-package --file src/dagster_jaffleshop/project.py
  ```
- Run the webserver:
  ```bash
  dagster dev -m dagster_jaffleshop.definitions
  ```

### Running the unit tests

- Synchronise the virtual environment: 
  ```bash
  uv sync --extra dev
  ```
- Use the virtual environment:
  ```bash
  source .venv/bin/activate
  ```
- Run the unit tests:
  ```bash
  pytest tests
  ```

### Running DBT Locally

You may wish to run DBT locally, which will execute the DAG on Snowflake directly:
```bash
uv sync --extra dev
source ./.venv/bin/activate
cd ./dbt
dbt deps
dbt build
```
