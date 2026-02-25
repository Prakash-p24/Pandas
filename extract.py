import pandas as pd
import numpy as np
from db import engine

employee = "SELECT * FROM employees;"
department = "SELECT * FROM departmants;"

# Read data into a DataFrame
read_employee = pd.read_sql(employee, engine)

read_department = pd.read_sql(department, engine)

#Filter


filtered = read_employee[read_employee['department_id'] == 1]
print(filtered.to_string())


#Like Operator

fname = read_department[read_department['department_name'].str.startswith('S')]
print(fname.to_string())

name = read_department[read_department['department_name'].str.contains('T') & (read_department['department_name'].str.len()==2)]
print(name.to_string())

lname = read_department[read_department['department_name'].str.endswith('g')]
print(lname.to_string())



#Logic operators


and_operator = read_department[(read_department['department_name']=='Sales') & (read_department['location']=='New York')]
print(and_operator.to_string())

or_operator =  read_employee[(read_employee['first_name']=='prakash') | (read_employee['last_name']=='Smith')]
print(or_operator.to_string())

between_operator =  read_employee[read_employee['salary'].between(60000.00,90000.00)]
print(between_operator.to_string())


in_operator = read_department[read_department['location'].isin(['New York','Seattle'])]
print(in_operator.to_string())

not_operator = read_department[~(read_department['location'].isin(['New York','Seattle']))]
print(not_operator.to_string())



#Group By

group = read_department.groupby('location')[['department_id']].count()
print(group)

#Having
having = group[group['department_id']>1].sort_values(by='location',ascending=False)
print(having)

# Aggregate Function

df = pd.merge(read_department[['department_id','department_name']], read_employee[['department_id','salary']], on='department_id', how='inner')
group = df.groupby('department_name').agg(
    total_salary=('salary', 'sum'),
    avg_salary=('salary', 'mean')
)

print(group)

df = pd.merge(read_department[['department_id','department_name']], read_employee[['department_id','salary']], on='department_id', how='inner')
group = df.groupby('department_id').agg(
    min_salary=('salary', 'min'),
    max_salary=('salary', 'max')
)

print(group)

