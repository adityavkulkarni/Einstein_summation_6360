# Einstein Summation CS6360

This repository contains an implementation of Einstein summation and tensor operations using SQL based on the paper "Efficient and Portable Einstein Summation in SQL". It leverages mapping tensor expressions in Einstein notation to SQL queries to enable in-database analytics.

## Overview

Key Aspects:
- Represents tensors as tables in sparse coordinate (COO) format
- Translates notation into joins, aggregations, common table expressions
- Uses Opt-Einsum to find efficient contraction paths
- Supports operations like:
  - Matrix multiplication
  - Vector outer products
  - Batch matrix computations
- Tested on SQLite, PostgreSQL, HyPer

## Requirements

### Python and Anaconda

Ensure you have Python version 3.8 and Anaconda version 4.9.2 installed.

The required Python packages are:
- numpy~=1.26.2
- matplotlib~=3.8.2
- pandas~=2.1.3
- tableauhyperapi (version 0.0.13287)
- opt_einsum (version 3.3.0)
- rdflib (version 6.2.0)
- python-sat (version 0.1.7.dev19)

### Postgres

Ensure you have Postgres installed.

### SQLite

Make sure to have SQLite installed.

### Hyper

If you want to use Hyper, ensure you have the necessary dependencies and follow the specific setup instructions.

## Running Experiments

After setting up the environment, you can run experiments interactively. Navigate to the relevant subfolder and execute the experiments:

```bash
cd case_study/quantum_circuits
python qc_sqlite.py
```

## Results

The folder docker results contain all the results along with performance metrics for SQLite, PostgreSQL, HyPer and Python.
