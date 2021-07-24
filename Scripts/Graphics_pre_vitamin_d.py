import matplotlib.pyplot as plt
import numpy as np
import datetime


def part_period(data, skip):
    return data[skip:skip+91]


def RD(data1, data2, text_data1, text_data2, period):
    cond = data2 != 0
    rd = np.abs((data1[cond]-data2[cond])/data2[cond])*100
    rd = np.mean(rd)
    print("RD\t{}\t{}\t{}\t{:.2f}".format(period,
                                          text_data1,
                                          text_data2,
                                          rd))


def obtain_month_names():
    months = []
    for i in range(1, 13):
        date = datetime.date(2000, i, 1)
        months.append(date.strftime("%b"))
    for i in range(5):
        months.append(months[0])
        months.pop(0)
    months.append(months[0])
    return months


parameters = {"path data": "../Data/Rosario_period/",
              "file data": "sza_vitamin_max.csv",
              "Herman data": "Herman_data.csv",
              "CIE data": "CIE_data.csv",
              "path graphics": "../Graphics/",
              "date initial": datetime.date(2019, 6, 1),
              "date final": datetime.date(2020, 5, 31),
              "date winter": 20,
              "date summer": 203,
              }
month_names = obtain_month_names()
days = (parameters["date final"]-parameters["date initial"]).days+1
date = np.loadtxt("{}{}".format(parameters["path data"],
                                parameters["file data"]),
                  delimiter=",",
                  skiprows=1,
                  usecols=0,
                  dtype=str)
data_vitamin = np.loadtxt("{}{}".format(parameters["path data"],
                                        parameters["file data"]),
                          delimiter=",",
                          skiprows=1,
                          usecols=2)
data_Herman = np.loadtxt("{}{}".format(parameters["path data"],
                                       parameters["Herman data"]),
                         delimiter=",",
                         skiprows=1,
                         unpack=True,
                         usecols=0)
data_CIE_ver = np.loadtxt("{}{}".format(parameters["path data"],
                                        parameters["CIE data"]),
                          delimiter=",",
                          skiprows=parameters["date summer"]+1,
                          max_rows=91)*2/40
data_CIE_inv = np.loadtxt("{}{}".format(parameters["path data"],
                                        parameters["CIE data"]),
                          delimiter=",",
                          skiprows=parameters["date winter"]+1,
                          max_rows=91)*1.6/40
x = np.arange(days)
x2 = np.arange(91)
plt.scatter(x, data_vitamin,
            c="#5158BB",
            label="Modelo TUV",
            marker=".")
plt.scatter(x, data_Herman,
            c="#000000",
            label="Herman",
            marker=".")
plt.scatter(x2[data_CIE_ver != 0]+parameters["date summer"],
            data_CIE_ver[data_CIE_ver != 0],
            c="#33B62B",
            label="Coef. Prop.",
              marker=".")
plt.scatter(x2[data_CIE_inv != 0]+parameters["date winter"],
            data_CIE_inv[data_CIE_inv != 0],
            c="#33B62B",
            marker=".")
plt.ylabel("Irradiancia pre-vitamina D$_3$ (W/m$^2$)",
           fontsize=12)
plt.xlabel("Periodo 2019-2020",
           fontsize=12)
plt.xlim(0, days)
plt.ylim(0, 1)
plt.xticks(np.linspace(0, days, 13), month_names,
           fontsize=12)
plt.yticks(np.arange(0, 1+0.1, 0.1),
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
# plt.savefig(parameters["path graphics"]+"Previtamin_D.png",
#             dpi=300)
plt.show()

data_Herman_ver = part_period(data_Herman, parameters["date summer"])
data_vitamin_ver = part_period(data_vitamin, parameters["date summer"])
data_Herman_inv = part_period(data_Herman, parameters["date winter"])
data_vitamin_inv = part_period(data_vitamin, parameters["date winter"])
RD(data_vitamin_inv, data_CIE_inv, "TUV", "CIE", "Invierno")
RD(data_vitamin_ver, data_CIE_ver, "TUV", "CIE", "Verano\t")
RD(data_Herman_inv, data_CIE_inv, "Herman", "CIE", "Invierno")
RD(data_Herman_ver, data_CIE_ver, "Herman", "CIE", "Verano\t")
RD(data_Herman_inv, data_vitamin_inv, "Hermam", "TUV", "Invierno")
RD(data_Herman_ver, data_vitamin_ver, "Hermam", "TUV", "Verano\t")
