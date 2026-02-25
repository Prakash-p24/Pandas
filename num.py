import pandas as pd
import numpy as np
from db import engine

employee = "SELECT * FROM employees;"
department = "SELECT * FROM departmants;"

# Read data into a DataFrame
read_employee = pd.read_sql(employee, engine)

read_department = pd.read_sql(department, engine)

#Integer Functions

expo = read_employee['salary'].apply(np.exp)
logo = read_employee['salary'].apply(np.log)
root = read_employee['salary'].apply(np.sqrt)
powe = read_employee['salary'].pow(2)


# 1. Exponential (exp)
read_employee['salary'] = expo
print(read_employee)

# 2. Logarithm (log - natural)
read_employee['salary'] = logo
print(read_employee)

# 3. Square Root (sqrt)
read_employee['salary'] = root
print(read_employee)

# 4. Power (power)
read_employee['salary'] = powe
print(read_employee)

# Type casting
read_employee['salary'] = read_employee['salary'].astype(str)
print(read_employee) 