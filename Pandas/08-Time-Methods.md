<h1>Table of Contents<span class="tocSkip"></span></h1>
<div class="toc"><ul class="toc-item"><li><span><a href="#Time-Methods" data-toc-modified-id="Time-Methods-1"><span class="toc-item-num">1&nbsp;&nbsp;</span>Time Methods</a></span><ul class="toc-item"><li><span><a href="#Python-Datetime-Review" data-toc-modified-id="Python-Datetime-Review-1.1"><span class="toc-item-num">1.1&nbsp;&nbsp;</span>Python Datetime Review</a></span></li></ul></li><li><span><a href="#Pandas" data-toc-modified-id="Pandas-2"><span class="toc-item-num">2&nbsp;&nbsp;</span>Pandas</a></span></li><li><span><a href="#Converting-to-datetime" data-toc-modified-id="Converting-to-datetime-3"><span class="toc-item-num">3&nbsp;&nbsp;</span>Converting to datetime</a></span><ul class="toc-item"><li><ul class="toc-item"><li><span><a href="#pd.to_datetime()" data-toc-modified-id="pd.to_datetime()-3.0.1"><span class="toc-item-num">3.0.1&nbsp;&nbsp;</span>pd.to_datetime()</a></span></li></ul></li><li><span><a href="#Custom-Time-String-Formatting" data-toc-modified-id="Custom-Time-String-Formatting-3.1"><span class="toc-item-num">3.1&nbsp;&nbsp;</span>Custom Time String Formatting</a></span></li><li><span><a href="#Data" data-toc-modified-id="Data-3.2"><span class="toc-item-num">3.2&nbsp;&nbsp;</span>Data</a></span></li><li><span><a href="#Attempt-to-Parse-Dates-Automatically" data-toc-modified-id="Attempt-to-Parse-Dates-Automatically-3.3"><span class="toc-item-num">3.3&nbsp;&nbsp;</span>Attempt to Parse Dates Automatically</a></span></li><li><span><a href="#Resample" data-toc-modified-id="Resample-3.4"><span class="toc-item-num">3.4&nbsp;&nbsp;</span>Resample</a></span></li></ul></li><li><span><a href="#.dt-Method-Calls" data-toc-modified-id=".dt-Method-Calls-4"><span class="toc-item-num">4&nbsp;&nbsp;</span>.dt Method Calls</a></span></li></ul></div>

# Time Methods

## Python Datetime Review

Basic Python outside of Pandas contains a datetime library:


```python
from datetime import datetime
```


```python
# To illustrate the order of arguments
my_year = 2017
my_month = 1
my_day = 2
my_hour = 13
my_minute = 30
my_second = 15
```


```python
# January 2nd, 2017
my_date = datetime(my_year,my_month,my_day)
```


```python
# Defaults to 0:00
my_date 
```




    datetime.datetime(2017, 1, 2, 0, 0)




```python
# January 2nd, 2017 at 13:30:15
my_date_time = datetime(my_year,my_month,my_day,my_hour,my_minute,my_second)
```


```python
my_date_time
```




    datetime.datetime(2017, 1, 2, 13, 30, 15)



You can grab any part of the datetime object you want


```python
my_date.day
```




    2




```python
my_date_time.hour
```




    13



# Pandas

# Converting to datetime

Often when data sets are stored, the time component may be a string. Pandas easily converts strings to datetime objects.


```python
import pandas as pd
```


```python
myser = pd.Series(['Nov 3, 2000', '2000-01-01', None])
```


```python
myser
```




    0    Nov 3, 2000
    1     2000-01-01
    2           None
    dtype: object




```python
myser[0]
```




    'Nov 3, 2000'



### pd.to_datetime()

https://pandas.pydata.org/pandas-docs/stable/user_guide/timeseries.html#converting-to-timestamps


```python
pd.to_datetime(myser)
```




    0   2000-11-03
    1   2000-01-01
    2          NaT
    dtype: datetime64[ns]




```python
pd.to_datetime(myser)[0]
```




    Timestamp('2000-11-03 00:00:00')




```python
obvi_euro_date = '31-12-2000'
```


```python
pd.to_datetime(obvi_euro_date) 
```




    Timestamp('2000-12-31 00:00:00')




```python
# 10th of Dec OR 12th of October?
# We may need to tell pandas
euro_date = '10-12-2000'
```


```python
pd.to_datetime(euro_date) 
```




    Timestamp('2000-10-12 00:00:00')




```python
pd.to_datetime(euro_date,dayfirst=True) 
```




    Timestamp('2000-12-10 00:00:00')



## Custom Time String Formatting

Sometimes dates can have a non standard format, luckily you can always specify to pandas the format. You should also note this could speed up the conversion, so it may be worth doing even if pandas can parse on its own.

A full table of codes can be found here: https://docs.python.org/3/library/datetime.html#strftime-and-strptime-format-codes


```python
style_date = '12--Dec--2000'
```


```python
pd.to_datetime(style_date, format='%d--%b--%Y')
```




    Timestamp('2000-12-12 00:00:00')




```python
strange_date = '12th of Dec 2000'
```


```python
pd.to_datetime(strange_date)
```




    Timestamp('2000-12-12 00:00:00')



## Data

Retail Sales: Beer, Wine, and Liquor Stores

Units:  Millions of Dollars, Not Seasonally Adjusted

Frequency:  Monthly


U.S. Census Bureau, Retail Sales: Beer, Wine, and Liquor Stores [MRTSSM4453USN], retrieved from FRED, Federal Reserve Bank of St. Louis; https://fred.stlouisfed.org/series/MRTSSM4453USN, July 2, 2020.


```python
sales = pd.read_csv('RetailSales_BeerWineLiquor.csv')
```


```python
sales
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>DATE</th>
      <th>MRTSSM4453USN</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1992-01-01</td>
      <td>1509</td>
    </tr>
    <tr>
      <th>1</th>
      <td>1992-02-01</td>
      <td>1541</td>
    </tr>
    <tr>
      <th>2</th>
      <td>1992-03-01</td>
      <td>1597</td>
    </tr>
    <tr>
      <th>3</th>
      <td>1992-04-01</td>
      <td>1675</td>
    </tr>
    <tr>
      <th>4</th>
      <td>1992-05-01</td>
      <td>1822</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>335</th>
      <td>2019-12-01</td>
      <td>6630</td>
    </tr>
    <tr>
      <th>336</th>
      <td>2020-01-01</td>
      <td>4388</td>
    </tr>
    <tr>
      <th>337</th>
      <td>2020-02-01</td>
      <td>4533</td>
    </tr>
    <tr>
      <th>338</th>
      <td>2020-03-01</td>
      <td>5562</td>
    </tr>
    <tr>
      <th>339</th>
      <td>2020-04-01</td>
      <td>5207</td>
    </tr>
  </tbody>
</table>
<p>340 rows × 2 columns</p>
</div>




```python
sales.iloc[0]['DATE']
```




    '1992-01-01'




```python
type(sales.iloc[0]['DATE'])
```




    str




```python
sales['DATE'] = pd.to_datetime(sales['DATE'])
```


```python
sales
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>DATE</th>
      <th>MRTSSM4453USN</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1992-01-01</td>
      <td>1509</td>
    </tr>
    <tr>
      <th>1</th>
      <td>1992-02-01</td>
      <td>1541</td>
    </tr>
    <tr>
      <th>2</th>
      <td>1992-03-01</td>
      <td>1597</td>
    </tr>
    <tr>
      <th>3</th>
      <td>1992-04-01</td>
      <td>1675</td>
    </tr>
    <tr>
      <th>4</th>
      <td>1992-05-01</td>
      <td>1822</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>335</th>
      <td>2019-12-01</td>
      <td>6630</td>
    </tr>
    <tr>
      <th>336</th>
      <td>2020-01-01</td>
      <td>4388</td>
    </tr>
    <tr>
      <th>337</th>
      <td>2020-02-01</td>
      <td>4533</td>
    </tr>
    <tr>
      <th>338</th>
      <td>2020-03-01</td>
      <td>5562</td>
    </tr>
    <tr>
      <th>339</th>
      <td>2020-04-01</td>
      <td>5207</td>
    </tr>
  </tbody>
