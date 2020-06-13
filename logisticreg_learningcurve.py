from sklearn.linear_model import LogisticRegression as LR
from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import learning_curve
import matplotlib.pyplot as plt

x, y = load_breast_cancer(return_X_y=True)

lrl1 = LR(penalty="l1", solver="liblinear", C=1, max_iter=1000)
lrl2 = LR(penalty="l2", solver="liblinear", C=1, max_iter=1000)

train_size, train_acc, test_acc = learning_curve(lrl2, x, y, cv=5)
print(x.shape)
print(train_size)

plt.plot(train_size, train_acc.mean(axis=1), label='train_acc')
plt.plot(train_size, test_acc.mean(axis=1), label='test_acc')
plt.legend()
plt.show()