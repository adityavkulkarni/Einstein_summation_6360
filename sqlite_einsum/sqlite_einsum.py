import random
import time

import numpy as np
from sqlite_handler import SQLiteHandler
from sqlite_einsum.einstein_notation_parsing import *


class EinsteinNotation:
    def __init__(self, int_only=False):
        self._int = int_only
        self._sqlite = SQLiteHandler(db_name="./sqlite_einsum/einsum.db")
        self._create_2d_tensor_query = ("CREATE TABLE {name} "
                                        "(i INT, j INT, val DOUBLE);")
        self._insert_2d_tensor_query = ("INSERT INTO {name} "
                                        "VALUES ({i}, {j}, {val});")
        self._create_3d_tensor_query = ("CREATE TABLE {name} "
                                        "(i INT, j INT, k INT, val DOUBLE);")
        self._insert_3d_tensor_query = ("INSERT INTO {name} "
                                        "VALUES ({i}, {j}, {k}, {val});")
        self._select_query = "SELECT * FROM {name};"
        self._delete_query = "DROP TABLE {name};"
        self._matrix_multiplication_query = ("SELECT {A}.i AS i, {B}.j AS j, SUM({B}.val * {A}.val) AS val "
                                             "FROM {Ai}, {B} WHERE {B}.i={A}.j GROUP BY {A}.i, {B}.j "
                                             "ORDER BY i, j")
        self._matrix_transpose_query = ("SELECT {A}.j AS i, {A}.i AS j, SUM({A}.val) AS val "
                                        "FROM {A} GROUP BY {A}.j, {A}.i ORDER BY i, j")
        self._matrix_diagonal_query = "SELECT SUM({A}.val) AS val FROM {A} WHERE {A}.i={A}.j"
        self._matrix_row_sum_query = "SELECT i AS i, SUM(val) AS val FROM {A} WHERE i=j GROUP BY i ORDER BY i"
        self._matrix_sum_query = "SELECT SUM({A}.val) AS val FROM {A}"

    def create_2d_tensor(self, name, tensor):
        self.delete_tensor(name)
        self._sqlite.execute_query(self._create_2d_tensor_query.format(name=name))
        for i in range(len(tensor)):
            for j in range(len(tensor[i])):
                self._sqlite.execute_query(
                    self._insert_2d_tensor_query.format(i=i,
                                                        j=j,
                                                        name=name,
                                                        val=tensor[i][j]))

    def delete_tensor(self, name):
        if self._sqlite.check_table_exist(name):
            self._sqlite.execute_query(self._delete_query.format(name=name))

    def get_tensor(self, name, sql=False):
        if self._sqlite.check_table_exist(name):
            sql_tensor, _ = self._sqlite.fetch_all_rows(self._select_query.format(name=name))
            if sql:
                return sql_tensor
            else:
                return self._2d_tensor_to_matrix(sql_tensor)
        else:
            print("Tensor not present")

    def _matrix_multiplication(self, operands):
        if len(operands) < 2:
            print(f"Less than 2 operands")
            return
        if len(operands) >= 2:
            k = [self._matrix_multiplication_query.format(A=operands[0],
                                                          Ai=operands[0],
                                                          B=operands[1])]
            for i in range(2, len(operands)):
                k.append(self._matrix_multiplication_query.format(A=f"K{i-2}",
                                                                  Ai=f"({k[i-2]}) as K{i - 2}",
                                                                  B=operands[i]))
            tensor, run_time = self._sqlite.fetch_all_rows(k[-1])
            return self._2d_tensor_to_matrix(tensor), run_time

    def _transpose(self, operand):
        tensor, run_time = self._sqlite.fetch_all_rows(
            self._matrix_transpose_query.format(A=operand))
        return self._2d_tensor_to_matrix(tensor), run_time

    def _get_diagonal_sum(self, operand):
        tensor, run_time = self._sqlite.fetch_all_rows(
            self._matrix_diagonal_query.format(A=operand))
        return tensor[0][0], run_time

    def _get_row_sum(self, operand):
        tensor, run_time = self._sqlite.fetch_all_rows(
            self._matrix_row_sum_query.format(A=operand))
        return self._1d_tensor_to_matrix(tensor), run_time

    def _get_sum(self, operand):
        tensor, run_time = self._sqlite.fetch_all_rows(
            self._matrix_sum_query.format(A=operand))
        return tensor[0][0], run_time

    def einstein_notation(self, operation, operands):
        if isinstance(operands, list) and validate_matrix_multiplication(operation, operands):
            print(f"Matrix multiplication on: {','.join(operands)}")
            return self._matrix_multiplication(operands)
        elif validate_sum(operation):
            print(f"Get sum of: {operands}")
            return self._get_sum(operands)
        elif validate_transpose(operation):
            print(f"Matrix transpose on: {operands}")
            return self._transpose(operands)
        elif validate_diagonal_sum(operation):
            print(f"Get diagonal sum of: {operands}")
            return self._get_diagonal_sum(operands)
        elif validate_row_sum(operation):
            print(f"Get row wise sum of: {operands}")
            return self._get_row_sum(operands)
        else:
            print("Unsupported operation\nCheck Einstein Notation/ Number of operands")
            return False, 0

    def _1d_tensor_to_matrix(self, tensor):
        max_i = max(t[0] for t in tensor) + 1

        matrix = [0 for _ in range(max_i)]
        for t in tensor:
            matrix[t[0]] = int(t[1]) if self._int else t[1]
        return matrix

    def _2d_tensor_to_matrix(self, tensor):
        max_i = max(t[0] for t in tensor) + 1
        max_j = max(t[1] for t in tensor) + 1

        matrix = [[0.0] * max_j for _ in range(max_i)]
        for t in tensor:
            matrix[t[0]][t[1]] = int(t[2]) if self._int else t[2]
        return matrix


