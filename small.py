"""
Use "New Format Sparse T"
Download as csv
run python clean.py
"""
import pandas as pd
import sys
from dateutil.parser import parse
from glob import glob


def my_date_parse(d):
    try:
        return parse(" 1 ".join(d.split()))
    except:
        return d


def get_data(spec):
    data = pd.read_csv(
        spec,
        sep=",",
        thousands=',',
        skiprows=(0, 1),
        usecols=["Commodity","Country","Time","Quantity 1 (Gen)"],
        converters={"Time": my_date_parse, "Commodity": lambda s: s[:10]})
    # print(f"{spec}\t{len(data)}")
    return data


data = pd.concat([get_data(filename) for filename in glob("small/*.csv")])

# Clean
data.loc[data.Country == 'Korea, South', 'Country'] = 'South Korea'
data = data.rename(columns={"Quantity 1 (Gen)": "kgs"})
data = data.drop_duplicates()

# Sort
data = data.sort_values(by=["Time", "Country", "Commodity"])

# print(f"report\t{len(data)}")

# Write
data[["Commodity", "Country", "Time", "kgs"]].to_csv("small_report.csv", index=False)
