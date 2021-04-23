import numpy as np
import datetime

def date_yymmdd(day,day_i):
    date=day_i+datetime.timedelta(days=day)
    year=str(date.year)[2:4]
    month=format_number(date.month)
    day=format_number(date.day)
    date_format=year+month+day
    return date_format,str(date.year),str(date.month),str(date.day)

def format_number(number):
    if number<10:
        number_str="0"+str(number)
    else:
        number_str=str(number)
    return number_str

day_i=datetime.date(2019,6,1)
day_f=datetime.date(2020,5,31)
n_days=(day_f-day_i).days+1
dir_tuv="TUV_model/"
dir_data_o3="../Data/Rosario_period/"
ozono_data=np.loadtxt(dir_data_o3+"data_ozono.csv",delimiter=",",usecols=1,dtype=str,skiprows=1)
file=open(dir_tuv+"datos.txt","w")
file.write(str(int(n_days))+"\n")
for i_day,o3 in zip(range(n_days),ozono_data):
    date,year,month,day=date_yymmdd(i_day,day_i)
    file.write(date+" "+o3+" "+year+" "+month+" "+day+"\n")
file.close()