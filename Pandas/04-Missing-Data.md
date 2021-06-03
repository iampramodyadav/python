<h1>Table of Contents<span class="tocSkip"></span></h1>
<div class="toc"><ul class="toc-item"><li><span><a href="#Missing-Data" data-toc-modified-id="Missing-Data-1"><span class="toc-item-num">1&nbsp;&nbsp;</span>Missing Data</a></span><ul class="toc-item"><li><span><a href="#What-Null/NA/nan-objects-look-like:" data-toc-modified-id="What-Null/NA/nan-objects-look-like:-1.1"><span class="toc-item-num">1.1&nbsp;&nbsp;</span>What Null/NA/nan objects look like:</a></span></li><li><span><a href="#Note!-Typical-comparisons-should-be-avoided-with-Missing-Values" data-toc-modified-id="Note!-Typical-comparisons-should-be-avoided-with-Missing-Values-1.2"><span class="toc-item-num">1.2&nbsp;&nbsp;</span>Note! Typical comparisons should be avoided with Missing Values</a></span></li><li><span><a href="#Data" data-toc-modified-id="Data-1.3"><span class="toc-item-num">1.3&nbsp;&nbsp;</span>Data</a></span></li><li><span><a href="#Checking-and-Selecting-for-Null-Values" data-toc-modified-id="Checking-and-Selecting-for-Null-Values-1.4"><span class="toc-item-num">1.4&nbsp;&nbsp;</span>Checking and Selecting for Null Values</a></span></li><li><span><a href="#Drop-Data" data-toc-modified-id="Drop-Data-1.5"><span class="toc-item-num">1.5&nbsp;&nbsp;</span>Drop Data</a></span></li><li><span><a href="#Fill-Data" data-toc-modified-id="Fill-Data-1.6"><span class="toc-item-num">1.6&nbsp;&nbsp;</span>Fill Data</a></span></li><li><span><a href="#Filling-with-Interpolation" data-toc-modified-id="Filling-with-Interpolation-1.7"><span class="toc-item-num">1.7&nbsp;&nbsp;</span>Filling with Interpolation</a></span></li></ul></li></ul></div>

# Missing Data

Make sure to review the video for a full discussion on the strategies of dealing with missing data.

--------


## What Null/NA/nan objects look like:

Source: https://github.com/pandas-dev/pandas/issues/28095

A new pd.NA value (singleton) is introduced to represent scalar missing values. Up to now, pandas used several values to represent missing data: np.nan is used for this for float data, np.nan or None for object-dtype data and pd.NaT for datetime-like data. The goal of pd.NA is to provide a “missing” indicator that can be used consistently across data types. pd.NA is currently used by the nullable integer and boolean data types and the new string data type


```python
import numpy as np
import pandas as pd
```


```python
np.nan
```




    nan




```python
pd.NA
```




    <NA>




```python
pd.NaT
```




    NaT



----
------
## Note! Typical comparisons should be avoided with Missing Values

* https://towardsdatascience.com/navigating-the-hell-of-nans-in-python-71b12558895b
* https://stackoverflow.com/questions/20320022/why-in-numpy-nan-nan-is-false-while-nan-in-nan-is-true

This is generally because the logic here is, since we don't know these values, we can't know if they are equal to each other.


```python
np.nan == np.nan
```




    False




```python
np.nan in [np.nan]
```




    True




```python
np.nan is np.nan
```




    True




```python
pd.NA == pd.NA
```




    <NA>



-------

## Data

People were asked to score their opinions of actors from a 1-10 scale before and after watching one of their movies. However, some data is missing.


```python
df = pd.read_csv('movie_scores.csv')
```


