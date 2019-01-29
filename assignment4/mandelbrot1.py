import numpy as np
import matplotlib.pylab as plt
import time

"""
This programm is a Python script which chooses some rectangle in the
complex plane, colors that rectangle according to mandelbrot method
and saves the coloring as an image  
"""

start=time.time()
def m1(z,maxx):
     c=z
     for i in range(maxx):
          if abs(z)>2:
               return i
          z=z**2+c
     return maxx


def m2(xmin,xmax,ymin,ymax,maxx,w,h):
     hold=np.zeros((w,h))
     for ii, i in enumerate(np.linspace(xmin,xmax,w)):
          for jj, j in enumerate(np.linspace(ymin,ymax,h)):
               c= complex(i,j)
               hold[ii,jj]=m1(c,maxx)
     return hold

def m3(hold,xmin,xmax,ymin,ymax,w,h):
     plt.imshow(hold,cmap = 'Greys',extent=(xmin,xmax,ymin,ymax))
     plt.colorbar()
     plt.title("The Mandelbrot set in the complex plane")
     plt.savefig("mandelbrot1.png")
     plt.show()
     
     
     

if __name__ == "__main__":
     xmin =-2;xmax=0.5;ymin=-1.5;ymax=1.25;maxx=100;w=1000;h=1000
     hold=m2(xmin,xmax,ymin,ymax,maxx,w,h)
     print(time.time() - start)
     m3(hold,xmin,xmax,ymin,ymax,w,h)
     
     
     
     
     
     
     
