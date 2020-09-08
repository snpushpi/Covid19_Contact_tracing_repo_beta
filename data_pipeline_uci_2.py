import pandas as pd 
import glob
import os
path = r'C:\Users\pushp\Desktop\test\gpsdata\gpsdata'
filenames = glob.glob(path+"/*.csv")
print(filenames)
concat_all_sheets = pd.DataFrame()
for i,file in enumerate(filenames):
    df = pd.read_csv(file)
    l = len(df)
    id_list = []
    for j in range(l):
        id_list.append(i)
    df['ID']=id_list
    concat_all_sheets = pd.concat([concat_all_sheets,df],sort=False)
    
concat_all_sheets.to_csv('Raw_dataset.csv')