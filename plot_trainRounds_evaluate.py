#-*-coding:utf8-*-
__author__ = 'yjd '


import matplotlib.pyplot as plt


#添加图形属性
plt.xlabel('Number of rounds')
plt.ylabel('Predict evaluate')
plt.title('CNN---evaluate')
a = plt.subplot(1, 1, 1)

plt.ylim=(10, 40000)

x1 = [5, 10, 15, 20, 25]
x2 = [6, 11, 16, 21, 26]


Y1 = [0.3032, 0.4001, 0.4567, 0.4880, 0.5003]
Y2 = [0.6021, 0.7011, 0.7554, 0.7883, 0.8011]


#这里需要注意在画图的时候加上label在配合plt.legend（）函数就能直接得到图例，简单又方便！

plt.bar(x1, Y1, facecolor='red', width=1, label = 'samplesOf_100')

plt.bar(x2, Y2, facecolor='blue', width=1, label = 'samplesOf_150')

plt.legend()

plt.show()