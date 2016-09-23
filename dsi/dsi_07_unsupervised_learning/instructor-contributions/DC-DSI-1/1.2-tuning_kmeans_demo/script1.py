#Set up imports
import pandas as pd
import numpy as np
from sklearn import cluster
from sklearn import metrics
from sklearn.metrics import pairwise_distances
from sklearn import cluster, datasets
import matplotlib.pyplot as plt
import matplotlib
matplotlib.style.use('ggplot')


#import the data
mydata = pd.read_csv("assets/datasets/wine.csv")

#visualize the data
scatter_plot = mydata.plot(kind='scatter',x='residual sugar',y='alcohol')
#plt.show(scatter_plot)


x = mydata[['fixed acidity','volatile acidity','citric acid','residual sugar', 'chlorides', 'free sulfur dioxide', 'total sulfur dioxide', 'density', 'pH', 'sulphates', 'alcohol']]
y = mydata['quality']


kmeans = cluster.KMeans(n_clusters=8)
kmeans.fit(x)

labels = kmeans.labels_
centroids = kmeans.cluster_centers_
#
# print(labels)
# print centroids

predY = np.choose(labels, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]).astype(np.int64)

accuracy_score = metrics.accuracy_score(y, predY)

#print accuracy_score

silhouette = metrics.silhouette_score(y, predY, metric='euclidean')
print silhouette
