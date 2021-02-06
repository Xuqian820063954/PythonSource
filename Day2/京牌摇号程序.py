import random
import string
count=0
while count<3:
    List=[]
    for i in range(20):
        n1=random.choice(string.ascii_uppercase)
        n2="".join(random.sample(string.ascii_uppercase+string.digits,5))
        car_number=f"京{n1}-{n2}"
        List.append(car_number)
        print(car_number,end="   ")
        if i % 5 == 4:
            print()
    choice=input("输入你喜欢的号：")
    choice.strip()
    if choice in List:
        print(f"恭喜你选择了新车牌号:{choice}")
        exit("Good luck!")
    else:
        print("不合法的选择...")
    count += 1
