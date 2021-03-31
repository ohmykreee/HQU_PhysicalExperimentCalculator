# 计算实验：测定空气的比热容比
import math

# 得到实验数据
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

# 计算每一组的空气比热容比
i = 0
r = []
for i in range(0, 6):
    getr = math.log((p1[i]/102)) / math.log((p1[i])/p2[i])
    r.append(getr)
    print('第 {} 组数据的空气比热容比为： {}'.format(i + 1, r[i]))
print('空气比热容比大致在 1.3 左右，若相差较大请检查你的算式/输入数据等。')

# 覆写数据
ifOverride = input('是否覆写以上数据(y/n)？')
if ifOverride == 'y':
    i = 0
    for i in range(0, 6):
        r[i] = float(input('第 {} 组空气比热容比：'.format(i + 1)))
elif ifOverride == 'n':
    print('套用以上数据。')
else:
    print('无法识别的输入，套用以上数据。')

# 计算平均数
averr = (r[0] + r[1] + r[2] + r[3] + r[4] + r[5]) / 6
print('空气比热容平均数为', averr)

# 计算不确定度
i = 0
a = 0
for i in range(0, 6):
    geta = pow(r[i] - averr, 2)
    a = a + geta
outa = math.sqrt(a / 30)
print('A类不确定度为：', outa)
