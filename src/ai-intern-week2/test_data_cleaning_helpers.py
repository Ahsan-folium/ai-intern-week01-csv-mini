import pandas as pd
from data_cleaning_helpers import fill_age_with_mean, fill_embarked_with_mode, drop_missing_cabin, encode_sex

def test_fill_age_with_mean():
    # create a test df with some missing ages
    df = pd.DataFrame({'Age': [22, None, 30]})
    df_clean = fill_age_with_mean(df.copy())
    assert df_clean['Age'].isnull().sum() == 0

def test_fill_embarked_with_mode():
    df = pd.DataFrame({'Embarked': ['S', None, 'S', 'C']})
    df_clean = fill_embarked_with_mode(df.copy())
    assert df_clean['Embarked'].isnull().sum() == 0

def test_drop_missing_cabin():
    df = pd.DataFrame({'Cabin': ['C85', None, 'E46']})
    df_clean = drop_missing_cabin(df.copy())
    assert df_clean.shape[0] == 2

def test_encode_sex():
    df = pd.DataFrame({'Sex': ['male', 'female', 'female']})
    df_clean = encode_sex(df.copy())
    assert set(df_clean['Sex'].unique()) <= {0, 1}
