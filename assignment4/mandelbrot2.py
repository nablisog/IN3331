import numpy as np
import matplotlib.pylab as plt
import time

"""
This programm is a numpy Python script which chooses some rectangle in the
complex plane, colors that rectangle according to mandelbrot method
and saves the coloring as an image  
"""

start=time.time()
def mandel(xmin,xmax,ymin,ymax,w,h,maxx):
    x = np.linspace(xmin, xmax, num=w).reshape((1, w))
    y = np.linspace(ymin, ymax, num=h).reshape((h, 1))
    v = np.tile(x, (h, 1)) + 1j * np.tile(y, (1, w))
 
    Z = np.zeros((h, w), dtype=complex)
    z = np.full((h, w), True, dtype=bool)
    for i in range(maxx):
        Z[z] = Z[z] * Z[z] + v[z]
        z[np.abs(Z) > 2] = False
    return z

xmin=-2
xmax=0.5
ymin=-1.5
ymax=1.25
w=1000
h=1000
maxx=100
p=mandel(xmin=-2,xmax=0.5,ymin=-1.5,ymax=1.25,w=1000,h=1000,maxx=100)
p=np.flipud(1+p)
image=plt.imshow(p,cmap = 'Greys',extent = (xmin,xmax,ymin,ymax))
plt.colorbar()
plt.title("The Mandelbrot set in the complex plane")
print(time.time()-start)
plt.savefig("mandelbrot2.png")
plt.show()
#plt.savefig("mandelbrot2.png")



