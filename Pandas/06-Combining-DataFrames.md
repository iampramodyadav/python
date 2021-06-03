<h1>Table of Contents<span class="tocSkip"></span></h1>
<div class="toc"><ul class="toc-item"><li><span><a href="#Combining-DataFrames" data-toc-modified-id="Combining-DataFrames-1"><span class="toc-item-num">1&nbsp;&nbsp;</span>Combining DataFrames</a></span><ul class="toc-item"><li><span><a href="#Full-Official-Guide-(Lots-of-examples!)" data-toc-modified-id="Full-Official-Guide-(Lots-of-examples!)-1.1"><span class="toc-item-num">1.1&nbsp;&nbsp;</span>Full Official Guide (Lots of examples!)</a></span><ul class="toc-item"><li><span><a href="#https://pandas.pydata.org/pandas-docs/stable/user_guide/merging.html" data-toc-modified-id="https://pandas.pydata.org/pandas-docs/stable/user_guide/merging.html-1.1.1"><span class="toc-item-num">1.1.1&nbsp;&nbsp;</span><a href="https://pandas.pydata.org/pandas-docs/stable/user_guide/merging.html" target="_blank">https://pandas.pydata.org/pandas-docs/stable/user_guide/merging.html</a></a></span></li></ul></li><li><span><a href="#Concatenation" data-toc-modified-id="Concatenation-1.2"><span class="toc-item-num">1.2&nbsp;&nbsp;</span>Concatenation</a></span></li><li><span><a href="#Axis-=-0" data-toc-modified-id="Axis-=-0-1.3"><span class="toc-item-num">1.3&nbsp;&nbsp;</span>Axis = 0</a></span><ul class="toc-item"><li><span><a href="#Concatenate-along-rows" data-toc-modified-id="Concatenate-along-rows-1.3.1"><span class="toc-item-num">1.3.1&nbsp;&nbsp;</span>Concatenate along rows</a></span></li></ul></li><li><span><a href="#Axis-=-1" data-toc-modified-id="Axis-=-1-1.4"><span class="toc-item-num">1.4&nbsp;&nbsp;</span>Axis = 1</a></span><ul class="toc-item"><li><span><a href="#Concatenate-along-columns" data-toc-modified-id="Concatenate-along-columns-1.4.1"><span class="toc-item-num">1.4.1&nbsp;&nbsp;</span>Concatenate along columns</a></span></li><li><span><a href="#Axis-0-,-but-columns-match-up" data-toc-modified-id="Axis-0-,-but-columns-match-up-1.4.2"><span class="toc-item-num">1.4.2&nbsp;&nbsp;</span>Axis 0 , but columns match up</a></span></li></ul></li></ul></li><li><span><a href="#Merge" data-toc-modified-id="Merge-2"><span class="toc-item-num">2&nbsp;&nbsp;</span>Merge</a></span><ul class="toc-item"><li><span><a href="#Data-Tables" data-toc-modified-id="Data-Tables-2.1"><span class="toc-item-num">2.1&nbsp;&nbsp;</span>Data Tables</a></span></li></ul></li><li><span><a href="#pd.merge()" data-toc-modified-id="pd.merge()-3"><span class="toc-item-num">3&nbsp;&nbsp;</span>pd.merge()</a></span></li><li><span><a href="#Inner,Left,-Right,-and-Outer-Joins" data-toc-modified-id="Inner,Left,-Right,-and-Outer-Joins-4"><span class="toc-item-num">4&nbsp;&nbsp;</span>Inner,Left, Right, and Outer Joins</a></span><ul class="toc-item"><li><span><a href="#Inner-Join" data-toc-modified-id="Inner-Join-4.1"><span class="toc-item-num">4.1&nbsp;&nbsp;</span>Inner Join</a></span></li><li><span><a href="#Left-Join" data-toc-modified-id="Left-Join-4.2"><span class="toc-item-num">4.2&nbsp;&nbsp;</span>Left Join</a></span></li><li><span><a href="#Right-Join" data-toc-modified-id="Right-Join-4.3"><span class="toc-item-num">4.3&nbsp;&nbsp;</span>Right Join</a></span></li><li><span><a href="#Outer-Join" data-toc-modified-id="Outer-Join-4.4"><span class="toc-item-num">4.4&nbsp;&nbsp;</span>Outer Join</a></span></li><li><span><a href="#Join-on-Index-or-Column" data-toc-modified-id="Join-on-Index-or-Column-4.5"><span class="toc-item-num">4.5&nbsp;&nbsp;</span>Join on Index or Column</a></span><ul class="toc-item"><li><span><a href="#Dealing-with-differing-key-column-names-in-joined-tables" data-toc-modified-id="Dealing-with-differing-key-column-names-in-joined-tables-4.5.1"><span class="toc-item-num">4.5.1&nbsp;&nbsp;</span>Dealing with differing key column names in joined tables</a></span></li><li><span><a href="#Pandas-automatically-tags-duplicate-columns" data-toc-modified-id="Pandas-automatically-tags-duplicate-columns-4.5.2"><span class="toc-item-num">4.5.2&nbsp;&nbsp;</span>Pandas automatically tags duplicate columns</a></span></li></ul></li></ul></li></ul></div>

