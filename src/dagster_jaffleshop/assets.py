from typing import Any, Mapping
from dagster import AssetExecutionContext
from dagster_dbt import DagsterDbtTranslator, DbtCliResource, dbt_assets

from .project import dagster_jaffleshop_project

class CustomDagsterDbtTranslator(DagsterDbtTranslator):
    def get_group_name(self, dbt_resource_props: Mapping[str, Any]) -> str | None:
        return "dagster_jaffleshop"

@dbt_assets(
    manifest=dagster_jaffleshop_project.manifest_path,
    dagster_dbt_translator=CustomDagsterDbtTranslator()
)
def dagster_jaffleshop_dbt_assets(context: AssetExecutionContext, dbt: DbtCliResource):
    yield from dbt.cli(["build"], context=context).stream()
    

