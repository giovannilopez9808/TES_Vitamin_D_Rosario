import matplotlib.pyplot as plt
import numpy as np
import datetime


def date_yymmdd(day, day_i):
    date = day_i+datetime.timedelta(days=day)
    year = str(date.year)[2:4]
    month = format_number(date.month)
    day = format_number(date.day)
    date = year+month+day
    return date


def format_number(number):
    if number < 10:
        number_str = "0"+str(number)
    else:
        number_str = str(number)
    return number_str


def conse_day(year, month, day, day_i):
    day_conse = (datetime.date(year, month, day)-day_i).days
    return day_conse


dir_data = "../Data/"
dir_files = "Rosario_period/"
day_i = datetime.date(2019, 6, 1)
day_f = datetime.date(2020, 5, 31)
n_days = (day_f-day_i).days+1
ozono_data = np.zeros([n_days, 2])
# <--------------Recopilacion de los datos de ozono--------------->
data_name = "data_ozono_cf_ref.csv"
lim_i, lim_f = 6174, 6570

date_list, ozono_list = np.loadtxt(dir_data+"data_OMI_OMT03.dat", skiprows=lim_i,
                                   unpack=True, usecols=[0, 11], dtype=str, max_rows=lim_f-lim_i)
for date, ozono in zip(date_list, ozono_list):
    if float(ozono) > 0:
        year = int(date[0:4])
        month = int(date[4:6])
        day = int(date[6:8])
        day_conse = conse_day(year, month, day, day_i)
        ozono_data[day_conse, 0] += float(ozono)
        ozono_data[day_conse, 1] += 1
n = 0
for ozono, count in ozono_data:
    if count != 0:
        ozono_data[n, 0] /= ozono_data[n, 1]
    n += 1
n = 0
for ozono, count in ozono_data:
    if count == 0:
        ozono_data[n, 0] = (ozono_data[n-1, 0]+ozono_data[n+1, 0])/2
    n += 1

data_file = open(dir_data+dir_files+data_name, "w")
data_file.write("date,ozono\n")
for day, ozono in zip(range(n_days), ozono_data[:, 0]):
    date = date_yymmdd(day, day_i)
    data_file.write(date+","+str(np.round(ozono, 2))+"\n")
data_file.close()
