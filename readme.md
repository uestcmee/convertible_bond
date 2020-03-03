# 0212转债回测结果 

[TOC]



## 1.数据情况

数据表包含的转债数量为**389**个，其中在整个回测期间均无数据的大致为**109**个，

由于四个不同的表中，数据全为0的转债个数并不相同，因此选择转债价格作为判断依据，认为当**转债价格**为0时，可转债到期

## 2.所用方法

1. 使用转债日度数据

2. 每个转债买入1000万，且最多持有十个转债

3. 买入策略

   1. 价格小于125时 且 溢价率小于25%
   2. 或
   3. 评级为AAA 且 到期收益率大于1.5% 且 转股溢价率小于40%

4. 卖出策略

   1. 债券到期（转债价格变为0）
   2. 或
   3. 价格超过140 或溢价率高于40%

   

## 3.回测结果

### 3.1转债指数&转债基金

1. 转债指数：使用[中证转债](http://www.csindex.com.cn/zh-CN/indices/index-detail/000832)作为参考，其五年期的指数走势如下图

![a5b881be889c6dd65788728dc21bfe5](C:\Users\zikep\AppData\Local\Temp\WeChat Files\a5b881be889c6dd65788728dc21bfe5.png)

2. 转债基金：使用[兴全可转债混合(340001)](http://fund.eastmoney.com/340001.html)，其五年期单位净值走势如下图

![73f0e759ab3a88eac0219dfa0d39fc1](C:\Users\zikep\AppData\Local\Temp\WeChat Files\73f0e759ab3a88eac0219dfa0d39fc1.png)

其五年期累计收益率如下图

![ca28ddfd0db7b5c92f4decddf99cb86](C:\Users\zikep\AppData\Local\Temp\WeChat Files\ca28ddfd0db7b5c92f4decddf99cb86.png)

### 3.2本次回测的结果

1. 以2015/1/5 为基准点计算的收益率

![1581444389524](C:\Users\zikep\AppData\Roaming\Typora\typora-user-images\1581444389524.png)

2. 每日较前一个交易日的日收益率

![1581444491051](C:\Users\zikep\AppData\Roaming\Typora\typora-user-images\1581444491051.png)

3. 每月5日较上个月环比收益率

![1581444541517](C:\Users\zikep\AppData\Roaming\Typora\typora-user-images\1581444541517.png)





## 4. 一些存在的问题

### 4.1前期收益率高的原因

由于前期一些转债会在两个交易日之间价值差距很大，例如格力转债（110030.SH）在2015年1月12日价格为100.0312，1月13日价格为138.26；使得本策略产生了很高的收益率

![da58f8b30cb734edfbc6915a9016bf3](C:\Users\zikep\AppData\Local\Temp\WeChat Files\da58f8b30cb734edfbc6915a9016bf3.png)

但是根据巨潮资讯关于[该转债的资料](http://www.cninfo.com.cn/information/bond/brief/110030.html)显示，该转债发行起始日为2014-12-25，上市日期为2015-01-13，因此该价格变化应该是由于转债上市发行所导致，不是很清楚这种价格波动是否应该纳入考虑。

### 4.2持有的转债数量少

在整个统计时间段内，可能由于购买的区间较窄，策略的结果中持有的债券支数的散点图如下图所示

![1581445081496](C:\Users\zikep\AppData\Roaming\Typora\typora-user-images\1581445081496.png)

整个回测时间内平均持有的转债支数约为**6.5**，大部分时候都没有达到10支的限制



附：输出结果