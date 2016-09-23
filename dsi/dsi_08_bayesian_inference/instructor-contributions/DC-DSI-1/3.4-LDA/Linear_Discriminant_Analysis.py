# -*- coding: utf-8 -*-
"""
Created on Wed Jun  8 11:39:05 2016

@author: JosephNelson
"""

# Possible solution

import matplotlib.pyplot as plt
from sklearn import datasets
from sklearn.lda import LDA

iris = datasets.load_iris()
X = iris.data; y = iris.target

target_names = iris.target_names


# Now, invoke the LDA method to compute and fit the model:

lda_classifier = LDA(n_components=2)
lda_x_axis = lda_classifier.fit(X, y).transform(X)

# Now output a simple visualization of the model result:

color_scheme = ['r', 'g', 'b']

for c, i, target_name in zip(color_scheme, [0, 1, 2], target_names):
    plt.scatter(lda_x_axis[y == i, 0], lda_x_axis[y == i, 1], c = c, label = target_names)

plt.xlabel('First LDA'); plt.ylabel('Second LDA')
plt.show()


# We have a score associated with the classifier's performance
lda_classifier.score(X, y, sample_weight=None)
