import pandas as pd

pd.set_option('display.max_columns', None)
pd.set_option('display.width',250)

df = pd.read_csv("HEA Phase DataSet v1d.csv", encoding="latin-1")
#utf-8' codec can't decode byte 0xb0 in position 2016: invalid start byte without encoding= latin-1

print(df.shape)                     # give the number of rows and columns
print(df.head(10))                  # show first 5 rows
df.info()