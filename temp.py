import  re

时间消费额字典={'2020-11-1 11:11:11':2,'2020-11-2 11:11:11':1,'2020-11-3 11:11:11':2,'2020-12-1 11:11:11':2,'2020-12-1 11:11:11':2,'2020-12-1 11:11:11':2}



十一月份的消费总额 = 0

for key,value in 时间消费额字典.items():
    if bool(re.search('-11-',key)):
        十一月份的消费总额+=value
        # print(bool(re.search('-11-',key)))



print(十一月份的消费总额)