# Combining DataFrames

## Full Official Guide (Lots of examples!)

### https://pandas.pydata.org/pandas-docs/stable/user_guide/merging.html

-------
-------


```python
import numpy as np
import pandas as pd
```

## Concatenation

Directly  "glue" together dataframes.


```python
data_one = {'A': ['A0', 'A1', 'A2', 'A3'],'B': ['B0', 'B1', 'B2', 'B3']}
```


```python
data_two = {'C': ['C0', 'C1', 'C2', 'C3'], 'D': ['D0', 'D1', 'D2', 'D3']}
```


```python
one = pd.DataFrame(data_one)
```


```python
two = pd.DataFrame(data_two)
```


```python
one
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
      <th>A</th>
      <th>B</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>A0</td>
      <td>B0</td>
    </tr>
    <tr>
      <th>1</th>
      <td>A1</td>
      <td>B1</td>
    </tr>
    <tr>
      <th>2</th>
      <td>A2</td>
      <td>B2</td>
    </tr>
    <tr>
      <th>3</th>
      <td>A3</td>
      <td>B3</td>
    </tr>
  </tbody>
</table>
</div>




```python
two
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
      <th>C</th>
      <th>D</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>C0</td>
      <td>D0</td>
    </tr>
    <tr>
      <th>1</th>
      <td>C1</td>
      <td>D1</td>
    </tr>
    <tr>
      <th>2</th>
      <td>C2</td>
      <td>D2</td>
    </tr>
    <tr>
      <th>3</th>
      <td>C3</td>
      <td>D3</td>
    </tr>
  </tbody>
</table>
</div>



## Axis = 0 

### Concatenate along rows


```python
axis0 = pd.concat([one,two],axis=0)
```


```python
axis0
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
      <th>A</th>
      <th>B</th>
      <th>C</th>
      <th>D</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>A0</td>
      <td>B0</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>1</th>
      <td>A1</td>
      <td>B1</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>2</th>
      <td>A2</td>
      <td>B2</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>3</th>
      <td>A3</td>
      <td>B3</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>0</th>
      <td>NaN</td>
      <td>NaN</td>
      <td>C0</td>
      <td>D0</td>
    </tr>
    <tr>
      <th>1</th>
      <td>NaN</td>
      <td>NaN</td>
      <td>C1</td>
      <td>D1</td>
    </tr>
    <tr>
      <th>2</th>
      <td>NaN</td>
      <td>NaN</td>
      <td>C2</td>
      <td>D2</td>
    </tr>
    <tr>
      <th>3</th>
      <td>NaN</td>
      <td>NaN</td>
      <td>C3</td>
      <td>D3</td>
    </tr>
  </tbody>
</table>
</div>



## Axis = 1

### Concatenate along columns


```python
axis1 = pd.concat([one,two],axis=1)
```


```python
axis1
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
      <th>A</th>
      <th>B</th>
      <th>C</th>
      <th>D</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>A0</td>
      <td>B0</td>
      <td>C0</td>
      <td>D0</td>
    </tr>
    <tr>
      <th>1</th>
      <td>A1</td>
      <td>B1</td>
      <td>C1</td>
      <td>D1</td>
    </tr>
    <tr>
      <th>2</th>
      <td>A2</td>
      <td>B2</td>
      <td>C2</td>
      <td>D2</td>
    </tr>
    <tr>
      <th>3</th>
      <td>A3</td>
      <td>B3</td>
      <td>C3</td>
      <td>D3</td>
    </tr>
  </tbody>
