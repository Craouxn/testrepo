import numpy as np
import matplotlib.pyplot as plt


height = np.round(np.random.normal(1.75, 0.2, 5000), 2)
weight = np.round(np.random.normal(60, 15, 5000), 2)
np_city = np.column_stack((height, weight))
np_city

np.corrcoef(np_city[:,0], np_city[:,1])
np.std(np_city[:,0])


plt.title("heights distribution in city")
plt.xlabel("height")
plt.ylabel("amount")
plt.yticks([0, 500, 1000])

plt.hist(height, bins = [1.3, 1.4, 1.5, 1.6, 1.7, 1.8, 1.9, 2.0, 2.1, 2.22, 2.50])
plt.show()
#testblabladd
#plt.scatter(np_city[:,0], np_city[:,1])
#max(height)


