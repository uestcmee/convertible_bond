#coding:utf-8
import pandas as pd
import numpy as np
import time
io='.\data\\'

def read_csv_file(filename):
    csv_data=pd.read_csv(io+filename,header=0,index_col=0)
    #c0=csv_data.columns
    csv_data.index=pd.DatetimeIndex(csv_data.index)
    nrow=len(csv_data.index)
    ncol=len(csv_data.iloc[1,])
    print('原有公司数：{}'.format(ncol))
    # 删除空列
    zero_col=[]
    for col in range(ncol):
        if csv_data.iloc[:,col].any()==0:
            zero_col.append(csv_data.iloc[:,col].name)
    for col_name in zero_col:
        csv_data.pop(col_name)
    ncol=len(csv_data.iloc[1,])
    print('删除后剩余公司数：{}'.format(ncol))
    return csv_data


price_data=read_csv_file('price.csv')

due_flag={}
start_flag={}
for date in price_data.index:
    print(str(date)[:10])
    for company in price_data.columns:
        price = price_data.loc[date][company]
        # 如果价格变为-了
        if price==0:
            if start_flag.get(company)!=None:  # 如果已经之前在发行，现在认为到期，否则只是还没开始发行
                due_flag[company]=date
                start_flag[company]==None #如果已经停止发行，那么发行flag重置
                #print('{} due at {}'.format(company,date))
        else:
            # 认为在发行
            start_flag[company]=date
            if due_flag.get(company)!=None:
                print('found {},due at{},today{}'.format(company,due_flag[company],date))
                due_flag[company]=None