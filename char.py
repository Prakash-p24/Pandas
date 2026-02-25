import pandas as pd
import numpy as np
from db import engine

employee = "SELECT * FROM employees;"
department = "SELECT * FROM departmants;"

# Read data into a DataFrame
read_employee = pd.read_sql(employee, engine)

read_department = pd.read_sql(department, engine)


# read_employee['full_name']=read_employee['first_name']+' '+ read_employee['last_name']
# print(read_employee)

#replace
read_employee['first_name']= read_employee['first_name'].replace('John', 'Prakash')
print(read_employee)


#Substring

read_employee.loc[0,'last_name']=read_employee.loc[0,'last_name'][:2]
print(read_employee)


#Reverse

read_employee.loc[0,'first_name']=read_employee.loc[0,'first_name'][::-1]
print(read_employee)