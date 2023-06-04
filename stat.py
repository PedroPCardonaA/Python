import numpy as np
m = np.array([[1,2,3],[4,5,6],[7,8,9]])
print(m)
print("")
print(np.ptp(m,axis=0))
print("")
print(np.percentile(m,50, axis=1))