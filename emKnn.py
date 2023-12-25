import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris
from sklearn.preprocessing import LabelEncoder
from sklearn.mixture import GaussianMixture
from sklearn.cluster import KMeans
iris = load_iris()
x=iris.data
y=iris.target
em_cluster=GaussianMixture(n_components=5).fit(x)
km_cluster=GaussianMixture(n_components=5).fit(x)
em_pred=em_cluster.predict(x)
km_pred=km_cluster.predict(x)
print("\n EM Predictions\n",em_pred)
print("\n KM Predictions\n",km_pred)
plt.scatter(x[:,1],x[:,2],c=em_pred)
plt.show()
plt.scatter(x[:,1],x[:,2],c=km_pred)
plt.show()

