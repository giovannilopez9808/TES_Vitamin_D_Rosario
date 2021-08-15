from Class_list import *
from functions import *


def obtain_RD(data: pd.DataFrame, datasets: dict):
    data["RD"] = (data[datasets["dataset1"]] -
                  data[datasets["dataset2"]])
    data["RD"] = data["RD"].abs()
    return data


parameters = {
    "path data": "../Data/",
    "file data": "Doses_time_",
    "city": "Rosario",
    "datasets": {"dataset1": "vitamin",
                 "dataset2": "1/4 MED"}
}
city_data = Citys_data(parameters["city"])
dataset = city_data.dataset
data = read_data(parameters["path data"],
                 "{}{}.csv".format(parameters["file data"],
                                   dataset["input file"]))
data = obtain_RD(data,
                 parameters["datasets"])
RD_mean = data["RD"].mean()
RD_std = data["RD"].std()
print("Diferencia:\n\tMean: {:.2f}\n\tStd: {:.2f}".format(RD_mean,
                                                          RD_std))
