from functions import *
import pandas as pd
import numpy as np
import os


class Herman_equation:
    def __init__(self, sza: float, ozone: float):
        self.coeficients = {"RAF": {"a": 1.349378286522954,
                                    "b": -0.0002926808443875372,
                                    "c": -0.0003059282407232034,
                                    "d": 2.879164470755759e-8,
                                    "e": 1.920553492457117e-8,
                                    "f": -8.580442654658103e-13},
                            "U": {"a": 0.9659616883022778,
                                  "b": 0.0001089314449687077,
                                  "c": -0.0002681987275053843,
                                  "d": 1.410783665933483e-8,
                                  "e": 1.894213900598701e-8,
                                  "f": 1.695104643516458e-12}
                            }
        self.ozone = ozone
        self.sza = sza
        self.equation()

    def equation(self):
        raf = self.obtain_raf()
        u = self.obtain_u()
        self.value = u*(self.ozone/200)**(-raf)

    def obtain_raf(self):
        coeficient = self.coeficients["RAF"]
        return self.coeficients_equation(coeficient)

    def obtain_u(self):
        coeficient = self.coeficients["U"]
        return self.coeficients_equation(coeficient)

    def coeficients_equation(self, coeficient: dict):
        up = coeficient["a"]+coeficient["c"] * self.sza**2
        up += coeficient["e"]*self.sza**4
        down = 1+coeficient["b"]*self.sza**2
        down += coeficient["d"]*self.sza**4+coeficient["f"]*self.sza**6
        return up/down


class OMI_data:
    def __init__(self, path_data: str, file_name: str, day_initial: str, day_final: str):
        """
        Lectura de los datos de OMI recompilados.

        ### Inputs
        + `path_data` -> Direccion donde se encuetran los datos
        + `file_name` -> Nombre del archivo que contiene los datos
        + `day_initial` -> Dia inicial del perido de analisis
        + `day_final` -> Dia final del perido de analisis
        """
        self.path_data = path_data
        self.file_name = file_name
        self.day_initial = pd.to_datetime(day_initial)
        self.day_final = pd.to_datetime(day_final)
        self.read_data()

    def read_data(self):
        """
        Funcion que realiza la lectura de los datos y aplica el formato
        a las fechas
        """
        self.data = pd.read_fwf("{}{}.dat".format(self.path_data,
                                                  self.file_name),
                                skiprows=27)
        self.date_format()
        self.select_data_from_dates()

    def date_format(self):
        """
        Funcion que realiza el formato de fechas a los datos
        """
        self.data["Date"] = self.data["Datetime"].str[0:4]+"-" + \
            self.data["Datetime"].str[4:6]+"-"+self.data["Datetime"].str[6:8]
        self.data["Date"] = pd.to_datetime(self.data["Date"])
        self.data.index = self.data["Date"]
        self.data = self.data.drop(["Date", "Datetime"], 1)

    def select_data_from_dates(self):
        """
        Funcion que corta los datos en un periodo
        """
        self.data = select_data_from_date_period(self.data,
                                                 self.day_initial,
                                                 self.day_final)


class TUV_model:
    """
    Clase que ejecuta el modelo TUV dados el ozono,
    hora inicial, final, aod y fecha
    """

    def __init__(self, path: str, date: pd.Timestamp, ozone: float, aod: float, hour_i: int, hour_f: int, max_rows: int):
        self.max_rows = max_rows
        self.hour_i = hour_i
        self.hour_f = hour_f
        self.ozone = ozone
        self.date = date
        self.path = path
        self.aod = aod
        self.obtain_yymmdd_from_date()

    def obtain_yymmdd_from_date(self):
        """
        Obtiene el nombre de salida, año, mes y día a partir de la fecha
        """
        self.outfile, self.year, self.month, self.day = date_to_yymmdd(
            self.date)

    def run(self):
        """
        Ejecucion del modelo TUv
        """
        self.create_TUV_input()
        os.system("./TUV_model/tuv.out")
        self.read_results()

    def create_TUV_input(self):
        """
        Creación del TUV input con el formato
        Outfile Ozone AOD Year Month Day Hour_initial Hour_final
        """
        input_file = open("TUV_input.txt",
                          "w")
        input_file.write("{} {} {} 20{} {} {} {} {}".format(self.outfile,
                                                            self.ozone,
                                                            self.aod,
                                                            self.year,
                                                            self.month,
                                                            self.day,
                                                            self.hour_i,
                                                            self.hour_f))
        input_file.close()

    def read_results(self):
        """
        Lectura de los datos del TUV
        """
        skiprows = 132
        self.hours, self.sza, self.uvi, self.vitamin = np.loadtxt("{}{}.txt".format(self.path,
                                                                                    self.outfile),
                                                                  skiprows=skiprows,
                                                                  max_rows=self.max_rows,
                                                                  unpack=True)
