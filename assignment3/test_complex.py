from Complex import Complex
"""
This is a unit test progamm for testing the Complex class.
"""

def test_add():
     assert Complex(2, 2) + Complex(2,2) == 4+4j


def test_sub():
     assert Complex(2,2) - Complex(1,1) == 1+1j


def test_con():
     a=Complex(2,2)
     assert a.conjugate() == 2-2j


def test_eq():
     b=Complex(2,2)
     assert b == 2+2j


def test_mul():
     assert Complex(2,3) * Complex(4,1) == 5+14j


def test_rmul():
     assert Complex(2,3) * complex(4,1) == 5+14j



def test_radd():
     assert Complex(2,2) + complex(2,2) == 4+4j
