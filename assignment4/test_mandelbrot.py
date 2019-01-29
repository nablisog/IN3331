from numpy import*
from mandelcompute import*

"""
This is a test program that tests if one chooses a region of the
plane outside or inside the Mandelbrot set  
"""

def test_higher():
     values=computemandelbrot(3,4,3,4,1000,1000,1000)
     assert(all(values==0))



def test_lower():
     values=computemandelbrot(-0.25,0.25,0.25,-0.25,100,100,100)
     assert(all(values > 0))