</table>
</div>



### Axis 0 , but columns match up
**In case you wanted this:**


```python
two.columns = one.columns
```


```python
pd.concat([one,two])
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
      <th>A</th>
      <th>B</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>A0</td>
      <td>B0</td>
    </tr>
    <tr>
      <th>1</th>
      <td>A1</td>
      <td>B1</td>
    </tr>
    <tr>
      <th>2</th>
      <td>A2</td>
      <td>B2</td>
    </tr>
    <tr>
      <th>3</th>
      <td>A3</td>
      <td>B3</td>
    </tr>
    <tr>
      <th>0</th>
      <td>C0</td>
      <td>D0</td>
    </tr>
    <tr>
      <th>1</th>
      <td>C1</td>
      <td>D1</td>
    </tr>
    <tr>
      <th>2</th>
      <td>C2</td>
      <td>D2</td>
    </tr>
    <tr>
      <th>3</th>
      <td>C3</td>
      <td>D3</td>
    </tr>
  </tbody>
</table>
</div>



# Merge

## Data Tables


```python
registrations = pd.DataFrame({'reg_id':[1,2,3,4],'name':['Andrew','Bobo','Claire','David']})
logins = pd.DataFrame({'log_id':[1,2,3,4],'name':['Xavier','Andrew','Yolanda','Bobo']})
```


```python
registrations
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
      <th>reg_id</th>
      <th>name</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1</td>
      <td>Andrew</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2</td>
      <td>Bobo</td>
    </tr>
    <tr>
      <th>2</th>
      <td>3</td>
      <td>Claire</td>
    </tr>
    <tr>
      <th>3</th>
      <td>4</td>
      <td>David</td>
    </tr>
  </tbody>
</table>
</div>




