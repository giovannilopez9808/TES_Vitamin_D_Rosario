import matplotlib.pyplot as plt
from functions import *
import pandas as pd


def obtain_filename_data(parameters: dict, ID: str):
    filename = "{}{}.csv".format(parameters["file data"],
                                 ID)
    return filename


def custom_sort_on_legend():
    handles, labels = plt.gca().get_legend_handles_labels()
    order = [2, 0, 1]
    plt.legend([handles[idx] for idx in order], [labels[idx] for idx in order],
               frameon=False,
               fontsize=11)


parameters = {"path data": "../Data/",
              "path graphics": "../Graphics/",
              "file data": "Doses_time_RARG.csv",
              "graphics name": "dosis_vitamin.png",
              "date initial": "2019-06-01",
              "date final": "2020-06-01",
              "Vitamin color": "#faa307",
              "Vitamin label": "1 MDD (136 J/m$^2$)",
              "1/4 MED color": "#e85d04",
              "1/4 MED label": "1/4 MED (62.5 J/m$^2$)",
              "1 MED color": "#9d0208",
              "1 MED label": "1 MED (250 J/m$^2$)",
              "dataset": {"AOD": "0.30",
                          "Ozone": "OMI"},
              }
data = read_data(parameters["path data"],
                 parameters["file data"])
months, months_names = obtain_xticks(data.index)
plt.plot(data.index, data["vitamin"],
         color=parameters["Vitamin color"],
         label=parameters["Vitamin label"],
         lw=1.5)
plt.fill_between(data.index, data["vitamin"],
                 data["1/4 MED"],
                 color="#faa307",
                 alpha=0.5)
plt.plot(data.index, data["1/4 MED"],
         color=parameters["1/4 MED color"],
         label=parameters["1/4 MED label"],
         lw=1.5)
plt.fill_between(data.index, data["vitamin"],
                 data["1 MED"],
                 color="#ffba08",
                 alpha=0.5)
plt.plot(data.index, data["1 MED"],
         color=parameters["1 MED color"],
         label=parameters["1 MED label"],
         lw=1.5)
plt.xticks(months,
           months_names)
plt.xlim(pd.to_datetime(parameters["date initial"]),
         pd.to_datetime(parameters["date final"]))
plt.xlabel("Periodo 2019-2020",
           fontsize=12)
plt.ylim(0, 80)
plt.yticks([tick for tick in range(0, 90, 10)])
plt.ylabel("TES (minutos)",
           fontsize=12)
# plt.title(title)
plt.grid(ls="--",
         color="grey",
         alpha=0.5)
plt.subplots_adjust(top=0.917,
                    bottom=0.132,
                    left=0.106,
                    right=0.958,
                    hspace=0.248,
                    wspace=0.2)
custom_sort_on_legend()
plt.tight_layout()
plt.savefig("{}{}".format(parameters["path graphics"],
                          parameters["graphics name"]),
            dpi=400)
