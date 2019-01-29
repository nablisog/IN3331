import numpy as np
import matplotlib.pylab as plt


def m1(z,maxtime):
     c=z
     for i in range(maxtime):
          if abs(z)>2:
               return i
          z=z**2+c
     return maxtime

def computemandelbrot(xmin,xmax,ymin,ymax,Nx,Ny,maxtime=1000,plotfilename=None):
     hold=np.zeros((Nx,Ny))
     for ii, i in enumerate(np.linspace(xmin,xmax,Nx)):
          for jj, j in enumerate(np.linspace(ymin,ymax,Ny)):
               c= complex(i,j)
               hold[ii,jj]=m1(c,maxtime)

     if plotfilename != None:
          m3(hold,xmin,xmax,ymin,ymax)
     return hold

def m3(hold,xmin,xmax,ymin,ymax,fname):
     plt.imshow(hold,cmap = 'Greys',extent=(xmin,xmax,ymin,ymax))
     plt.title("The Mandelbrot set in the complex plane")
     plt.show()
     plt.savefig(fname)
     
     

if __name__ == "__main__":
     xmin =-2;xmax=0.5;ymin=-1.5;ymax=1.25;Nx=1000;Ny=1000;maxtime=1000
     hold=computemandelbrot(xmin,xmax,ymin,ymax,Nx,Ny,maxtime)
     m3(hold,xmin,xmax,ymin,ymax,'josh')
     
     
     
     
     
     
     


     
     
     
     


          
          


 
 
          
          
