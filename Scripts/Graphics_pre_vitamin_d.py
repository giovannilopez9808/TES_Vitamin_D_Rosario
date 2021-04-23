import matplotlib.pyplot as plt
import numpy as np
import datetime


def part_period(data, skip):
    return data[skip:skip+91]


def RD(data1, data2, text_data1, text_data2, period):
    cond = data2 != 0
    rd = np.round(
        np.mean(np.abs((data1[cond]-data2[cond])/data2[cond])), 4)*100
    print("RD\t{}\t{}\t{}\t{:.2f}".format(period, text_data1, text_data2, rd))


meses = ["jun", "jul", "ago", "sep", "oct", "nov",
         "dic", "ene", "feb", "mar", "abr", "may", "jun"]
dir_vitamin_d = "../Data/Rosario_period/"
dir_graphics = "../Graphics/"
day_i = datetime.date(2019, 6, 1)
day_f = datetime.date(2020, 5, 31)
inv = 20
ver = 203
n_days = (day_f-day_i).days+1
date = np.loadtxt(dir_vitamin_d+"sza_vitamin_max.csv",
                  delimiter=",",
                  skiprows=1,
                  usecols=0,
                  dtype=str)
data_vitamin = np.loadtxt(
    dir_vitamin_d+"sza_vitamin_max.csv",
    delimiter=",",
    skiprows=1,
    usecols=2)
data_Herman = np.loadtxt(
    dir_vitamin_d+"Herman_data.csv",
    delimiter=",",
    skiprows=1,
    unpack=True,
    usecols=0)
data_CIE_ver = np.loadtxt(
    dir_vitamin_d+"CIE_data.csv",
    delimiter=",",
    skiprows=ver+1,
    max_rows=91)*2/40
data_CIE_inv = np.loadtxt(
    dir_vitamin_d+"CIE_data.csv",
    delimiter=",",
    skiprows=inv+1,
    max_rows=91)*1.6/40
x = np.arange(n_days)
x2 = np.arange(91)
plt.scatter(x, data_vitamin,
            c="#5158BB",
            label="Modelo TUV",
            marker=".")
plt.scatter(x, data_Herman,
            c="#000000",
            label="Herman",
            marker=".")
plt.scatter(x2[data_CIE_ver != 0]+ver, data_CIE_ver[data_CIE_ver != 0],
            c="#33B62B",
            label="Coef. Prop.",
              marker=".")
plt.scatter(x2[data_CIE_inv != 0]+inv, data_CIE_inv[data_CIE_inv != 0],
            c="#33B62B",
            marker=".")
plt.ylabel("Irradiancia pre-vitamina D$_3$ (W/m$^2$)",
           fontsize=12)
plt.xlabel("Periodo 2019-2020",
           fontsize=12)
plt.xlim(0, n_days)
plt.ylim(0, 1)
plt.xticks(np.linspace(0, n_days, 13), meses,
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
plt.savefig(dir_graphics+"Previtamin_D.png",
            dpi=300)
plt.show()

data_Herman_ver = part_period(data_Herman, ver)
data_vitamin_ver = part_period(data_vitamin, ver)
data_Herman_inv = part_period(data_Herman, inv)
data_vitamin_inv = part_period(data_vitamin, inv)
RD(data_vitamin_inv, data_CIE_inv, "TUV", "CIE", "Invierno")
RD(data_vitamin_ver, data_CIE_ver, "TUV", "CIE", "Verano")
RD(data_Herman_inv, data_CIE_inv, "Herman", "CIE", "Invierno")
RD(data_Herman_ver, data_CIE_ver, "Herman", "CIE", "Verano")
RD(data_Herman, data_vitamin, "Hermam", "TUV", "")
