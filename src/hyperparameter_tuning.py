import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import GridSearchCV
import joblib

def load_data():
    X_train = pd.read_csv('data/processed/X_train.csv')
    y_train = pd.read_csv('data/processed/y_train.csv')
    return X_train, y_train

def tune_hyperparameters(X_train, y_train):
    param_grid = {
        'n_estimators': [50, 100, 200],
        'max_depth': [None, 10, 20, 30],
        'min_samples_split': [2, 5, 10]
    }
    model = RandomForestRegressor(random_state=42)
    grid_search = GridSearchCV(estimator=model, param_grid=param_grid, cv=5, n_jobs=-1)
    grid_search.fit(X_train, y_train.values.ravel())
    return grid_search.best_estimator_

def save_model(model, file_path='models/final_model.pkl'):
    joblib.dump(model, file_path)

if __name__ == "__main__":
    X_train, y_train = load_data()
    best_model = tune_hyperparameters(X_train, y_train)
    save_model(best_model)
