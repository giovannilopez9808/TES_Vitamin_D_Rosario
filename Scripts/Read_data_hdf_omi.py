import numpy as np
import datetime
import h5py
import os


def date(day, year):
    """
    Formato a las fechas
    """
    # Calculo de la fecha
    date = datetime.date(year, 1, 1)+datetime.timedelta(days=day)
    # Distribucion dia,mes,año
    year, month, day = str(date.year)[2:4], date.month, date.day
    month = date_format(month)
    day = date_format(day)
    date = year+month+day
    return date


def date_format(number):
    """
    Formato de las fechas a dos digitos
    """
    return str(number).zfill(2)


def loc_grid(ini, data, n_grid):
    """
    Localizacion la celda en el archivo HDF
    """
    return int(np.abs(ini-data)/n_grid)


def conse_day(year, month, day, year_i):
    """
    Transformacion de fecha yyddmm a dia consecutivo
    """
    day_conse = (datetime.date(year, month, day) -
                 datetime.date(year, 1, 1)).days
    year += -year_i
    return day_conse, year


def obtain_yymmdd_from_name(name):
    date = name.split("-")[3]
    year = int(date[0:4])
    month = int(date[5:7])
    day = int(date[7:9])
    return year, month, day


def which_dataset(parameters):
    datasets = {"OMI": {"path data": "/HDFEOS/GRIDS/ColumnAmountAerosol/Data Fields/AbsorbingAerosolOpticalThicknessMW",
                        "version": "OMI/",
                        "filename": "AOD_OMI.csv",
                        "degrees": 0.25,
                        "scale factor": 0.001, },
                "OMI 500": {"path data": "/HDFEOS/GRIDS/Aerosol NearUV Grid/Data Fields/FinalAerosolOpticalDepth500",
                            "version": "OMI_500/",
                            "filename": "AOD_OMI_500.csv",
                            "degrees": 1,
                            "scale factor": 1, }

                }
    return datasets[parameters["dataset"]]


parameters = {"path data": "../Data/",
              "dataset": "OMI,",
              "lat": -32.946155,
              "lon": -60.681494,
              "year": 2019,
              }
dataset = which_dataset(parameters)
lat_loc = loc_grid(-90,
                   parameters["lat"],
                   dataset["degrees"])
lon_loc = loc_grid(-180,
                   parameters["lon"],
                   dataset["degrees"])
parameters["year"] = 2019
aod_data = np.zeros([365, 2])
files = os.listdir("{}{}".format(parameters["path data"],
                                 dataset["version"]))
print("Leyendo informacion")
for file in files:
    grid = h5py.File("{}{}{}".format(parameters["path data"],
                                     dataset["version"],
                                     file),
                     "r")
    # Extraccion de los valores
    if parameters["dataset"] == "OMI":
        dataset = (grid[dataset["path data"]][4])[
            lat_loc-1:lat_loc+2, lon_loc-1:lon_loc+2]
    else:
        dataset = (grid[dataset["path data"]])[
            lat_loc-1:lat_loc+1, lon_loc-1:lon_loc+1]
    values = dataset[dataset > 0]
    if np.size(values) != 0:
        year, month, day = obtain_yymmdd_from_name(file)
        # Dia consecutivo
        day, year = conse_day(year, month, day, parameters["year"])
        aod_data[day, year] = np.mean(values)*dataset["scale factor"]
print("Escribiendo archivo "+dataset["filename"])
file = open("{}{}".format(parameters["path data"],
                          dataset["filename"]),
            "w")
file.write("day,AOD\n")
for year in range(2):
    for day in range(365):
        if aod_data[day, year] != 0:
            date_name = date(day, year+parameters["year"])
            file.write("{},{:.3f}\n".format(date_name,
                                            aod_data[day, year]))
file.close()
