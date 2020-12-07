from os import listdir
import numpy as np
import datetime

def date_yymmdd(day,day_i):
    date=day_i+datetime.timedelta(days=day)
    year=str(date.year)[2:4]
    month=format_number(date.month)
    day=format_number(date.day)
    date=year+month+day
    return date

def format_number(number):
    if number<10:
        number_str="0"+str(number)
    else:
        number_str=str(number)
    return number_str

dir_vitamin_d="../PreVitamin_D/"
dir_results="../Data/Rosario_period/"
day_i=datetime.date(2019,6,1)
day_f=datetime.date(2020,5,31)
n_days=(day_f-day_i).days+1
files=np.sort(listdir(dir_vitamin_d))
file_result=open(dir_results+"sza_vitamin_max.csv","w")
file_result.write("Day,SZA,Pre vitamin\n")
for file in files:
    sza_list,vitamin_list=np.loadtxt(dir_vitamin_d+file,usecols=[1,2],delimiter=",",unpack=True)
    vitamin_max=np.max(vitamin_list)
    sza_max=np.max(sza_list[vitamin_max==vitamin_list])
    file_result.write(file[0:6]+","+str(sza_max)+","+str(vitamin_max)+"\n")
file_result.close()