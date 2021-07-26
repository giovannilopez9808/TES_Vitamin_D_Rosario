from os import listdir
import pandas as pd


parameters = {"path data": "../PreVitamin_D/Rosario/",
              "path results": "../Data/",
              "file results": "Daily_TUV_data.csv",
              }
files = sorted(listdir(parameters["path data"]))
file_result = open("{}{}".format(parameters["path results"],
                                 parameters["file results"]),
                   "w")
file_result.write("Date,SZA,UVI,Vitamin D\n")
for file in files:
    data = pd.read_csv("{}{}".format(parameters["path data"],
                                     file))
    uvi_max = data["UVI"].max()
    vitamin_max = data["Vitamin D"].max()
    sza_min = data["SZA"].min()
    file_result.write("{},{},{},{}\n".format(file.replace(".csv", ""),
                                             sza_min,
                                             uvi_max,
                                             vitamin_max))
file_result.close()
