from matrix_objects import Vector

from unittest import TestCase

m = Vector([3, 4])
n = Vector([5, 0])

v = Vector([1, 3, 0])
w = Vector([0, 2, 4])
u = Vector([1, 1, 1])
y = Vector([10, 20, 30])
z = Vector([0, 0, 0])

def test_shape_works_on_vector():
    assert m.shape() == 2

def test_shape_vectors():
    """shape should take a vector or matrix and return a tuple with the
    number of rows (for a vector) or the number of rows and columns
    (for a matrix.)"""
    assert v+w == [1, 5, 4]
    assert u+y == [11, 21, 31]
    #assert shape(m) == (2,)
    #assert shape(v) == (3,)
    #assert shape([1]) == (1,)

class VectorTestCases(TestCase):

    def test_fails(self):
        self.assertEqual(v + w, [1, 5, 4])
        self.assertEqual(u + y, [11, 21, 31])
        self.assertEqual(u + z, u.vector1)

    def test_dot_works(self):
        self.assertEqual(w * y, 160)
    #go back over dot function
