import numpy as np;

X = np.random.rand(10,3)
Y = np.random.rand(3)

print("a", X+Y)
print("b",X[np.newaxis, :] + Y )

# THis is the only one cannot be broad cast. 
#print("c", X + Y[: , np.newaxis])

print("d",X[:, np.newaxis] + Y) 
print("e",X + Y[np.newaxis, :]) 
print("f", X[:, np.newaxis, :] + Y)