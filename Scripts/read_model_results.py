import numpy as np
from os import listdir
dir_tuv_results = "../ResultadosTUV/"
dir_vitamin_d = "../PreVitamin_D/"
files = listdir(dir_tuv_results)
for file in files:
    file_vitamin = open(dir_vitamin_d+file[0:6]+".csv", "w")
    file_vitamin.write("hora,sza,uv,pre vitamina D\n")
    for _j in range(4):
        k = 132+194*_j
        hour_list, sza_list, uv_list, vitamin_list = np.loadtxt(
            dir_tuv_results+file, skiprows=k, max_rows=60, dtype=str, unpack=True)
        for hour, sza, data_uv, data_vitamin in zip(hour_list, sza_list, uv_list, vitamin_list):
            file_vitamin.write(hour+","+sza+","+data_uv+","+data_vitamin+"\n")
    file_vitamin.close()
