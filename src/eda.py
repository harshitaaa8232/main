import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

def load_data(file_path):
    # Check if file exists
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"File not found: {file_path}")
    
    # Load the data
    data = pd.read_csv(file_path, parse_dates=['Date'], index_col='Date')
    return data

def plot_time_series(data, column):
    plt.figure(figsize=(10, 6))
    plt.plot(data.index, data[column])
    plt.title(f'{column} over Time')
    plt.xlabel('Date')
    plt.ylabel(column)
    plt.show()

if __name__ == "__main__":
    # Dynamically construct the path based on script location
    current_dir = os.path.dirname(os.path.abspath(__file__))  # Get current directory of this script
    processed_data_path = os.path.join(current_dir, '..', 'data', 'processed_data.csv')

    # Load the processed data
    try:
        data = load_data(processed_data_path)
    except FileNotFoundError as e:
        print(e)
        exit()  # Stop execution if file is not found
    
    # Plot the time series for 'Price' column
    plot_time_series(data, 'Price')
