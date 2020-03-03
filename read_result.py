#coding:utf-8
import pandas as pd
import os
io='.\\result\\'

def read_csv_file(filename):
    csv_data=pd.read_csv(io+filename,encoding='gbk',header=0,index_col=0)
    #c0=csv_data.columns
    #csv_data.index=pd.DatetimeIndex(csv_data.index)
    return csv_data
pf=pd.DataFrame(index=[110+2*i for i in range(10)],columns=[130+2*i for i in range(10)])
print(pf)

for low in range(110,130,2):
    for high in range(130,150,2):
        file_name='result_{}_{}.csv'.format(low,high)
        # print(file_name)
        data=read_csv_file(file_name)
        #print(data)

        totr=float(data.iloc[-1][0])/10000
        pf.loc[low].loc[high]=totr

print(pf)
pf.to_csv('multi_result.csv')
