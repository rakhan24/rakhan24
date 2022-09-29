#import libraries
import pandas as pd
#load dataset
df=pd.read_csv('bestsellers with categories.csv')
#observe the overall dataset
print('print overall dataset')
print(df.info())
#observe the 1st 10th rows of dataset
print('print 1st 10th rows')
print(df.head(10))
#observe the last 10th rows of dataset
print('print last 10th rows')
print(df.tail(10))
#finding the missing values
print('print null values')
print(df.isnull().sum())
