from os import listdir
import numpy as np
import datetime


def calc_dosis(hour, data, lim):
    var = False
    n = 0
    dosis = 0
    while var == False:
        dosis += data[n]*60
        if dosis > lim:
            var = True
        else:
            n += 1
    time = str(int((hour[n]-hour[0])*60)+1)
    return time


dir_data = "../PreVitamin_D/Rosario/"
dir_results = "../Data/Rosario_period/"
files = np.sort(listdir(dir_data))
dosis_vitamin = 136
dosis_med = 250
time_vitamin = []
time_med = []
file_result = open(dir_results+"dosis_time.csv", "w")
file_result.write("Dia,vitamin,MED\n")
for file in files:
    print(file)
    hour, uv_list, vitamin_list = np.loadtxt(dir_data+file,
                                             delimiter=",",
                                             skiprows=1,
                                             usecols=[0, 2, 3],
                                             unpack=True)
    time_vitamin = calc_dosis(hour, vitamin_list, dosis_vitamin)
    time_med = calc_dosis(hour, uv_list/40, dosis_med)
    file_result.write(file[0:6]+","+time_vitamin+","+time_med+"\n")
file_result.close()
