#coding:utf-8
import pandas as pd
import numpy as np
import time
io='.\data\\'


rating_data = pd.read_csv('./data/rating.csv', index_col=0)
# print(rating_data)
rating_list={}



def read_csv_file(filename):
    csv_data=pd.read_csv(io+filename,header=0,index_col=0)
    csv_data.index=pd.DatetimeIndex(csv_data.index)
    return csv_data



price_data=read_csv_file('price.csv')
rating_data.columns=price_data.columns

for company in rating_data.columns:
    rating = rating_data.loc['rating'][company]
    # if (rating_data.isnull().loc['rating'][company]):
    #     rating='AAA'
    if rating_list.get(rating)==None:
        rating_list[rating]=[company]
    else:
        rating_list[rating]+=[company]

for rate in rating_list:
    print(rate,rating_list[rate])
print( '1137.SH' in rating_list['A+']+rating_list['AAA'])
print(rating_list.keys())