```python
df
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
      <th>first_name</th>
      <th>last_name</th>
      <th>age</th>
      <th>sex</th>
      <th>pre_movie_score</th>
      <th>post_movie_score</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Tom</td>
      <td>Hanks</td>
      <td>63.0</td>
      <td>m</td>
      <td>8.0</td>
      <td>10.0</td>
    </tr>
    <tr>
      <th>1</th>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Hugh</td>
      <td>Jackman</td>
      <td>51.0</td>
      <td>m</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>3</th>
      <td>Oprah</td>
      <td>Winfrey</td>
      <td>66.0</td>
      <td>f</td>
      <td>6.0</td>
      <td>8.0</td>
    </tr>
    <tr>
      <th>4</th>
      <td>Emma</td>
      <td>Stone</td>
      <td>31.0</td>
      <td>f</td>
      <td>7.0</td>
      <td>9.0</td>
    </tr>
  </tbody>
</table>
</div>



## Checking and Selecting for Null Values


```python
df
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
      <th>first_name</th>
      <th>last_name</th>
      <th>age</th>
      <th>sex</th>
      <th>pre_movie_score</th>
      <th>post_movie_score</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Tom</td>
      <td>Hanks</td>
      <td>63.0</td>
      <td>m</td>
      <td>8.0</td>
      <td>10.0</td>
    </tr>
    <tr>
      <th>1</th>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Hugh</td>
      <td>Jackman</td>
      <td>51.0</td>
      <td>m</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>3</th>
      <td>Oprah</td>
      <td>Winfrey</td>
      <td>66.0</td>
      <td>f</td>
      <td>6.0</td>
      <td>8.0</td>
    </tr>
    <tr>
      <th>4</th>
      <td>Emma</td>
      <td>Stone</td>
      <td>31.0</td>
      <td>f</td>
      <td>7.0</td>
      <td>9.0</td>
    </tr>
  </tbody>
</table>
</div>




```python
df.isnull()
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
      <th>first_name</th>
      <th>last_name</th>
      <th>age</th>
      <th>sex</th>
      <th>pre_movie_score</th>
      <th>post_movie_score</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
    </tr>
    <tr>
      <th>1</th>
      <td>True</td>
      <td>True</td>
      <td>True</td>
      <td>True</td>
      <td>True</td>
      <td>True</td>
    </tr>
    <tr>
      <th>2</th>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>True</td>
      <td>True</td>
    </tr>
    <tr>
      <th>3</th>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
    </tr>
    <tr>
      <th>4</th>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
    </tr>
  </tbody>
</table>
</div>




```python
df.notnull()
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
      <th>first_name</th>
      <th>last_name</th>
      <th>age</th>
      <th>sex</th>
      <th>pre_movie_score</th>
      <th>post_movie_score</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>True</td>
      <td>True</td>
      <td>True</td>
      <td>True</td>
      <td>True</td>
      <td>True</td>
    </tr>
    <tr>
      <th>1</th>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
    </tr>
    <tr>
      <th>2</th>
      <td>True</td>
      <td>True</td>
      <td>True</td>
      <td>True</td>
      <td>False</td>
      <td>False</td>
    </tr>
    <tr>
      <th>3</th>
      <td>True</td>
      <td>True</td>
      <td>True</td>
      <td>True</td>
      <td>True</td>
      <td>True</td>
    </tr>
    <tr>
      <th>4</th>
      <td>True</td>
      <td>True</td>
      <td>True</td>
      <td>True</td>
      <td>True</td>
      <td>True</td>
    </tr>
  </tbody>
</table>
</div>




```python
df['first_name']
```




    0      Tom
    1      NaN
    2     Hugh
    3    Oprah
    4     Emma
    Name: first_name, dtype: object




