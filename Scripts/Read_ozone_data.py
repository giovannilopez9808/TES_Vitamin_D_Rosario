import pandas as pd
from numpy import nan


def read_OMI_data(path="", file=""):
    data = pd.read_fwf("{}{}".format(path,
                                     file),
                       skiprows=27)
    data = format_data(data)
    data = clean_data(data)
    return data


def format_data(data=pd.DataFrame()):
    data["Year"] = data["Datetime"].astype(str).str[0:4]
    data["Month"] = data["Datetime"].astype(str).str[4:6]
    data["Day"] = data["Datetime"].astype(str).str[6:8]
    data["Date"] = data["Year"]+"-"+data["Month"]+"-"+data["Day"]
    data.index = pd.to_datetime(data["Date"])
    return data


def clean_data(data=pd.DataFrame()):
    columns = data.columns
    data = data.drop(columns.drop("Ozone"), 1)
    data = data[data["Ozone"] < 400]
    data = data[data["Ozone"] > 200]
    return data


def select_data_from_period(data=pd.DataFrame(), date_initial="2020-01-01", date_final="2021-01-01"):
    data = data[data.index >= date_initial]
    data = data[data.index <= date_final]
    return data


def format_number(number):
    return str(number).zfill(2)


def obtain_mean(number1, number2):
    return (number1+number2)/2


parameters = {"path data": "../Data/",
              "path files": "Rosario_period/",
              "file data": "data_OMI_OMT03.dat",
              "filename": "data_ozono.csv",
              "date initial": "2019-06-01",
              "date final": "2020-05-31",
              }

data = read_OMI_data(parameters["path data"],
                     parameters["file data"])
data = select_data_from_period(data,
                               parameters["date initial"],
                               parameters["date final"])
data = data.resample("D").mean()
monthly_mean = data.resample("MS").mean()
data = data.fillna(-1)
for date in data.index:
    if data["Ozone"][date] == -1:
        index_i = date+pd.Timedelta(days=-1)
        index_f = date+pd.Timedelta(days=1)
        mean = obtain_mean(data["Ozone"][index_i],
                           data["Ozone"][index_f])
        data["Ozone"][date] = mean
data.to_csv("{}{}{}".format(parameters["path data"],
                            parameters["path files"],
                            parameters["filename"]),
            float_format="%.2f")