```python
logins
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
      <th>log_id</th>
      <th>name</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1</td>
      <td>Xavier</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2</td>
      <td>Andrew</td>
    </tr>
    <tr>
      <th>2</th>
      <td>3</td>
      <td>Yolanda</td>
    </tr>
    <tr>
      <th>3</th>
      <td>4</td>
      <td>Bobo</td>
    </tr>
  </tbody>
</table>
</div>



# pd.merge()

Merge pandas DataFrames based on key columns, similar to a SQL join. Results based on the **how** parameter.


```python
help(pd.merge)
```

    Help on function merge in module pandas.core.reshape.merge:
    
    merge(left, right, how: str = 'inner', on=None, left_on=None, right_on=None, left_index: bool = False, right_index: bool = False, sort: bool = False, suffixes=('_x', '_y'), copy: bool = True, indicator: bool = False, validate=None) -> 'DataFrame'
        Merge DataFrame or named Series objects with a database-style join.
        
        The join is done on columns or indexes. If joining columns on
        columns, the DataFrame indexes *will be ignored*. Otherwise if joining indexes
        on indexes or indexes on a column or columns, the index will be passed on.
        When performing a cross merge, no column specifications to merge on are
        allowed.
        
        Parameters
        ----------
        left : DataFrame
        right : DataFrame or named Series
            Object to merge with.
        how : {'left', 'right', 'outer', 'inner', 'cross'}, default 'inner'
            Type of merge to be performed.
        
            * left: use only keys from left frame, similar to a SQL left outer join;
              preserve key order.
            * right: use only keys from right frame, similar to a SQL right outer join;
              preserve key order.
            * outer: use union of keys from both frames, similar to a SQL full outer
              join; sort keys lexicographically.
            * inner: use intersection of keys from both frames, similar to a SQL inner
              join; preserve the order of the left keys.
            * cross: creates the cartesian product from both frames, preserves the order
              of the left keys.
        
              .. versionadded:: 1.2.0
        
        on : label or list
            Column or index level names to join on. These must be found in both
            DataFrames. If `on` is None and not merging on indexes then this defaults
            to the intersection of the columns in both DataFrames.
        left_on : label or list, or array-like
            Column or index level names to join on in the left DataFrame. Can also
            be an array or list of arrays of the length of the left DataFrame.
            These arrays are treated as if they are columns.
        right_on : label or list, or array-like
            Column or index level names to join on in the right DataFrame. Can also
            be an array or list of arrays of the length of the right DataFrame.
            These arrays are treated as if they are columns.
        left_index : bool, default False
            Use the index from the left DataFrame as the join key(s). If it is a
            MultiIndex, the number of keys in the other DataFrame (either the index
            or a number of columns) must match the number of levels.
        right_index : bool, default False
            Use the index from the right DataFrame as the join key. Same caveats as
            left_index.
        sort : bool, default False
            Sort the join keys lexicographically in the result DataFrame. If False,
            the order of the join keys depends on the join type (how keyword).
        suffixes : list-like, default is ("_x", "_y")
            A length-2 sequence where each element is optionally a string
            indicating the suffix to add to overlapping column names in
            `left` and `right` respectively. Pass a value of `None` instead
            of a string to indicate that the column name from `left` or
            `right` should be left as-is, with no suffix. At least one of the
            values must not be None.
        copy : bool, default True
            If False, avoid copy if possible.
        indicator : bool or str, default False
            If True, adds a column to the output DataFrame called "_merge" with
            information on the source of each row. The column can be given a different
            name by providing a string argument. The column will have a Categorical
            type with the value of "left_only" for observations whose merge key only
            appears in the left DataFrame, "right_only" for observations
            whose merge key only appears in the right DataFrame, and "both"
            if the observation's merge key is found in both DataFrames.
        
        validate : str, optional
            If specified, checks if merge is of specified type.
        
            * "one_to_one" or "1:1": check if merge keys are unique in both
              left and right datasets.
            * "one_to_many" or "1:m": check if merge keys are unique in left
              dataset.
            * "many_to_one" or "m:1": check if merge keys are unique in right
              dataset.
            * "many_to_many" or "m:m": allowed, but does not result in checks.
        
        Returns
        -------
        DataFrame
            A DataFrame of the two merged objects.
        
        See Also
        --------
        merge_ordered : Merge with optional filling/interpolation.
        merge_asof : Merge on nearest keys.
        DataFrame.join : Similar method using indices.
        
        Notes
        -----
        Support for specifying index levels as the `on`, `left_on`, and
        `right_on` parameters was added in version 0.23.0
        Support for merging named Series objects was added in version 0.24.0
        
        Examples
        --------
        >>> df1 = pd.DataFrame({'lkey': ['foo', 'bar', 'baz', 'foo'],
        ...                     'value': [1, 2, 3, 5]})
        >>> df2 = pd.DataFrame({'rkey': ['foo', 'bar', 'baz', 'foo'],
        ...                     'value': [5, 6, 7, 8]})
        >>> df1
            lkey value
        0   foo      1
        1   bar      2
        2   baz      3
        3   foo      5
        >>> df2
            rkey value
        0   foo      5
        1   bar      6
        2   baz      7
        3   foo      8
        
        Merge df1 and df2 on the lkey and rkey columns. The value columns have
        the default suffixes, _x and _y, appended.
        
        >>> df1.merge(df2, left_on='lkey', right_on='rkey')
          lkey  value_x rkey  value_y
        0  foo        1  foo        5
        1  foo        1  foo        8
        2  foo        5  foo        5
        3  foo        5  foo        8
        4  bar        2  bar        6
        5  baz        3  baz        7
        
        Merge DataFrames df1 and df2 with specified left and right suffixes
        appended to any overlapping columns.
        
        >>> df1.merge(df2, left_on='lkey', right_on='rkey',
        ...           suffixes=('_left', '_right'))
          lkey  value_left rkey  value_right
        0  foo           1  foo            5
        1  foo           1  foo            8
        2  foo           5  foo            5
        3  foo           5  foo            8
        4  bar           2  bar            6
        5  baz           3  baz            7
        
        Merge DataFrames df1 and df2, but raise an exception if the DataFrames have
        any overlapping columns.
        
        >>> df1.merge(df2, left_on='lkey', right_on='rkey', suffixes=(False, False))
        Traceback (most recent call last):
        ...
        ValueError: columns overlap but no suffix specified:
            Index(['value'], dtype='object')
        
        >>> df1 = pd.DataFrame({'a': ['foo', 'bar'], 'b': [1, 2]})
        >>> df2 = pd.DataFrame({'a': ['foo', 'baz'], 'c': [3, 4]})
        >>> df1
              a  b
        0   foo  1
        1   bar  2
        >>> df2
              a  c
        0   foo  3
        1   baz  4
        
        >>> df1.merge(df2, how='inner', on='a')
              a  b  c
        0   foo  1  3
        
        >>> df1.merge(df2, how='left', on='a')
              a  b  c
        0   foo  1  3.0
        1   bar  2  NaN
        
        >>> df1 = pd.DataFrame({'left': ['foo', 'bar']})
        >>> df2 = pd.DataFrame({'right': [7, 8]})
        >>> df1
            left
        0   foo
        1   bar
        >>> df2
            right
        0   7
        1   8
        
        >>> df1.merge(df2, how='cross')
           left  right
        0   foo      7
        1   foo      8
        2   bar      7
        3   bar      8
    
    

-----

# Inner,Left, Right, and Outer Joins

## Inner Join

**Match up where the key is present in BOTH tables. There should be no NaNs due to the join, since by definition to be part of the Inner Join they need info in both tables.**
**Only Andrew and Bobo both registered and logged in.**


```python
# Notice pd.merge doesn't take in a list like concat
pd.merge(registrations,logins,how='inner',on='name')
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
      <th>reg_id</th>
      <th>name</th>
      <th>log_id</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1</td>
      <td>Andrew</td>
      <td>2</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2</td>
      <td>Bobo</td>
      <td>4</td>
    </tr>
  </tbody>
