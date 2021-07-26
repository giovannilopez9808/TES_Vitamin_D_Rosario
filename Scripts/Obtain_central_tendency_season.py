from functions import *
import pandas as pd


parameters = {"path data": "../Data/",
              "file data": "Daily_TUV_data.csv",
              "seasons": {"winter": [pd.to_datetime("2019-06-21"),
                                     pd.to_datetime("2019-09-20")],
                          "summer": [pd.to_datetime("2019-12-21"),
                                     pd.to_datetime("2020-03-20")],
                          }
              }
data = read_data(parameters["path data"],
                 parameters["file data"])
UVI_data = data["UVI"]
for season in parameters["seasons"]:
    print("Season: {}".format(season))
    dates = parameters["seasons"][season]
    season_data = select_data_from_date_period(UVI_data, dates[0], dates[1])
    print("\tMean: {:.3f}".format(season_data.mean()))
    print("\tSTD: {:.3f}".format(season_data.std()))
