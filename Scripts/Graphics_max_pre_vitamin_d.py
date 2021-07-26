import matplotlib.pyplot as plt
from functions import *
import pandas as pd

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
            c="#5158BB",
            label="Modelo TUV",
            marker=".")
plt.scatter(data_Herman.index, data_Herman["Herman"],
            c="#000000",
            label="Herman",
            marker="+",
            alpha=0.75)
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
