# 计算实验：测定空气的比热容比
import math

print('请输入每组的p1数据，单位kPa')
p1 = []
for i in range(0, 6):
    print('第 {} 组数据：'.format(i + 1))
    getp1 = float(input())
    p1.append(getp1)
print('请输入每组的p2数据，单位kPa')
p2 = []
for i in range(0, 6):
    print('第 {} 组数据：'.format(i + 1))
    getp2 = float(input())
    p2.append(getp2)

i = 0
r = []
for i in range(0, 6):
    getr = math.log((p1[i]/102)) / math.log((p1[i])/p2[i])
    r.append(getr)
    print('第 {} 组数据的空气比热容比为： {}'.format(i + 1, r[i]))
averr = (r[0] + r[1] + r[2] + r[3] + r[4] + r[5]) / 6
print('空气比热容平均数为', averr)

i = 0
a = 0
for i in range(0, 6):
    geta = pow(r[i] - averr, 2)
    a = a + geta
outa = pow(a / 30, 0.5)
print('A类不确定度为：', outa)
