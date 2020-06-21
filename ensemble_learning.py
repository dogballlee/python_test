#集成学习分为bagging和boosting。
# 其中bagging中各个模型相互独立，通过表决进行判断学习，遵从少数服从多数；
# boosting中低层模型到高层模型存在顺序关系，逐渐提高


from sklearn.datasets import load_wine
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier,BaggingClassifier,AdaBoostClassifier
from sklearn.tree import DecisionTreeClassifier

x,y = load_wine(return_X_y=True)
train_x,test_x,train_y,test_y = train_test_split(x,y,test_size=.3,random_state=22)
rfc = RandomForestClassifier(random_state=22).fit(train_x,train_y)
dtc = DecisionTreeClassifier(random_state=22).fit(train_x,train_y)
bc = BaggingClassifier(random_state=22).fit(train_x,train_y)
abc = AdaBoostClassifier(random_state=22).fit(train_x,train_y)

print(rfc.score(test_x,test_y))
print(dtc.score(test_x,test_y))
print(bc.score(test_x,test_y))
print(abc.score(test_x,test_y))