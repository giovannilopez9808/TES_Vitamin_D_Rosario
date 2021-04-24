import matplotlib.pyplot as plt
import numpy as np
import datetime
#


def write_OMI(dir_data, data_name, file_name, lim_i, lim_f):
    date_list, aod_list = np.loadtxt(
        dir_data+data_name, delimiter=",", skiprows=lim_i, max_rows=lim_f-lim_i, dtype=str, unpack=True)
    data_file = open(dir_data+dir_files+file_name, "w")
    data_file.write("date,day consecutive,AOD\n")
    for date, aod in zip(date_list, aod_list):
        year = int("20"+date[0:2])
        month = int(date[2:4])
        day = int(date[4:6])
        data_file.write(date+","+conse_day(year, month, day)+","+aod+"\n")
    data_file.close()


def conse_day(year, month, day):
    day_conse = str((datetime.date(year, month, day) -
                     datetime.date(year, 1, 1)).days)
    return day_conse


dir_data = "../Data/"
dir_files = "Fire_period/"
day_ini = "200603"
day_lim = "200831"
year_i = 2020
# <--------------Recopilacion de los datos de ozono--------------->
data_name = "data_ozono_cf_ref.csv"
lim_i, lim_f = 6570, 6670
date_list, ozono_list, cloud_list, ref_surface_list = np.loadtxt(
    dir_data+"data_OMI_OMT03.dat", skiprows=lim_i, unpack=True, usecols=[0, 11, 15, 16], dtype=str, max_rows=lim_f-lim_i)
data_file = open(dir_data+dir_files+data_name, "w")
data_file.write("date,ozono,cloud factor,effective surface reflectivity\n")
for date, ozono, cloud, ref_surface in zip(date_list, ozono_list, cloud_list, ref_surface_list):
    data_file.write(date[2:8]+","+ozono+","+cloud+","+ref_surface+"\n")
data_file.close()
# <----------------Recopilacion de los datos de AOD 448 nm---------------->
lim_i, lim_f = 168, 201
file_name = "data_OMI.csv"
data_name = "AOD_OMI.csv"
write_OMI(dir_data, data_name, file_name, lim_i, lim_f)
# <----------------Recopilacion de los datos de AOD 500 nm------------->
lim_i, lim_f = 260, 303
file_name = "data_OMI_500.csv"
data_name = "AOD_OMI_500.csv"
write_OMI(dir_data, data_name, file_name, lim_i, lim_f)
