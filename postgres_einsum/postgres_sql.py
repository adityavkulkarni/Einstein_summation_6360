import numpy as np
import psycopg2


def execute_query(query):
    conn = psycopg2.connect(database="postgres", user="postgres", password="password", host="localhost")
    cur = conn.cursor()
    cur.execute(query)
    result = cur.fetchone()
    print(f"Solution: {result[0]}")
    cur.close()
    conn.close()


# from paper
def solving_sat_problem():
    sat_query = """
    WITH 
        T1(i, j, val) AS (VALUES (0, 0, 1), (0, 1, 1), (1, 0, 1)), 
        T2(i, j, k, val) AS (
            VALUES (0, 0, 0, 1), (0, 1, 0, 1), (0, 1, 1, 1), (1, 0, 0, 1), (1, 0, 1, 1),(1, 1, 0, 1), (1, 1, 1, 1)
        ) 
    SELECT 
        SUM(T1.val * T2.val) AS val FROM T1, T2
    WHERE T1.i=T2.i;"""
    execute_query(sat_query)


# from paper
def using_loop(a, b, v):
    r = np.zeros(a.shape[0])
    for i in range(a.shape[0]):
        for j in range(b.shape[0]):
            for k in range(a.shape[1]):
                r[i] += a[i, k] * b[j, k] * v[j]
    return r


def get_tables(a, b, v):
    # Convert each tensor to a list of tuples, each tuple representing a row in the SQL table
    a_values = [(i, j, val) for i, row in enumerate(a) for j, val in enumerate(row) if val != 0]
    b_values = [(i, j, val) for i, row in enumerate(b) for j, val in enumerate(row) if val != 0]
    v_values = [(i, val) for i, val in enumerate(v) if val != 0]

    # Format the values into SQL VALUES table format
    a_table = ', '.join(f"({i}, {j}, {val})" for i, j, val in a_values)
    b_table = ', '.join(f"({i}, {j}, {val})" for i, j, val in b_values)
    v_table = ', '.join(f"({i}, {val})" for i, val in v_values)

    return a_table, b_table, v_table


# derived from paper
def tensors_to_initial_sql(a, b, v):
    a_table, b_table, v_table = get_tables(a, b, v)

    # Construct the SQL query
    sql_query = f"""
    WITH 
        A(i, j, val) AS (VALUES {a_table}), 
        B(i, j, val) AS (VALUES {b_table}), 
        v(i, val) AS (VALUES {v_table})
    SELECT A.i AS i,
        SUM(A.val * B.val * v.val) AS val
    FROM A, B, v
    WHERE A.j=B.j AND B.i=v.i
    GROUP BY A.i;"""

    return sql_query


def tensors_to_sql_optimized(a, b, v):
    a_table, b_table, v_table = get_tables(a, b, v)

    # Construct the SQL query with the k vector optimization
    sql_query = f"""
    WITH 
        A(i, j, val) AS (VALUES {a_table}), 
        B(i, j, val) AS (VALUES {b_table}), 
        v(i, val) AS (VALUES {v_table}), 
        k(i, val) AS (SELECT B.j, SUM(v.val * B.val) FROM v, B WHERE v.i=B.i GROUP BY B.j) 
    SELECT A.i AS i, SUM(k.val * A.val) AS val
      FROM k, A WHERE k.i=A.j GROUP BY A.i;"""

    return sql_query


# from paper
def efficient_loop(a, b, v):
    r = np.zeros(a.shape[0])
    tmp = np.zeros(a.shape[1])
    for j in range(b.shape[0]):
        for k in range(a.shape[1]):
            tmp[k] += b[j, k] * v[j]
    for k in range(a.shape[1]):
        for i in range(a.shape[0]):
            r[i] += a[i, k] * tmp[k]
    return r
