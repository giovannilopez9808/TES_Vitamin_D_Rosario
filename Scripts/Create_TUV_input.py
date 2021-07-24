import pandas as pd


def read_ozono_data(path="", file=""):
    data = pd.read_csv("{}{}".format(path,
                                     file))
    data["Date"] = pd.to_datetime(data["Date"])
    return data


def date_yymmdd(date):
    year = str(date.year)[2:4]
    month = format_number(date.month)
    day = format_number(date.day)
    date_format = year+month+day
    return date_format, str(date.year), str(date.month), str(date.day)


def format_number(number):
    return str(number).zfill(2)


parameters = {"path TUV": "TUV_model/",
              "path data": "../Data/Rosario_period/",
              "file ozono data": "data_ozono.csv",
              }
ozono_data = read_ozono_data(parameters["path data"],
                             parameters["file ozono data"])
file = open("{}datos.txt".format(parameters["path TUV"]),
            "w")
file.write("{}\n".format(len(ozono_data.index)))
for index in ozono_data.index:
    date = ozono_data["Date"][index]
    date, year, month, day = date_yymmdd(date)
    file.write("{} {} {} {} {}\n".format(date,
                                         ozono_data["Ozone"][index],
                                         year,
                                         month,
                                         day))
file.close()
