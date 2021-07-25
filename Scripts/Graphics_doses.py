import matplotlib.pyplot as plt
import numpy as np


def plot_grids(lim, div):
    for x in np.linspace(0, 366, 13):
        plt.plot([x, x], [0, lim],
                 ls="--",
                 color="grey",
                 alpha=0.5)
    for y in np.arange(0, lim+div, div):
        plt.plot([0, 366], [y, y],
                 ls="--",
                 color="grey",
                 alpha=0.5)


def plot_data(im, div, meses, days, title, color):
    plt.yticks(np.arange(0, lim+div, div),
               fontsize=11)
    plt.xlim(0, days)
    plt.ylim(0, lim)
    plt.xticks(np.linspace(0, days, 13), meses,
               fontsize=11)
    plt.ylabel("TES (minutos)",
               fontsize=12)
    plt.xlabel("Periodo 2019-2020",
               fontsize=12)
    plt.grid(ls="--",
             color="grey",
             alpha=0.5)


meses = ["jun", "jul", "ago", "sep", "oct", "nov",
         "dic", "ene", "feb", "mar", "abr", "may", "jun"]
dir_data = "../Data/Rosario_period/"
dir_graphics = "../Graphics/"
dates, time_vitamin, time_med = np.loadtxt(
    dir_data+"dosis_time.csv",
    delimiter=",",
    unpack=True,
    skiprows=1)
days = 366
title = "Dosis pre-vitamina D 136 J/m$^2$"
color = "#E7CA01"
plt.plot(np.arange(len(time_vitamin)), time_vitamin,
         color=color,
         label=title,
         lw=1.5)
plt.fill_between(np.arange(len(time_vitamin)), time_vitamin,
                 time_med,
                 color="#E7CA01",
                 alpha=0.5)
lim, div = 90, 10
title = "Dosis eritémica mínima 250 J/m$^2$"
color = "#fb8500"
plt.plot(np.arange(len(time_med)), time_med,
         color=color,
         label=title,
         lw=1.5)
plot_data(lim, div, meses, days, title, color)
plt.subplots_adjust(top=0.956,
                    bottom=0.132,
                    left=0.106,
                    right=0.958,
                    hspace=0.248,
                    wspace=0.2
                    )
plt.legend(frameon=False,
           fontsize=10)
# plt.savefig(dir_graphics+"dosis_vitamin.png",
#             dpi=300)
plt.show()