```python
df[df['first_name'].notnull()]
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
      <th>first_name</th>
      <th>last_name</th>
      <th>age</th>
      <th>sex</th>
      <th>pre_movie_score</th>
      <th>post_movie_score</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Tom</td>
      <td>Hanks</td>
      <td>63.0</td>
      <td>m</td>
      <td>8.0</td>
      <td>10.0</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Hugh</td>
      <td>Jackman</td>
      <td>51.0</td>
      <td>m</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>3</th>
      <td>Oprah</td>
      <td>Winfrey</td>
      <td>66.0</td>
      <td>f</td>
      <td>6.0</td>
      <td>8.0</td>
    </tr>
    <tr>
      <th>4</th>
      <td>Emma</td>
      <td>Stone</td>
      <td>31.0</td>
      <td>f</td>
      <td>7.0</td>
      <td>9.0</td>
    </tr>
  </tbody>
</table>
</div>




```python
df[(df['pre_movie_score'].isnull()) & df['sex'].notnull()]
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
      <th>first_name</th>
      <th>last_name</th>
      <th>age</th>
      <th>sex</th>
      <th>pre_movie_score</th>
      <th>post_movie_score</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>2</th>
      <td>Hugh</td>
      <td>Jackman</td>
      <td>51.0</td>
      <td>m</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
  </tbody>
</table>
</div>



## Drop Data


```python
df
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
      <th>first_name</th>
      <th>last_name</th>
      <th>age</th>
      <th>sex</th>
      <th>pre_movie_score</th>
      <th>post_movie_score</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Tom</td>
      <td>Hanks</td>
      <td>63.0</td>
      <td>m</td>
      <td>8.0</td>
      <td>10.0</td>
    </tr>
    <tr>
      <th>1</th>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Hugh</td>
      <td>Jackman</td>
      <td>51.0</td>
      <td>m</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>3</th>
      <td>Oprah</td>
      <td>Winfrey</td>
      <td>66.0</td>
      <td>f</td>
      <td>6.0</td>
      <td>8.0</td>
    </tr>
    <tr>
      <th>4</th>
      <td>Emma</td>
      <td>Stone</td>
      <td>31.0</td>
      <td>f</td>
      <td>7.0</td>
      <td>9.0</td>
    </tr>
  </tbody>
</table>
</div>




```python
help(df.dropna)
```

    Help on method dropna in module pandas.core.frame:
    
    dropna(axis=0, how='any', thresh=None, subset=None, inplace=False) method of pandas.core.frame.DataFrame instance
        Remove missing values.
        
        See the :ref:`User Guide <missing_data>` for more on which values are
        considered missing, and how to work with missing data.
        
        Parameters
        ----------
        axis : {0 or 'index', 1 or 'columns'}, default 0
            Determine if rows or columns which contain missing values are
            removed.
        
            * 0, or 'index' : Drop rows which contain missing values.
            * 1, or 'columns' : Drop columns which contain missing value.
        
            .. versionchanged:: 1.0.0
        
               Pass tuple or list to drop on multiple axes.
               Only a single axis is allowed.
        
        how : {'any', 'all'}, default 'any'
            Determine if row or column is removed from DataFrame, when we have
            at least one NA or all NA.
        
            * 'any' : If any NA values are present, drop that row or column.
            * 'all' : If all values are NA, drop that row or column.
        
        thresh : int, optional
            Require that many non-NA values.
        subset : array-like, optional
            Labels along other axis to consider, e.g. if you are dropping rows
            these would be a list of columns to include.
        inplace : bool, default False
            If True, do operation inplace and return None.
        
        Returns
        -------
        DataFrame
            DataFrame with NA entries dropped from it.
        
        See Also
        --------
        DataFrame.isna: Indicate missing values.
        DataFrame.notna : Indicate existing (non-missing) values.
        DataFrame.fillna : Replace missing values.
        Series.dropna : Drop missing values.
        Index.dropna : Drop missing indices.
        
        Examples
        --------
        >>> df = pd.DataFrame({"name": ['Alfred', 'Batman', 'Catwoman'],
        ...                    "toy": [np.nan, 'Batmobile', 'Bullwhip'],
        ...                    "born": [pd.NaT, pd.Timestamp("1940-04-25"),
        ...                             pd.NaT]})
        >>> df
               name        toy       born
        0    Alfred        NaN        NaT
        1    Batman  Batmobile 1940-04-25
        2  Catwoman   Bullwhip        NaT
        
        Drop the rows where at least one element is missing.
        
        >>> df.dropna()
             name        toy       born
        1  Batman  Batmobile 1940-04-25
        
        Drop the columns where at least one element is missing.
        
        >>> df.dropna(axis='columns')
               name
        0    Alfred
        1    Batman
        2  Catwoman
        
        Drop the rows where all elements are missing.
        
        >>> df.dropna(how='all')
               name        toy       born
        0    Alfred        NaN        NaT
        1    Batman  Batmobile 1940-04-25
        2  Catwoman   Bullwhip        NaT
        
        Keep only the rows with at least 2 non-NA values.
        
        >>> df.dropna(thresh=2)
               name        toy       born
        1    Batman  Batmobile 1940-04-25
        2  Catwoman   Bullwhip        NaT
        
        Define in which columns to look for missing values.
        
        >>> df.dropna(subset=['name', 'born'])
               name        toy       born
        1    Batman  Batmobile 1940-04-25
        
        Keep the DataFrame with valid entries in the same variable.
        
        >>> df.dropna(inplace=True)
        >>> df
             name        toy       born
        1  Batman  Batmobile 1940-04-25
    
    


```python
df.dropna()
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
      <th>first_name</th>
      <th>last_name</th>
      <th>age</th>
      <th>sex</th>
      <th>pre_movie_score</th>
      <th>post_movie_score</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Tom</td>
      <td>Hanks</td>
      <td>63.0</td>
      <td>m</td>
      <td>8.0</td>
      <td>10.0</td>
    </tr>
    <tr>
      <th>3</th>
      <td>Oprah</td>
      <td>Winfrey</td>
      <td>66.0</td>
      <td>f</td>
      <td>6.0</td>
      <td>8.0</td>
    </tr>
    <tr>
      <th>4</th>
      <td>Emma</td>
      <td>Stone</td>
      <td>31.0</td>
      <td>f</td>
      <td>7.0</td>
      <td>9.0</td>
    </tr>
  </tbody>
