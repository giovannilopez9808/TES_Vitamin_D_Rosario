from functions import *
import pandas as pd


parameters = {"path data": "../Data/",
              "file data": "Doses_time_RARG.csv",
              "seasons": {"winter": [pd.to_datetime("2019-06-21"),
                                     pd.to_datetime("2019-09-20")],
                          "summer": [pd.to_datetime("2019-12-21"),
                                     pd.to_datetime("2020-03-20")],
                          }
              }
data = read_data(parameters["path data"],
                 parameters["file data"])
for doses in data.columns:
    print("------------------------")
    print("Resultados para {}".format(doses))
    doses_data = data[doses]
    for season in parameters["seasons"]:
        print("Season: {}".format(season))
        dates = parameters["seasons"][season]
        season_data = select_data_from_date_period(doses_data,
                                                   dates[0],
                                                   dates[1])
        print("\tMean: {:.0f}".format(season_data.mean()))
        print("\tSTD: {:.0f}".format(season_data.std()))
