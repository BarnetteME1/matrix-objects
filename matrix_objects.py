from functools import reduce

class Vector:

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
            new_vector.append(self.vector1[pos] * other.vector1[pos])
        return reduce(lambda x, y: x + y, new_vector)


    def magnitude(self):
        scalar = 0
        vector_len = len(self.vector1)
        for spot in range(0, vector_len):
            scalar += (self.vector1[spot] **2)
        return (scalar **(1/2))

class Matrix:

    def __init__(self, matrix1):
        self.matrix1 = matrix1

    def __str__(self):
        return "{}".format(self.matrix1)

    def column(self, num):
        col = []
        for line in self.matrix1:
            col.append(line[num])
        return col

    def row(self, num):
        return self.matrix1[num]

    def matrix_shape(self):
        column = len(self.matrix1)
        row = len(self.matrix1[0])
        return column, row

    def shape_check(self, other):
        if isinstance(other, Vector):
            if self.shape()[1] != other.shape():
                return self.shape_rule()
        if isinstance(other, self.__class__):
            if self.shape() != other.shape():
                return self.shape_rule()

    def shape(self):
        column = len(self.matrix1)
        row = len(self.matrix1[0])
        return column, row

    def shape_rule(other):
        raise ValueError("Incompatible shapes")

    def __add__(self, other):
        self.shape_check(other)
        new_matrix = []
        for pos in range(len(self.column(0))):
            new_row = []
            for posi in range(len(self.row(0))):
                new_row.append(self.matrix1[pos][posi] + other.matrix1[pos][posi])
            new_matrix.append(new_row)
        return new_matrix

    def __sub__(self, other):
        self.shape_check(other)
        new_matrix = []
        for pos in range(len(self.column(0))):
            new_row = []
            for posi in range(len(self.row(0))):
                new_row.append(self.matrix1[pos][posi] - other.matrix1[pos][posi])
            new_matrix.append(new_row)
        return new_matrix

    def __mul__(self, other):
        self.shape_check(other)
        if isinstance(other, int):
            new_matrix = []
            for pos in range(len(self.column(0))):
                new_row = []
                for posi in range(len(self.row(0))):
                    new_row.append(self.matrix1[pos][posi] * other)
                new_matrix.append(new_row)
            return new_matrix
        if isinstance(other, Vector):
            new_vec = []
            for row in self.matrix1:
                number = 0
                for pos in range(len(self.row(0))):
                    number += (other.vector1[pos] * row[pos])
                new_vec.append(number)
            return new_vec
