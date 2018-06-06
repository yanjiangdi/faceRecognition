#-*-coding:utf8-*-
__author__ = 'yjd '


import matplotlib.pyplot as plt
from pylab import *                                 #支持中文


names = ['1', '2', '3', '4', '5']
x = range(len(names))
y = [0.5011, 0.6001, 0.6651, 0.7101, 0.7378]
y1=[0.6501,0.7221,0.7781,0.8049,0.8193]
#plt.plot(x, y, 'ro-')
#plt.plot(x, y1, 'bo-')
#pl.xlim(-1, 11)  # 限定横轴的范围
#pl.ylim(-1, 110)  # 限定纵轴的范围
plt.plot(x, y, marker='o', mec='r', mfc='w',label=u'y=poolingOf_1')
plt.plot(x, y1, marker='*', ms=10,label=u'y=poolingOf_3')
plt.legend()  # 让图例生效
plt.xticks(x, names, rotation=45)
plt.margins(0)
plt.subplots_adjust(bottom=0.15)
plt.xlabel(u"convolution_count") #X轴标签
plt.ylabel("evaluate") #Y轴标签
plt.title("CNN_evaluate") #标题

plt.show()