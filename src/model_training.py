import pandas as pd
from sklearn.ensemble import RandomForestRegressor
import joblib

def load_data():
    X_train = pd.read_csv('data/processed/X_train.csv')
    y_train = pd.read_csv('data/processed/y_train.csv')
    return X_train, y_train

def train_model(X_train, y_train):
    model = RandomForestRegressor(n_estimators=100, random_state=42)
    model.fit(X_train, y_train.values.ravel())
    return model

def save_model(model, file_path='models/final_model.pkl'):
    joblib.dump(model, file_path)

if __name__ == "__main__":
    X_train, y_train = load_data()
    model = train_model(X_train, y_train)
    save_model(model)
