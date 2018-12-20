import os
import glob
import pandas as pd


folder_path = "./input/"
# if directory of file path is not exist >> make it
if not os.path.exists(os.path.dirname(folder_path)):
    try:
        os.makedirs(os.path.dirname(folder_path))
    except OSError as ex:  # Guard against race condition
        raise ValueError('can not make directory {} {}'.format(folder_path, ex))



# function
"""
get_list_of_category(
    data                pandas data frame
    category            column's category
)

"""
def get_list_of_category(data,category):
    list_of_category = set()
    for index, row in data.iterrows():
        list_of_category.add(row[category])
    return list_of_category



#process



stores = {'2:花堂店', '3:春江店', '1:大願寺店'}

list = glob.glob("./input/*.xlsx")


data_1 = pd.DataFrame()
data_2 = pd.DataFrame()
data_3 = pd.DataFrame()

for item in list:
    print("Preparing to read:"+str(item))
    try:
        data = pd.read_excel(item)
        for index,row in data.iterrows():
        if row["店舗"] == "1:大願寺店":
            data_1 = data_1.append(row,ignore_index=True)
        elif row["店舗"] == "2:花堂店":
            data_2 = data_2.append(row,ignore_index=True)
        elif row["店舗"] == "3:春江店":
            data_3 = data_3.append(row,ignore_index=True)
    except Exception as ex:
        print('can not read file {} {}'.format(item, ex))



# print(data_1)
# print(data_2)
# print(data_3)


"""
save to csv file


"""
output_path = "./output/"
if os.path.exists(os.path.dirname(output_path)) is False:
    try:
        os.makedirs(os.path.dirname(output_path))
    except OSError as ex:  # Guard against race condition
        raise ValueError('Folder is not exist {}'.format(output_path))
      
output1 ='output/1.csv'
output2 ='output/2.csv'
output3 ='output/3.csv'

data_1.to_csv(output)
data_1.to_csv(output)
data_1.to_csv(output)
