# Cleaning tests
import pytest
import pandas as pd
 
@pytest.fixture
def sample_df():
    """Sample DataFrame for testing."""
    return pd.DataFrame({
        'id': [1, 2, 3,3],
        'name': ['Alice', 'Bob', 'Charlie','Ian']
    })

def test_remove_duplicates(sample_df):
    assert sample_df['id'].is_unique
 