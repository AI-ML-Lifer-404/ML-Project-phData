import json
import pathlib
import pickle
from typing import List
from typing import Tuple


import pandas
from sklearn import model_selection
from sklearn import neighbors
from sklearn import pipeline
from sklearn import preprocessing
from sklearn.metrics import mean_squared_error, r2_score
from math import sqrt
from sklearn.model_selection import GridSearchCV


SALES_PATH = "data/kc_house_data.csv"  # path to CSV with home sale data
# DEMOGRAPHICS_PATH = "data/zipcode_demographics.csv"  # path to CSV with demographics
# List of columns (subset) that will be taken from home sale data
SALES_COLUMN_SELECTION = [
    'price', 'bedrooms', 'bathrooms', 'sqft_living', 'sqft_lot', 'floors',
    'sqft_above', 'sqft_basement', 'zipcode', 'yr_built', 'yr_renovated', 'waterfront', 'view', 'grade', 'lat', 'long', 'sqft_living15', 'sqft_lot15'
]
OUTPUT_DIR = "model"  # Directory where output artifacts will be saved


def load_data(
    sales_path: str
) -> Tuple[pandas.DataFrame, pandas.Series]:
    """Load the target and feature data by merging sales and demographics.

    Args:
        sales_path: path to CSV file with home sale data
        demographics_path: path to CSV file with home sale data
        sales_column_selection: list of columns from sales data to be used as
            features

    Returns:
        Tuple containg with two elements: a DataFrame and a Series of the same
        length.  The DataFrame contains features for machine learning, the
        series contains the target variable (home sale price).

    """
    # 9
    data = pandas.read_csv(sales_path,
                           usecols=SALES_COLUMN_SELECTION,
                           dtype={'zipcode': str})
    # demographics = pandas.read_csv("data/zipcode_demographics.csv",
    # dtype={'zipcode': str})

    # merged_data = data.merge(demographics, how="left",
    # on = "zipcode").drop(columns="zipcode")
    # Remove the target variable from the dataframe, features will remain

    y = data.pop('price')
    x = data

    return x, y


def main():
    """Load data, train model, and export artifacts."""
    x, y = load_data(SALES_PATH)
    x_train, _x_test, y_train, _y_test = model_selection.train_test_split(
        x, y, random_state=42)
    print(x.columns)

    param_grid_knn = {
        'n_neighbors': [2, 5, 10, 15, 20, 30, 45],
        'algorithm': ['ball_tree', 'kd_tree', 'brute', 'auto'],
        'metric': ['minkowski', 'euclidean', 'manhattan', 'chebyshev']
    }


    model = pipeline.make_pipeline(preprocessing.RobustScaler(), neighbors.KNeighborsRegressor())
    grid = GridSearchCV(model, param_grid_knn, cv=5, n_jobs=-1, verbose=True, refit=True)
    grid.fit(x_train, y_train)
    best_knn__model = grid.best_estimator_

    # Print the best hyperparameters
    print('=========================================[Best Hyperparameters info]=====================================')
    print(grid.best_params_)

    # summarize best
    print('Best MAE: %.3f' % grid.best_score_)
    print('Best Config: %s' % grid.best_params_)
    print('==========================================================================================================')
    y_pred = model.predict(_x_test)

    # Evaluate the model
    mse = mean_squared_error(_y_test, y_pred)
    r2 = r2_score(_y_test, y_pred)
    rmse = sqrt(mean_squared_error(_y_test, y_pred))


    print(f'Mean Squared Error: {mse}')
    print(f'R-squared: {r2}')
    print(f'Root Mean Squared Error: {rmse}')


    output_dir = pathlib.Path(OUTPUT_DIR)
    output_dir.mkdir(exist_ok=True)

    # Output model artifacts: pickled model and JSON list of features
    pickle.dump(model, open(output_dir / "model.pkl", 'wb'))
    json.dump(list(x_train.columns),
              open(output_dir / "model_features.json", 'w'))


if __name__ == "__main__":
    main()