</table>
</div>




```python
df.dropna(thresh=1)
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
      <th>first_name</th>
      <th>last_name</th>
      <th>age</th>
      <th>sex</th>
      <th>pre_movie_score</th>
      <th>post_movie_score</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Tom</td>
      <td>Hanks</td>
      <td>63.0</td>
      <td>m</td>
      <td>8.0</td>
      <td>10.0</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Hugh</td>
      <td>Jackman</td>
      <td>51.0</td>
      <td>m</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>3</th>
      <td>Oprah</td>
      <td>Winfrey</td>
      <td>66.0</td>
      <td>f</td>
      <td>6.0</td>
      <td>8.0</td>
    </tr>
    <tr>
      <th>4</th>
      <td>Emma</td>
      <td>Stone</td>
      <td>31.0</td>
      <td>f</td>
      <td>7.0</td>
      <td>9.0</td>
    </tr>
  </tbody>
</table>
</div>




```python
df.dropna(axis=1)
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
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
    </tr>
    <tr>
      <th>1</th>
    </tr>
    <tr>
      <th>2</th>
    </tr>
    <tr>
      <th>3</th>
    </tr>
    <tr>
      <th>4</th>
    </tr>
  </tbody>
</table>
</div>




```python
df.dropna(thresh=4,axis=1)
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
      <th>first_name</th>
      <th>last_name</th>
      <th>age</th>
      <th>sex</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Tom</td>
      <td>Hanks</td>
      <td>63.0</td>
      <td>m</td>
    </tr>
    <tr>
      <th>1</th>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Hugh</td>
      <td>Jackman</td>
      <td>51.0</td>
      <td>m</td>
    </tr>
    <tr>
      <th>3</th>
      <td>Oprah</td>
      <td>Winfrey</td>
      <td>66.0</td>
      <td>f</td>
    </tr>
    <tr>
      <th>4</th>
      <td>Emma</td>
      <td>Stone</td>
      <td>31.0</td>
      <td>f</td>
    </tr>
  </tbody>
</table>
</div>



## Fill Data


```python
df
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
      <th>first_name</th>
      <th>last_name</th>
      <th>age</th>
      <th>sex</th>
      <th>pre_movie_score</th>
      <th>post_movie_score</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Tom</td>
      <td>Hanks</td>
      <td>63.0</td>
      <td>m</td>
      <td>8.0</td>
      <td>10.0</td>
    </tr>
    <tr>
      <th>1</th>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Hugh</td>
      <td>Jackman</td>
      <td>51.0</td>
      <td>m</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>3</th>
      <td>Oprah</td>
      <td>Winfrey</td>
      <td>66.0</td>
      <td>f</td>
      <td>6.0</td>
      <td>8.0</td>
    </tr>
    <tr>
      <th>4</th>
      <td>Emma</td>
      <td>Stone</td>
      <td>31.0</td>
      <td>f</td>
      <td>7.0</td>
      <td>9.0</td>
    </tr>
  </tbody>
