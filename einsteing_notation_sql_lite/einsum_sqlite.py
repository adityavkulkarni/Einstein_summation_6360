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
                                             "FROM {B}, {A} WHERE {B}.i={A}.j GROUP BY {A}.i, {B}.j "
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
        if len(operands) == 2:
            tensor, run_time = self._sqlite.fetch_all_rows(
                self._matrix_multiplication_query.format(A=operands[0], B=operands[1]))
            print(f" --- {run_time} seconds --- ")
            return self._2d_tensor_to_matrix(tensor)
        k1 = self._matrix_multiplication_query.format(A=operands[0], B=operands[1])

    def einstein_notation(self, operation, operands):
        if self._validate_matrix_multiplication(operation):
            print(f"Matrix multiplication on: {','.join(operands)}")
            return self._matrix_multiplication(operands)

    def _2d_tensor_to_matrix(self, tensor):
        max_i = max(t[0] for t in tensor) + 1
        max_j = max(t[1] for t in tensor) + 1

        matrix = [[0.0] * max_j for _ in range(max_i)]
        for t in tensor:
            matrix[t[0]][t[1]] = int(t[2]) if self._int else t[2]
        return matrix

    @staticmethod
    def _validate_matrix_multiplication(exp):
        input_indices, output_indices = exp.split('->')
        input_indices = input_indices.split(',')
        output_indices = output_indices.strip()
        pred_output = f"{input_indices[0][0]}{input_indices[-1][-1]}"
        if pred_output != output_indices: return False
        for ind in range(len(input_indices)):
            if ind:
                if nxt_i != input_indices[ind][0]:
                    return False
            nxt_i = input_indices[ind][1]
        return True


if __name__ == "__main__":
    es = EinsteinNotation(int_only=True)
    A = [[random.randint(1, 100) for _ in range(100)] for _ in range(100)]
    B = [[random.randint(1, 100) for _ in range(100)] for _ in range(100)]

    es.create_2d_tensor("A", A)
    es.create_2d_tensor("B", B)

    # print(f"A: {es.get_tensor('A')}\nB: {es.get_tensor('B')}")
    result = es.einstein_notation("ij,jk->ik", ["A", "B"])
    print(f"Result= {result}")
    es.delete_tensor("A")
    es.delete_tensor("B")

    start_time = time.time()
    np_result = np.einsum("ij,jk->ik", A, B)
    end_time = time.time()
    print(f"Numpy Time: {format(end_time - start_time, '.5f')}")


