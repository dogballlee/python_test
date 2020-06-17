from sklearn.datasets import make_blobs,make_circles
from sklearn.cluster import KMeans,DBSCAN
import matplotlib.pyplot as plt
import numpy as np
from sklearn.metrics import silhouette_score    #轮廓系数，表征样本点距离临近簇的距离

# x,y = make_blobs(n_samples=500,n_features=2,centers=4,random_state=22)
# fig,ax = plt.subplots(1,3,figsize=(12,4))
# ax[0].scatter(x[:,0],x[:,1],s=8)    #ax[0]指第一个子图，s指样本点大小是8
#
# color = ["r","g","b","orange"]
#
# for i in range(4):
#     ax[1].scatter(x[y==i,0],x[y==i,1],s=8,c=color[i])
#
# pred = KMeans(n_clusters=4,random_state=22).fit_predict(x)
# for i in range(4):
#     ax[2].scatter(x[:,0],x[:,1],s=8,c=pred) #kmeans预测结果中包含分类的颜色信息，此处的c可以直接等于pred
#
# plt.show()


x1,_ = make_circles(n_samples=5000,factor=.5,noise=0.05)
x2,_ = make_blobs(n_samples=1000,n_features=2,centers=[[1.2,1.2]],cluster_std=0.1)
#聚类不存在y值，此处直接用_代之

fig,ax = plt.subplots(1,3,figsize=(16,4))
x = np.concatenate((x1,x2)) #该numpy函数能把两个数据集合成一个
ax[0].scatter(x[:,0],x[:,1],s=8)

pred = KMeans(n_clusters=3).fit_predict(x)
ax[1].scatter(x[:,0],x[:,1],s=8,c=pred)

pred = DBSCAN(eps=0.1,min_samples=10).fit_predict(x)
ax[2].scatter(x[:,0],x[:,1],s=8,c=pred)

plt.show()  #DBSCAN真鸡儿牛逼