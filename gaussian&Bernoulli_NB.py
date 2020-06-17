from sklearn.naive_bayes import GaussianNB,BernoulliNB
from sklearn.model_selection import cross_val_score
from sklearn.datasets import load_digits


x, y = load_digits(return_X_y=True)
print(cross_val_score(GaussianNB(),x,y,cv=5,scoring='accuracy').mean())
print(cross_val_score(BernoulliNB(),x,y,cv=5,scoring='accuracy').mean())
