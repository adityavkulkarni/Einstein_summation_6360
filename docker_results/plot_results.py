import os
import re

import matplotlib.pyplot as plt
import pandas as pd


def show_figure(file_name, num_iter):
    # Load data from CSV file
    df = pd.read_csv(file_name)

    features = df['feature']
    sqlite_data = df['SQLite']
    postgresql_data = df['PostgreSQL']
    hyper_data = df['HyPer']
    python_data = df['Python']

    # Plot the data
    plt.plot(features, sqlite_data, marker="o", label='SQLite')
    plt.plot(features, postgresql_data, marker="o", label='PostgreSQL')
    plt.plot(features, hyper_data, marker="o", label='HyPer')
    plt.plot(features, python_data, marker="o", label='Python')

    plt.xlabel('nbits_c')
    plt.ylabel('Iterations per second')
    plt.title(f'quantum_use_case, iterations: {num_iter}')
    plt.legend()
    plt.xticks(features)

    max_y = df.iloc[:, 1:].max().max()
    min_y = df.iloc[:, 1:].min().min()
    step = (max_y - min_y) / 10
    plt.yticks([min_y + i * step for i in range(11)])

    plt.tight_layout()
    plt.show()


def main():
    for entry in os.scandir(".\\results"):
        file = entry.path
        if file.endswith(".csv"):
            num_iter = re.search(r'\d+', file)
            if num_iter:
                show_figure(entry.path, num_iter.group())


if __name__ == "__main__":
    main()
