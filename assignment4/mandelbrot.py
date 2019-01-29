import argparse
import numpy as np
import matplotlib.pyplot as plt
from numba import jit

"""
This programm provides a command line user interface and also it
provides instructions by calling it with a --help  
"""


def mandel(z,maxx):
     c=z
     for i in range(maxx):
          if abs(z)>2:
               return i
          z=z**2+c
     return maxx

def mandel_python(xmin,xmax,ymin,ymax,width,height,maxx):
     hold=np.zeros((width,height))
     for ii, i in enumerate(np.linspace(xmin,xmax,w)):
          for jj, j in enumerate(np.linspace(ymin,ymax,h)):
               c= complex(i,j)
               hold[ii,jj]=mandel(c,maxx)
     return hold
     

     
def mandel_numpy(xmin,xmax,ymin,ymax,width,height,maxx):
     x = np.linspace(xmin, xmax, num=width).reshape((1, width))
     y = np.linspace(ymin, ymax, num=height).reshape((height, 1))
     v = np.tile(x, (height, 1)) + 1j * np.tile(y, (1, width))
 
     Z = np.zeros((height, width), dtype=complex)
     z = np.full((height, width), True, dtype=bool)
     for i in range(maxx):
         Z[z] = Z[z] * Z[z] + v[z]
         z[np.abs(Z) > 2] = False
     return z
     


@jit(nopython=True)
def mandel_numba(xmin,xmax,ymin,ymax,width,height,maxx):
     hold=np.zeros((w,h))
     for ii, i in enumerate(np.linspace(xmin,xmax,width)):
          for jj, j in enumerate(np.linspace(ymin,ymax,height)):
               c= complex(i,j)
               hold[ii,jj]=mandel(c,maxx)
     return hold

     

if __name__ == '__main__':
     parser = argparse.ArgumentParser()
     parser.add_argument("xmin",  type = float)
     parser.add_argument("xmax",  type = float)
     parser.add_argument("ymin",  type = float)
     parser.add_argument("ymax",  type = float)
     parser.add_argument("width", type = float)
     parser.add_argument("height",type = float)
     parser.add_argument("maxx",  type = float)
     parser.add_argument("filename")
     parser.add_argument('choice',type = str)
     args=parser.parse_args()
     
     if args.choice == 'python':
          mandel_python(parser.xmin,parser.xmax,parser.ymin,parser.ymax,parser.width,parser.height,parser.maxx)
          plt.imshow(hold,cmap = 'Greys',extent =(xmin,xmax,ymin,ymax))
          plt.title("The Mandelbrot set in the complex plane using python")
          plt.savefig(parser.filename)
          plt.show()
          
          
                        
     elif args.choice == 'numpy':
          mandel_numpy(parser.xmin,parser.xmax,parser.ymin,parser.ymax,parser.width,parser.height,parser.maxx)
          p=np.flipud(1+p)
          image=plt.imshow(p,cmap = 'Greys',extent = (xmin,xmax,ymin,ymax))
          plt.title("The Mandelbrot set in the complex plane using numpy")
          plt.savefig(parser.filename)
          plt.show()
          



     elif args.choice == 'numba':
          mandel_numba(parser.xmin,parser.xmax,parser.ymin,parser.ymax,parser.width,parser.height,parser.maxx)
          plt.imshow(hold,cmap = 'Greys',extent =(xmin,xmax,ymin,ymax))
          plt.title("The Mandelbrot set in the complex plane using numba")
          plt.savefig(parser.filename)
          plt.show()
          

     else:
          print('Wrong Input')
     
     
