from dagster import AssetSelection, define_asset_job
from ..partitions import monthly_partitions, weekly_partitions

trips_by_week = AssetSelection.assets("trips_by_week")

trip_update_job = define_asset_job(
    name="trip_update_job",
    partitions_def=monthly_partitions,
    selection=AssetSelection.all() - trips_by_week
)

weekly_update_job = define_asset_job(
    name="weekly_update_job",
    partitions_def=weekly_partitions,
    selection=trips_by_week
)


