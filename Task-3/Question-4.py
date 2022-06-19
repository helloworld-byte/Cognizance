import pandas as pd
ser = pd.Series(['amrita', 'school', 'of', 'engineering', 'chennai', 'campus'])
print("Series before : ")
print(ser)
print(ser.str.capitalize())