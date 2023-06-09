import numpy as np
m = np.array([[1,-1,2],[3,2,0]])
print(m)
print("")
m1 = np.array([[1],[2],[3]])
print(m1)
print("")
print(np.transpose(m1))
print("")
A = np.array([[2,1,-2],[3,0,1],[1,1,-1]])
b = np.array([[-3],[5],[2]])
x = np.linalg.solve(A,b)
print(x)
print(np.allclose(np.dot(A,x),b))
