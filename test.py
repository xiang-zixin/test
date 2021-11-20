# -*- coding: utf-8 -*-
"""
Created on Thu Nov 18 16:49:43 2021

@author: HP
"""

import pandas as pd
import numpy as np
from netCDF4 import Dataset
import matplotlib.pyplot as plt
import matplotlib.mlab as mlab
from scipy.stats import norm
import math
# Data= pd.read_csv(r"./A2021001032500.L2_LAC_OC.nc", encoding="ISO-8859-1")
# data1=Data[Data['happen year']<2021]
# # data1=data1[data1['happen month']==1]
# data1.drop_duplicates(subset=['SID'],keep='first',inplace=True)


# # tem=np.zeros(80,dtype=int)
# tem=[]
# filename=r"./A2021001032500.L2_LAC_OC.nc"
# data2=Dataset(filename,encoding="ISO-8859-1")
# # print(data)
# for i in data2.variables.groups():
#     print(i)
    
# import h5py

# filename = r'./A2021001032500.L2_LACOC.nc'
# #filename = 'D:/d.hdf'

# f1 = h5py.File(filename,mode = 'r')

# #获取所有变量列表
# all_vars = list(f1.keys())

# #获取第4个变量的数据,并输出数据类型
# data = f1[all_vars[3]][:]
# print(type(data)) 
# f1.close()
# import h5py
# # import numpy as np

#                          #关闭文件

# #HDF5的读取：
# f = h5py.File(r'./A2021001032500.L2_LACOC.nc','r')   #打开h5文件
# # 可以查看所有的主键
# for key in f.keys():
#     print(f[key].name)
# #     # print(f[key].shape)
#     # print(f[key].value)

# Read HDF5 file.
# f = h5py.File(r'./A2021001032500.L2_LACOC.nc', "r")    # mode = {'w', 'r', 'a'}

	# Print the keys of groups and datasets under '/'.
# print(f.filename, ":")
# print([key for key in f.keys()], "\n")  

from netCDF4 import Dataset
# rootgrp = Dataset(r'./A2021001032500.L2_LACOC.nc')
# print(rootgrp.groups)
# for i in rootgrp.va
source_dataset = Dataset(r'./A2021001032500.L2_LACOC.nc')
source_geo_group = source_dataset['/geophysical_data/aot_869'][:]
print(source_geo_group)
# print(source_dataset)
# print(source_geo_group)
# print()
# print(source_geo_group.variables)
# print()
# a=source_geo_group['wavelength'][:]


