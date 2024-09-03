import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

def load_data(file_path):
    data = pd.read_csv(file_path)
    return data

def clean_data(data):
    data.dropna(inplace=True)
    return data

def feature_engineering(data):
    data['price_moving_avg'] = data['price'].rolling(window=3).mean()
    return data

def preprocess_data(data):
    features = data.drop(columns=['price'])
    target = data['price']
    
    scaler = StandardScaler()
    features_scaled = scaler.fit_transform(features)
    
    return features_scaled, target

def split_data(X, y, test_size=0.2, random_state=42):
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=test_size, random_state=random_state)
    return X_train, X_test, y_train, y_test

if __name__ == "__main__":
    data = load_data('data/raw/raw_data.csv')
    data = clean_data(data)
    data = feature_engineering(data)
    X, y = preprocess_data(data)
    X_train, X_test, y_train, y_test = split_data(X, y)
    pd.DataFrame(X_train).to_csv('data/processed/X_train.csv', index=False)
    pd.DataFrame(X_test).to_csv('data/processed/X_test.csv', index=False)
    pd.DataFrame(y_train).to_csv('data/processed/y_train.csv', index=False)
    pd.DataFrame(y_test).to_csv('data/processed/y_test.csv', index=False)