</table>
<p>340 rows × 2 columns</p>
</div>




```python
sales.iloc[0]['DATE']
```




    Timestamp('1992-01-01 00:00:00')




```python
type(sales.iloc[0]['DATE'])
```




    pandas._libs.tslibs.timestamps.Timestamp



------

## Attempt to Parse Dates Automatically

**parse_dates** - bool or list of int or names or list of lists or dict, default False
The behavior is as follows:

    boolean. If True -> try parsing the index.

    list of int or names. e.g. If [1, 2, 3] -> try parsing columns 1, 2, 3 each as a separate date column.

    list of lists. e.g. If [[1, 3]] -> combine columns 1 and 3 and parse as a single date column.

    dict, e.g. {‘foo’ : [1, 3]} -> parse columns 1, 3 as date and call result ‘foo’

    If a column or index cannot be represented as an array of datetimes, say because of an unparseable value or a mixture of timezones, the column or index will be returned unaltered as an object data type. For non-standard datetime parsing, use pd.to_datetime after pd.read_csv. To parse an index or column with a mixture of timezones, specify date_parser to be a partially-applied pandas.to_datetime() with utc=True. See Parsing a CSV with mixed timezones for more.


```python
# Parse Column at Index 0 as Datetime
sales = pd.read_csv('RetailSales_BeerWineLiquor.csv',parse_dates=[0])
```


```python
sales
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>DATE</th>
      <th>MRTSSM4453USN</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1992-01-01</td>
      <td>1509</td>
    </tr>
    <tr>
      <th>1</th>
      <td>1992-02-01</td>
      <td>1541</td>
    </tr>
    <tr>
      <th>2</th>
      <td>1992-03-01</td>
      <td>1597</td>
    </tr>
    <tr>
      <th>3</th>
      <td>1992-04-01</td>
      <td>1675</td>
    </tr>
    <tr>
      <th>4</th>
      <td>1992-05-01</td>
      <td>1822</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>335</th>
      <td>2019-12-01</td>
      <td>6630</td>
    </tr>
    <tr>
      <th>336</th>
      <td>2020-01-01</td>
      <td>4388</td>
    </tr>
    <tr>
      <th>337</th>
      <td>2020-02-01</td>
      <td>4533</td>
    </tr>
    <tr>
      <th>338</th>
      <td>2020-03-01</td>
      <td>5562</td>
    </tr>
    <tr>
      <th>339</th>
      <td>2020-04-01</td>
      <td>5207</td>
    </tr>
  </tbody>
</table>
<p>340 rows × 2 columns</p>
</div>




```python
type(sales.iloc[0]['DATE'])
```




    pandas._libs.tslibs.timestamps.Timestamp



## Resample


A common operation with time series data is resampling based on the time series index. Let's see how to use the resample() method. [[reference](https://pandas.pydata.org/pandas-docs/stable/generated/pandas.DataFrame.resample.html)]


```python
# Our index
sales.index
```




    RangeIndex(start=0, stop=340, step=1)




```python
# Reset DATE to index
```


```python
sales = sales.set_index("DATE")
```


```python
sales
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>MRTSSM4453USN</th>
    </tr>
    <tr>
      <th>DATE</th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>1992-01-01</th>
      <td>1509</td>
    </tr>
    <tr>
      <th>1992-02-01</th>
      <td>1541</td>
    </tr>
    <tr>
      <th>1992-03-01</th>
      <td>1597</td>
    </tr>
    <tr>
      <th>1992-04-01</th>
      <td>1675</td>
    </tr>
    <tr>
      <th>1992-05-01</th>
      <td>1822</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
    </tr>
    <tr>
      <th>2019-12-01</th>
      <td>6630</td>
    </tr>
    <tr>
      <th>2020-01-01</th>
      <td>4388</td>
    </tr>
    <tr>
      <th>2020-02-01</th>
      <td>4533</td>
    </tr>
    <tr>
      <th>2020-03-01</th>
      <td>5562</td>
    </tr>
    <tr>
      <th>2020-04-01</th>
      <td>5207</td>
    </tr>
  </tbody>
</table>
<p>340 rows × 1 columns</p>
</div>



When calling `.resample()` you first need to pass in a **rule** parameter, then you need to call some sort of aggregation function.

