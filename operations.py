import numpy as np
m = np.arange(24).reshape(4,6)
#print(m [3,4])
#print(m)
m1 = np.linspace(100,10,20)
#print(m1)
#print(np.sort(m1))
m_power = np.array([1,2,3,4,5,6])
m2 = np.array([100,200,300,400,500,600])
#print(np.array(m_power >= 4))
#print(np.power(m_power,3))
#print(np.concatenate((m_power,m2)))

m2d1 = np.array([[1,2,3],[4,5,6],[7,8,9]])
m2d2 = np.array([[7,8,9],[10,11,12],[13,14,15]])

print(m2d2 + m2d1)

# Multiplication of matrix

print(m2d2.dot(m2d1))


