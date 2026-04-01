# Cleaning tests
import pytest
import pandas as pd
import os 
import re

os.chdir('..')
from src.data_processing.cleaning import remove_duplicates, handle_missing_values, standardize_dates

@pytest.fixture
def sample_df():
    """Sample DataFrame for testing."""
    return pd.DataFrame({
        'id': [1, 2, 3],
        'name': ['Alice', 'Bob', 'Charlie'],
        'DOB' : ['2000-01-23','1984-09-02','1999-12-31']
    })

def test_remove_duplicates(sample_df):
    df = remove_duplicates(sample_df)
    assert df['id'].is_unique
 

def test_handle_missing_values(sample_df):
    df = handle_missing_values(sample_df,columns='name')
    assert df.isnull().any().any().any() == False


    
def test_standardize_dates(sample_df):
    df = standardize_dates(sample_df,date_columns=['DOB'])
    for x in df['DOB']:
        assert re.match(r'^\d{4}-\d{2}-\d{2}$', x) 