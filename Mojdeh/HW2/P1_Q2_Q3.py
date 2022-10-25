
import numpy as np;
x, y = np.mgrid[:10, :5]
z = x + y 
print(x.shape, y.shape, z.shape)
x, y = np.ogrid[:10, :5] 
z = x + y 
print(x.shape, y.shape, z.shape)

# They will have the same shape.

# np.ogrid needs less storage, and we can obtain np.mgrid from np.ogrid by using np.broadcast_arrays