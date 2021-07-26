import matplotlib.pyplot as plt
from functions import *
import pandas as pd
import numpy as np


def obtain_RD_season(data1=pd.DataFrame(), data2=pd.DataFrame(), text1="", text2="", dates=[]):
    data1 = select_data_from_date_period(data1, dates[0], dates[1])
    data2 = select_data_from_date_period(data2, dates[0], dates[1])
    data1 = data1[data2.index]
    data1 = np.array(list(data1))
    data2 = np.array(list(data2))
    obtain_RD(data1,
              data2,
              text1,
              text2)


def obtain_RD(data1, data2, text1, text2):
    no_zeros = data2 != 0
    data1 = data1[no_zeros]
    data2 = data2[no_zeros]
    rd = np.abs((data1-data2)/data2)*100
    rd = np.mean(rd)
    print("\t{}\t{}\t{:.2f}".format(text1,
                                    text2,
                                    rd))


parameters = {"path data": "../Data/",
              "file data": "Daily_TUV_data.csv",
              "Herman data": "Herman_data.csv",
              "CIE data": "CIE_data.csv",
              "path graphics": "../Graphics/",
              "graphics name": "Max_previtamin_D.png",
              "date initial": "2019-06-01",
              "date final": "2020-05-31",
              "seasons": {"winter": [pd.to_datetime("2019-06-21"),
                                     pd.to_datetime("2019-09-20")],
                           "summer": [pd.to_datetime("2019-12-21"),
                                      pd.to_datetime("2020-03-20")],
                          }
              }
data = read_data(parameters["path data"],
                 parameters["file data"])
data_Herman = read_data(parameters["path data"],
                        parameters["Herman data"])
data_CIE = read_data(parameters["path data"],
                     parameters["CIE data"])
data_CIE = format_CIE_data(data_CIE)
for season in parameters["seasons"]:
    dates = parameters["seasons"][season]
    print("RD for {} season".format(season))
    obtain_RD_season(data["Vitamin D"],
                     data_CIE["CIE-2014"],
                     "TUV",
                     "CIE",
                     dates)
    obtain_RD_season(data_Herman["Herman"],
                     data_CIE["CIE-2014"],
                     "Herman",
                     "CIE",
                     dates)
    obtain_RD_season(data_Herman["Herman"],
                     data["Vitamin D"],
                     "Herman",
                     "TUV",
                     dates)
