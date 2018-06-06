#-*-coding:utf8-*-
__author__ = 'yjd '

import matplotlib.pyplot as plt
from pylab import *                                 #支持中文


names = [100, 200,300,400,500]
x = range(len(names))
y = [0.5011, 0.6001, 0.6451, 0.6701, 0.7078]
#plt.plot(x, y, 'ro-')
#plt.plot(x, y1, 'bo-')
#pl.xlim(-1, 11)  # 限定横轴的范围
#pl.ylim(-1, 110)  # 限定纵轴的范围
plt.plot(x, y, marker='o', mec='r', mfc='w')

plt.legend()  # 让图例生效
plt.xticks(x, names, rotation=45)
plt.margins(0)
plt.subplots_adjust(bottom=0.15)
plt.xlabel(u"train_Nums") #X轴标签
plt.ylabel("evaluate") #Y轴标签
plt.title("CNN_evaluate") #标题

plt.show()