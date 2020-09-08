import pandas as pd 
import glob
import os
import csv
def txt_to_csv_converter(file,i):
    with open(file,'r') as in_file:
        stripped = (line.strip() for line in in_file)
        lines = (line.split("|") for line in stripped if line)
        f_string = 'log'+'{}'.format(i)+'.csv'
        with open(f_string,'w') as out_file:
            writer = csv.writer(out_file)
            writer.writerow(('latitude','lognitude','timestamp','',''))
            writer.writerows(lines)
path = r'C:\Users\pushp\Desktop\test\gpsdata\gpsdata\person1\0530'
filenames = glob.glob(path+"/*.txt")
print(filenames)
concat_all_sheets = pd.DataFrame()
for i,file in enumerate(filenames):
    txt_to_csv_converter(file,i)
