import matplotlib.pyplot as plt

import numpy as np
def get_file(acc_list,loss_list,filename):
    f1 = open(filename, 'r')
    for line in f1.readlines():
        # print(line)
        line = line.strip('\n')
        str_list = line.split(':')

        loss = float(str_list[-2].split(',')[0])
        acc = float(str_list[-1])
        loss_list.append(acc)

        acc_list.append(loss)


baseline_acc=[]
baseline_loss=[]
dgc_acc=[]
dgc_loss=[]
ip_acc=[]
ip_loss=[]
rand_4_dgc_acc=[]
rand_4_dgc_loss=[]


# 获取acc,loss数据
get_file(baseline_acc,baseline_loss,'./cifar10/valid_cifar10_baseline.txt')
get_file(dgc_acc,dgc_loss,'./cifar10/valid_cifar10_dgc.txt')
get_file(ip_acc,ip_loss,'./cifar10/valid_cifar10_ip_optim.txt')
get_file(rand_4_dgc_acc,rand_4_dgc_loss,'./cifar10/valid_cifar10_rand_dgc_4.txt')


plt.figure()
number = 60
# 横坐标轴
x = [i for i in range(0,number)]

# 在绘制时设置lable, 逗号是必须的
# l1, = plt.plot(x, baseline_loss[0:94], label = 'line', color = 'b', linewidth = 1.0, linestyle = '-')
# l2, = plt.plot(x, dgc_loss[0:94], label = 'line', color = 'g', linewidth = 1.0, linestyle = '-')
# l3, = plt.plot(x, ip_loss[0:94], label = 'line', color = 'r', linewidth = 1.0, linestyle = '-')
# l4, = plt.plot(x, rand_4_dgc_loss[0:94], label = 'line', color = 'c', linewidth = 1.0, linestyle = '-')

l1, = plt.plot(x, baseline_acc[0:number], label = 'line', color = 'b', linewidth = 1.0, linestyle = '-')
l2, = plt.plot(x, dgc_acc[0:number], label = 'line', color = 'g', linewidth = 1.0, linestyle = '-')
l3, = plt.plot(x, ip_acc[0:number], label = 'line', color = 'r', linewidth = 1.0, linestyle = '-')
l4, = plt.plot(x, rand_4_dgc_acc[0:number], label = 'line', color = 'c', linewidth = 1.0, linestyle = '-')

# 设置坐标轴的lable
plt.xlabel('epoch')
# plt.ylabel('loss')
plt.ylabel('acc')
# 设置legend
plt.legend(handles = [l1, l2, l3,l4], labels = ['baseline', 'dgc','ip','rand_4_dgc'], loc = 'best')
plt.grid()
# plt.show()
# plt.savefig('loss.jpg')
plt.savefig('acc_cifar10.jpg')