def generate_random_matrix(i, j):
    return [[random.randint(1, 10) for _ in range(j)] for _ in range(i)]


if __name__ == "__main__":
    es = EinsteinNotation(int_only=True)

    # Matrix generation
    A = generate_random_matrix(5, 5)
    B = generate_random_matrix(5, 6)
    C = generate_random_matrix(6, 6)
    D = generate_random_matrix(6, 5)
    E = generate_random_matrix(5, 5)
    F = generate_random_matrix(5, 7)
    G = generate_random_matrix(7, 7)
    H = generate_random_matrix(7, 5)
    I = generate_random_matrix(5, 5)
    J = generate_random_matrix(5, 5)
    Z = generate_random_matrix(15, 15)

    # Tensor creation
    es.create_2d_tensor("A", A)
    es.create_2d_tensor("B", B)
    es.create_2d_tensor("C", C)
    es.create_2d_tensor("D", D)
    es.create_2d_tensor("E", E)
    es.create_2d_tensor("F", F)
    es.create_2d_tensor("G", G)
    es.create_2d_tensor("H", H)
    es.create_2d_tensor("I", I)
    es.create_2d_tensor("J", J)
    es.create_2d_tensor("Z", Z)
    print("-------------------------------")
    # Matrix multiplication
    e = "ij,jk,kl,lm,mn,no,op,pq,qr,rs->is"
    tables = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J"]
    result, rt = es.einstein_notation(e, tables)
    """for table in tables:
        print(f"{table}: {es.get_tensor(table)}")"""
    start_time = time.time()
    np_result = np.einsum(e, A, B, C, D, E, F, G, H, I, J)
    end_time = time.time()
    # print(f"SQLite Result: {result}")
    # print(f"Numpy  Result: {np_result.tolist()}")
    print(f"SQLite Time: {rt} ms")
    print(f"Numpy  Time: {format((end_time - start_time)*1000, '.5f')} ms")
    print(f"Validation: {all(all(element for element in row) for row in result == np_result)}")
    print("-------------------------------")
    # Transpose
    e = "ij->ji"
    result, rt = es.einstein_notation(e, "Z")
    start_time = time.time()
    np_result = np.einsum(e, Z)
    end_time = time.time()
    # print(f"J: {es.get_tensor('J')}")
    # print(f"SQLite Result: {result}")
    # print(f"Numpy  Result: {np_result.tolist()}")
    print(f"SQLite Time: {rt} ms")
    print(f"Numpy  Time: {format((end_time - start_time)*1000, '.5f')} ms")
    print(f"Validation: {all(all(element for element in row) for row in result == np_result)}")
    print("-------------------------------")
    # Diagonal Sum
    e = "ii->"
    result, rt = es.einstein_notation(e, "Z")
    start_time = time.time()
    np_result = np.einsum(e, Z)
    end_time = time.time()
    # print(f"I: {es.get_tensor('Z')}")
    print(f"SQLite Result: {result}")
    print(f"Numpy  Result: {np_result.tolist()}")
    print(f"SQLite Time: {rt} ms")
    print(f"Numpy  Time: {format((end_time - start_time)*1000, '.5f')} ms")
    print(f"Validation: {int(result) == int(np_result)}")
    print("-------------------------------")
    # Row wise sum
    e = "ii->i"
    result, rt = es.einstein_notation(e, "Z")
    start_time = time.time()
    np_result = np.einsum(e, Z)
    end_time = time.time()
    # print(f"I: {es.get_tensor('Z')}")
    print(f"SQLite Result: {result}")
    print(f"Numpy  Result: {np_result.tolist()}")
    print(f"SQLite Time: {rt} ms")
    print(f"Numpy  Time: {format((end_time - start_time)*1000, '.5f')} ms")
    print(f"Validation: {all(row for row in result == np_result)}")
    print("-------------------------------")
    # Sum of Matrix
    e = "ij->"
    result, rt = es.einstein_notation(e, "Z")
    start_time = time.time()
    np_result = np.einsum(e, Z)
    end_time = time.time()
    # print(f"I: {es.get_tensor('Z')}")
    print(f"SQLite Result: {result}")
    print(f"Numpy  Result: {np_result.tolist()}")
    print(f"SQLite Time: {rt} ms")
    print(f"Numpy  Time: {format((end_time - start_time)*1000, '.5f')} ms")
    print(f"Validation: {int(result) == int(np_result)}")
    for table in tables:
        es.delete_tensor(table)
