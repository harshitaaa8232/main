
# AI-ML Price Prediction for Agri-Horticultural Commodities

## Problem Statement

**Problem Statement ID:** 1647  
**Title:** Development of AI-ML based models for predicting prices of agri-horticultural commodities such as pulses and vegetables (onion, potato, etc.)

The Department of Consumer Affairs monitors the daily prices of 22 essential food commodities through 550 price reporting centers across the country. The Department also maintains buffer stock of pulses (gram, tur, urad, moong, and masur), and onion for strategic market interventions to stabilize the volatility in prices. Decisions for market interventions, such as the release of stocks from the buffer, are taken based on price trends and outlook. Currently, price analyses are based on seasonality, historical and emerging trends, market intelligence inputs, crop sowing, and production estimates. ARIMA-based economic models have also been used to examine and forecast prices of pulses.

## Project Overview

This project aims to develop AI/ML models, specifically SARIMA (Seasonal AutoRegressive Integrated Moving Average), to forecast the prices of selected agri-horticultural commodities. The prediction models will assist the Ministry of Consumer Affairs in stabilizing prices and planning effective market interventions.

## Dataset

The dataset consists of daily prices of various agri-horticultural commodities. You can find the raw data in the `data/raw_data.csv` file.

## Usage

1. **Data Preprocessing:**
   - Run the `data_preprocessing.py` script to clean and prepare the data for modeling:
   bash
   python src/data_preprocessing.py
   ```

2. **Exploratory Data Analysis:**
   - Run the `eda.py` script to visualize trends and patterns in the data:
   ```bash
   python src/eda.py
   ```

3. **Model Training:**
   - Train the SARIMA model by running the `model.py` script:
   ```bash
   python src/model.py
   ```

4. **Model Evaluation:**
   - Evaluate the model's performance using the `evaluation.py` script:
   ```bash
   python src/evaluation.py
   ```

## Additional Notebooks

- **Data Preprocessing Notebook (`notebooks/data_preprocessing.ipynb`):** Interactive exploration and preprocessing of the data.
- **EDA Notebook (`notebooks/exploratory_analysis.ipynb`):** Exploratory analysis and visualizations.
- **Model Training Notebook (`notebooks/model_training.ipynb`):** SARIMA model training and result visualization.

## Future Enhancements

- **Model Comparison:** Implement and compare other forecasting models (e.g., LSTM, Prophet).
- **Integration with Real-Time Data:** Connect the model to live data streams for real-time predictions.
- **User Interface:** Develop a web-based dashboard for visualizing predictions.

