import numpy as np
import os

inputs = {
    "path data": "../PreVitamin_D/",
    "citys": ["Punta_Arenas/", "Santiago/"],
    "Dosis MED": 250,
    "Dosis Vitamin": 134,
}
for city in inputs["citys"]:
    path = inputs["path data"]+city
    files = sorted(os.listdir(path))
    for file in files:
        hours, uv_list = np.loadtxt(path+file,
                                    unpack=True,
                                    usecols=[0, 2],
                                    skiprows=1,
                                    delimiter=",")
        uv_list = uv_list/40
        pos_max = np.where(uv_list.max() == uv_list)[0][0]
        hour_i = hours[pos_max]
        hours = hours[pos_max:]
        uv_list = uv_list[pos_max:]
        sum_value = 0
        var = False
        n = 0
        while not var:
            sum_value += uv_list[n]*60
            #print(sum_value, inputs["Dosis MED"], hours[n])
            if sum_value > inputs["Dosis MED"]:
                time = int((hours[n]-hour_i)*60)+1
                var = True
            else:
                n += 1
        print("{}\t{}\t{}".format(file.split(".")[0], city, time))
