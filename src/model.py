import pandas as pd
from statsmodels.tsa.statespace.sarimax import SARIMAX
import joblib
import os

def load_data(file_path):
    # Check if file exists
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"File not found: {file_path}")
    
    # Load the data
    data = pd.read_csv(file_path, parse_dates=['Date'], index_col='Date')
    return data

def train_sarima_model(data, order, seasonal_order):
    model = SARIMAX(data, order=order, seasonal_order=seasonal_order, enforce_stationarity=False, enforce_invertibility=False)
    sarima_model = model.fit(disp=False)
    return sarima_model

def save_model(model, output_path):
    # Save the trained SARIMA model to disk
    joblib.dump(model, output_path)

if __name__ == "__main__":
    # Dynamically construct the paths based on the current script location
    current_dir = os.path.dirname(os.path.abspath(__file__))
    processed_data_path = os.path.join(current_dir, '..', 'data', 'processed_data.csv')
    model_output_path = os.path.join(current_dir, '..', 'models', 'sarima_model.pkl')

    # Load the processed data
    try:
        data = load_data(processed_data_path)
    except FileNotFoundError as e:
        print(e)
        exit()

    # Train the SARIMA model using the processed data
    sarima_model = train_sarima_model(data['Price'], order=(1, 1, 1), seasonal_order=(1, 1, 1, 12))

    # Save the trained SARIMA model
    save_model(sarima_model, model_output_path)
    print(f"Model saved successfully to {model_output_path}")
