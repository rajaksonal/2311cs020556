import pandas as pd
screen_time=[2,4,6,8,9]
sleep_hours=[3,7,8,2,10]
stu_name=["sony","chinnu","bunny","sai","Adhi"]
dict1={
    "screen_time":screen_time,
    "sleep_hours":sleep_hours,
    "stu_name":stu_name,
}
print(dict1)
df = pd.DataFrame(dict1)
print(df)