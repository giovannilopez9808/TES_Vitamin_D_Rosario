import matplotlib.pyplot as plt
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
dir_graphics="../Graphics/"
day_i=datetime.date(2019,6,1)
day_f=datetime.date(2020,5,31)
n_days=(day_f-day_i).days+1
values_max=[]
files=np.sort(listdir(dir_vitamin_d))
for file in files:
    data=np.loadtxt(dir_vitamin_d+file,usecols=1)
    values_max=np.append(values_max,np.max(data))
x=np.arange(0,n_days,25)
x=np.append(x,n_days)
ticks=[]
for day in x:
    date=date_yymmdd(int(day),day_i)
    ticks=np.append(ticks,date)
plt.scatter(np.arange(n_days),values_max,color="#6a040f")
plt.xlim(0,n_days)
plt.ylim(0,1)
plt.xticks(x,ticks,rotation=60)
plt.yticks(np.arange(0,1+0.1,0.1))
plt.grid(ls="--",color="grey",alpha=0.3)
plt.subplots_adjust(left=0.114,bottom=0.171,right=0.945,top=0.94)
plt.savefig(dir_graphics+"Previtamin_D.png",dpi=300)