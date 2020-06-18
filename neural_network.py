from sklearn.datasets import fetch_california_housing
from sklearn.neural_network import MLPRegressor
from sklearn.model_selection import cross_val_score

x,y = fetch_california_housing(return_X_y=True)
# print(x.shape)

NN = MLPRegressor(hidden_layer_sizes=(15,),random_state=22)
loss = -cross_val_score(NN,x,y,scoring='neg_mean_squared_error').mean()
print(loss)