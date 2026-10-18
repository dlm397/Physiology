from pprint import pp as printp
from Data import dataGet
import matplotlib.pyplot as plt, numpy as np, pandas as pd

data = dataGet.daily_data()

predictors = ["sleep", "steps", "stress", "heart_rate", "oxygen", "respiration", "skin_temp", "stress"]
paired = data[predictors + ["energy"]].dropna()

predictor_data = paired[predictors]
X = predictor_data.to_numpy()
y = paired["energy"].to_numpy()

# Add a column of ones to fit an intercept
X = np.column_stack([np.ones(len(X)), X])

coefficients, _, _, _ = np.linalg.lstsq(X, y, rcond=None)
intercept = coefficients[0]
predictor_coefficients = pd.Series(coefficients[1:], index=predictor_data.columns, name="coefficient")

#y_pred = X @ coefficients
