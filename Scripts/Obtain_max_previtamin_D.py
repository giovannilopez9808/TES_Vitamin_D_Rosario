from os import listdir
import pandas as pd
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
    number_str = number
    number_str = number_str.zfill(2)
    return number_str


parameters = {"path data": "../PreVitamin_D/Rosario/",
              "path results": "../Data/",
              "file results": "Max_pre_vitamin_D.csv",
              "date initial": datetime.date(2019, 6, 1),
              "date final": datetime.date(2020, 5, 31)
              }
files = np.sort(listdir(parameters["path data"]))
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
