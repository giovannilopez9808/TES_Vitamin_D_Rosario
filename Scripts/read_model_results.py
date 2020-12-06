import numpy as np
from os import listdir
dir_tuv_results="../ResultadosTUV/"
dir_vitamin_d="../PreVitamin_D/"
dir_uv_index="../UV_index/"
files=listdir(dir_tuv_results)
for file in files:
    file_vitamin=open(dir_vitamin_d+file,"w")
    file_uv=open(dir_uv_index+file,"w")
    for _j in range(4):
        k=132+194*_j
        hour_list,data_uv_list,data_vitamin_list=np.loadtxt(dir_tuv_results+file,skiprows=k,usecols=[0,2,3],max_rows=60,dtype=str,unpack=True)
        for hour,data_uv,data_vitamin in zip(hour_list,data_uv_list,data_vitamin_list):
            file_vitamin.write(hour+" "+data_vitamin+"\n")
            file_uv.write(hour+" "+data_uv+"\n")
    file_vitamin.close()
    file_uv.close()