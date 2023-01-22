import sys
B = [[1, 1, 1, 1],
     [1, 1, 1, 1],
     [1, 1, 1, 1]]

A = [[1, 1, 1],
     [1, 1, 1],
     [1, 1, 1],
     [6, 1, 1]]


class Matrix:
    def __init__(self, mat_list):
        self.matrix = mat_list

    def __show_result(self, result):
        for i in range(len(result)):
            print(result[i])

    def show_matrix(self, result):
        for i in range(len(result)):
            print(result[i])

    def addition(self, other_matrix):
        self.__check_add_sub(other_matrix)
        res_add = self.__result()
        for i in range(len(self.matrix)):
            for j in range(len(self.matrix[0])):
                res_add[i][j] = self.matrix[i][j] + other_matrix.matrix[i][j]
        self.__show_result(res_add)

    def substraction(self, other_matrix):
        self.__check_add_sub(other_matrix)
        res_sub = self.__result()
        for i in range(len(self.matrix)):
            for j in range(len(self.matrix[0])):
                res_sub[i][j] = self.matrix[i][j] - other_matrix.matrix[i][j]
        self.__show_result(res_sub)

    def __result(self):
        __res = []
        for i in range(len(self.matrix)):
            __res.append([])
            for j in range(len(self.matrix[0])):
                __res[i].append(0)
        return __res

    def __check_add_sub(self, second_mat):
        y1 = len(self.matrix)
        y2 = len(second_mat.matrix)
        x1 = len(self.matrix[0])
        x2 = len(second_mat.matrix[0])
        if y1 == y2:
            if x1 == x2:
                pass
            else:
                self.__add_zero(second_mat, y1, y2, x1, x2)
        else:
            self.__add_zero(second_mat, y1, y2, x1, x2)

    def __add_zero(self, second_mat, y1, y2, x1, x2):
        delta_y = y1 - y2
        delta_x = x1 - x2
        if delta_y > 0:
            for i in range(abs(delta_y)):
                second_mat.matrix.append([])
                for j in range(x2):
                    second_mat.matrix[y2 + i].append(0)
        elif delta_y < 0:
            for i in range(abs(delta_y)):
                self.matrix.append([])
                for j in range(x1):
                    self.matrix[y1 + i].append(0)
        if delta_x > 0:
            for i in range(len(second_mat.matrix)):
                for j in range(abs(delta_x)):
                    second_mat.matrix[i].append(0)
        elif delta_x < 0:
            for i in range(len(self.matrix)):
                for j in range(abs(delta_x)):
                    self.matrix[i].append(0)

    def transpose(self):
        res_transpose = self.__result()
        for i in range(len(self.matrix)):
            for j in range(len(self.matrix[0])):
                res_transpose[j][i] = self.matrix[i][j]
        self.__show_result(res_transpose)

    def multip_num(self, num):
        res_multip_num = self.__result()
        for i in range(len(self.matrix)):
            for j in range(len(self.matrix[0])):
                res_multip_num[i][j] = self.matrix[i][j] * num
        self.__show_result(res_multip_num)

    def multiplication(self, other_matrix):
        try:
            res_mul = self.__result_multiplication(other_matrix)
            for i in range(len(self.matrix)):
                for j in range(len(other_matrix.matrix[0])):
                    for k in range(len(other_matrix.matrix)):
                        res_mul[i][j] += self.matrix[i][k] * other_matrix.matrix[k][j]
            self.__show_result(res_mul)
        except Exception as ex:
            print(f"Помилка {ex}\nВаші матриці не відповідають правилам множенням матриці на матрицю!", file=sys.stderr)

    def __result_multiplication(self, second_mat):
        __res_m = []
        y1 = len(self.matrix)
        y2 = len(second_mat.matrix)
        x1 = len(self.matrix[0])
        x2 = len(second_mat.matrix[0])
        if y1 >= y2:
            for i in range(y1):
                __res_m.append([])
        else:
            for i in range(y2):
                __res_m.append([])
        if x1 >= x2:
            for i in range(len(__res_m)):
                for j in range(x1):
                    __res_m[i].append(0)
        else:
            for i in range(len(__res_m)):
                for j in range(x2):
                    __res_m[i].append(0)
        return __res_m


c = Matrix(A)
y = Matrix(B)

# c.addition(y)
# y.substraction(c)

# c.transpose()
# c.multip_num(5)

c.multiplication(y)
