import random
import string

worker_list = []
#员工录入
for i in range(300):#设置员工编号1~300
    worker_list.append(input("请输入员工姓名："))
#三等奖
third_prize=random.sample(worker_list,30)
for str in third_prize:
    worker_list.remove(str)
print("三等奖名单：")
for i in range(30):
    print(third_prize[i],end=",")
    if i%10==9:
        print()
print("恭喜获得奖品：避孕套⼀盒")
#二等奖
second_prize=random.sample(worker_list,6)
for str in second_prize:
    worker_list.remove(str)
str=",".join(second_prize)
print(f"二等奖名单：{str}")
print("恭喜获得奖品：IPhone手机")
#一等奖
first_prize=random.sample(worker_list,3)
str=",".join(first_prize)
print(f"一等奖名单：{str}")
print("恭喜获得奖品：泰国5日游")
