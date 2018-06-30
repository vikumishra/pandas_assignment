import pandas as pd
#Question-1
data={'Name':['Vivek','Ajay'],'Age':[21,21],'E-mail':['vikumishra7073@gmail.com','ajaykhanna123@gmail.com'],'Phone-No.':[9872435977,9876545672]}
df=pd.DataFrame(data)
print(df)
print('\n')

#Question-2
data1=pd.read_csv("test9.csv")
df1=pd.DataFrame(data1)
#(a)
print("First five rows are..")
print(df1.head(5))
print('\n')

#(b)
print("First ten rows are....")
print(df1.head(10))
print('\n')

#(c)
print("Basic Statistics on particular dataset are..")
print(df1.dtypes)
print(df1.size)
print(df1.axes)
print(df1.shape)
print(df1.ndim)
print('\n')

#(d)
print("Last five rows are")
print(df1.tail(5))
print('\n')

#(e)
a=df1.iloc[:,1]
print("Basic Statistics of Second Column are..")
print(a.dtype)
print(a.size)
print(a.axes)
print(a.shape)
print(a.ndim)
