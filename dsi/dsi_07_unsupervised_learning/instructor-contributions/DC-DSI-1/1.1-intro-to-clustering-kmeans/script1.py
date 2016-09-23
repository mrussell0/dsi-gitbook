#setup imports
import pandas as pd
import numpy as np
from sklearn import cluster
from sklearn import metrics
from sklearn.metrics import pairwise_distances
from sklearn import cluster, datasets
import matplotlib.pyplot as plt
import matplotlib
matplotlib.style.use('ggplot')

#load and check out data
iris = pd.read_csv("assets/datasets/iris.csv")
#print iris.head(n=5)

df = pd.DataFrame(data=iris, columns=['SepalLength', 'SepalWidth', 'PetalLength', 'PetalWidth', 'Name'])

def name_to_numeric(x):
    if x=='Iris-setosa':
        return 1
    if x=='Iris-virginica':
        return 2
    if x=='Iris-versicolor':
        return 3

#and apply by creating a new column with the numeric values and deleting the old one

df['Name_Num'] = df['Name'].apply(name_to_numeric)
del df['Name']

sepal_length = df.plot(kind='scatter',x='SepalWidth',y='SepalLength')

#plt.show(sepal_length)

dn = df.as_matrix(columns=None)

kmeans = cluster.KMeans(n_clusters=2)
kmeans.fit(dn)

labels = kmeans.labels_
#Coordinates of cluster centers
centroids = kmeans.cluster_centers_
#print labels
#what do coordinates mean?
#print centroids

silhouette = metrics.silhouette_score(dn, labels, metric='euclidean')
print silhouette
