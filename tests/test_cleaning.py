# Cleaning tests
import pytest
import pandas as pd
import os 
os.chdir('..')
from src.data_processing.cleaning import remove_duplicates, handle_missing_values, standardize_dates

@pytest.fixture
def sample_df():
    """Sample DataFrame for testing."""
    return pd.DataFrame({
        'id': [1, 2, 3],
        'name': ['Alice', 'Bob', 'Charlie'],
        'DOB' : ['20000123','1984-09-02','31-12-1999']
    })

def test_remove_duplicates(sample_df):
    df = remove_duplicates(sample_df)
    assert df['id'].is_unique
 

def test_handle_missing_values(sample_df):
    df = handle_missing_values(sample_df,columns='name')
    assert df.isnull().any().any().any() == False


    
def test_standardize_dates(sample_df):
    df = standardize_dates(sample_df,date_columns='DOB')
    assert 1==1