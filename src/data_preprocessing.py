import pandas as pd
import os

# Define paths
base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))  # Get the base directory
raw_data_path = os.path.join(base_dir, 'data', 'raw_data.csv')          # Define the path to raw_data.csv
processed_data_path = os.path.join(base_dir, 'data', 'processed_data.csv')  # Define path for processed data

def load_data(file_path):
    if os.path.exists(file_path):
        print(f"Loading data from {file_path}")
        data = pd.read_csv(file_path, parse_dates=['Date'])
        return data
    else:
        raise FileNotFoundError(f"File not found: {file_path}")

def preprocess_data(data):
    data = data.fillna(method='ffill')  # Fill missing values
    data = data.sort_values(by='Date')  # Sort by Date
    return data

def save_processed_data(data, output_path):
    data.to_csv(output_path, index=False)
    print(f"Data saved to {output_path}")

if __name__ == "__main__":
    # Load and preprocess the data
    raw_data = load_data(raw_data_path)
    processed_data = preprocess_data(raw_data)
    save_processed_data(processed_data, processed_data_path)
