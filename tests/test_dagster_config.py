from dagster import DefaultScheduleStatus
from dagster_jaffleshop.assets import dagster_jaffleshop_dbt_assets
from dagster_jaffleshop.definitions import defs
from dagster_jaffleshop.project import repo_project_dir, dagster_jaffleshop_project
from dagster_jaffleshop.schedules import schedules

def test_schedule_config():
    schedule = schedules[0]
    assert schedule.cron_schedule == "0 13 * * *"
    assert schedule.default_status == DefaultScheduleStatus.RUNNING


def test_definitions_wire_assets_and_resources():
    asset_graph = defs.resolve_asset_graph()
    asset_groups = {a.group_name for a in asset_graph.asset_nodes}
    assert "dagster_jaffleshop" in asset_groups
    asset_key_names = {a.key.path[-1] for a in asset_graph.asset_nodes}
    assert set(["customers", "orders"]).issubset(asset_key_names)
