import matplotlib.pyplot as plt
from functions import *
import pandas as pd


parameters = {"path data": "../Data/",
              "path graphics": "../Graphics/",
              "file data": "doses_time.csv",
              "graphics name": "dosis_vitamin.png",
              "date initial": "2019-06-01",
              "date final": "2020-06-01",
              "Vitamin color": "#E7CA01",
              "Vitamin label": "Dosis pre-vitamina D 136 J/m$^2$",
              "MED color": "#fb8500",
              "MED label": "Dosis eritémica mínima 250 J/m$^2$",
              }
data = read_data(parameters["path data"],
                 parameters["file data"])
months, months_names = obtain_xticks(data.index)
plt.plot(data.index, data["vitamin"],
         color=parameters["Vitamin color"],
         label=parameters["Vitamin label"],
         lw=1.5)
plt.fill_between(data.index, data["vitamin"],
                 data["MED"],
                 color="#E7CA01",
                 alpha=0.5)
plt.plot(data.index, data["MED"],
         color=parameters["MED color"],
         label=parameters["MED label"],
         lw=1.5)
plt.xlim(pd.to_datetime(parameters["date initial"]),
         pd.to_datetime(parameters["date final"]))
plt.xticks(months,
           months_names)
plt.xlabel("Periodo 2019-2020",
           fontsize=12)
plt.ylim(0, 100)
plt.yticks([tick for tick in range(0, 110, 10)])
plt.ylabel("TES (minutos)",
           fontsize=12)
plt.grid(ls="--",
         color="grey",
         alpha=0.5)
plt.subplots_adjust(top=0.956,
                    bottom=0.132,
                    left=0.106,
                    right=0.958,
                    hspace=0.248,
                    wspace=0.2
                    )
plt.legend(frameon=False,
           fontsize=12)
plt.savefig("{}{}".format(parameters["path graphics"],
                          parameters["graphics name"]),
            dpi=400)
