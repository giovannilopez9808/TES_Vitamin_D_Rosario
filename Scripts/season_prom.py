from os import listdir
import numpy as np
import datetime

def consecutive_day(day,month,year):
    return (datetime.date(year,month,day)-datetime.date(year,1,1)).days

def results(data,text):
    mean=np.round(np.mean(data),2)
    std=np.round(np.std(data),2)
    print("  ",text,mean,std)

inv_days=[consecutive_day(21,6,2019),consecutive_day(21,9,2019)]
ver_days=[consecutive_day(21,12,2019),consecutive_day(21,3,2019)]
dir_data="../Data/Rosario_period/"
dates=np.loadtxt(dir_data+"dosis_time.csv",delimiter=",",skiprows=1,usecols=0,dtype=str)
vitamin_list,ertitemica_list=np.loadtxt(dir_data+"dosis_time.csv",delimiter=",",skiprows=1,usecols=[1,2],unpack=True)
ver_data_vitamin=[]
inv_data_vitamin=[]
ver_data_eritemica=[]
inv_data_eritemica=[]
for date,vitamin,eritemica in zip(dates,vitamin_list,ertitemica_list):
    year=int("20"+date[0:2])
    month=int(date[2:4])
    day=int(date[4:6])
    conse_day=consecutive_day(day,month,year)
    if inv_days[1]>=conse_day>=inv_days[0]:
        inv_data_vitamin=np.append(inv_data_vitamin,vitamin)
        inv_data_eritemica=np.append(inv_data_eritemica,eritemica)
    elif ver_days[0]>=conse_day<=ver_days[1]:
        ver_data_vitamin=np.append(ver_data_vitamin,vitamin)
        ver_data_eritemica=np.append(ver_data_eritemica,eritemica)
print("Vitamina")
results(inv_data_vitamin,"Invierno")
results(ver_data_vitamin,"Verano  ")
print("Eritemica")
results(inv_data_eritemica,"Invierno")
results(ver_data_eritemica,"Verano  ")