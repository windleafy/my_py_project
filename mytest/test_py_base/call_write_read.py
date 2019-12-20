from os.path import dirname, abspath

import base_kit.base_requests
from base_kit.base_urlopen import *
from base_kit.base_file import *
import json
import csv


# 案例：json2file
'''
my_data = {
    "details": {
        "data":
        [
            {
                "name": "zhangsan",
                "age": "14"
            },
            {
                "name": "lisi",
                "age": "15"
            },
            {
                "name": "wangwu",
                "age": "16"
            }
        ]
    },
    "status": "ok"
}
my_json_string = json.dumps(my_data)
file_path = "./outfile/wind2/"
file_name = "json2file.json"
json2file(my_json_string, file_path, file_name)
'''

# 案例：str_list2csv()
'''
data = ['1001,zhangsan', '1002,lisi', '1003,wangwu']
save_path = "./outfile/wind1/"
save_name = "list2txt.csv"
str_list2csv(data, save_path, save_name)
'''



# 案例：list2csv()

'''
class DataList2Csv:
    pass


data_1 = DataList2Csv
data_1.save_name = "./outfile/tmp/tmp.csv"
data_1.rows = [
   ['AA', 39.48, '6/11/2007', '9:36am', -0.18, 181800],
   ['AIG', 71.38, '6/11/2007', '9:36am', -0.15, 195500],
   ['AXP', 62.58, '6/11/2007', '9:36am', -0.46, 935000],
]
data_1.header = ['Symbol', 'Price', 'Date', 'Time', 'Change', 'Volume']
list2csv(data_1)
'''

# 案例：dict2csv()
'''
class DataDict2Csv:
    pass


data_2 = DataDict2Csv
data_2.file_name = "tmp3.csv"
data_2.file_path = "./outfile/tmp/wind2/"
data_2.rows = [
   {'Symbol': 'AA', 'Price': 39.48, 'Date': '6/11/2007',
    'Time': '9:36am', 'Change': -0.18, 'Volume': 181800},
   {'Symbol': 'AIG', 'Price': 71.38, 'Date': '6/11/2007',
    'Time': '9:36am', 'Change': -0.15, 'Volume': 195500},
   {'Symbol': '哈哈', 'Price': 62.58, 'Date': '6/11/2007',
    'Time': '9:36am', 'Change': -0.46, 'Volume': 935000},
]

data_2.header = ['Symbol', 'Price', 'Date', 'Time', 'Change', 'Volume']

new_item = {
    'Symbol': 'WindData',
    'Price': '56.32',
    'Date': '6/11/2007',
    'Time': '9:36am',
    'Change': -0.13,
    'Volume': 935000
}
data_2.rows.append(new_item)

dict_list2csv(data_2)
'''

# 案例：csv2list
'''
file_path = './outfile/tmp.csv'
header, data = csv2list(file_path)
if header:
    for i in data:
        print(i)
else:
    print('文件不存在')
'''

# 案例：json_file2dict
'''
file_path = './outfile/tmp.json'
json_dict = json_file2dict(file_path)
if json_dict:
    print(json_dict)
else:
    print('文件不存在')
'''

# 案例：路径处理
'''
# 取当前文件的绝对路径
path1 = dirname(abspath(__file__))
print(f"绝对路径：{path1}")

# 取当前文件的相对路径
path2 = os.path.relpath(path1, r'G:\PycharmProjects\mytest')
print(f"相对路径：{path2}")

# 取绝对路径与相对路径的差值
path3 = path1[0:path1.find(path2)]
print(f"差值路径：{path3}")
'''
