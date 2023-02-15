import numpy as np
import matplotlib.pyplot as plt

# give us 100 2d values centered at 0
# X = np.random.randn(100, 2)
#
# plt.scatter(X[:,0], X[:,1])
# plt.show()

X = np.random.randn(200, 2)
# create clusters of data
# select all the rows from index 0 to index 50 and add a 3 to all elements
X[:50] += 3

# this is a 1d array that colors the particular clusters
Y = np.zeros(200)
Y[:50] = 1

plt.scatter(X[:,0], X[:,1], c=Y)
plt.show()