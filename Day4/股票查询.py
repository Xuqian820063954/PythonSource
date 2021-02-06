import re
import operator

stock_list={}
valid_filter_columns={"当前价","涨跌幅","换手率"}
with open("stock_data", "r",encoding="utf-8") as file:
    header=file.readline().strip().split(',')
    header.insert(0,"序号")
    i=1
    for line in file:
        record=line.strip().split(',')
        code=record[0]
        record.insert(0,str(i))
        stock_list[code]=record
        i+=1
while True:
    count=0
    cmd=input("请输入您要查询的股票信息：").strip()
    #空输入判断
    if not cmd:
        print("输入为空，重新输入")
        continue
    #语义分析
    cmd_list=re.split("[<>]",cmd)
    #输入格式有误
    if len(cmd_list)>2:
        print("输入格式有误，应如：啤酒>30".center(50,'-'))
        continue
    #查询功能，输入命令只包含一个参数
    if len(cmd_list)==1:
        for code,row in stock_list.items():
            if cmd in row[2]:
                print(f"股票信息是：{row}")
                count+=1
    #筛选功能，输入命令格式：column >(或<) value
    else:
        filter_column,filter_value=cmd_list
        filter_value=float(filter_value)
        if filter_column not in valid_filter_columns:
            print("该字段不支持查询，目前只支持当前价、涨跌幅、换手率")
        column_index=header.index(filter_column)
        #筛选条件设置
        compare_function=operator.gt if '>' in cmd else operator.lt
        print(header)
        for code,row in stock_list.items():
            #获取某条记录的column_index值
            real_value=float(row[column_index].strip('%'))
            if not compare_function(real_value,filter_value):
                continue
            print(row)
            count+=1
    if count>0:
        print(f"找到{count}条")
    else:
        print("不存在满足条件的股票")



