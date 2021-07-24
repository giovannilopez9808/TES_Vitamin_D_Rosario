import matplotlib.pyplot as plt
import numpy as np
import datetime


def consecutive_day(month, day):
    day_conse = (datetime.date(2020, month, day) -
                 datetime.date(2020, 1, 1)).days
    return day_conse


def date_mmdd(day):
    date = datetime.date(2020, 1, 1)+datetime.timedelta(days=day)
    date = str(date.day)+"-"+date.strftime("%b")
    return date


dir_data = "../Data/Fire_period/"
files = ["data_OMI.csv", "data_OMI_500.csv"]
labels = ["OMI 448nm", "OMI 500nm"]

day_i = consecutive_day(6, 3)
day_f = consecutive_day(8, 31)
dates, num_inc = np.loadtxt("../Data/suomiNIA.txt", unpack=True)
num_inc = num_inc/(np.max(num_inc))
plt.plot(dates, num_inc, label="Incendios", color="red")

dates = np.loadtxt("{}{}".format(dir_data,
                                 "data_ozono_cf_ref.csv"),
                   delimiter=",",
                   usecols=0,
                   skiprows=1,
                   dtype=str)
reflectivity = np.loadtxt("{}{}".format(dir_data,
                                        "data_ozono_cf_ref.csv"),
                          delimiter=",",
                          usecols=3,
                          skiprows=1)
conse_day = []
reflectivity = reflectivity/(100)
for date in dates:
    conse_day = np.append(conse_day, consecutive_day(
        int(date[2:4]), int(date[4:6])))
# plt.plot(conse_day[reflectivity>0],reflectivity[reflectivity>0],label="Reflectividad",color="green")

dates = np.loadtxt(dir_data+"data_ozono_cf_ref.csv",
                   delimiter=",",
                   usecols=0,
                   skiprows=1,
                   dtype=str)
cloud_factor = np.loadtxt(dir_data+"data_ozono_cf_ref.csv",
                          delimiter=",",
                          usecols=2,
                          skiprows=1)
conse_day = []
print(np.max(cloud_factor))
for date in dates:
    conse_day = np.append(conse_day, consecutive_day(
        int(date[2:4]), int(date[4:6])))
plt.scatter(conse_day[cloud_factor >= 0],
            cloud_factor[cloud_factor >= 0], label="Cloud factor", color="green")

for file, label in zip(files, labels):
    dates = np.loadtxt(dir_data+file, delimiter=",",
                       skiprows=1, dtype=str, usecols=0)
    conse_day, aod = np.loadtxt("{}{}".format(dir_data, file),
                                delimiter=",",
                                unpack=True,
                                skiprows=1,
                                usecols=[1, 2])
    # plt.scatter(conse_day,aod,label=label)
days_select = np.arange(day_i, day_f, 6)
if not(day_f in days_select):
    days_select = np.append(days_select, day_f)
dates = []
for day_select in days_select:
    dates = np.append(dates, date_mmdd(int(day_select)))
plt.subplots_adjust(left=0.095,
                    bottom=0.16,
                    right=0.964,
                    top=0.94)
plt.ylim(0, 1)
plt.xlim(day_i, day_f)
plt.legend(ncol=4,
           mode="expand",
           frameon=False)
plt.xticks(days_select, dates,
           rotation=90)
plt.yticks(np.arange(0, 1.1, 0.1))
plt.grid(ls="--",
         alpha=0.5,
         color="grey")
plt.ylabel("AOD")
plt.show()