</table>
</div>




```python
df.fillna("NEW VALUE!")
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
      <th>first_name</th>
      <th>last_name</th>
      <th>age</th>
      <th>sex</th>
      <th>pre_movie_score</th>
      <th>post_movie_score</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Tom</td>
      <td>Hanks</td>
      <td>63</td>
      <td>m</td>
      <td>8</td>
      <td>10</td>
    </tr>
    <tr>
      <th>1</th>
      <td>NEW VALUE!</td>
      <td>NEW VALUE!</td>
      <td>NEW VALUE!</td>
      <td>NEW VALUE!</td>
      <td>NEW VALUE!</td>
      <td>NEW VALUE!</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Hugh</td>
      <td>Jackman</td>
      <td>51</td>
      <td>m</td>
      <td>NEW VALUE!</td>
      <td>NEW VALUE!</td>
    </tr>
    <tr>
      <th>3</th>
      <td>Oprah</td>
      <td>Winfrey</td>
      <td>66</td>
      <td>f</td>
      <td>6</td>
      <td>8</td>
    </tr>
    <tr>
      <th>4</th>
      <td>Emma</td>
      <td>Stone</td>
      <td>31</td>
      <td>f</td>
      <td>7</td>
      <td>9</td>
    </tr>
  </tbody>
</table>
</div>




```python
df['first_name'].fillna("Empty")
```




    0      Tom
    1    Empty
    2     Hugh
    3    Oprah
    4     Emma
    Name: first_name, dtype: object




```python
df['first_name'] = df['first_name'].fillna("Empty")
```


```python
df
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
      <th>first_name</th>
      <th>last_name</th>
      <th>age</th>
      <th>sex</th>
      <th>pre_movie_score</th>
      <th>post_movie_score</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Tom</td>
      <td>Hanks</td>
      <td>63.0</td>
      <td>m</td>
      <td>8.0</td>
      <td>10.0</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Empty</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Hugh</td>
      <td>Jackman</td>
      <td>51.0</td>
      <td>m</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>3</th>
      <td>Oprah</td>
      <td>Winfrey</td>
      <td>66.0</td>
      <td>f</td>
      <td>6.0</td>
      <td>8.0</td>
    </tr>
    <tr>
      <th>4</th>
      <td>Emma</td>
      <td>Stone</td>
      <td>31.0</td>
      <td>f</td>
      <td>7.0</td>
      <td>9.0</td>
    </tr>
  </tbody>
</table>
</div>




```python
df['pre_movie_score'].mean()
```




    7.0




```python
df['pre_movie_score'].fillna(df['pre_movie_score'].mean())
```




    0    8.0
    1    7.0
    2    7.0
    3    6.0
    4    7.0
    Name: pre_movie_score, dtype: float64




