import pandas as pd 

dataframe = pd.read_csv('Q2-Dataset.csv')

print("\nOLD CSV FILE WITH NaN AND NULL VALUES")
print(dataframe)
print("\nNUMBER OF NULL VALUES IN EACH COLUMNS")
print(dataframe.isnull().sum())
df = dataframe.fillna(0)
print("\nNEW CSV FILE WITH NULL VALUES REPLACED BY ZEROES")
print(dataframe)
print("\nNUMBER OF NULL VALUES IN EACH COLUMNS AFTER UPDATE")
print(df.isnull().sum())

df.to_csv('Q2-Dataset_new.csv')
