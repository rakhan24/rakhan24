#Import libraries
import pandas as pd
# load dataset
df=pd.read_csv('movies_metadata.csv')
#observe csv file dataset
print('print overall dataset')
print(df.info())
#observe 1st 10 rows
print('print 1st 10 rows')
print(df.head(10))
#observe last 10 rows
print('print last 10 rows')
print(df.tail(10))
#finding all the missing values
print('print null values')
print(df.isnull().sum())
