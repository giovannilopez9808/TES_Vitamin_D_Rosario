from os import listdir
import numpy as np
parameters = {"path results": "../ResultadosTUV/",
              "path pre vitamin D": "../PreVitamin_D/Rosario/",
              }
files = listdir(parameters["path results"])
for file in files:
    file_vitamin = open("{}{}".format(parameters["path pre vitamin D"],
                                      file.replace(".txt", ".csv")),
                        "w")
    file_vitamin.write("hora,sza,uv,pre vitamina D\n")
    for _j in range(8):
        k = 132+194*_j
        hour_list, sza_list, uv_list, vitamin_list = np.loadtxt("{}{}".format(parameters["path results"],
                                                                              file),
                                                                skiprows=k,
                                                                max_rows=60,
                                                                dtype=str,
                                                                unpack=True)
        for hour, sza, data_uv, data_vitamin in zip(hour_list, sza_list, uv_list, vitamin_list):
            file_vitamin.write("{},{},{},{}\n".format(hour,
                                                      sza,
                                                      data_uv,
                                                      data_vitamin))
    file_vitamin.close()
