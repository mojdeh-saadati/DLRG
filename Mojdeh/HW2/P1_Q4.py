import numpy as np;
import matplotlib.pyplot as plt;


distance = []
print("enter the list:")
str = input();
distance = [int(dist) for dist in str.split(" ")]
# Considering the fact that there is no direct way between cities and we need to pass the city b to get from a to c:
print("enter city names:")
str = input();
names = str.split(" ");

print("enter the name of city you want to see the distance from:")
str = input()
idx = names.index(str)
distCity = np.zeros(10)

def Cumulative(lists):
    cu_list = []
    length = len(lists)
    cu_list = [sum(lists[0:x:1]) for x in range(0, length+1)]
    return cu_list[1:]


distCity[(idx+1):] = Cumulative(distance[(idx+1):])
distCity[0:(idx-1)] = Cumulative(distance[(idx+1):])

plt.bar(x = names, y = distCity)
plt.show()