</table>
</div>




```python
# Pandas smart enough to figure out key column (on parameter) if only one column name matches up
pd.merge(registrations,logins,how='inner')
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
      <th>reg_id</th>
      <th>name</th>
      <th>log_id</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1</td>
      <td>Andrew</td>
      <td>2</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2</td>
      <td>Bobo</td>
      <td>4</td>
    </tr>
  </tbody>
</table>
</div>




```python
# Pandas reports an error if "on" key column isn't in both dataframes
# pd.merge(registrations,logins,how='inner',on='reg_id')
```

---

## Left Join

**Match up AND include all rows from Left Table.**
**Show everyone who registered on Left Table, if they don't have login info, then fill with NaN.**


```python
pd.merge(registrations,logins,how='left')
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
      <th>reg_id</th>
      <th>name</th>
      <th>log_id</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1</td>
      <td>Andrew</td>
      <td>2.0</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2</td>
      <td>Bobo</td>
      <td>4.0</td>
    </tr>
    <tr>
      <th>2</th>
      <td>3</td>
      <td>Claire</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>3</th>
      <td>4</td>
      <td>David</td>
      <td>NaN</td>
    </tr>
  </tbody>
</table>
</div>



## Right Join
**Match up AND include all rows from Right Table.**
**Show everyone who logged in on the Right Table, if they don't have registration info, then fill with NaN.**


