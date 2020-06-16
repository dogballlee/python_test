from sklearn.svm import SVC, LinearSVC
import matplotlib.pyplot as plt
from sklearn.model_selection import cross_val_score
from sklearn.datasets import make_blobs

# x, y = make_blobs(n_samples=50, centers=2, random_state=0, cluster_std=0.6)
# plt.scatter(x[:,0],x[:,1],c=y,s=50)
# plt.show()

print(cross_val_score(LinearSVC(),x,y,cv=5,scoring='accuracy').mean())
print(cross_val_score(SVC(kernel='linear'),x,y,cv=5,scoring='accuracy').mean())