
import argparse
import logging


class Matrix:
    '''Класс, представляющий матрицу.

    Атрибуты:
        - rows (int): количество строк в матрице
        - cols (int): количество столбцов в матрице
        - data (list): двумерный список, содержащий элементы матрицы

    Методы:
        - __init__(rows, cols): инициализация матрицы с заданным числом строк и столбцов
        - __str__(): возвращает строковое представление матрицы
        - __repr__(): возвращает строковое представление матрицы, которое может быть использовано для создания нового
         объекта
        - __eq__(other): определяет операцию "равно" для двух матриц
        - __add__(other): определяет операцию сложения двух матриц
        - __mul__(other): определяет операцию умножения двух матриц'''

    def __init__(self, rows, cols):
        '''Инициализация матрицы с заданным числом строк и столбцов.

        Аргументы:
            - rows (int): количество строк
            - cols (int): количество столбцов'''
        self.rows = rows
        self.cols = cols
        self.data = [[0 for j in range(cols)] for i in range(rows)]

    def __str__(self):
        '''Возвращает строковое представление матрицы.'''
        return '\n'.join([' '.join(map(str, row)) for row in self.data])

    def __repr__(self):
        '''Возвращает строковое представление матрицы, которое может быть использовано для создания нового объекта.'''
        return f'Matrix({self.rows}, {self.cols})'

    def __eq__(self, other):
        '''Определяет операцию "равно" для двух матриц.

        Аргументы:
            - other (Matrix): вторая матрица

        Возвращает:
            - bool: True, если матрицы равны, иначе False'''
        if self.rows != other.rows or self.cols != other.cols:
            return False
        for i in range(self.rows):
            for j in range(self.cols):
                if self.data[i][j] != other.data[i][j]:
                    return False
        return True

    def __add__(self, other):
        '''Определяет операцию сложения двух матриц.

        Аргументы:
            - other (Matrix): вторая матрица

        Возвращает:
            - Matrix: новая матрица, полученная путем сложения двух исходных матриц'''
        if self.rows != other.rows or self.cols != other.cols:
            raise ValueError('Матрицы должны иметь одинаковые размеры')
        result = Matrix(self.rows, self.cols)
        for i in range(self.rows):
            for j in range(self.cols):
                result.data[i][j] = self.data[i][j] + other.data[i][j]
        return result

    def __mul__(self, other):
        '''Определяет операцию умножения двух матриц.

        Аргументы:
            - other (Matrix): вторая матрица

        Возвращает:
            - Matrix: новая матрица, полученная путем умножения двух исходных матриц'''
        if self.cols != other.rows:
            raise ValueError('Количество столбцов первой матрицы должно быть равно количеству строк второй матрицы')
        result = Matrix(self.rows, other.cols)
        for i in range(self.rows):
            for j in range(other.cols):
                for k in range(self.cols):
                    result.data[i][j] += self.data[i][k] * other.data[k][j]
        return result


def main():
    logging.basicConfig(filename='matrix_operations.log', level=logging.INFO, encoding='utf-8',
                        format='%(asctime)s - %(levelname)s - %(message)s')

    parser = argparse.ArgumentParser(description='Matrix operations')
    parser.add_argument('operation', choices=['add', 'multiply'], help='Operation to perform: add or multiply')
    parser.add_argument('matrix1_rows', type=int, help='Number of rows in matrix 1')
    parser.add_argument('matrix1_cols', type=int, help='Number of columns in matrix 1')
    parser.add_argument('matrix2_rows', type=int, help='Number of rows in matrix 2')
    parser.add_argument('matrix2_cols', type=int, help='Number of columns in matrix 2')

    args = parser.parse_args()

    logging.info(f"Requested operation: {args.operation}")

    if args.operation == 'add':
        matrix1 = Matrix(args.matrix1_rows, args.matrix1_cols)
        matrix1.data = [[1, 2, 3], [4, 5, 6]]  # Пример значений для матрицы 1

        matrix2 = Matrix(args.matrix2_rows, args.matrix2_cols)
        matrix2.data = [[7, 8, 9], [10, 11, 12]]  # Пример значений для матрицы 2

        try:
            matrix_sum = matrix1 + matrix2
            print(matrix_sum)
        except ValueError as e:
            logging.error(f"Error performing addition: {e}")

    elif args.operation == 'multiply':
        matrix3 = Matrix(3, 2)
        matrix3.data = [[1, 2], [3, 4], [5, 6]]  # Пример значений для матрицы 3

        matrix4 = Matrix(2, 2)
        matrix4.data = [[7, 8], [9, 10]]  # Пример значений для матрицы 4

        try:
            result = matrix3 * matrix4
            print(result)
        except ValueError as e:
            logging.error(f"Error performing multiplication: {e}")

    else:
        logging.error("Invalid operation specified.")


if __name__ == "__main__":
    main()

