from sklearn.linear_model import LinearRegression, Lasso, Ridge, ElasticNet
from sklearn.datasets import fetch_california_housing
from sklearn.model_selection import cross_val_score
import pandas as pd

x, y = fetch_california_housing(return_X_y=True)

lr = LinearRegression()

loss = -cross_val_score(lr, x, y, cv = 5, scoring = 'neg_mean_squared_error').mean()

print(y.min(), y.max())
print(loss)