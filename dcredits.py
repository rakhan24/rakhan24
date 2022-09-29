#import libraries
import pandas as pd
#load dataset
df=pd.read_csv('credits.csv')
#observe the overall dataset
print('print all the dataset')
print(df.info())
#observe 1st 10th rows of dataset
print('print 1st 10th rows')
print(df.head(10))
#observe the last 10th rows of dataset
print('print last 10th rows')
print(df.tail(10))
#find the missing Values
print('print null values')
print(df.isnull().sum())
