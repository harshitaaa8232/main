import pandas as pd
import matplotlib.pyplot as plt
import joblib
import os

def load_data(file_path):
    # Check if file exists
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"File not found: {file_path}")
    
    # Load the data
    data = pd.read_csv(file_path, parse_dates=['Date'], index_col='Date')
    return data

def load_model(model_path):
    if not os.path.exists(model_path):
        raise FileNotFoundError(f"Model file not found: {model_path}")
    
    # Load the saved model
    return joblib.load(model_path)

def plot_predictions(test_data, predictions):
    plt.figure(figsize=(10, 6))
    plt.plot(test_data.index, test_data, label='Actual Prices')
    plt.plot(test_data.index, predictions, label='Predicted Prices', linestyle='--')
    plt.title('Actual vs Predicted Prices')
    plt.xlabel('Date')
    plt.ylabel('Price')
    plt.legend()
    plt.show()

if __name__ == "__main__":
    # Dynamically construct the paths based on script location
    current_dir = os.path.dirname(os.path.abspath(__file__))
    processed_data_path = os.path.join(current_dir, '..', 'data', 'processed_data.csv')
    model_path = os.path.join(current_dir, '..', 'models', 'sarima_model.pkl')

    # Load processed data and model
    try:
        data = load_data(processed_data_path)
    except FileNotFoundError as e:
        print(e)
        exit()
    
    try:
        sarima_model = load_model(model_path)
    except FileNotFoundError as e:
        print(e)
        exit()

    # Ensure that the test dataset length matches the number of forecast steps
    test_data_length = min(7, len(data))  # Get the minimum of 7 or the length of your dataset
    test_data = data.iloc[-test_data_length:]

    # Generate predictions
    predictions = sarima_model.forecast(steps=test_data_length)  # Forecast for the number of test data points

    # Plot actual vs predicted values
    plot_predictions(test_data['Price'], predictions)
