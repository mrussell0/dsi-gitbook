# -*- coding: utf-8 -*-
"""
Created on Mon Jun  6 14:13:34 2016

@author: JosephNelson
"""

from matplotlib import pyplot as plt
import numpy as np

x = np.linspace(0,1,100)   # We want to ensure we have enough "granularity" in the graph so we set hasmarks to 100
y = x**5*(1-x)**4  # Mapping the Bernoulli scheme
plt.plot(x,y)

plt.show()


# MLE v MAP Estimation



# Solution

from matplotlib import pyplot as plt
import numpy as np

x = np.arange(0,1.,.01)   # We want to ensure we have enough "granularity" in the graph so we set hash marks to 100
y = (x**5)*(1-x)**4  # Mapping the Bernoulli scheme

# Alter the prior and see how that visually alters the posterior

prior = (x**.46)*(1-x)**.32
z = y*prior

#plt.plot(x,prior)
plt.plot(x, y, 'r',x, z, 'g--')
plt.axvline(x=.55556,color='k',ls='dashed')

plt.show()