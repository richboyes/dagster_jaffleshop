## Dagster/DBT Jaffle Shop Snowflake ❄️ Project 

[![Serverless Prod Deployment](https://github.com/richboyes/dagster_jaffleshop/actions/workflows/deploy.yml/badge.svg)](https://github.com/richboyes/dagster_jaffleshop/actions/workflows/deploy.yml)

Basic project to ingest fictional jaffle shop data from DBT and create basic data pipelines that ingests data to snowflake,
using Dagster cloud and [DBT](https://www.getdbt.com/).

Currently deployed to https://admiral-pioneer-poc.eu.dagster.plus/

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

### Dagster Cloud

See github actions under https://github.com/richboyes/dagster_jaffleshop/actions for deployment to Dagster cloud, also see [deploy.yml](.github/workflows/deploy.yml).


### Running DBT Locally

You may wish to run DBT locally, which will execute the DAG on Snowflake directly:
```bash
uv sync --extra dev
source ./.venv/bin/activate
cd ./dbt
dbt deps
dbt build
```
