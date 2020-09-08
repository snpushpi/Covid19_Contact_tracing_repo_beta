import pandas as pd 
df = pd.read_csv('Raw_Dataset.csv')
max_x = df['latitude'].idxmax()
min_x = df['latitude'].idxmin()
max_y = df['lognitude'].idxmax()
min_y = df['lognitude'].idxmin()
print(df['latitude'][max_x], df['latitude'][min_x])
print(df['lognitude'][max_y], df['lognitude'][min_y])