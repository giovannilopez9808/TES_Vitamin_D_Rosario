from Class_list import *
from functions import *


def obtain_RD(data: pd.DataFrame, datasets: dict):
    data["RD"] = (data[datasets["dataset1"]] -
                  data[datasets["dataset2"]])
    data["RD"] = data["RD"].abs()
    return data


def print_results(mean: float, std: float):
    print("Diferencia:\n\tMean: {:.2f}\n\tStd: {:.2f}".format(mean,
                                                              std))


parameters = {
    "path data": "../Data/",
    "file data": "Doses_time_",
    "city": "Rosario",
    "seasons": {"winter": [pd.to_datetime("2019-06-21"),
                           pd.to_datetime("2019-09-20")],
                "summer": [pd.to_datetime("2019-12-21"),
                           pd.to_datetime("2020-03-20")],
                },
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
print_results(RD_mean, RD_std)
for season in parameters["seasons"]:
    dates = parameters["seasons"][season]
    data_season = select_data_from_date_period(data,
                                               dates[0],
                                               dates[1])
    RD_mean = data_season["RD"].mean()
    RD_std = data_season["RD"].std()
    print("-------------------------")
    print(season)
    print_results(RD_mean, RD_std)
