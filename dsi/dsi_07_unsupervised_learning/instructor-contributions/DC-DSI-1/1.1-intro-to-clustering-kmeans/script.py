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

#Let's convert data into pandas dataframe
df = pd.DataFrame(data=iris, columns=['SepalLength', 'SepalWidth', 'PetalLength', 'PetalWidth', 'Name'])

#Our dataframe has the column 'Name'. Let's convert this to numerical data for K-means to accept
#Typically, that would take a simple if statement to for all of the values in the categorical column
# For this dataset, the name column has Iris-setosa, Iris-virginica, and Iris-versicolor as attributes

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

#let's plot what we have
sepal_length = df.plot(kind='scatter',x='SepalWidth',y='SepalLength')

#plt.show(sepal_length)

#Let's convert data into numpy array

dn = df.as_matrix(columns=None)

#Let's choose 2 for k, looking at previous data.
#implementing k-means is simple in Python
#note:  Because we aren't predicting anything, there's no risk of overfitting, so we'll train our model on the whole dataset

kmeans = cluster.KMeans(n_clusters=2)
kmeans.fit(dn)

#We can use Scikit's built-in functions to determine the locations of the centroids and their labels
#labels indicate what cluster a point belongs to
labels = kmeans.labels_
#Coordinates of cluster centers
centroids = kmeans.cluster_centers_
# print labels
# print centroids

#Determine the silhouette coefficient, a metric to test how well each of the data points lies within the cluster
#The best value is 1 and the worst value is -1.
#Values near 0 indicate overlapping clusters.
# Negative values generally indicate that a sample has been assigned to the wrong cluster, as a different cluster is more similar.
silhouette = metrics.silhouette_score(dn, labels, metric='euclidean')

#print silhouette

plt.plot(silhouette)
plt.ylabel("Silhouette")
plt.xlabel("k")
plt.show(silhouette)
