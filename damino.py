#import libraries
import pandas as pd
#load dataset
df=pd.read_csv('aminoacids.csv')
#observe overall dataset
print('overall dataset info')
print(df.info())
#observe the 1st 10th rows of the dataset
print('print 1st 10th rows')
print(df.head(10))
#observe the last 10th rows of the dataset
print('print last 10th rows')
print(df.tail(10))
#find all the missing values of the dataset
print('print null vallues')
print(df.isnull().sum()) 
