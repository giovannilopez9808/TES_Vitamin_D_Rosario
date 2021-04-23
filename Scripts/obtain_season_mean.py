import pandas as pd
import datetime
import os


def get_season(date):
    year = int("20"+date[0:2])
    month = int(date[2:4])
    day = int(date[4:6])
    date = datetime.date(year, month, day)
    seasons = {'Winter': (datetime.date(year, 6, 21),
                          datetime.date(year, 9, 22)),
               'Spring': (datetime.date(year, 9, 23),
                          datetime.date(year, 12, 20)),
               'Autumn': (datetime.date(year, 3, 21),
                          datetime.date(year, 6, 20))}
    for season, (season_start, season_end) in seasons.items():
        if date >= season_start and date <= season_end:
            return season
    else:
        return 'Summer'


inputs = {
    "path data": "../PreVitamin_D/Rosario/",
    "seasons": ["Summer",
                "Autumn",
                "Spring",
                "Winter"],
}
files = sorted(os.listdir(inputs["path data"]))
data_max = pd.DataFrame(columns=inputs["seasons"],
                        index=["Sum",
                               "Count"]).fillna(0.0)
for file in files:
    date = file.split(".")[0]
    season = get_season(date)
    data = pd.read_csv(inputs["path data"]+file)
    max_value = data.max()["uv"]/40
    data_max[season]["Sum"] = data_max[season]["Sum"]+max_value
    data_max[season]["Count"] = data_max[season]["Count"]+1
for season in inputs["seasons"]:
    data_max[season]["Sum"] = round(
        data_max[season]["Sum"]/data_max[season]["Count"], 2)
print(data_max)
