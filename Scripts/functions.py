import pandas as pd


def select_data_from_date_period(data, day_initial, day_final):
    data = data[data.index.date >= day_initial]
    data = data[data.index.date <= day_final]
    return data


def date_to_yymmdd(date):
    year = str(date.year)[2:4]
    month = str(date.month).zfill(2)
    day = str(date.day).zfill(2)
    date = year+month+day
    return date, year, month, day


def obtain_xticks(dates):
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
    date = obtain_first_date_for_month(months[-1])
    months.append(date)
    months_names = obtain_month_names(months)
    return months, months_names


def obtain_first_date_for_month(date):
    year = date.year
    month = date.month
    date = pd.to_datetime("{}-{}-01".format(year,
                                            str(month).zfill(2)))
    return date


def obtain_month_names(dates):
    months_names = []
    for date in dates:
        months_names.append(date.strftime("%b"))
    return months_names


def read_data(path="", file=""):
    data = pd.read_csv("{}{}".format(path,
                                     file))
    data = format_data(data)
    return data


def format_data(data: pd.DataFrame()):
    data.index = pd.to_datetime(data["Date"])
    data = data.drop("Date", 1)
    return data


def format_CIE_data(data: pd.DataFrame()):
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
