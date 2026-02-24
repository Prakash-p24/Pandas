import pandas as pd
import numpy as np
from sqlalchemy import create_engine

SQLALCHEMY_DATABASE_URL ="postgresql://postgres:35@localhost:5432/pandas"
engine = create_engine(SQLALCHEMY_DATABASE_URL)

# Define your SQL query
employee = "SELECT * FROM employees;"
department = "SELECT * FROM departmants;"

# Read data into a DataFrame
read_employee = pd.read_sql(employee, engine)

read_department = pd.read_sql(department, engine)

# print(read_employee.to_string())
# print(read_department.to_string())

#Filter


filtered = read_employee[read_employee['department_id'] == 1]
print(type(read_employee['hire_date']))

# print(filtered.to_string())


#Like Operator

fname = read_department[read_department['department_name'].str.startswith('S')]
# print(fname.to_string())

name = read_department[read_department['department_name'].str.contains('T') & (read_department['department_name'].str.len()==2)]
# print(name.to_string())

lname = read_department[read_department['department_name'].str.endswith('g')]

# print(lname.to_string())

#Logic operators


and_operator = read_department[(read_department['department_name']=='Sales') & (read_department['location']=='New York')]
# print(and_operator.to_string())

or_operator =  read_employee[(read_employee['first_name']=='prakash') | (read_employee['last_name']=='Smith')]
# print(or_operator.to_string())

between_operator =  read_employee[read_employee['salary'].between(60000.00,90000.00)]
# print(between_operator.to_string())


in_operator = read_department[read_department['location'].isin(['New York','Seattle'])]
# print(in_operator.to_string())

not_operator = read_department[~(read_department['location'].isin(['New York','Seattle']))]

# print(not_operator.to_string())



#Group By

group = read_department.groupby('location')[['department_id']].count()
print(group)

#Having
having = group[group['department_id']>1].sort_values(by='location',ascending=False)
print(having)


#Limit
# print(having.head(1))

#Join
df = pd.merge(read_department[['department_id','department_name','location']], read_employee[['department_id']], on='department_id', how='inner')
group = df.groupby('location')[['department_id']].count()
having = group[group['department_id']>2].sort_values(by='location',ascending=False)
#print(having)

df = pd.merge(read_department[['department_id','department_name','location']], read_employee[['department_id']], on='department_id', how='inner')
filtered = df[df['department_name'] != 'Marketing']
# print(filtered)


#Left Join
df = pd.merge(read_department[['department_id']], read_employee[['department_id','salary']], on='department_id', how='left')

group = df.groupby('salary')[['department_id']].count().reset_index()
filtered =group[group['salary'] > 60000]
print(filtered)


df = pd.merge(read_employee[['department_id','salary']],read_department[['department_id']],on='department_id', how='left')
group = df.groupby('salary')[['department_id']].count()
# print(group)



#Right Join

# df = pd.merge(read_department[['department_id','location']], read_employee[['department_id']], on='department_id', how='right')
# group = df.groupby('location')[['department_id']].count()
# # print(group)

# df = pd.merge(read_employee[['department_id','first_name','last_name']], read_department[['department_id']],on='department_id', how='right')
# df['full_name'] = df['first_name']+' '+df['last_name']
# # print(df)


# #Full Join
df = pd.merge(read_department[['department_id']], read_employee[['department_id','salary']], on='department_id', how='outer')
group = df.groupby('salary')[['department_id']].count()
having=df[df['salary']>=75000]
# print(having)


#String Function

#concat
read_employee['full_name']=read_employee['first_name']+' '+ read_employee['last_name']
# print(read_employee)

#replace
read_employee['first_name'] = read_employee['first_name'].replace('John', 'Prakash')
# print(read_employee)


#Reverse
read_employee.loc[0,'first_name']=read_employee.loc[0,'first_name'][::-1]
# print(read_employee)

#Substring

read_employee.loc[0,'last_name']=read_employee.loc[0,'last_name'][:1]
# print(read_employee)




#Integer Functions

# # 1. Exponential (exp)
# read_employee['salary'] = read_employee['salary'].apply(np.exp)
# print(read_employee)

# # 2. Logarithm (log - natural)
# read_employee['salary'] = read_employee['salary'].apply(np.log)
# print(read_employee)

# # 3. Square Root (sqrt)
# read_employee['salary'] = read_employee['salary'] ** 0.5
# print(read_employee)

# 4. Power (power)
# read_employee['salary'] = read_employee['salary'].pow(2)
# print(read_employee)


#Date Function


#Extract Date part


read_employee['hire_date'] = pd.to_datetime(read_employee['hire_date'])


# read_employee['hire_date'] = read_employee['hire_date'].dt.month_name()
# print(read_employee)
# read_employee['hire_date'] = read_employee['hire_date'].dt.day_name()
# print(read_employee)
# read_employee['hire_date'] = read_employee['hire_date'].dt.year
# print(read_employee)

#Date Difference
# from datetime import date
# current_date =pd.to_datetime(date.today())

# read_employee['hire_date'] = (current_date - read_employee['hire_date']).dt.days
# print(read_employee)


#Adds Date
from pandas.tseries.offsets import DateOffset

# read_employee['hire_date'] = read_employee['hire_date'] + pd.Timedelta(days=7)
# read_employee['hire_date'] = read_employee['hire_date'] + DateOffset(months=1)
# print(read_employee)



#Type casting
read_employee['salary'] = read_employee['salary'].astype(int)
# print(read_employee) 


#Aggregate Function

# df = pd.merge(read_department[['department_id','department_name']], read_employee[['department_id','salary']], on='department_id', how='inner')
# group = df.groupby('department_name').agg(
#     total_salary=('salary', 'sum'),
#     avg_salary=('salary', 'mean')
# )

# print(group)

# df = pd.merge(read_department[['department_id','department_name']], read_employee[['department_id','salary']], on='department_id', how='inner')
# group = df.groupby('department_id  ').agg(
#     total_salary=('salary', 'min'),
#     avg_salary=('salary', 'max')
# )

# print(group)