```python
df.fillna(df.mean())
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
      <th>first_name</th>
      <th>last_name</th>
      <th>age</th>
      <th>sex</th>
      <th>pre_movie_score</th>
      <th>post_movie_score</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Tom</td>
      <td>Hanks</td>
      <td>63.00</td>
      <td>m</td>
      <td>8.0</td>
      <td>10.0</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Empty</td>
      <td>NaN</td>
      <td>52.75</td>
      <td>NaN</td>
      <td>7.0</td>
      <td>9.0</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Hugh</td>
      <td>Jackman</td>
      <td>51.00</td>
      <td>m</td>
      <td>7.0</td>
      <td>9.0</td>
    </tr>
    <tr>
      <th>3</th>
      <td>Oprah</td>
      <td>Winfrey</td>
      <td>66.00</td>
      <td>f</td>
      <td>6.0</td>
      <td>8.0</td>
    </tr>
    <tr>
      <th>4</th>
      <td>Emma</td>
      <td>Stone</td>
      <td>31.00</td>
      <td>f</td>
      <td>7.0</td>
      <td>9.0</td>
    </tr>
  </tbody>
</table>
</div>



## Filling with Interpolation

Be careful with this technique, you should try to really understand whether or not this is a valid choice for your data. You should also note there are several methods available, the default is a linear method.

Full Docs on this Method:
https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.interpolate.html


```python
airline_tix = {'first':100,'business':np.nan,'economy-plus':50,'economy':30}
```


```python
ser = pd.Series(airline_tix)
```


```python
ser
```




    first           100.0
    business          NaN
    economy-plus     50.0
    economy          30.0
    dtype: float64




```python
ser.interpolate()
```




    first           100.0
    business         75.0
    economy-plus     50.0
    economy          30.0
    dtype: float64




```python
ser.interpolate(method='spline')
```


    ---------------------------------------------------------------------------

    ValueError                                Traceback (most recent call last)

    <ipython-input-163-106f2287918c> in <module>
    ----> 1 ser.interpolate(method='spline')
    

    c:\users\marcial\anaconda3\envs\ml_master\lib\site-packages\pandas\core\generic.py in interpolate(self, method, axis, limit, inplace, limit_direction, limit_area, downcast, **kwargs)
       6992             if method not in methods and not is_numeric_or_datetime:
       6993                 raise ValueError(
    -> 6994                     "Index column must be numeric or datetime type when "
       6995                     f"using {method} method other than linear. "
       6996                     "Try setting a numeric or datetime index column before "
    

    ValueError: Index column must be numeric or datetime type when using spline method other than linear. Try setting a numeric or datetime index column before interpolating.



```python
df = pd.DataFrame(ser,columns=['Price'])
```


```python
df
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
      <th>Price</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>first</th>
      <td>100.0</td>
    </tr>
    <tr>
      <th>business</th>
      <td>NaN</td>
    </tr>
    <tr>
      <th>economy-plus</th>
      <td>50.0</td>
    </tr>
    <tr>
      <th>economy</th>
      <td>30.0</td>
    </tr>
  </tbody>
</table>
</div>




```python
df.interpolate()
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
      <th>Price</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>first</th>
      <td>100.0</td>
    </tr>
    <tr>
      <th>business</th>
      <td>75.0</td>
    </tr>
    <tr>
      <th>economy-plus</th>
      <td>50.0</td>
    </tr>
    <tr>
      <th>economy</th>
      <td>30.0</td>
    </tr>
  </tbody>
</table>
</div>




```python
df = df.reset_index()
```


```python
df
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
      <th>index</th>
      <th>Price</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>first</td>
      <td>100.0</td>
    </tr>
    <tr>
      <th>1</th>
      <td>business</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>2</th>
      <td>economy-plus</td>
      <td>50.0</td>
    </tr>
    <tr>
      <th>3</th>
      <td>economy</td>
      <td>30.0</td>
    </tr>
  </tbody>
</table>
</div>




```python
df.interpolate(method='spline',order=2)
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
      <th>index</th>
      <th>Price</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>first</td>
      <td>100.000000</td>
    </tr>
    <tr>
      <th>1</th>
      <td>business</td>
      <td>73.333333</td>
    </tr>
    <tr>
      <th>2</th>
      <td>economy-plus</td>
      <td>50.000000</td>
    </tr>
    <tr>
      <th>3</th>
      <td>economy</td>
      <td>30.000000</td>
    </tr>
  </tbody>
</table>
</div>


