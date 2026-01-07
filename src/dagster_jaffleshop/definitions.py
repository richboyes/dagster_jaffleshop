from dagster import Definitions
from dagster_dbt import DbtCliResource
from .assets import dagster_jaffleshop_dbt_assets
from .project import dagster_jaffleshop_project
from .schedules import schedules

defs = Definitions(
    assets=[dagster_jaffleshop_dbt_assets],
    schedules=schedules,
    resources={
        "dbt": DbtCliResource(project_dir=dagster_jaffleshop_project),
    },
)

