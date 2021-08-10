from Class_list import TUV_model, Citys_data
import pandas as pd
import os


def read_data(path: str, file: str):
    data = pd.read_csv("{}{}".format(path,
                                     file))
    data = format_data(data)
    return data


def format_data(data: pd.DataFrame):
    data.index = pd.to_datetime(data["Date"])
    data = data.drop("Date", 1)
    return data


def print_header_terminal(date: pd.Timestamp):
    text = "Calculando dia {}".format(date.date())
    print("="*len(text))
    print(text)


parameters = {
    "path data": "../Data/",
    "file data": "ozone_data.csv",
    # Direccion guardada en el archivo savout.f line 174
    "path results": "../PreVitamin_D/",
    "City": "Rosario",
    "hour initial": 11,
    "hour final": 19,
    "max rows": 60}
data = read_data(parameters["path data"],
                 parameters["file data"])
City_dataset = Citys_data(parameters["City"])
dataset = City_dataset.dataset
parameters["path results"] = "{}{}/".format(parameters["path results"],
                                            dataset["folder"])
dates = read_data(parameters["path data"],
                  dataset["file dates"])
for date in dates.index:
    print_header_terminal(date)
    file = open("{}{}.csv".format(parameters["path results"],
                                  date.date()),
                "w")
    file.write("Hour,SZA,UVI,Vitamin D\n")
    for hour in range(parameters["hour initial"], parameters["hour final"]):
        TUV = TUV_model(parameters["path results"],
                        dataset["input file"],
                        date,
                        data["Ozone"][date],
                        dataset["AOD"],
                        hour,
                        hour+1,
                        parameters["max rows"])
        TUV.run()
        for TUV_hour, TUV_sza, TUV_uvi, TUV_vitamin in zip(TUV.hours, TUV.sza, TUV.uvi, TUV.vitamin):
            file.write("{},{},{},{}\n".format(TUV_hour,
                                              TUV_sza,
                                              TUV_uvi,
                                              TUV_vitamin))
    file.close()
os.system("rm {}*.txt".format(parameters["path results"]))
print("\n")
