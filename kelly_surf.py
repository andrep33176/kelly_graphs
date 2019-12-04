from mpl_toolkits import mplot3d
import numpy as np
import matplotlib.pyplot as plt
import time

t1=time.time()
odds = np.linspace(1, 100, 100)
p = np.linspace(0.01,1,100) 
def kelly(odds, p):
    return ((odds*p) - (1-p))/odds

# Everything above this is setup, the answer to your question lies here:
kellyv = np.vectorize(kelly)
kelly_fraction = kellyv(odds[:, np.newaxis], p)

fig = plt.figure()
ax = plt.axes(projection='3d')

ax.plot_surface(odds, p, kelly_fraction, edgecolor='none')
ax.set_title('Kelly Plot')
ax.set_xlabel('Payoffs')
ax.set_ylabel('Probability of a Win')
ax.set_zlabel('Allocations')
plt.show()
plt.savefig('kellysurf.png')
t2=time.time()
print (t2-t1)