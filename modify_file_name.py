import os,re
dir='./result'
for low in range(110,130,2):
    for high in range(146,150,2):
        os.rename('./result/result初始策略修正{}_{}.csv'.format(low,high),'./result/result_{}_{}.csv'.format(low,high))
        file_name='./result/result_{}_{}.csv'.format(low,high)
        f=open(file_name,'r')
        lines=f.readlines()
        out_file_name = './result/Result_{}_{}.csv'.format(low, high)
        open(out_file_name,'w').close()
        fw = open(out_file_name, 'a')

        for line in lines:
            new_line=re.sub('(?<=\w)FULL_purchase_fail','',line)
            fw.write(new_line)
        fw.close()
