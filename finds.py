import pandas as pd
import numpy as np
data=pd.read_csv('data.csv', header=None).to_numpy()
num_attribute = len(data[0])-1
arraydata=np.array(data) [:,: - 1 ]
target=np.array (data) [:,-1]
hypothesis = ['0']*num_attribute
print("\nThe initial hypothesis is: ", hypothesis)
for i, val in enumerate (target):
  if val=='yes':
    h=arraydata[i]
    break
for i, val in enumerate (target):
  if val=='yes':
    for j,val in enumerate(arraydata[i]):
      if h[j] ==val :
        continue
      h[j]='?'
    print(h)
print("Maximal Specific Hypothesis for the given training example is ", list(h) )
