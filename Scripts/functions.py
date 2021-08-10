import pandas as pd


def select_data_from_date_period(data: pd.DataFrame, day_initial: str, day_final: str):
    """
    Obtiene los datos que estan contenidos en un periodo de tiempo
    """
    data = data[data.index.date >= day_initial]
    data = data[data.index.date <= day_final]
    return data


def date_to_yymmdd(date: pd.DataFrame):
    """
    Convierte la fecha de formato yyyy-mm-dd a yymmdd
    """
    year = str(date.year)[2:4]
    month = str(date.month).zfill(2)
    day = str(date.day).zfill(2)
    date = year+month+day
    return date, year, month, day


def obtain_xticks(dates: list):
    """
    Crea una lista con el primer día del mes a partir de una lista que contiene los dias de los datos
    """
    months = [obtain_first_date_for_month(dates[0])]
    for date in dates:
        if months[-1].month != date.month:
            date = obtain_first_date_for_month(date)
            months.append(date)
    year = months[-1].year
    month = months[-1].month+1
    if month > 12:
        month = 1
        year += 1
    date = pd.to_datetime("{}-{}-01".format(year,
                                            str(month).zfill(2)))
    months.append(date)
    months_names = obtain_month_names(months)
    return months, months_names


def obtain_first_date_for_month(date: pd.Timestamp):
    """
    Obtiene el primer dia del mes correspondiente a la fecha dada
    """
    year = date.year
    month = date.month
    date = pd.to_datetime("{}-{}-01".format(year,
                                            str(month).zfill(2)))
    return date


def obtain_month_names(dates: list):
    """
    Obtiene el nombre de los meses dadas las fechas
    """
    months_names = []
    for date in dates:
        months_names.append(date.strftime("%b"))
    return months_names


def read_data(path: str, file: str):
    """
    Lectura de los datos donde la columna de las fechas tiene como header Date
    """
    data = pd.read_csv("{}{}".format(path,
                                     file))
    data = format_data(data)
    return data


def format_data(data: pd.DataFrame):
    """
    Formato a la columna de fechas con header Date
    """
    data.index = pd.to_datetime(data["Date"])
    data = data.drop("Date", 1)
    return data


def format_CIE_data(data: pd.DataFrame):
    """
    Aplicar el valor correspondiente a los datos de UVI segun CIE para invierno y verano
    """
    seasons = {"winter": {"Period": [pd.to_datetime("2019-06-21"),
                                     pd.to_datetime("2019-09-20")],
                          "value": 1.6/40},
               "summer": {"Period": [pd.to_datetime("2019-12-21"),
                                     pd.to_datetime("2020-03-20")],
                          "value": 2/40
                          }
               }
    for date in data.index:
        value = data["CIE-2014"][date]
        for season in seasons:
            dataset = seasons[season]
            if date >= dataset["Period"][0] and date <= dataset["Period"][1]:
                data["CIE-2014"][date] = value * dataset["value"]
    # Drop zeros
    zeros = data[data["CIE-2014"] == 0]
    data = data.drop(zeros.index)
    return data
