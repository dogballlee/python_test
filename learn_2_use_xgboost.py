from sklearn.datasets import fetch_california_housing
import xgboost      #sklearn自带xgb，但是效果速度都十分感人，推荐使用陈天奇自己写的库
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error as MSE

x,y = fetch_california_housing(return_X_y=True)
train_x,test_x,train_y,test_y = train_test_split(x,y,test_size=.2,random_state=22)

#xgb不能使用sklearn自带的功能模块进行训练，需先转化为如下的dtrain/dtest
dtrain = xgboost.DMatrix(train_x,train_y)
dtest = xgboost.DMatrix(test_x,test_y)


param = {'silent':False,'objective':'reg:linear','eta':.1}      #silent参数用来选择是否在运行结果中显示建树过程;objective此处需要设置为线性回归，因为默认是分类模型;eta指学习率
xgb = xgboost.train(param,dtrain,num_boost_round=175)       #建175棵树
pred = xgb.predict(dtest)
print(MSE(test_y,pred))     #实力强大，竞赛必备