The **rule** parameter describes the frequency with which to apply the aggregation function (daily, monthly, yearly, etc.)<br>
It is passed in using an "offset alias" - refer to the table below. [[reference](http://pandas.pydata.org/pandas-docs/stable/user_guide/timeseries.html#offset-aliases)]

The aggregation function is needed because, due to resampling, we need some sort of mathematical rule to join the rows (mean, sum, count, etc.)

<table style="display: inline-block">
    <caption style="text-align: center"><strong>TIME SERIES OFFSET ALIASES</strong></caption>
<tr><th>ALIAS</th><th>DESCRIPTION</th></tr>
<tr><td>B</td><td>business day frequency</td></tr>
<tr><td>C</td><td>custom business day frequency (experimental)</td></tr>
<tr><td>D</td><td>calendar day frequency</td></tr>
<tr><td>W</td><td>weekly frequency</td></tr>
<tr><td>M</td><td>month end frequency</td></tr>
<tr><td>SM</td><td>semi-month end frequency (15th and end of month)</td></tr>
<tr><td>BM</td><td>business month end frequency</td></tr>
<tr><td>CBM</td><td>custom business month end frequency</td></tr>
<tr><td>MS</td><td>month start frequency</td></tr>
<tr><td>SMS</td><td>semi-month start frequency (1st and 15th)</td></tr>
<tr><td>BMS</td><td>business month start frequency</td></tr>
<tr><td>CBMS</td><td>custom business month start frequency</td></tr>
<tr><td>Q</td><td>quarter end frequency</td></tr>
<tr><td></td><td><font color=white>intentionally left blank</font></td></tr></table>

<table style="display: inline-block; margin-left: 40px">
<caption style="text-align: center"></caption>
<tr><th>ALIAS</th><th>DESCRIPTION</th></tr>
<tr><td>BQ</td><td>business quarter endfrequency</td></tr>
<tr><td>QS</td><td>quarter start frequency</td></tr>
<tr><td>BQS</td><td>business quarter start frequency</td></tr>
<tr><td>A</td><td>year end frequency</td></tr>
<tr><td>BA</td><td>business year end frequency</td></tr>
<tr><td>AS</td><td>year start frequency</td></tr>
<tr><td>BAS</td><td>business year start frequency</td></tr>
<tr><td>BH</td><td>business hour frequency</td></tr>
<tr><td>H</td><td>hourly frequency</td></tr>
<tr><td>T, min</td><td>minutely frequency</td></tr>
<tr><td>S</td><td>secondly frequency</td></tr>
<tr><td>L, ms</td><td>milliseconds</td></tr>
<tr><td>U, us</td><td>microseconds</td></tr>
<tr><td>N</td><td>nanoseconds</td></tr></table>


```python
# Yearly Means
sales.resample(rule='A').mean()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>MRTSSM4453USN</th>
    </tr>
    <tr>
      <th>DATE</th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>1992-12-31</th>
      <td>1807.250000</td>
    </tr>
    <tr>
      <th>1993-12-31</th>
      <td>1794.833333</td>
    </tr>
    <tr>
      <th>1994-12-31</th>
      <td>1841.750000</td>
    </tr>
    <tr>
      <th>1995-12-31</th>
      <td>1833.916667</td>
    </tr>
    <tr>
      <th>1996-12-31</th>
      <td>1929.750000</td>
    </tr>
    <tr>
      <th>1997-12-31</th>
      <td>2006.750000</td>
    </tr>
    <tr>
      <th>1998-12-31</th>
      <td>2115.166667</td>
    </tr>
    <tr>
      <th>1999-12-31</th>
      <td>2206.333333</td>
    </tr>
    <tr>
      <th>2000-12-31</th>
      <td>2375.583333</td>
    </tr>
    <tr>
      <th>2001-12-31</th>
      <td>2468.416667</td>
    </tr>
    <tr>
      <th>2002-12-31</th>
      <td>2491.166667</td>
    </tr>
    <tr>
      <th>2003-12-31</th>
      <td>2539.083333</td>
    </tr>
    <tr>
      <th>2004-12-31</th>
      <td>2682.416667</td>
    </tr>
    <tr>
      <th>2005-12-31</th>
      <td>2797.250000</td>
    </tr>
    <tr>
      <th>2006-12-31</th>
      <td>3001.333333</td>
    </tr>
    <tr>
      <th>2007-12-31</th>
      <td>3177.333333</td>
    </tr>
    <tr>
      <th>2008-12-31</th>
      <td>3292.000000</td>
    </tr>
    <tr>
      <th>2009-12-31</th>
      <td>3353.750000</td>
    </tr>
    <tr>
      <th>2010-12-31</th>
      <td>3450.083333</td>
    </tr>
    <tr>
      <th>2011-12-31</th>
      <td>3532.666667</td>
    </tr>
    <tr>
      <th>2012-12-31</th>
      <td>3697.083333</td>
    </tr>
    <tr>
      <th>2013-12-31</th>
      <td>3839.666667</td>
    </tr>
    <tr>
      <th>2014-12-31</th>
      <td>4023.833333</td>
    </tr>
    <tr>
      <th>2015-12-31</th>
      <td>4212.500000</td>
    </tr>
    <tr>
      <th>2016-12-31</th>
      <td>4434.416667</td>
    </tr>
    <tr>
      <th>2017-12-31</th>
      <td>4602.666667</td>
    </tr>
    <tr>
      <th>2018-12-31</th>
      <td>4830.666667</td>
    </tr>
    <tr>
      <th>2019-12-31</th>
      <td>4972.750000</td>
    </tr>
    <tr>
      <th>2020-12-31</th>
      <td>4922.500000</td>
    </tr>
  </tbody>
</table>
</div>



Resampling rule 'A' takes all of the data points in a given year, applies the aggregation function (in this case we calculate the mean), and reports the result as the last day of that year. Note 2020 in this data set was not complete.

# .dt Method Calls

Once a column or index is ina  datetime format, you can call a variety of methods off of the .dt library inside pandas:

https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.Series.dt.html


```python
sales = sales.reset_index()
```


```python
sales
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>DATE</th>
      <th>MRTSSM4453USN</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1992-01-01</td>
      <td>1509</td>
    </tr>
    <tr>
      <th>1</th>
      <td>1992-02-01</td>
      <td>1541</td>
    </tr>
    <tr>
      <th>2</th>
      <td>1992-03-01</td>
      <td>1597</td>
    </tr>
    <tr>
      <th>3</th>
      <td>1992-04-01</td>
      <td>1675</td>
    </tr>
    <tr>
      <th>4</th>
      <td>1992-05-01</td>
      <td>1822</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>335</th>
      <td>2019-12-01</td>
      <td>6630</td>
    </tr>
    <tr>
      <th>336</th>
      <td>2020-01-01</td>
      <td>4388</td>
    </tr>
    <tr>
      <th>337</th>
      <td>2020-02-01</td>
      <td>4533</td>
    </tr>
    <tr>
      <th>338</th>
      <td>2020-03-01</td>
      <td>5562</td>
    </tr>
    <tr>
      <th>339</th>
      <td>2020-04-01</td>
      <td>5207</td>
    </tr>
  </tbody>
</table>
<p>340 rows × 2 columns</p>
</div>




```python
help(sales['DATE'].dt)
```

    Help on DatetimeProperties in module pandas.core.indexes.accessors object:
    
    class DatetimeProperties(Properties)
     |  Accessor object for datetimelike properties of the Series values.
     |  
     |  Examples
     |  --------
     |  >>> s.dt.hour
     |  >>> s.dt.second
     |  >>> s.dt.quarter
     |  
     |  Returns a Series indexed like the original Series.
     |  Raises TypeError if the Series does not contain datetimelike values.
     |  
     |  Method resolution order:
     |      DatetimeProperties
     |      Properties
     |      pandas.core.accessor.PandasDelegate
     |      pandas.core.base.PandasObject
     |      pandas.core.accessor.DirNamesMixin
     |      pandas.core.base.NoNewAttributesMixin
     |      builtins.object
     |  
     |  Methods defined here:
     |  
     |  ceil(self, *args, **kwargs)
     |      Perform ceil operation on the data to the specified `freq`.
     |      
     |      Parameters
     |      ----------
     |      freq : str or Offset
     |          The frequency level to ceil the index to. Must be a fixed
     |          frequency like 'S' (second) not 'ME' (month end). See
     |          :ref:`frequency aliases <timeseries.offset_aliases>` for
     |          a list of possible `freq` values.
     |      ambiguous : 'infer', bool-ndarray, 'NaT', default 'raise'
     |          Only relevant for DatetimeIndex:
     |      
     |          - 'infer' will attempt to infer fall dst-transition hours based on
     |            order
     |          - bool-ndarray where True signifies a DST time, False designates
     |            a non-DST time (note that this flag is only applicable for
     |            ambiguous times)
     |          - 'NaT' will return NaT where there are ambiguous times
     |          - 'raise' will raise an AmbiguousTimeError if there are ambiguous
     |            times.
     |      
     |          .. versionadded:: 0.24.0
     |      
     |      nonexistent : 'shift_forward', 'shift_backward', 'NaT', timedelta, default 'raise'
     |          A nonexistent time does not exist in a particular timezone
     |          where clocks moved forward due to DST.
     |      
     |          - 'shift_forward' will shift the nonexistent time forward to the
     |            closest existing time
     |          - 'shift_backward' will shift the nonexistent time backward to the
     |            closest existing time
     |          - 'NaT' will return NaT where there are nonexistent times
     |          - timedelta objects will shift nonexistent times by the timedelta
     |          - 'raise' will raise an NonExistentTimeError if there are
     |            nonexistent times.
     |      
     |          .. versionadded:: 0.24.0
     |      
     |      Returns
     |      -------
     |      DatetimeIndex, TimedeltaIndex, or Series
     |          Index of the same type for a DatetimeIndex or TimedeltaIndex,
     |          or a Series with the same index for a Series.
     |      
     |      Raises
     |      ------
     |      ValueError if the `freq` cannot be converted.
     |      
     |      Examples
     |      --------
     |      **DatetimeIndex**
     |      
     |      >>> rng = pd.date_range('1/1/2018 11:59:00', periods=3, freq='min')
     |      >>> rng
     |      DatetimeIndex(['2018-01-01 11:59:00', '2018-01-01 12:00:00',
     |                     '2018-01-01 12:01:00'],
     |                    dtype='datetime64[ns]', freq='T')
     |      >>> rng.ceil('H')
     |      DatetimeIndex(['2018-01-01 12:00:00', '2018-01-01 12:00:00',
     |                     '2018-01-01 13:00:00'],
     |                    dtype='datetime64[ns]', freq=None)
     |      
     |      **Series**
     |      
     |      >>> pd.Series(rng).dt.ceil("H")
     |      0   2018-01-01 12:00:00
     |      1   2018-01-01 12:00:00
     |      2   2018-01-01 13:00:00
     |      dtype: datetime64[ns]
     |  
     |  day_name(self, *args, **kwargs)
     |      Return the day names of the DateTimeIndex with specified locale.
     |      
     |      .. versionadded:: 0.23.0
     |      
     |      Parameters
     |      ----------
     |      locale : str, optional
     |          Locale determining the language in which to return the day name.
     |          Default is English locale.
     |      
     |      Returns
     |      -------
     |      Index
     |          Index of day names.
     |      
     |      Examples
     |      --------
     |      >>> idx = pd.date_range(start='2018-01-01', freq='D', periods=3)
     |      >>> idx
     |      DatetimeIndex(['2018-01-01', '2018-01-02', '2018-01-03'],
     |                    dtype='datetime64[ns]', freq='D')
     |      >>> idx.day_name()
     |      Index(['Monday', 'Tuesday', 'Wednesday'], dtype='object')
     |  
     |  floor(self, *args, **kwargs)
     |      Perform floor operation on the data to the specified `freq`.
     |      
     |      Parameters
     |      ----------
     |      freq : str or Offset
     |          The frequency level to floor the index to. Must be a fixed
     |          frequency like 'S' (second) not 'ME' (month end). See
     |          :ref:`frequency aliases <timeseries.offset_aliases>` for
     |          a list of possible `freq` values.
     |      ambiguous : 'infer', bool-ndarray, 'NaT', default 'raise'
     |          Only relevant for DatetimeIndex:
     |      
     |          - 'infer' will attempt to infer fall dst-transition hours based on
     |            order
     |          - bool-ndarray where True signifies a DST time, False designates
     |            a non-DST time (note that this flag is only applicable for
     |            ambiguous times)
     |          - 'NaT' will return NaT where there are ambiguous times
     |          - 'raise' will raise an AmbiguousTimeError if there are ambiguous
     |            times.
     |      
     |          .. versionadded:: 0.24.0
     |      
     |      nonexistent : 'shift_forward', 'shift_backward', 'NaT', timedelta, default 'raise'
     |          A nonexistent time does not exist in a particular timezone
     |          where clocks moved forward due to DST.
     |      
     |          - 'shift_forward' will shift the nonexistent time forward to the
     |            closest existing time
     |          - 'shift_backward' will shift the nonexistent time backward to the
     |            closest existing time
     |          - 'NaT' will return NaT where there are nonexistent times
     |          - timedelta objects will shift nonexistent times by the timedelta
     |          - 'raise' will raise an NonExistentTimeError if there are
     |            nonexistent times.
     |      
     |          .. versionadded:: 0.24.0
     |      
     |      Returns
     |      -------
     |      DatetimeIndex, TimedeltaIndex, or Series
     |          Index of the same type for a DatetimeIndex or TimedeltaIndex,
     |          or a Series with the same index for a Series.
     |      
     |      Raises
     |      ------
     |      ValueError if the `freq` cannot be converted.
     |      
     |      Examples
     |      --------
     |      **DatetimeIndex**
     |      
     |      >>> rng = pd.date_range('1/1/2018 11:59:00', periods=3, freq='min')
     |      >>> rng
     |      DatetimeIndex(['2018-01-01 11:59:00', '2018-01-01 12:00:00',
     |                     '2018-01-01 12:01:00'],
     |                    dtype='datetime64[ns]', freq='T')
     |      >>> rng.floor('H')
     |      DatetimeIndex(['2018-01-01 11:00:00', '2018-01-01 12:00:00',
     |                     '2018-01-01 12:00:00'],
     |                    dtype='datetime64[ns]', freq=None)
     |      
     |      **Series**
     |      
     |      >>> pd.Series(rng).dt.floor("H")
     |      0   2018-01-01 11:00:00
     |      1   2018-01-01 12:00:00
     |      2   2018-01-01 12:00:00
     |      dtype: datetime64[ns]
     |  
     |  month_name(self, *args, **kwargs)
     |      Return the month names of the DateTimeIndex with specified locale.
     |      
     |      .. versionadded:: 0.23.0
     |      
     |      Parameters
     |      ----------
     |      locale : str, optional
     |          Locale determining the language in which to return the month name.
     |          Default is English locale.
     |      
     |      Returns
     |      -------
     |      Index
     |          Index of month names.
     |      
     |      Examples
     |      --------
     |      >>> idx = pd.date_range(start='2018-01', freq='M', periods=3)
     |      >>> idx
     |      DatetimeIndex(['2018-01-31', '2018-02-28', '2018-03-31'],
     |                    dtype='datetime64[ns]', freq='M')
     |      >>> idx.month_name()
     |      Index(['January', 'February', 'March'], dtype='object')
     |  
     |  normalize(self, *args, **kwargs)
     |      Convert times to midnight.
     |      
     |      The time component of the date-time is converted to midnight i.e.
     |      00:00:00. This is useful in cases, when the time does not matter.
     |      Length is unaltered. The timezones are unaffected.
     |      
     |      This method is available on Series with datetime values under
     |      the ``.dt`` accessor, and directly on Datetime Array/Index.
     |      
     |      Returns
     |      -------
     |      DatetimeArray, DatetimeIndex or Series
     |          The same type as the original data. Series will have the same
     |          name and index. DatetimeIndex will have the same name.
     |      
     |      See Also
     |      --------
     |      floor : Floor the datetimes to the specified freq.
     |      ceil : Ceil the datetimes to the specified freq.
     |      round : Round the datetimes to the specified freq.
     |      
     |      Examples
     |      --------
     |      >>> idx = pd.date_range(start='2014-08-01 10:00', freq='H',
     |      ...                     periods=3, tz='Asia/Calcutta')
     |      >>> idx
     |      DatetimeIndex(['2014-08-01 10:00:00+05:30',
     |                     '2014-08-01 11:00:00+05:30',
     |                     '2014-08-01 12:00:00+05:30'],
     |                      dtype='datetime64[ns, Asia/Calcutta]', freq='H')
     |      >>> idx.normalize()
     |      DatetimeIndex(['2014-08-01 00:00:00+05:30',
     |                     '2014-08-01 00:00:00+05:30',
     |                     '2014-08-01 00:00:00+05:30'],
     |                     dtype='datetime64[ns, Asia/Calcutta]', freq=None)
     |  
     |  round(self, *args, **kwargs)
     |      Perform round operation on the data to the specified `freq`.
     |      
     |      Parameters
     |      ----------
     |      freq : str or Offset
     |          The frequency level to round the index to. Must be a fixed
     |          frequency like 'S' (second) not 'ME' (month end). See
     |          :ref:`frequency aliases <timeseries.offset_aliases>` for
     |          a list of possible `freq` values.
     |      ambiguous : 'infer', bool-ndarray, 'NaT', default 'raise'
     |          Only relevant for DatetimeIndex:
     |      
     |          - 'infer' will attempt to infer fall dst-transition hours based on
     |            order
     |          - bool-ndarray where True signifies a DST time, False designates
     |            a non-DST time (note that this flag is only applicable for
     |            ambiguous times)
     |          - 'NaT' will return NaT where there are ambiguous times
     |          - 'raise' will raise an AmbiguousTimeError if there are ambiguous
     |            times.
     |      
     |          .. versionadded:: 0.24.0
     |      
     |      nonexistent : 'shift_forward', 'shift_backward', 'NaT', timedelta, default 'raise'
     |          A nonexistent time does not exist in a particular timezone
     |          where clocks moved forward due to DST.
     |      
     |          - 'shift_forward' will shift the nonexistent time forward to the
     |            closest existing time
     |          - 'shift_backward' will shift the nonexistent time backward to the
     |            closest existing time
     |          - 'NaT' will return NaT where there are nonexistent times
     |          - timedelta objects will shift nonexistent times by the timedelta
     |          - 'raise' will raise an NonExistentTimeError if there are
     |            nonexistent times.
     |      
     |          .. versionadded:: 0.24.0
     |      
     |      Returns
     |      -------
     |      DatetimeIndex, TimedeltaIndex, or Series
     |          Index of the same type for a DatetimeIndex or TimedeltaIndex,
     |          or a Series with the same index for a Series.
     |      
     |      Raises
     |      ------
     |      ValueError if the `freq` cannot be converted.
     |      
     |      Examples
     |      --------
     |      **DatetimeIndex**
     |      
     |      >>> rng = pd.date_range('1/1/2018 11:59:00', periods=3, freq='min')
     |      >>> rng
     |      DatetimeIndex(['2018-01-01 11:59:00', '2018-01-01 12:00:00',
     |                     '2018-01-01 12:01:00'],
     |                    dtype='datetime64[ns]', freq='T')
     |      >>> rng.round('H')
     |      DatetimeIndex(['2018-01-01 12:00:00', '2018-01-01 12:00:00',
     |                     '2018-01-01 12:00:00'],
     |                    dtype='datetime64[ns]', freq=None)
     |      
     |      **Series**
     |      
     |      >>> pd.Series(rng).dt.round("H")
     |      0   2018-01-01 12:00:00
     |      1   2018-01-01 12:00:00
     |      2   2018-01-01 12:00:00
     |      dtype: datetime64[ns]
     |  
     |  strftime(self, *args, **kwargs)
     |      Convert to Index using specified date_format.
     |      
     |      Return an Index of formatted strings specified by date_format, which
     |      supports the same string format as the python standard library. Details
     |      of the string format can be found in `python string format
     |      doc <https://docs.python.org/3/library/datetime.html#strftime-and-strptime-behavior>`__.
     |      
     |      Parameters
     |      ----------
     |      date_format : str
     |          Date format string (e.g. "%Y-%m-%d").
     |      
     |      Returns
     |      -------
     |      ndarray
     |          NumPy ndarray of formatted strings.
     |      
     |      See Also
     |      --------
     |      to_datetime : Convert the given argument to datetime.
     |      DatetimeIndex.normalize : Return DatetimeIndex with times to midnight.
     |      DatetimeIndex.round : Round the DatetimeIndex to the specified freq.
     |      DatetimeIndex.floor : Floor the DatetimeIndex to the specified freq.
     |      
     |      Examples
     |      --------
     |      >>> rng = pd.date_range(pd.Timestamp("2018-03-10 09:00"),
     |      ...                     periods=3, freq='s')
     |      >>> rng.strftime('%B %d, %Y, %r')
     |      Index(['March 10, 2018, 09:00:00 AM', 'March 10, 2018, 09:00:01 AM',
     |             'March 10, 2018, 09:00:02 AM'],
     |            dtype='object')
     |  
     |  to_period(self, *args, **kwargs)
     |      Cast to PeriodArray/Index at a particular frequency.
     |      
     |      Converts DatetimeArray/Index to PeriodArray/Index.
     |      
     |      Parameters
     |      ----------
     |      freq : str or Offset, optional
     |          One of pandas' :ref:`offset strings <timeseries.offset_aliases>`
     |          or an Offset object. Will be inferred by default.
     |      
     |      Returns
     |      -------
     |      PeriodArray/Index
     |      
     |      Raises
     |      ------
     |      ValueError
     |          When converting a DatetimeArray/Index with non-regular values,
     |          so that a frequency cannot be inferred.
     |      
     |      See Also
     |      --------
     |      PeriodIndex: Immutable ndarray holding ordinal values.
     |      DatetimeIndex.to_pydatetime: Return DatetimeIndex as object.
     |      
     |      Examples
     |      --------
     |      >>> df = pd.DataFrame({"y": [1, 2, 3]},
     |      ...                   index=pd.to_datetime(["2000-03-31 00:00:00",
     |      ...                                         "2000-05-31 00:00:00",
     |      ...                                         "2000-08-31 00:00:00"]))
     |      >>> df.index.to_period("M")
     |      PeriodIndex(['2000-03', '2000-05', '2000-08'],
     |                  dtype='period[M]', freq='M')
     |      
     |      Infer the daily frequency
     |      
     |      >>> idx = pd.date_range("2017-01-01", periods=2)
     |      >>> idx.to_period()
     |      PeriodIndex(['2017-01-01', '2017-01-02'],
     |                  dtype='period[D]', freq='D')
     |  
     |  to_pydatetime(self)
     |      Return the data as an array of native Python datetime objects.
     |      
     |      Timezone information is retained if present.
     |      
     |      .. warning::
     |      
     |         Python's datetime uses microsecond resolution, which is lower than
     |         pandas (nanosecond). The values are truncated.
     |      
     |      Returns
     |      -------
     |      numpy.ndarray
     |          Object dtype array containing native Python datetime objects.
     |      
     |      See Also
     |      --------
     |      datetime.datetime : Standard library value for a datetime.
     |      
     |      Examples
     |      --------
     |      >>> s = pd.Series(pd.date_range('20180310', periods=2))
     |      >>> s
     |      0   2018-03-10
     |      1   2018-03-11
     |      dtype: datetime64[ns]
     |      
     |      >>> s.dt.to_pydatetime()
     |      array([datetime.datetime(2018, 3, 10, 0, 0),
     |             datetime.datetime(2018, 3, 11, 0, 0)], dtype=object)
     |      
     |      pandas' nanosecond precision is truncated to microseconds.
     |      
     |      >>> s = pd.Series(pd.date_range('20180310', periods=2, freq='ns'))
     |      >>> s
     |      0   2018-03-10 00:00:00.000000000
     |      1   2018-03-10 00:00:00.000000001
     |      dtype: datetime64[ns]
     |      
     |      >>> s.dt.to_pydatetime()
     |      array([datetime.datetime(2018, 3, 10, 0, 0),
     |             datetime.datetime(2018, 3, 10, 0, 0)], dtype=object)
     |  
     |  tz_convert(self, *args, **kwargs)
     |      Convert tz-aware Datetime Array/Index from one time zone to another.
     |      
     |      Parameters
     |      ----------
     |      tz : str, pytz.timezone, dateutil.tz.tzfile or None
     |          Time zone for time. Corresponding timestamps would be converted
     |          to this time zone of the Datetime Array/Index. A `tz` of None will
     |          convert to UTC and remove the timezone information.
     |      
     |      Returns
     |      -------
     |      Array or Index
     |      
     |      Raises
     |      ------
     |      TypeError
     |          If Datetime Array/Index is tz-naive.
     |      
     |      See Also
     |      --------
     |      DatetimeIndex.tz : A timezone that has a variable offset from UTC.
     |      DatetimeIndex.tz_localize : Localize tz-naive DatetimeIndex to a
     |          given time zone, or remove timezone from a tz-aware DatetimeIndex.
     |      
     |      Examples
     |      --------
     |      With the `tz` parameter, we can change the DatetimeIndex
     |      to other time zones:
     |      
     |      >>> dti = pd.date_range(start='2014-08-01 09:00',
     |      ...                     freq='H', periods=3, tz='Europe/Berlin')
     |      
     |      >>> dti
     |      DatetimeIndex(['2014-08-01 09:00:00+02:00',
     |                     '2014-08-01 10:00:00+02:00',
     |                     '2014-08-01 11:00:00+02:00'],
     |                    dtype='datetime64[ns, Europe/Berlin]', freq='H')
     |      
     |      >>> dti.tz_convert('US/Central')
     |      DatetimeIndex(['2014-08-01 02:00:00-05:00',
     |                     '2014-08-01 03:00:00-05:00',
     |                     '2014-08-01 04:00:00-05:00'],
     |                    dtype='datetime64[ns, US/Central]', freq='H')
     |      
     |      With the ``tz=None``, we can remove the timezone (after converting
     |      to UTC if necessary):
     |      
     |      >>> dti = pd.date_range(start='2014-08-01 09:00', freq='H',
     |      ...                     periods=3, tz='Europe/Berlin')
     |      
     |      >>> dti
     |      DatetimeIndex(['2014-08-01 09:00:00+02:00',
     |                     '2014-08-01 10:00:00+02:00',
     |                     '2014-08-01 11:00:00+02:00'],
     |                      dtype='datetime64[ns, Europe/Berlin]', freq='H')
     |      
     |      >>> dti.tz_convert(None)
     |      DatetimeIndex(['2014-08-01 07:00:00',
     |                     '2014-08-01 08:00:00',
     |                     '2014-08-01 09:00:00'],
     |                      dtype='datetime64[ns]', freq='H')
     |  
     |  tz_localize(self, *args, **kwargs)
     |      Localize tz-naive Datetime Array/Index to tz-aware
     |      Datetime Array/Index.
     |      
     |      This method takes a time zone (tz) naive Datetime Array/Index object
     |      and makes this time zone aware. It does not move the time to another
     |      time zone.
     |      Time zone localization helps to switch from time zone aware to time
     |      zone unaware objects.
     |      
     |      Parameters
     |      ----------
     |      tz : str, pytz.timezone, dateutil.tz.tzfile or None
     |          Time zone to convert timestamps to. Passing ``None`` will
     |          remove the time zone information preserving local time.
     |      ambiguous : 'infer', 'NaT', bool array, default 'raise'
     |          When clocks moved backward due to DST, ambiguous times may arise.
     |          For example in Central European Time (UTC+01), when going from
     |          03:00 DST to 02:00 non-DST, 02:30:00 local time occurs both at
     |          00:30:00 UTC and at 01:30:00 UTC. In such a situation, the
     |          `ambiguous` parameter dictates how ambiguous times should be
     |          handled.
     |      
     |          - 'infer' will attempt to infer fall dst-transition hours based on
     |            order
     |          - bool-ndarray where True signifies a DST time, False signifies a
     |            non-DST time (note that this flag is only applicable for
     |            ambiguous times)
     |          - 'NaT' will return NaT where there are ambiguous times
     |          - 'raise' will raise an AmbiguousTimeError if there are ambiguous
     |            times.
     |      
     |      nonexistent : 'shift_forward', 'shift_backward, 'NaT', timedelta, default 'raise'
     |          A nonexistent time does not exist in a particular timezone
     |          where clocks moved forward due to DST.
     |      
     |          - 'shift_forward' will shift the nonexistent time forward to the
     |            closest existing time
     |          - 'shift_backward' will shift the nonexistent time backward to the
     |            closest existing time
     |          - 'NaT' will return NaT where there are nonexistent times
     |          - timedelta objects will shift nonexistent times by the timedelta
     |          - 'raise' will raise an NonExistentTimeError if there are
     |            nonexistent times.
     |      
     |          .. versionadded:: 0.24.0
     |      
     |      Returns
     |      -------
     |      Same type as self
     |          Array/Index converted to the specified time zone.
     |      
     |      Raises
     |      ------
     |      TypeError
     |          If the Datetime Array/Index is tz-aware and tz is not None.
     |      
     |      See Also
     |      --------
     |      DatetimeIndex.tz_convert : Convert tz-aware DatetimeIndex from
     |          one time zone to another.
     |      
     |      Examples
     |      --------
     |      >>> tz_naive = pd.date_range('2018-03-01 09:00', periods=3)
     |      >>> tz_naive
     |      DatetimeIndex(['2018-03-01 09:00:00', '2018-03-02 09:00:00',
     |                     '2018-03-03 09:00:00'],
     |                    dtype='datetime64[ns]', freq='D')
     |      
     |      Localize DatetimeIndex in US/Eastern time zone:
     |      
     |      >>> tz_aware = tz_naive.tz_localize(tz='US/Eastern')
     |      >>> tz_aware
     |      DatetimeIndex(['2018-03-01 09:00:00-05:00',
     |                     '2018-03-02 09:00:00-05:00',
     |                     '2018-03-03 09:00:00-05:00'],
     |                    dtype='datetime64[ns, US/Eastern]', freq='D')
     |      
     |      With the ``tz=None``, we can remove the time zone information
     |      while keeping the local time (not converted to UTC):
     |      
     |      >>> tz_aware.tz_localize(None)
     |      DatetimeIndex(['2018-03-01 09:00:00', '2018-03-02 09:00:00',
     |                     '2018-03-03 09:00:00'],
     |                    dtype='datetime64[ns]', freq='D')
     |      
     |      Be careful with DST changes. When there is sequential data, pandas can
     |      infer the DST time:
     |      
     |      >>> s = pd.to_datetime(pd.Series(['2018-10-28 01:30:00',
     |      ...                               '2018-10-28 02:00:00',
     |      ...                               '2018-10-28 02:30:00',
     |      ...                               '2018-10-28 02:00:00',
     |      ...                               '2018-10-28 02:30:00',
     |      ...                               '2018-10-28 03:00:00',
     |      ...                               '2018-10-28 03:30:00']))
     |      >>> s.dt.tz_localize('CET', ambiguous='infer')
     |      0   2018-10-28 01:30:00+02:00
     |      1   2018-10-28 02:00:00+02:00
     |      2   2018-10-28 02:30:00+02:00
     |      3   2018-10-28 02:00:00+01:00
     |      4   2018-10-28 02:30:00+01:00
     |      5   2018-10-28 03:00:00+01:00
     |      6   2018-10-28 03:30:00+01:00
     |      dtype: datetime64[ns, CET]
     |      
     |      In some cases, inferring the DST is impossible. In such cases, you can
     |      pass an ndarray to the ambiguous parameter to set the DST explicitly
     |      
     |      >>> s = pd.to_datetime(pd.Series(['2018-10-28 01:20:00',
     |      ...                               '2018-10-28 02:36:00',
     |      ...                               '2018-10-28 03:46:00']))
     |      >>> s.dt.tz_localize('CET', ambiguous=np.array([True, True, False]))
     |      0   2015-03-29 03:00:00+02:00
     |      1   2015-03-29 03:30:00+02:00
     |      dtype: datetime64[ns, Europe/Warsaw]
     |      
     |      If the DST transition causes nonexistent times, you can shift these
     |      dates forward or backwards with a timedelta object or `'shift_forward'`
     |      or `'shift_backwards'`.
     |      
     |      >>> s = pd.to_datetime(pd.Series(['2015-03-29 02:30:00',
     |      ...                               '2015-03-29 03:30:00']))
     |      >>> s.dt.tz_localize('Europe/Warsaw', nonexistent='shift_forward')
     |      0   2015-03-29 03:00:00+02:00
     |      1   2015-03-29 03:30:00+02:00
     |      dtype: datetime64[ns, 'Europe/Warsaw']
     |      >>> s.dt.tz_localize('Europe/Warsaw', nonexistent='shift_backward')
     |      0   2015-03-29 01:59:59.999999999+01:00
     |      1   2015-03-29 03:30:00+02:00
     |      dtype: datetime64[ns, 'Europe/Warsaw']
     |      >>> s.dt.tz_localize('Europe/Warsaw', nonexistent=pd.Timedelta('1H'))
     |      0   2015-03-29 03:30:00+02:00
     |      1   2015-03-29 03:30:00+02:00
     |      dtype: datetime64[ns, 'Europe/Warsaw']
     |  
     |  ----------------------------------------------------------------------
     |  Data descriptors defined here:
     |  
     |  date
     |      Returns numpy array of python datetime.date objects (namely, the date
     |      part of Timestamps without timezone information).
     |  
     |  day
     |      The month as January=1, December=12.
     |  
     |  dayofweek
     |      The day of the week with Monday=0, Sunday=6.
     |      
     |      Return the day of the week. It is assumed the week starts on
     |      Monday, which is denoted by 0 and ends on Sunday which is denoted
     |      by 6. This method is available on both Series with datetime
     |      values (using the `dt` accessor) or DatetimeIndex.
     |      
     |      Returns
     |      -------
     |      Series or Index
     |          Containing integers indicating the day number.
     |      
     |      See Also
     |      --------
     |      Series.dt.dayofweek : Alias.
     |      Series.dt.weekday : Alias.
     |      Series.dt.day_name : Returns the name of the day of the week.
     |      
     |      Examples
     |      --------
     |      >>> s = pd.date_range('2016-12-31', '2017-01-08', freq='D').to_series()
     |      >>> s.dt.dayofweek
     |      2016-12-31    5
     |      2017-01-01    6
     |      2017-01-02    0
     |      2017-01-03    1
     |      2017-01-04    2
     |      2017-01-05    3
     |      2017-01-06    4
     |      2017-01-07    5
     |      2017-01-08    6
     |      Freq: D, dtype: int64
     |  
     |  dayofyear
     |      The ordinal day of the year.
     |  
     |  days_in_month
     |      The number of days in the month.
     |  
     |  daysinmonth
     |      The number of days in the month.
     |  
     |  freq
     |  
     |  hour
     |      The hours of the datetime.
     |  
     |  is_leap_year
     |      Boolean indicator if the date belongs to a leap year.
     |      
     |      A leap year is a year, which has 366 days (instead of 365) including
     |      29th of February as an intercalary day.
     |      Leap years are years which are multiples of four with the exception
     |      of years divisible by 100 but not by 400.
     |      
     |      Returns
     |      -------
     |      Series or ndarray
     |           Booleans indicating if dates belong to a leap year.
     |      
     |      Examples
     |      --------
     |      This method is available on Series with datetime values under
     |      the ``.dt`` accessor, and directly on DatetimeIndex.
     |      
     |      >>> idx = pd.date_range("2012-01-01", "2015-01-01", freq="Y")
     |      >>> idx
     |      DatetimeIndex(['2012-12-31', '2013-12-31', '2014-12-31'],
     |                    dtype='datetime64[ns]', freq='A-DEC')
     |      >>> idx.is_leap_year
     |      array([ True, False, False], dtype=bool)
     |      
     |      >>> dates = pd.Series(idx)
     |      >>> dates_series
     |      0   2012-12-31
     |      1   2013-12-31
     |      2   2014-12-31
     |      dtype: datetime64[ns]
     |      >>> dates_series.dt.is_leap_year
     |      0     True
     |      1    False
     |      2    False
     |      dtype: bool
     |  
     |  is_month_end
     |      Indicates whether the date is the last day of the month.
     |      
     |      Returns
     |      -------
     |      Series or array
     |          For Series, returns a Series with boolean values.
     |          For DatetimeIndex, returns a boolean array.
     |      
     |      See Also
     |      --------
     |      is_month_start : Return a boolean indicating whether the date
     |          is the first day of the month.
     |      is_month_end : Return a boolean indicating whether the date
     |          is the last day of the month.
     |      
     |      Examples
     |      --------
     |      This method is available on Series with datetime values under
     |      the ``.dt`` accessor, and directly on DatetimeIndex.
     |      
     |      >>> s = pd.Series(pd.date_range("2018-02-27", periods=3))
     |      >>> s
     |      0   2018-02-27
     |      1   2018-02-28
     |      2   2018-03-01
     |      dtype: datetime64[ns]
     |      >>> s.dt.is_month_start
     |      0    False
     |      1    False
     |      2    True
     |      dtype: bool
     |      >>> s.dt.is_month_end
     |      0    False
     |      1    True
     |      2    False
     |      dtype: bool
     |      
     |      >>> idx = pd.date_range("2018-02-27", periods=3)
     |      >>> idx.is_month_start
     |      array([False, False, True])
     |      >>> idx.is_month_end
     |      array([False, True, False])
     |  
     |  is_month_start
     |      Indicates whether the date is the first day of the month.
     |      
     |      Returns
     |      -------
     |      Series or array
     |          For Series, returns a Series with boolean values.
     |          For DatetimeIndex, returns a boolean array.
     |      
     |      See Also
     |      --------
     |      is_month_start : Return a boolean indicating whether the date
     |          is the first day of the month.
     |      is_month_end : Return a boolean indicating whether the date
     |          is the last day of the month.
     |      
     |      Examples
     |      --------
     |      This method is available on Series with datetime values under
     |      the ``.dt`` accessor, and directly on DatetimeIndex.
     |      
     |      >>> s = pd.Series(pd.date_range("2018-02-27", periods=3))
     |      >>> s
     |      0   2018-02-27
     |      1   2018-02-28
     |      2   2018-03-01
     |      dtype: datetime64[ns]
     |      >>> s.dt.is_month_start
     |      0    False
     |      1    False
     |      2    True
     |      dtype: bool
     |      >>> s.dt.is_month_end
     |      0    False
     |      1    True
     |      2    False
     |      dtype: bool
     |      
     |      >>> idx = pd.date_range("2018-02-27", periods=3)
     |      >>> idx.is_month_start
     |      array([False, False, True])
     |      >>> idx.is_month_end
     |      array([False, True, False])
     |  
     |  is_quarter_end
     |      Indicator for whether the date is the last day of a quarter.
     |      
     |      Returns
     |      -------
     |      is_quarter_end : Series or DatetimeIndex
     |          The same type as the original data with boolean values. Series will
     |          have the same name and index. DatetimeIndex will have the same
     |          name.
     |      
     |      See Also
     |      --------
     |      quarter : Return the quarter of the date.
     |      is_quarter_start : Similar property indicating the quarter start.
     |      
     |      Examples
     |      --------
     |      This method is available on Series with datetime values under
     |      the ``.dt`` accessor, and directly on DatetimeIndex.
     |      
     |      >>> df = pd.DataFrame({'dates': pd.date_range("2017-03-30",
     |      ...                    periods=4)})
     |      >>> df.assign(quarter=df.dates.dt.quarter,
     |      ...           is_quarter_end=df.dates.dt.is_quarter_end)
     |             dates  quarter    is_quarter_end
     |      0 2017-03-30        1             False
     |      1 2017-03-31        1              True
     |      2 2017-04-01        2             False
     |      3 2017-04-02        2             False
     |      
     |      >>> idx = pd.date_range('2017-03-30', periods=4)
     |      >>> idx
     |      DatetimeIndex(['2017-03-30', '2017-03-31', '2017-04-01', '2017-04-02'],
     |                    dtype='datetime64[ns]', freq='D')
     |      
     |      >>> idx.is_quarter_end
     |      array([False,  True, False, False])
     |  
     |  is_quarter_start
     |      Indicator for whether the date is the first day of a quarter.
     |      
     |      Returns
     |      -------
     |      is_quarter_start : Series or DatetimeIndex
     |          The same type as the original data with boolean values. Series will
     |          have the same name and index. DatetimeIndex will have the same
     |          name.
     |      
     |      See Also
     |      --------
     |      quarter : Return the quarter of the date.
     |      is_quarter_end : Similar property for indicating the quarter start.
     |      
     |      Examples
     |      --------
     |      This method is available on Series with datetime values under
     |      the ``.dt`` accessor, and directly on DatetimeIndex.
     |      
     |      >>> df = pd.DataFrame({'dates': pd.date_range("2017-03-30",
     |      ...                   periods=4)})
     |      >>> df.assign(quarter=df.dates.dt.quarter,
     |      ...           is_quarter_start=df.dates.dt.is_quarter_start)
     |             dates  quarter  is_quarter_start
     |      0 2017-03-30        1             False
     |      1 2017-03-31        1             False
     |      2 2017-04-01        2              True
     |      3 2017-04-02        2             False
     |      
     |      >>> idx = pd.date_range('2017-03-30', periods=4)
     |      >>> idx
     |      DatetimeIndex(['2017-03-30', '2017-03-31', '2017-04-01', '2017-04-02'],
     |                    dtype='datetime64[ns]', freq='D')
     |      
     |      >>> idx.is_quarter_start
     |      array([False, False,  True, False])
     |  
     |  is_year_end
     |      Indicate whether the date is the last day of the year.
     |      
     |      Returns
     |      -------
     |      Series or DatetimeIndex
     |          The same type as the original data with boolean values. Series will
     |          have the same name and index. DatetimeIndex will have the same
     |          name.
     |      
     |      See Also
     |      --------
     |      is_year_start : Similar property indicating the start of the year.
     |      
     |      Examples
     |      --------
     |      This method is available on Series with datetime values under
     |      the ``.dt`` accessor, and directly on DatetimeIndex.
     |      
     |      >>> dates = pd.Series(pd.date_range("2017-12-30", periods=3))
     |      >>> dates
     |      0   2017-12-30
     |      1   2017-12-31
     |      2   2018-01-01
     |      dtype: datetime64[ns]
     |      
     |      >>> dates.dt.is_year_end
     |      0    False
     |      1     True
     |      2    False
     |      dtype: bool
     |      
     |      >>> idx = pd.date_range("2017-12-30", periods=3)
     |      >>> idx
     |      DatetimeIndex(['2017-12-30', '2017-12-31', '2018-01-01'],
     |                    dtype='datetime64[ns]', freq='D')
     |      
     |      >>> idx.is_year_end
     |      array([False,  True, False])
     |  
     |  is_year_start
     |      Indicate whether the date is the first day of a year.
     |      
     |      Returns
     |      -------
     |      Series or DatetimeIndex
     |          The same type as the original data with boolean values. Series will
     |          have the same name and index. DatetimeIndex will have the same
     |          name.
     |      
     |      See Also
     |      --------
     |      is_year_end : Similar property indicating the last day of the year.
     |      
     |      Examples
     |      --------
     |      This method is available on Series with datetime values under
     |      the ``.dt`` accessor, and directly on DatetimeIndex.
     |      
     |      >>> dates = pd.Series(pd.date_range("2017-12-30", periods=3))
     |      >>> dates
     |      0   2017-12-30
     |      1   2017-12-31
     |      2   2018-01-01
     |      dtype: datetime64[ns]
     |      
     |      >>> dates.dt.is_year_start
     |      0    False
     |      1    False
     |      2    True
     |      dtype: bool
     |      
     |      >>> idx = pd.date_range("2017-12-30", periods=3)
     |      >>> idx
     |      DatetimeIndex(['2017-12-30', '2017-12-31', '2018-01-01'],
     |                    dtype='datetime64[ns]', freq='D')
     |      
     |      >>> idx.is_year_start
     |      array([False, False,  True])
     |  
     |  microsecond
     |      The microseconds of the datetime.
     |  
     |  minute
     |      The minutes of the datetime.
     |  
     |  month
     |      The month as January=1, December=12.
     |  
     |  nanosecond
     |      The nanoseconds of the datetime.
     |  
     |  quarter
     |      The quarter of the date.
     |  
     |  second
     |      The seconds of the datetime.
     |  
     |  time
     |      Returns numpy array of datetime.time. The time part of the Timestamps.
     |  
     |  timetz
     |      Returns numpy array of datetime.time also containing timezone
     |      information. The time part of the Timestamps.
     |  
     |  tz
     |      Return timezone, if any.
     |      
     |      Returns
     |      -------
     |      datetime.tzinfo, pytz.tzinfo.BaseTZInfo, dateutil.tz.tz.tzfile, or None
     |          Returns None when the array is tz-naive.
     |  
     |  week
     |      The week ordinal of the year.
     |  
     |  weekday
     |      The day of the week with Monday=0, Sunday=6.
     |      
     |      Return the day of the week. It is assumed the week starts on
     |      Monday, which is denoted by 0 and ends on Sunday which is denoted
     |      by 6. This method is available on both Series with datetime
     |      values (using the `dt` accessor) or DatetimeIndex.
     |      
     |      Returns
     |      -------
     |      Series or Index
     |          Containing integers indicating the day number.
     |      
     |      See Also
     |      --------
     |      Series.dt.dayofweek : Alias.
     |      Series.dt.weekday : Alias.
     |      Series.dt.day_name : Returns the name of the day of the week.
     |      
     |      Examples
     |      --------
     |      >>> s = pd.date_range('2016-12-31', '2017-01-08', freq='D').to_series()
     |      >>> s.dt.dayofweek
     |      2016-12-31    5
     |      2017-01-01    6
     |      2017-01-02    0
     |      2017-01-03    1
     |      2017-01-04    2
     |      2017-01-05    3
     |      2017-01-06    4
     |      2017-01-07    5
     |      2017-01-08    6
     |      Freq: D, dtype: int64
     |  
     |  weekofyear
     |      The week ordinal of the year.
     |  
     |  year
     |      The year of the datetime.
     |  
     |  ----------------------------------------------------------------------
     |  Methods inherited from Properties:
     |  
     |  __init__(self, data, orig)
     |      Initialize self.  See help(type(self)) for accurate signature.
     |  
     |  ----------------------------------------------------------------------
     |  Data descriptors inherited from pandas.core.accessor.PandasDelegate:
     |  
     |  __dict__
     |      dictionary for instance variables (if defined)
     |  
     |  __weakref__
     |      list of weak references to the object (if defined)
     |  
     |  ----------------------------------------------------------------------
     |  Methods inherited from pandas.core.base.PandasObject:
     |  
     |  __repr__(self) -> str
     |      Return a string representation for a particular object.
     |  
     |  __sizeof__(self)
     |      Generates the total memory usage for an object that returns
     |      either a value or Series of values
     |  
     |  ----------------------------------------------------------------------
     |  Methods inherited from pandas.core.accessor.DirNamesMixin:
     |  
     |  __dir__(self)
     |      Provide method name lookup and completion.
     |      
     |      Notes
     |      -----
     |      Only provide 'public' methods.
     |  
     |  ----------------------------------------------------------------------
     |  Data and other attributes inherited from pandas.core.accessor.DirNamesMixin:
     |  
     |  __annotations__ = {'_accessors': typing.Set[str], '_deprecations': typ...
     |  
     |  ----------------------------------------------------------------------
     |  Methods inherited from pandas.core.base.NoNewAttributesMixin:
     |  
     |  __setattr__(self, key, value)
     |      Implement setattr(self, name, value).
    
    


```python
sales['DATE'].dt.month
```




    0       1
    1       2
    2       3
    3       4
    4       5
           ..
    335    12
    336     1
    337     2
    338     3
    339     4
    Name: DATE, Length: 340, dtype: int64




```python
sales['DATE'].dt.is_leap_year
```




    0       True
    1       True
    2       True
    3       True
    4       True
           ...  
    335    False
    336     True
    337     True
    338     True
    339     True
    Name: DATE, Length: 340, dtype: bool


