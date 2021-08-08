from Class_list import Herman_equation
from functions import *
import pandas as pd


def read_SZA_data(path: str, file: str):
    data = read_data(path,
                     file)
    return data["SZA"]


parameters = {"path data": "../Data/",
              "ozone data": "ozone_data.csv",
              "SZA data": "Daily_TUV_data.csv",
              "file results": "Herman_data.csv"}
data = read_data(parameters["path data"],
                 parameters["ozone data"])
data["SZA"] = read_SZA_data(parameters["path data"],
                            parameters["SZA data"])
file = open("{}{}".format(parameters["path data"],
                          parameters["file results"]),
            "w")
file.write("Date,Herman\n")
for date in data.index:
    Herman_data = Herman_equation(data["SZA"][date],
                                  data["Ozone"][date])
    file.write("{},{:.5f}\n".format(date.date(),
                                    Herman_data.value))
file.close()
