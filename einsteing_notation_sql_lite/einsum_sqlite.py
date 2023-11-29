import random
import time

import numpy as np
from sqlite_handler import SQLiteHandler


class EinsteinNotation:
    def __init__(self, int_only = False):
        self._int = int_only
        self._sqlite = SQLiteHandler("einsum.db")
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
            """tensor, run_time = self._sqlite.fetch_all_rows(
                self._matrix_multiplication_query.format(A=operands[0],
                                                         Ai=operands[0],
                                                         B=operands[1]))
            return self._2d_tensor_to_matrix(tensor), run_time"""
        k = [self._matrix_multiplication_query.format(A=operands[0],
                                                      Ai=operands[0],
                                                      B=operands[1])]
        for i in range(2, len(operands)):
            k.append(self._matrix_multiplication_query.format(A=f"K{i-2}",
                                                              Ai=f"({k[i-2]}) as K{i - 2}",
                                                              B=operands[i]))
        tensor, run_time = self._sqlite.fetch_all_rows(k[-1])
        return self._2d_tensor_to_matrix(tensor), run_time

    def einstein_notation(self, operation, operands):
        if self._validate_matrix_multiplication(operation, operands):
            print(f"Matrix multiplication on: {','.join(operands)}")
            return self._matrix_multiplication(operands)
        else:
            print("Unsupported operation\nCheck Einstein Notation/ Number of operands")
            return False, 0

    def _2d_tensor_to_matrix(self, tensor):
        max_i = max(t[0] for t in tensor) + 1
        max_j = max(t[1] for t in tensor) + 1

        matrix = [[0.0] * max_j for _ in range(max_i)]
        for t in tensor:
            matrix[t[0]][t[1]] = int(t[2]) if self._int else t[2]
        return matrix

    @staticmethod
    def _validate_matrix_multiplication(exp, ope):
        input_indices, output_indices = exp.split('->')
        input_indices = input_indices.split(',')
        output_indices = output_indices.strip()
        pred_output = f"{input_indices[0][0]}{input_indices[-1][-1]}"
        if len(input_indices) != len(ope): return False
        if pred_output != output_indices: return False
        for ind in range(len(input_indices)):
            if ind:
                if nxt_i != input_indices[ind][0]:
                    return False
            nxt_i = input_indices[ind][1]
        return True


def generate_random_matrix(i, j):
    return [[random.randint(1, 10) for _ in range(j)] for _ in range(i)]


if __name__ == "__main__":
    es = EinsteinNotation(int_only=True)

    # Matrix generation
    A = generate_random_matrix(2, 3)
    B = generate_random_matrix(3, 4)
    C = generate_random_matrix(4, 5)
    D = generate_random_matrix(5, 6)
    E = generate_random_matrix(6, 7)
    F = generate_random_matrix(7, 8)
    G = generate_random_matrix(8, 9)
    H = generate_random_matrix(9, 10)
    I = generate_random_matrix(10, 11)
    J = generate_random_matrix(11, 12)

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

    # Matrix multiplication
    e = "ij,jk,kl,lm,mn,no,op,pq,qr,rs->is"
    tables = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J"]
    result, rt = es.einstein_notation(e, tables)
    if result:
        for t in tables:
            print(f"{t}: {es.get_tensor(t)}")
        print(f"SQLite Result: {result}")
        start_time = time.time()
        np_result = np.einsum(e, A, B, C, D, E, F, G, H, I, J)
        end_time = time.time()
        print(f"Numpy Result: {np_result.tolist()}")
        print(f"SQLite time: {rt}")
        print(f"Numpy Time: {format(end_time - start_time, '.5f')}")
        print(f"Validation: {all(all(element for element in row) for row in result == np_result)}")

        for t in tables:
            es.delete_tensor(t)
