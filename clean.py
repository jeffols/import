"""
Use "New Format Sparse T"
Download as csv
run python clean.py
"""
import pandas as pd
import sys
from dateutil.parser import parse
from glob import glob

def my_parse(d):
    try:
        return parse(" 1 ".join(d.split()))
    except:
        return d

def get_data(spec):
    return pd.read_csv(
        spec,
        sep=",",
        thousands=',',
        skiprows=(0, 1),
        converters={0:my_parse, 2: lambda s: s[:10]})


data = pd.concat([get_data(filename) for filename in glob("raw/*.csv")])

# Clean
data.loc[data.Country == 'Korea, South', 'Country'] = 'South Korea'
data = data.rename(columns={"Quantity 1 (Gen)": "kgs"})

# Sort
data = data.sort_values(by=["Time", "Country", "Commodity"])
data = data.drop_duplicates()

# Write
data[["Time", "Country", "Commodity", "kgs"]].to_csv("report.csv", index=False)
