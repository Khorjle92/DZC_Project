from mage_ai.io.file import FileIO
import pandas as pd
import os
if 'data_loader' not in globals():
    from mage_ai.data_preparation.decorators import data_loader
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test


@data_loader
def load_data_from_file(*args, **kwargs):
    """
    Template for loading data from filesystem.
    Load data from 1 file or multiple file directories.

    For multiple directories, use the following:
        FileIO().load(file_directories=['dir_1', 'dir_2'])

    Docs: https://docs.mage.ai/design/data-loading#fileio
    """
    '''
    repeat process by changing country to 
    country_social_economic_year,
    countrycode,
    population,
    suicide_data
    '''
    tablename = 'suicide_data'
    filepath = f"/home/src/dataset/{tablename}.csv"
    
 
   
    return pd.read_csv(filepath)



