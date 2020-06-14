from sklearn import datasets
from sklearn import preprocessing
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier

knn = KNeighborsClassifier()
iris = datasets.load_iris()
x = iris.data
y = iris.target

x_s = preprocessing.MinMaxScaler().fit_transform(x)
# x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.3)
x_train, x_test, y_train, y_test = train_test_split(x_s, y, test_size=0.3)

knn.fit(x_train, y_train)

acc = knn.score(x_test, y_test)
print(acc)