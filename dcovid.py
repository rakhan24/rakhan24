#import libraries
import pandas as pd
#load dataset
df=pd.read_csv('country_wise_latest.csv')
#observe the overall dataset
print('print all dataset')
print(df.info())
#observe the 1st 10th rows of dataset
print('print 1st 10th rows')
print(df.head(10))
#observe the last 10th dataset
print('print last 10th rows')
print(df.tail(10))
#find all the missing values
print('print null values')
print(df.isnull().sum())
