import matplotlib.pyplot as plt
import numpy as np
import datetime
meses = ["jun", "jul", "ago", "sep", "oct", "nov",
         "dic", "ene", "feb", "mar", "abr", "may", "jun"]
dir_vitamin_d = "../Data/Rosario_period/"
dir_graphics = "../Graphics/"
day_i = datetime.date(2019, 6, 1)
day_f = datetime.date(2020, 5, 31)
n_days = (day_f-day_i).days+1
date = np.loadtxt(dir_vitamin_d+"sza_vitamin_max.csv",
                  delimiter=",", skiprows=1, usecols=0, dtype=str)
data_vitamin = np.loadtxt(
    dir_vitamin_d+"sza_vitamin_max.csv", delimiter=",", skiprows=1, usecols=2)
data_Herman = np.loadtxt(
    dir_vitamin_d+"CIE_Herman_data.csv", delimiter=",", skiprows=1, unpack=True, usecols=1)
data_CIE_ver = np.loadtxt(
    dir_vitamin_d+"CIE_Herman_data.csv", delimiter=",", skiprows=21, unpack=True, usecols=0, max_rows=91)
data_CIE_inv = np.loadtxt(
    dir_vitamin_d+"CIE_Herman_data.csv", delimiter=",", skiprows=204, unpack=True, usecols=0, max_rows=91)
x = np.arange(n_days)
x2 = np.arange(91)
plt.scatter(x, data_vitamin, c="#f72585", label="Modelo TUV", marker=".")
plt.scatter(x, data_Herman, c="#3a0ca3", label="Herman", marker=".")
plt.scatter(x2[data_CIE_ver != 0]+20, data_CIE_ver[data_CIE_ver != 0],
            c="#185C27", label="CIE-WMO", marker=".")
plt.scatter(x2[data_CIE_inv != 0]+203, data_CIE_inv[data_CIE_inv != 0],
            c="#185C27", marker=".")
plt.ylabel("Irradiancia pre-vitamina D$_3$ (W/m$^2$)", fontsize=12)
plt.xlabel("Periodo 2019-2020", fontsize=12)
plt.xlim(0, n_days)
plt.ylim(0, 1)
plt.xticks(np.linspace(0, n_days, 13), meses, fontsize=12)
plt.yticks(np.arange(0, 1+0.1, 0.1), fontsize=12)
plt.grid(ls="--", color="grey", alpha=0.3)
plt.legend(frameon=False, ncol=3, markerscale=2)
plt.subplots_adjust(left=0.117, bottom=0.138, right=0.93, top=0.957)
plt.savefig(dir_graphics+"Previtamin_D.png", dpi=300)
plt.show()
