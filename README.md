https://usatrade.census.gov


[U.S. Steel Import Monitor](https://www.trade.gov/data-visualization/us-steel-import-monitor)
[Harmonized Terrif Schedule](https://hts.usitc.gov/search?query=7218)


[DuckDB csv Import](https://duckdb.org/docs/stable/data/csv/overview.html)


## Cold Rolled Strip

```
7220201010
7220201015
7220201060
7220201080
7220206005
7220206010
7220206015
7220206060
7220206080
7220207005
7220207010
7220207015
7220207060
7220207080
7220208000
7220209030
7220209060
7220900010
7220900015
7220900060
7220900080
```

## Stainless Cold Rolled Sheets

```
7219320005
7219320020
7219320025
7219320035
7219320036
7219320038
7219320042
7219320044
7219320045
7219320060
7219330005
7219330020
7219330025
7219330035
7219330036
7219330038
7219330042
7219330044
7219330045
7219330070
7219330080
7219340005
7219340020
7219340025
7219340030
7219340035
7219340050
7219350005
7219350015
7219350030
7219350035
7219350050
7219900010
7219900020
7219900025
7219900060
7219900080
```

```sql
Create Table data AS
  SELECT *
  FROM read_csv('report.csv',
      delim = ',',
      header = true,
      columns = {
          'Commodity': 'VARCHAR',
          'Country': 'VARCHAR',
          'Time': 'DATE',
          'kgs': 'INT'
      });

CREATE TABLE lookup AS
  SELECT  *
  FROM  read_csv(
          'hts_lookup.csv',
          delim = ',',
          header = false,
          columns = {
            'Commodity': 'VARCHAR',
            'Category': 'VARCHAR'
          });

```

```sql
create table test as
with source as (
  select 
    country
    ,time
    ,Commodity
    ,kgs from data 
  where Country = 'Taiwan' 
    and time >= '2024-01-01' 
    and time <= ' 2024-12-31' 
  order by 1, 2, 3
  )
select 
  lookup.Category
  ,source.Country
  ,source.Time
  ,SUM(source.kgs) / 1000 as tonnes
from source join lookup on source.Commodity = lookup.Commodity
group by 1, 2, 3
order by 1, 2, 3;
```
