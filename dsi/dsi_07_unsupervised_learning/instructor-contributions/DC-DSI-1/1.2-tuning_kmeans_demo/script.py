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
plt.show(scatter_plot)

#PERFORM A KMEANS test

# let's define the columns.
#We're going to using "quality" to define class as "y"
#and the rest of our variables as "x."

x = mydata[['fixed acidity','volatile acidity','citric acid','residual sugar', 'chlorides', 'free sulfur dioxide', 'total sulfur dioxide', 'density', 'pH', 'sulphates', 'alcohol']]
y = mydata['quality']

#let's estimate 8 clusters and tune

kmeans = cluster.KMeans(n_clusters=8)
kmeans.fit(x)

#let's define labels and centroids

labels = kmeans.labels_
centroids = kmeans.cluster_centers_

#print(labels)

#Now let's define predicted class labels
predY = np.choose(labels, [1, 2, 3, 4, 5, 6, 7, 8]).astype(np.int64)

#Let's evaluate the clusters

#Check accuracy score

accuracy_score = metrics.accuracy_score(y, predY)

#print accuracy_score

# Compute Silhouette Score
# returns error saying Passing 1d arrays as data is deprecated in 0.17 and willraise ValueError in 0.19.
silhouette = metrics.silhouette_score(y, predY, metric='euclidean')

#print silhouette

#Check the F-Score, Precision, and Recall:
#returns same error

print(metrics.classification_report(predY, labels))

#Confusion matrix
print(metrics.confusion_matrix(y, predY))
