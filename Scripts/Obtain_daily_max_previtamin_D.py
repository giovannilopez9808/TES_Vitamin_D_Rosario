from os import listdir
import pandas as pd


parameters = {"path data": "../PreVitamin_D/Rosario/",
              "path results": "../Data/",
              "file results": "Daily_max_pre_vitamin_D.csv",
              }
files = sorted(listdir(parameters["path data"]))
file_result = open("{}{}".format(parameters["path results"],
                                 parameters["file results"]),
                   "w")
file_result.write("Date,Vitamin D\n")
for file in files:
    data = pd.read_csv("{}{}".format(parameters["path data"],
                                     file))
    vitamin_max = data["Vitamin D"].max()
    file_result.write("{},{}\n".format(file.replace(".csv", ""),
                                       vitamin_max))
file_result.close()
