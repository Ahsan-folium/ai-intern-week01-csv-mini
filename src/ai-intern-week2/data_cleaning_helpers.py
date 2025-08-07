import pandas as pd

def fill_age_with_mean(df):
    df['Age'] = df['Age'].fillna(df['Age'].mean())
    return df

def fill_embarked_with_mode(df):
    df['Embarked'] = df['Embarked'].fillna(df['Embarked'].mode()[0])
    return df

def drop_missing_cabin(df):
    return df.dropna(subset=['Cabin'])

def encode_sex(df):
    df['Sex'] = df['Sex'].map({'male': 0, 'female': 1})
    return df

def encode_embarked_onehot(df):
    dummies = pd.get_dummies(df['Embarked'], drop_first=True).astype(int)
    df = pd.concat([df.drop('Embarked', axis=1), dummies], axis=1)
    return df