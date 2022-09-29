# importing libraries
import pandas as pd
#loading data sets 
df=pd.read_csv('Airbnb_NYC.csv')
#review the entire dataset
print('print all dataset')
print(df.info())
# observing the 1st  10 rows of the data set
print('print 1st 10th rows')
print(df.head(10))
#observing the last 10th row of the datasets 
print('print the last 10th row of the datasets')
print(df.tail(10))
#find missing valus 
print('print the total missing values')
print(df.isnull().sum())
