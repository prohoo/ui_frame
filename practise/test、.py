# dict = {'err_no': 0, 'err_str': 'OK', 'pic_id': '2194721260999960002', 'pic_str': '1062', 'md5': 'ef0fd1512fb13f78847562a0acf02f51'}
#
# print(dict["pic_str"])
#
# dict = {"a" : 1 ,"b":2}
# d={'key1':'value1','key2':'value2'}
# print(*d)
import os
from pathlib import Path

path = str(os.getcwd()+"")
print(path)

cuurent_path = str(Path(__file__).parent)
print(cuurent_path)