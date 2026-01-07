from dagster import DefaultScheduleStatus

from dagster_dbt import build_schedule_from_dbt_selection

from .assets import dagster_jaffleshop_dbt_assets

schedules = [
    build_schedule_from_dbt_selection(
        [dagster_jaffleshop_dbt_assets],
        job_name="materialize_dbt_models",
        cron_schedule="0 13 * * *",
        default_status=DefaultScheduleStatus.RUNNING,
        dbt_select="+customers +orders",
    ),
]