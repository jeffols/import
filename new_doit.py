"""
Use "New Format Sparse T"
Download as csv
Remove last comma from line 3:
"Time","Country","Commodity","Quantity",
run python new_doit.py input.csv
"""
import pandas as pd
import sys
from dateutil.parser import parse

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

data = get_data(sys.argv[1])

data.loc[data.Country == 'Korea, South', 'Country'] = 'South Korea'
data = data.rename(columns={"Quantity 1 (Gen)": "kgs"})
data[["Time", "Country", "Commodity", "kgs"]].to_csv("cleaned_" + sys.argv[1], index=False)