```python
pd.merge(registrations,logins,how='right')
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
      <th>reg_id</th>
      <th>name</th>
      <th>log_id</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>NaN</td>
      <td>Xavier</td>
      <td>1</td>
    </tr>
    <tr>
      <th>1</th>
      <td>1.0</td>
      <td>Andrew</td>
      <td>2</td>
    </tr>
    <tr>
      <th>2</th>
      <td>NaN</td>
      <td>Yolanda</td>
      <td>3</td>
    </tr>
    <tr>
      <th>3</th>
      <td>2.0</td>
      <td>Bobo</td>
      <td>4</td>
    </tr>
  </tbody>
</table>
</div>



## Outer Join

**Match up on all info found in either Left or Right Table.**
**Show everyone that's in the Log in table and the registrations table. Fill any missing info with NaN**


```python
pd.merge(registrations,logins,how='outer')
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
      <th>reg_id</th>
      <th>name</th>
      <th>log_id</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1.0</td>
      <td>Andrew</td>
      <td>2.0</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2.0</td>
      <td>Bobo</td>
      <td>4.0</td>
    </tr>
    <tr>
      <th>2</th>
      <td>3.0</td>
      <td>Claire</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>3</th>
      <td>4.0</td>
      <td>David</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>4</th>
      <td>NaN</td>
      <td>Xavier</td>
      <td>1.0</td>
    </tr>
    <tr>
      <th>5</th>
      <td>NaN</td>
      <td>Yolanda</td>
      <td>3.0</td>
    </tr>
  </tbody>
</table>
</div>



## Join on Index or Column

**Use combinations of left_on,right_on,left_index,right_index to merge a column or index on each other**


```python
registrations
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
      <th>reg_id</th>
      <th>name</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1</td>
      <td>Andrew</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2</td>
      <td>Bobo</td>
    </tr>
    <tr>
      <th>2</th>
      <td>3</td>
      <td>Claire</td>
    </tr>
    <tr>
      <th>3</th>
      <td>4</td>
      <td>David</td>
    </tr>
  </tbody>
</table>
</div>




```python
logins
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
      <th>log_id</th>
      <th>name</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1</td>
      <td>Xavier</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2</td>
      <td>Andrew</td>
    </tr>
    <tr>
      <th>2</th>
      <td>3</td>
      <td>Yolanda</td>
    </tr>
    <tr>
      <th>3</th>
      <td>4</td>
      <td>Bobo</td>
    </tr>
  </tbody>
</table>
</div>




```python
registrations = registrations.set_index("name")
```


```python
registrations
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
      <th>reg_id</th>
    </tr>
    <tr>
      <th>name</th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Andrew</th>
      <td>1</td>
    </tr>
    <tr>
      <th>Bobo</th>
      <td>2</td>
    </tr>
    <tr>
      <th>Claire</th>
      <td>3</td>
    </tr>
    <tr>
      <th>David</th>
      <td>4</td>
    </tr>
  </tbody>
</table>
</div>




```python
pd.merge(registrations,logins,left_index=True,right_on='name')
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
      <th>reg_id</th>
      <th>log_id</th>
      <th>name</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>1</th>
      <td>1</td>
      <td>2</td>
      <td>Andrew</td>
    </tr>
    <tr>
      <th>3</th>
      <td>2</td>
      <td>4</td>
      <td>Bobo</td>
    </tr>
  </tbody>
</table>
</div>




