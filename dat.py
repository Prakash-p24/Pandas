import pandas as pd
import numpy as np
from db import engine

employee = "SELECT * FROM employees;"
department = "SELECT * FROM departmants;"

# Read data into a DataFrame
read_employee = pd.read_sql(employee, engine)

read_department = pd.read_sql(department, engine)

#Date Function


#Extract Date part


date_diff = pd.to_datetime(read_employee['hire_date'])
print(date_diff)

read_employee['hire_date'] = pd.to_datetime(read_employee['hire_date'])


# Adds Date
# read_employee['hire_date'] = pd.to_datetime(read_employee['hire_date']

month = read_employee['hire_date'].dt.month_name()
day = read_employee['hire_date'].dt.day_name()
year = read_employee['hire_date'].dt.year
read_employee['month'] = month
read_employee['day'] = day
read_employee['year'] = year
print(read_employee)

# Filter for March and year 2020
filtered_df = read_employee[
    (read_employee['hire_date'].dt.month_name() == 'March') &
    (read_employee['hire_date'].dt.year == 2020) 
]
print(filtered_df)



from pandas.tseries.offsets import DateOffset
# read_employee['hire_date'] = pd.to_datetime(read_employee['hire_date'])
read_employee['hire_date'] = date_diff + pd.Timedelta(days=7)
print(read_employee)
read_employee['hire_date'] = date_diff + DateOffset(months=1)
print(read_employee)
read_employee['hire_date'] = date_diff + DateOffset(years=1)
print(read_employee)


# Date Difference
from datetime import date
current_date =pd.to_datetime(date.today())

diff = (current_date - date_diff).dt.days
read_employee['current_date'] = current_date
read_employee['difference'] = diff
print(read_employee)