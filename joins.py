import pandas as pd
import numpy as np
from db import engine

employee = "SELECT * FROM employees;"
department = "SELECT * FROM departmants;"

# Read data into a DataFrame
read_employee = pd.read_sql(employee, engine)

read_department = pd.read_sql(department, engine)

#Join
df = pd.merge(read_department[['department_id','department_name','location']], read_employee[['department_id']], on='department_id', how='inner')
group = df.groupby('location')[['department_id']].count()
having = group[group['department_id']>2].sort_values(by='location',ascending=False)
print(having)

df = pd.merge(read_department[['department_id','department_name','location']], read_employee[['department_id']], on='department_id', how='inner')
filtered = df[df['department_name'] != 'Marketing']
print(filtered)


#Left Join
df = pd.merge(read_department[['department_id']], read_employee[['department_id','salary']], on='department_id', how='left')
group = df.groupby('salary')[['department_id']].count().reset_index()
filtered =group[group['salary'] > 60000]
print(filtered)


df = pd.merge(read_employee[['department_id','salary']],read_department[['department_id']],on='department_id', how='left')
group = df.groupby('salary')[['department_id']].count()
print(group)





# #Full Join
df = pd.merge(read_department[['department_id']], read_employee[['department_id','salary']], on='department_id', how='outer')
group = df.groupby('salary')[['department_id']].count().reset_index()
filtered =group[group['salary'] >= 75000]
print(filtered)



#Cross Join
df = pd.merge(read_employee[['first_name']],read_department[['department_name']], how='cross')
filtered =df[df['first_name'] != 'Mike']
print(filtered)

#Right Join

df = pd.merge(read_department[['department_id','location']], read_employee[['department_id']], on='department_id', how='right')
group = df.groupby('location')[['department_id']].count()
print(group)

read_employee['full_name'] = read_employee['first_name']+' '+read_employee['last_name']
df = pd.merge(read_employee[['department_id','full_name','salary']], read_department,on='department_id', how='right')
# df['full_name'] = df['first_name']+' '+df['last_name']
print(df)
