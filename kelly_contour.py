from mpl_toolkits import mplot3d
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm
import time

t1=time.time()
def kelly(odds, p):
    return ((odds*p) - (1-p))/odds
odds = np.linspace(1, 100, 100)
p = np.linspace(0.01,1,100)

X, Y = np.meshgrid(odds,p)
Z = kelly(X, Y)

fig = plt.figure()
ax = plt.axes(projection='3d')
ax.contour3D(X, Y, Z, 50, cmap=cm.Blues)
ax.set_xlabel('Odds')
ax.set_ylabel('Probability of A Win')
ax.set_zlabel('Allocations')
ax.set_title('Kelly Plot')
plt.show()
plt.savefig('kellycontour.png')
t2=time.time()
print(t2-t1)