```python
pd.merge(logins,registrations,right_index=True,left_on='name')
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
      <th>log_id</th>
      <th>name</th>
      <th>reg_id</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>1</th>
      <td>2</td>
      <td>Andrew</td>
      <td>1</td>
    </tr>
    <tr>
      <th>3</th>
      <td>4</td>
      <td>Bobo</td>
      <td>2</td>
    </tr>
  </tbody>
</table>
</div>



### Dealing with differing key column names in joined tables


```python
registrations = registrations.reset_index()
```


```python
registrations
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
      <th>name</th>
      <th>reg_id</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Andrew</td>
      <td>1</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Bobo</td>
      <td>2</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Claire</td>
      <td>3</td>
    </tr>
    <tr>
      <th>3</th>
      <td>David</td>
      <td>4</td>
    </tr>
  </tbody>
</table>
</div>




```python
logins
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
      <th>log_id</th>
      <th>name</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1</td>
      <td>Xavier</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2</td>
      <td>Andrew</td>
    </tr>
    <tr>
      <th>2</th>
      <td>3</td>
      <td>Yolanda</td>
    </tr>
    <tr>
      <th>3</th>
      <td>4</td>
      <td>Bobo</td>
    </tr>
  </tbody>
</table>
</div>




```python
registrations.columns = ['reg_name','reg_id']
```


```python
registrations
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
      <th>reg_name</th>
      <th>reg_id</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Andrew</td>
      <td>1</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Bobo</td>
      <td>2</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Claire</td>
      <td>3</td>
    </tr>
    <tr>
      <th>3</th>
      <td>David</td>
      <td>4</td>
    </tr>
  </tbody>
</table>
</div>




```python
# ERROR
# pd.merge(registrations,logins)
```


```python
pd.merge(registrations,logins,left_on='reg_name',right_on='name')
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
      <th>reg_name</th>
      <th>reg_id</th>
      <th>log_id</th>
      <th>name</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Andrew</td>
      <td>1</td>
      <td>2</td>
      <td>Andrew</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Bobo</td>
      <td>2</td>
      <td>4</td>
      <td>Bobo</td>
    </tr>
  </tbody>
</table>
</div>




```python
pd.merge(registrations,logins,left_on='reg_name',right_on='name').drop('reg_name',axis=1)
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
      <th>reg_id</th>
      <th>log_id</th>
      <th>name</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1</td>
      <td>2</td>
      <td>Andrew</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2</td>
      <td>4</td>
      <td>Bobo</td>
    </tr>
  </tbody>
</table>
</div>



### Pandas automatically tags duplicate columns


```python
registrations.columns = ['name','id']
```


```python
logins.columns = ['id','name']
```


```python
registrations
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
      <th>name</th>
      <th>id</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Andrew</td>
      <td>1</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Bobo</td>
      <td>2</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Claire</td>
      <td>3</td>
    </tr>
    <tr>
      <th>3</th>
      <td>David</td>
      <td>4</td>
    </tr>
  </tbody>
</table>
</div>




```python
logins
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
      <th>id</th>
      <th>name</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1</td>
      <td>Xavier</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2</td>
      <td>Andrew</td>
    </tr>
    <tr>
      <th>2</th>
      <td>3</td>
      <td>Yolanda</td>
    </tr>
    <tr>
      <th>3</th>
      <td>4</td>
      <td>Bobo</td>
    </tr>
  </tbody>
</table>
</div>




```python
# _x is for left
# _y is for right
pd.merge(registrations,logins,on='name')
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
      <th>name</th>
      <th>id_x</th>
      <th>id_y</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Andrew</td>
      <td>1</td>
      <td>2</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Bobo</td>
      <td>2</td>
      <td>4</td>
    </tr>
  </tbody>
</table>
</div>




```python
pd.merge(registrations,logins,on='name',suffixes=('_reg','_log'))
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
      <th>name</th>
      <th>id_reg</th>
      <th>id_log</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Andrew</td>
      <td>1</td>
      <td>2</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Bobo</td>
      <td>2</td>
      <td>4</td>
    </tr>
  </tbody>
</table>
</div>



-----------
----------
