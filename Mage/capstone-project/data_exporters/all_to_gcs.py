from mage_ai.settings.repo import get_repo_path
from mage_ai.io.config import ConfigFileLoader
from mage_ai.io.google_cloud_storage import GoogleCloudStorage
from pandas import DataFrame
from os import path

if 'data_exporter' not in globals():
    from mage_ai.data_preparation.decorators import data_exporter


@data_exporter
def export_data_to_google_cloud_storage(df, **kwargs) -> None:
    """
    Template for exporting data to a Google Cloud Storage bucket.
    Specify your configuration settings in 'io_config.yaml'.

    Docs: https://docs.mage.ai/design/data-loading#googlecloudstorage
    """
    config_path = path.join(get_repo_path(), 'io_config.yaml')
    config_profile = 'default'
    '''
    repeat process by changing country to 
    country_social_economic_year,
    countrycode,
    population,
    suicide_data
    '''
    tablename = 'suicide_data'
    bucket_name = 'dzc_capstone_412212'
    object_key = f"{tablename}.parquet"

    GoogleCloudStorage.with_config(ConfigFileLoader(config_path, config_profile)).export(
                df,
                bucket_name,
                object_key,
            )

    