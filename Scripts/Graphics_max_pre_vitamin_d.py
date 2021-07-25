import matplotlib.pyplot as plt
from functions import *
import pandas as pd
import numpy as np


def RD(data1, data2, text_data1, text_data2, period):
    cond = data2 != 0
    rd = np.abs((data1[cond]-data2[cond])/data2[cond])*100
    rd = np.mean(rd)
    print("RD\t{}\t{}\t{}\t{:.2f}".format(period,
                                          text_data1,
                                          text_data2,
                                          rd))


def format_CIE_data(data: pd.DataFrame()):
    seasons = {"winter": {"Period": [pd.to_datetime("2019-06-21"),
                                     pd.to_datetime("2019-09-20")],
                          "value": 1.6/40},
               "summer": {"Period": [pd.to_datetime("2019-12-21"),
                                     pd.to_datetime("2020-03-20")],
                          "value": 2/40
                          }
               }
    for date in data.index:
        value = data["CIE-2014"][date]
        for season in seasons:
            dataset = seasons[season]
            if date >= dataset["Period"][0] and date <= dataset["Period"][1]:
                data["CIE-2014"][date] = value * dataset["value"]
    # Drop zeros
    zeros = data[data["CIE-2014"] == 0]
    data = data.drop(zeros.index)
    return data


parameters = {"path data": "../Data/",
              "file data": "Daily_TUV_data.csv",
              "Herman data": "Herman_data.csv",
              "CIE data": "CIE_data.csv",
              "path graphics": "../Graphics/",
              "graphics name": "Max_previtamin_D.png",
              "date initial": "2019-06-01",
              "date final": "2020-05-31",
              "date winter": 20,
              "date summer": 203,
              }
data = read_data(parameters["path data"],
                 parameters["file data"])
data_Herman = read_data(parameters["path data"],
                        parameters["Herman data"])
data_CIE = read_data(parameters["path data"],
                     parameters["CIE data"])
data_CIE = format_CIE_data(data_CIE)
plt.scatter(data.index, data["Vitamin D"],
            c="#aaaff0",
            label="Modelo TUV",
            marker=".")
plt.scatter(data_Herman.index, data_Herman["Herman"],
            c="#000000",
            label="Herman",
            marker=".")
plt.scatter(data_CIE.index, data_CIE["CIE-2014"],
            c="#33B62B",
            label="Coef. Prop.",
              marker=".")
plt.xlim(pd.to_datetime(parameters["date initial"]),
         pd.to_datetime(parameters["date final"]))
months, month_names = obtain_xticks(data.index)
plt.xticks(months,
           month_names,
           fontsize=12)
plt.ylabel("Irradiancia pre-vitamina D$_3$ (W/m$^2$)",
           fontsize=12)
plt.xlabel("Periodo 2019-2020",
           fontsize=12)
plt.ylim(0, 1)
plt.yticks([tick/10 for tick in range(0, 11, 1)],
           fontsize=12)
plt.grid(ls="--",
         color="grey",
         alpha=0.3)
plt.legend(frameon=False,
           ncol=3,
           markerscale=2)
plt.subplots_adjust(top=0.954,
                    bottom=0.138,
                    left=0.126,
                    right=0.957,
                    hspace=0.2,
                    wspace=0.2
                    )
plt.savefig("{}{}".format(parameters["path graphics"],
                          parameters["graphics name"]),
            dpi=400)
# obtan_season_RD(data,data_CIE,)
# data_Herman_ver = part_period(data_Herman, parameters["date summer"])
# data_vitamin_ver = part_period(data_vitamin, parameters["date summer"])
# data_Herman_inv = part_period(data_Herman, parameters["date winter"])
# data_vitamin_inv = part_period(data_vitamin, parameters["date winter"])
# RD(data_vitamin_inv, data_CIE_inv, "TUV", "CIE", "Invierno")
# RD(data_vitamin_ver, data_CIE_ver, "TUV", "CIE", "Verano\t")
# RD(data_Herman_inv, data_CIE_inv, "Herman", "CIE", "Invierno")
# RD(data_Herman_ver, data_CIE_ver, "Herman", "CIE", "Verano\t")
# RD(data_Herman_inv, data_vitamin_inv, "Hermam", "TUV", "Invierno")
# RD(data_Herman_ver, data_vitamin_ver, "Hermam", "TUV", "Verano\t")
