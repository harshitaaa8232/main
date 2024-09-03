import pandas as pd
from sklearn.metrics import mean_absolute_error, mean_squared_error
import joblib

def load_data():
    X_test = pd.read_csv('data/processed/X_test.csv')
    y_test = pd.read_csv('data/processed/y_test.csv')
    return X_test, y_test

def load_model(file_path='models/final_model.pkl'):
    model = joblib.load(file_path)
    return model

def evaluate_model(model, X_test, y_test):
    predictions = model.predict(X_test)
    mae = mean_absolute_error(y_test, predictions)
    mse = mean_squared_error(y_test, predictions)
    print(f'MAE: {mae}')
    print(f'MSE: {mse}')
    return mae, mse

if __name__ == "__main__":
    X_test, y_test = load_data()
    model = load_model()
    evaluate_model(model, X_test, y_test)
