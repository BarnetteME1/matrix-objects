from functools import reduce

class Vector(list):

    def __init__(self, vector1):
        self.vector1 = vector1

    def __str__(self):
        return "{}".format(self.vector1)

    def shape(self):
        return len(self.vector1)

    def shape_rule(self):
        raise ValueError("Incompatible shapes")

    def shape_check(self, other):
        if self.shape() != other.shape():
            return self.shape_rule()

    def __add__(self, other):
        self.shape_check(other)
        new_vector = []
        for num in range(self.shape()):
            new_vector.append(self.vector1[num] + other.vector1[num])
        return new_vector

    def __sub__(self, other):
        self.shape_check(other)
        new_vector = []
        for num in range(self.shape()):
            new_vector.append(self.vector1[num] - other.vector1[num])
        return new_vector

    def __mul__(self, other):
        new_vector = []
        for num in range(self.shape()):
            new_vector.append(self.vector1[num] * other)
        return new_vector

    def dot(self, other):
        new_vector = []
        self.shape_check(other)
        vec_len = range(len(self.vector1))
        for pos in vec_len:
            new_vector.append(self.vector1[pos]*other.vector1[pos])
        return reduce(lambda x, y: x+y, new_vector)


    def magnitude(self):
        scalar = 0
        vector_len = len(self.vector1)
        for spot in range(0, vector_len):
            scalar += (self.vector1[spot] **2)
        return (scalar **(1/2))
