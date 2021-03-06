import os
import glob
import pandas as pd
from datetime import datetime


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

#take columns values (header)
try:
    header = pd.read_excel(list[0]).columns.values
except Exception as ex:
        print('can not read file {} {}'.format(item, ex))


#output folder declare
output_path = "./output/"
if os.path.exists(os.path.dirname(output_path)) is False:
    try:
        os.makedirs(os.path.dirname(output_path))
    except OSError as ex:  # Guard against race condition
        raise ValueError('Folder is not exist {}'.format(output_path))


#output filename declare

output1 ='output/store1_2018.csv'
output2 ='output/store1_2017.csv'
output3 ='output/store1_2016.csv'
output4 ='output/store1_2015.csv'

output21 ='output/store2_2018.csv'
output22 ='output/store2_2017.csv'
output23 ='output/store2_2016.csv'
output24 ='output/store2_2015.csv'

output31 ='output/store3_2018.csv'
output32 ='output/store3_2017.csv'
output33 ='output/store3_2016.csv'
output34 ='output/store3_2015.csv'

for item in list:
    print("Reading:"+str(item))
    try:
        #create output dataframe
        data_1_2018 = pd.DataFrame(columns=header)
        data_1_2017 = pd.DataFrame(columns=header)
        data_1_2016 = pd.DataFrame(columns=header)
        data_1_2015 = pd.DataFrame(columns=header)

        data_2_2018 = pd.DataFrame(columns=header)
        data_2_2017 = pd.DataFrame(columns=header)
        data_2_2016 = pd.DataFrame(columns=header)
        data_2_2015 = pd.DataFrame(columns=header)

        data_3_2018 = pd.DataFrame(columns=header)
        data_3_2017 = pd.DataFrame(columns=header)
        data_3_2016 = pd.DataFrame(columns=header)
        data_3_2015 = pd.DataFrame(columns=header)

        #read input dataframe
        data = pd.read_excel(item)
        for index,row in data.iterrows():
            year = row['計上日付'].date().year
            if row["店舗"] == "1:大願寺店":
                if year == 2018 :
                    data_1_2018 = data_1_2018.append(row,ignore_index=True)
                elif year == 2017 :
                    data_1_2017 = data_1_2017.append(row,ignore_index=True)
                elif year == 2016 :
                    data_1_2016 = data_1_2016.append(row,ignore_index=True)
                elif year == 2015 :
                    data_1_2015 = data_1_2015.append(row,ignore_index=True)
            elif row["店舗"] == "2:花堂店":
                if year == 2018 :
                    data_2_2018 = data_2_2018.append(row,ignore_index=True)
                elif year == 2017 :
                    data_2_2017 = data_2_2017.append(row,ignore_index=True)
                elif year == 2016 :
                    data_2_2016 = data_2_2016.append(row,ignore_index=True)
                elif year == 2015 :
                    data_2_2015 = data_2_2015.append(row,ignore_index=True)
            elif row["店舗"] == "3:春江店":
                if year == 2018 :
                    data_3_2018 = data_3_2018.append(row,ignore_index=True)
                elif year == 2017 :
                    data_3_2017 = data_3_2017.append(row,ignore_index=True)
                elif year == 2016 :
                    data_3_2016 = data_3_2016.append(row,ignore_index=True)
                elif year == 2015 :
                    data_3_2015 = data_3_2015.append(row,ignore_index=True)

        print("Completed loading "+str(item)+"!")
        print("Saving to csv file...")
        data_1_2018.to_csv(output1,encoding="utf-8",mode="a",header=False)
        data_1_2017.to_csv(output2,encoding="utf-8",mode="a",header=False)
        data_1_2016.to_csv(output3,encoding="utf-8",mode="a",header=False)
        data_1_2015.to_csv(output4,encoding="utf-8",mode="a",header=False)

        data_2_2018.to_csv(output21,encoding="utf-8",mode="a",header=False)
        data_2_2017.to_csv(output22,encoding="utf-8",mode="a",header=False)
        data_2_2016.to_csv(output23,encoding="utf-8",mode="a",header=False)
        data_2_2015.to_csv(output24,encoding="utf-8",mode="a",header=False)

        data_3_2018.to_csv(output31,encoding="utf-8",mode="a",header=False)
        data_3_2017.to_csv(output32,encoding="utf-8",mode="a",header=False)
        data_3_2016.to_csv(output33,encoding="utf-8",mode="a",header=False)
        data_3_2015.to_csv(output34,encoding="utf-8",mode="a",header=False)
    except Exception as ex:
        print('can not read file {} {}'.format(item, ex))




print("All done!")
