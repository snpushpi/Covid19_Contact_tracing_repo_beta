import pandas as pd 
df = pd.read_csv('Raw_Dataset1.csv')
def list_generator(new_dataframe,user_num):
    user_x = new_dataframe[new_dataframe.ID==user_num]['latitude'].to_list()
    user_y = new_dataframe[new_dataframe.ID==user_num]['lognitude'].to_list()
    user_timestamp = new_dataframe[new_dataframe.ID==user_num]['timestamp'].to_list()
    l = len(new_dataframe[new_dataframe.ID==user_num])
    user_path = [(user_x[i],user_y[i],user_timestamp[i])for i in range(l)]
    return user_path 
querier_path = list_generator(df,0)
infected_list = []
for i in range(1,19):
    infected_list.append(list_generator(df,i))
intersection_set = set()
def intersection(l1,l2):
    return set(l1)&set(l2)
intersection_set = set()
#intersection check
for i in range(18):
    intersection_set|=intersection(querier_path,infected_list[i])
result_set = set()
for e in intersection_set:
    result_set.add(e[2])
print(result_set)
print(len(result_set))