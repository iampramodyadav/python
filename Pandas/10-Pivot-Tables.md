<h1>Table of Contents<span class="tocSkip"></span></h1>
<div class="toc"><ul class="toc-item"><li><span><a href="#Pivot-Tables" data-toc-modified-id="Pivot-Tables-1"><span class="toc-item-num">1&nbsp;&nbsp;</span>Pivot Tables</a></span><ul class="toc-item"><li><span><a href="#Data" data-toc-modified-id="Data-1.1"><span class="toc-item-num">1.1&nbsp;&nbsp;</span>Data</a></span></li></ul></li><li><span><a href="#The-pivot()-method" data-toc-modified-id="The-pivot()-method-2"><span class="toc-item-num">2&nbsp;&nbsp;</span>The pivot() method</a></span><ul class="toc-item"><li><ul class="toc-item"><li><ul class="toc-item"><li><span><a href="#Note:" data-toc-modified-id="Note:-2.0.0.1"><span class="toc-item-num">2.0.0.1&nbsp;&nbsp;</span>Note:</a></span></li></ul></li></ul></li><li><span><a href="#The-pivot_table()-method" data-toc-modified-id="The-pivot_table()-method-2.1"><span class="toc-item-num">2.1&nbsp;&nbsp;</span>The pivot_table() method</a></span></li></ul></li></ul></div>

# Pivot Tables

Pivoting data can sometimes help clarify relationships and connections.

Full documentation on a variety of related pivot methods: https://pandas.pydata.org/docs/user_guide/reshaping.html

## Data


```python
import numpy as np
import pandas as pd
```


```python
df = pd.read_csv('Sales_Funnel_CRM.csv')
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
      <th>Account Number</th>
      <th>Company</th>
      <th>Contact</th>
      <th>Account Manager</th>
      <th>Product</th>
      <th>Licenses</th>
      <th>Sale Price</th>
      <th>Status</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>2123398</td>
      <td>Google</td>
      <td>Larry Pager</td>
      <td>Edward Thorp</td>
      <td>Analytics</td>
      <td>150</td>
      <td>2100000</td>
      <td>Presented</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2123398</td>
      <td>Google</td>
      <td>Larry Pager</td>
      <td>Edward Thorp</td>
      <td>Prediction</td>
      <td>150</td>
      <td>700000</td>
      <td>Presented</td>
    </tr>
    <tr>
      <th>2</th>
      <td>2123398</td>
      <td>Google</td>
      <td>Larry Pager</td>
      <td>Edward Thorp</td>
      <td>Tracking</td>
      <td>300</td>
      <td>350000</td>
      <td>Under Review</td>
    </tr>
    <tr>
      <th>3</th>
      <td>2192650</td>
      <td>BOBO</td>
      <td>Larry Pager</td>
      <td>Edward Thorp</td>
      <td>Analytics</td>
      <td>150</td>
      <td>2450000</td>
      <td>Lost</td>
    </tr>
    <tr>
      <th>4</th>
      <td>420496</td>
      <td>IKEA</td>
      <td>Elon Tusk</td>
      <td>Edward Thorp</td>
      <td>Analytics</td>
      <td>300</td>
      <td>4550000</td>
      <td>Won</td>
    </tr>
    <tr>
      <th>5</th>
      <td>636685</td>
      <td>Tesla Inc.</td>
      <td>Elon Tusk</td>
      <td>Edward Thorp</td>
      <td>Analytics</td>
      <td>300</td>
      <td>2800000</td>
      <td>Under Review</td>
    </tr>
    <tr>
      <th>6</th>
      <td>636685</td>
      <td>Tesla Inc.</td>
      <td>Elon Tusk</td>
      <td>Edward Thorp</td>
      <td>Prediction</td>
      <td>150</td>
      <td>700000</td>
      <td>Presented</td>
    </tr>
    <tr>
      <th>7</th>
      <td>1216870</td>
      <td>Microsoft</td>
      <td>Will Grates</td>
      <td>Edward Thorp</td>
      <td>Tracking</td>
      <td>300</td>
      <td>350000</td>
      <td>Under Review</td>
    </tr>
    <tr>
      <th>8</th>
      <td>2200450</td>
      <td>Walmart</td>
      <td>Will Grates</td>
      <td>Edward Thorp</td>
      <td>Analytics</td>
      <td>150</td>
      <td>2450000</td>
      <td>Lost</td>
    </tr>
    <tr>
      <th>9</th>
      <td>405886</td>
      <td>Apple</td>
      <td>Cindy Phoner</td>
      <td>Claude Shannon</td>
      <td>Analytics</td>
      <td>300</td>
      <td>4550000</td>
      <td>Won</td>
    </tr>
    <tr>
      <th>10</th>
      <td>470248</td>
      <td>Exxon Mobile</td>
      <td>Cindy Phoner</td>
      <td>Claude Shannon</td>
      <td>Analytics</td>
      <td>150</td>
      <td>2100000</td>
      <td>Presented</td>
    </tr>
    <tr>
      <th>11</th>
      <td>698032</td>
      <td>ATT</td>
      <td>Cindy Phoner</td>
      <td>Claude Shannon</td>
      <td>Tracking</td>
      <td>150</td>
      <td>350000</td>
      <td>Under Review</td>
    </tr>
    <tr>
      <th>12</th>
      <td>698032</td>
      <td>ATT</td>
      <td>Cindy Phoner</td>
      <td>Claude Shannon</td>
      <td>Prediction</td>
      <td>150</td>
      <td>700000</td>
      <td>Presented</td>
    </tr>
    <tr>
      <th>13</th>
      <td>902797</td>
      <td>CVS Health</td>
      <td>Emma Gordian</td>
      <td>Claude Shannon</td>
      <td>Tracking</td>
      <td>450</td>
      <td>490000</td>
      <td>Won</td>
    </tr>
    <tr>
      <th>14</th>
      <td>2046943</td>
      <td>Salesforce</td>
      <td>Emma Gordian</td>
      <td>Claude Shannon</td>
      <td>Analytics</td>
      <td>750</td>
      <td>7000000</td>
      <td>Won</td>
    </tr>
    <tr>
      <th>15</th>
      <td>2169499</td>
      <td>Cisco</td>
      <td>Emma Gordian</td>
      <td>Claude Shannon</td>
      <td>Analytics</td>
      <td>300</td>
      <td>4550000</td>
      <td>Lost</td>
    </tr>
    <tr>
      <th>16</th>
      <td>2169499</td>
      <td>Cisco</td>
      <td>Emma Gordian</td>
      <td>Claude Shannon</td>
      <td>GPS Positioning</td>
      <td>300</td>
      <td>350000</td>
      <td>Presented</td>
    </tr>
  </tbody>
</table>
</div>



# The pivot() method

The pivot method reshapes data based on column values and reassignment of the index. Keep in mind, it doesn't always make sense to pivot data. In our machine learning lessons, we will see that our data doesn't need to be pivoted. Pivot methods are mainly for data analysis,visualization, and exploration.

----

Here is an image showing the idea behind a pivot() call:

< img src='reshaping_pivot.png'>

![Pivot](https://pandas.pydata.org/pandas-docs/version/0.25.3/_images/reshaping_pivot.png)


```python
help(pd.pivot)
```

    Help on function pivot in module pandas.core.reshape.pivot:
    
    pivot(data:'DataFrame', index=None, columns=None, values=None) -> 'DataFrame'
        Return reshaped DataFrame organized by given index / column values.
        
        Reshape data (produce a "pivot" table) based on column values. Uses
        unique values from specified `index` / `columns` to form axes of the
        resulting DataFrame. This function does not support data
        aggregation, multiple values will result in a MultiIndex in the
        columns. See the :ref:`User Guide <reshaping>` for more on reshaping.
        
        Parameters
        ----------
        data : DataFrame
        index : str or object, optional
            Column to use to make new frame's index. If None, uses
            existing index.
        columns : str or object
            Column to use to make new frame's columns.
        values : str, object or a list of the previous, optional
            Column(s) to use for populating new frame's values. If not
            specified, all remaining columns will be used and the result will
            have hierarchically indexed columns.
        
            .. versionchanged:: 0.23.0
               Also accept list of column names.
        
        Returns
        -------
        DataFrame
            Returns reshaped DataFrame.
        
        Raises
        ------
        ValueError:
            When there are any `index`, `columns` combinations with multiple
            values. `DataFrame.pivot_table` when you need to aggregate.
        
        See Also
        --------
        DataFrame.pivot_table : Generalization of pivot that can handle
            duplicate values for one index/column pair.
        DataFrame.unstack : Pivot based on the index values instead of a
            column.
        
        Notes
        -----
        For finer-tuned control, see hierarchical indexing documentation along
        with the related stack/unstack methods.
        
        Examples
        --------
        >>> df = pd.DataFrame({'foo': ['one', 'one', 'one', 'two', 'two',
        ...                            'two'],
        ...                    'bar': ['A', 'B', 'C', 'A', 'B', 'C'],
        ...                    'baz': [1, 2, 3, 4, 5, 6],
        ...                    'zoo': ['x', 'y', 'z', 'q', 'w', 't']})
        >>> df
            foo   bar  baz  zoo
        0   one   A    1    x
        1   one   B    2    y
        2   one   C    3    z
        3   two   A    4    q
        4   two   B    5    w
        5   two   C    6    t
        
        >>> df.pivot(index='foo', columns='bar', values='baz')
        bar  A   B   C
        foo
        one  1   2   3
        two  4   5   6
        
        >>> df.pivot(index='foo', columns='bar')['baz']
        bar  A   B   C
        foo
        one  1   2   3
        two  4   5   6
        
        >>> df.pivot(index='foo', columns='bar', values=['baz', 'zoo'])
              baz       zoo
        bar   A  B  C   A  B  C
        foo
        one   1  2  3   x  y  z
        two   4  5  6   q  w  t
        
        A ValueError is raised if there are any duplicates.
        
        >>> df = pd.DataFrame({"foo": ['one', 'one', 'two', 'two'],
        ...                    "bar": ['A', 'A', 'B', 'C'],
        ...                    "baz": [1, 2, 3, 4]})
        >>> df
           foo bar  baz
        0  one   A    1
        1  one   A    2
        2  two   B    3
        3  two   C    4
        
        Notice that the first two rows are the same for our `index`
        and `columns` arguments.
        
        >>> df.pivot(index='foo', columns='bar', values='baz')
        Traceback (most recent call last):
           ...
        ValueError: Index contains duplicate entries, cannot reshape
    
    

----
#### Note:
***Common Point of Confusion: Students often just randomly pass in index,column, and value choices in an attempt to see the changes. This often just leads to formatting errors. You should first go through this checklist BEFORE running a pivot():***

* What question are you trying to answer?
* What would a dataframe that answers the question look like? Does it need a pivot()
* What you want the resulting pivot to look like? Do you need all the original columns?

-----


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
      <th>Account Number</th>
      <th>Company</th>
      <th>Contact</th>
      <th>Account Manager</th>
      <th>Product</th>
      <th>Licenses</th>
      <th>Sale Price</th>
      <th>Status</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>2123398</td>
      <td>Google</td>
      <td>Larry Pager</td>
      <td>Edward Thorp</td>
      <td>Analytics</td>
      <td>150</td>
      <td>2100000</td>
      <td>Presented</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2123398</td>
      <td>Google</td>
      <td>Larry Pager</td>
      <td>Edward Thorp</td>
      <td>Prediction</td>
      <td>150</td>
      <td>700000</td>
      <td>Presented</td>
    </tr>
    <tr>
      <th>2</th>
      <td>2123398</td>
      <td>Google</td>
      <td>Larry Pager</td>
      <td>Edward Thorp</td>
      <td>Tracking</td>
      <td>300</td>
      <td>350000</td>
      <td>Under Review</td>
    </tr>
    <tr>
      <th>3</th>
      <td>2192650</td>
      <td>BOBO</td>
      <td>Larry Pager</td>
      <td>Edward Thorp</td>
      <td>Analytics</td>
      <td>150</td>
      <td>2450000</td>
      <td>Lost</td>
    </tr>
    <tr>
      <th>4</th>
      <td>420496</td>
      <td>IKEA</td>
      <td>Elon Tusk</td>
      <td>Edward Thorp</td>
      <td>Analytics</td>
      <td>300</td>
      <td>4550000</td>
      <td>Won</td>
    </tr>
    <tr>
      <th>5</th>
      <td>636685</td>
      <td>Tesla Inc.</td>
      <td>Elon Tusk</td>
      <td>Edward Thorp</td>
      <td>Analytics</td>
      <td>300</td>
      <td>2800000</td>
      <td>Under Review</td>
    </tr>
    <tr>
      <th>6</th>
      <td>636685</td>
      <td>Tesla Inc.</td>
      <td>Elon Tusk</td>
      <td>Edward Thorp</td>
      <td>Prediction</td>
      <td>150</td>
      <td>700000</td>
      <td>Presented</td>
    </tr>
    <tr>
      <th>7</th>
      <td>1216870</td>
      <td>Microsoft</td>
      <td>Will Grates</td>
      <td>Edward Thorp</td>
      <td>Tracking</td>
      <td>300</td>
      <td>350000</td>
      <td>Under Review</td>
    </tr>
    <tr>
      <th>8</th>
      <td>2200450</td>
      <td>Walmart</td>
      <td>Will Grates</td>
      <td>Edward Thorp</td>
      <td>Analytics</td>
      <td>150</td>
      <td>2450000</td>
      <td>Lost</td>
    </tr>
    <tr>
      <th>9</th>
      <td>405886</td>
      <td>Apple</td>
      <td>Cindy Phoner</td>
      <td>Claude Shannon</td>
      <td>Analytics</td>
      <td>300</td>
      <td>4550000</td>
      <td>Won</td>
    </tr>
    <tr>
      <th>10</th>
      <td>470248</td>
      <td>Exxon Mobile</td>
      <td>Cindy Phoner</td>
      <td>Claude Shannon</td>
      <td>Analytics</td>
      <td>150</td>
      <td>2100000</td>
      <td>Presented</td>
    </tr>
    <tr>
      <th>11</th>
      <td>698032</td>
      <td>ATT</td>
      <td>Cindy Phoner</td>
      <td>Claude Shannon</td>
      <td>Tracking</td>
      <td>150</td>
      <td>350000</td>
      <td>Under Review</td>
    </tr>
    <tr>
      <th>12</th>
      <td>698032</td>
      <td>ATT</td>
      <td>Cindy Phoner</td>
      <td>Claude Shannon</td>
      <td>Prediction</td>
      <td>150</td>
      <td>700000</td>
      <td>Presented</td>
    </tr>
    <tr>
      <th>13</th>
      <td>902797</td>
      <td>CVS Health</td>
      <td>Emma Gordian</td>
      <td>Claude Shannon</td>
      <td>Tracking</td>
      <td>450</td>
      <td>490000</td>
      <td>Won</td>
    </tr>
    <tr>
      <th>14</th>
      <td>2046943</td>
      <td>Salesforce</td>
      <td>Emma Gordian</td>
      <td>Claude Shannon</td>
      <td>Analytics</td>
      <td>750</td>
      <td>7000000</td>
      <td>Won</td>
    </tr>
    <tr>
      <th>15</th>
      <td>2169499</td>
      <td>Cisco</td>
      <td>Emma Gordian</td>
      <td>Claude Shannon</td>
      <td>Analytics</td>
      <td>300</td>
      <td>4550000</td>
      <td>Lost</td>
    </tr>
    <tr>
      <th>16</th>
      <td>2169499</td>
      <td>Cisco</td>
      <td>Emma Gordian</td>
      <td>Claude Shannon</td>
      <td>GPS Positioning</td>
      <td>300</td>
      <td>350000</td>
      <td>Presented</td>
    </tr>
  </tbody>
</table>
</div>



--------
** What type of question does a pivot help answer?**

**Imagine we wanted to know, how many licenses of each product type did Google purchase? Currently the way the data is formatted is hard to read. Let's pivot it so this is clearer, we will take a subset of the data for the question at hand.**


```python
# Let's take a subset, otherwise we'll get an error due to duplicate rows and data
licenses = df[['Company','Product','Licenses']]
licenses
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
      <th>Company</th>
      <th>Product</th>
      <th>Licenses</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Google</td>
      <td>Analytics</td>
      <td>150</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Google</td>
      <td>Prediction</td>
      <td>150</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Google</td>
      <td>Tracking</td>
      <td>300</td>
    </tr>
    <tr>
      <th>3</th>
      <td>BOBO</td>
      <td>Analytics</td>
      <td>150</td>
    </tr>
    <tr>
      <th>4</th>
      <td>IKEA</td>
      <td>Analytics</td>
      <td>300</td>
    </tr>
    <tr>
      <th>5</th>
      <td>Tesla Inc.</td>
      <td>Analytics</td>
      <td>300</td>
    </tr>
    <tr>
      <th>6</th>
      <td>Tesla Inc.</td>
      <td>Prediction</td>
      <td>150</td>
    </tr>
    <tr>
      <th>7</th>
      <td>Microsoft</td>
      <td>Tracking</td>
      <td>300</td>
    </tr>
    <tr>
      <th>8</th>
      <td>Walmart</td>
      <td>Analytics</td>
      <td>150</td>
    </tr>
    <tr>
      <th>9</th>
      <td>Apple</td>
      <td>Analytics</td>
      <td>300</td>
    </tr>
    <tr>
      <th>10</th>
      <td>Exxon Mobile</td>
      <td>Analytics</td>
      <td>150</td>
    </tr>
    <tr>
      <th>11</th>
      <td>ATT</td>
      <td>Tracking</td>
      <td>150</td>
    </tr>
    <tr>
      <th>12</th>
      <td>ATT</td>
      <td>Prediction</td>
      <td>150</td>
    </tr>
    <tr>
      <th>13</th>
      <td>CVS Health</td>
      <td>Tracking</td>
      <td>450</td>
    </tr>
    <tr>
      <th>14</th>
      <td>Salesforce</td>
      <td>Analytics</td>
      <td>750</td>
    </tr>
    <tr>
      <th>15</th>
      <td>Cisco</td>
      <td>Analytics</td>
      <td>300</td>
    </tr>
    <tr>
      <th>16</th>
      <td>Cisco</td>
      <td>GPS Positioning</td>
      <td>300</td>
    </tr>
  </tbody>
</table>
</div>




```python
pd.pivot(data=licenses,index='Company',columns='Product',values='Licenses')
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
      <th>Product</th>
      <th>Analytics</th>
      <th>GPS Positioning</th>
      <th>Prediction</th>
      <th>Tracking</th>
    </tr>
    <tr>
      <th>Company</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Google</th>
      <td>150.0</td>
      <td>NaN</td>
      <td>150.0</td>
      <td>300.0</td>
    </tr>
    <tr>
      <th>ATT</th>
      <td>NaN</td>
      <td>NaN</td>
      <td>150.0</td>
      <td>150.0</td>
    </tr>
    <tr>
      <th>Apple</th>
      <td>300.0</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>BOBO</th>
      <td>150.0</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>CVS Health</th>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>450.0</td>
    </tr>
    <tr>
      <th>Cisco</th>
      <td>300.0</td>
      <td>300.0</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>Exxon Mobile</th>
      <td>150.0</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>IKEA</th>
      <td>300.0</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>Microsoft</th>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>300.0</td>
    </tr>
    <tr>
      <th>Salesforce</th>
      <td>750.0</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>Tesla Inc.</th>
      <td>300.0</td>
      <td>NaN</td>
      <td>150.0</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>Walmart</th>
      <td>150.0</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
  </tbody>
</table>
</div>



## The pivot_table() method

Similar to the pivot() method, the pivot_table() can add aggregation functions to a pivot call.


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
      <th>Account Number</th>
      <th>Company</th>
      <th>Contact</th>
      <th>Account Manager</th>
      <th>Product</th>
      <th>Licenses</th>
      <th>Sale Price</th>
      <th>Status</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>2123398</td>
      <td>Google</td>
      <td>Larry Pager</td>
      <td>Edward Thorp</td>
      <td>Analytics</td>
      <td>150</td>
      <td>2100000</td>
      <td>Presented</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2123398</td>
      <td>Google</td>
      <td>Larry Pager</td>
      <td>Edward Thorp</td>
      <td>Prediction</td>
      <td>150</td>
      <td>700000</td>
      <td>Presented</td>
    </tr>
    <tr>
      <th>2</th>
      <td>2123398</td>
      <td>Google</td>
      <td>Larry Pager</td>
      <td>Edward Thorp</td>
      <td>Tracking</td>
      <td>300</td>
      <td>350000</td>
      <td>Under Review</td>
    </tr>
    <tr>
      <th>3</th>
      <td>2192650</td>
      <td>BOBO</td>
      <td>Larry Pager</td>
      <td>Edward Thorp</td>
      <td>Analytics</td>
      <td>150</td>
      <td>2450000</td>
      <td>Lost</td>
    </tr>
    <tr>
      <th>4</th>
      <td>420496</td>
      <td>IKEA</td>
      <td>Elon Tusk</td>
      <td>Edward Thorp</td>
      <td>Analytics</td>
      <td>300</td>
      <td>4550000</td>
      <td>Won</td>
    </tr>
    <tr>
      <th>5</th>
      <td>636685</td>
      <td>Tesla Inc.</td>
      <td>Elon Tusk</td>
      <td>Edward Thorp</td>
      <td>Analytics</td>
      <td>300</td>
      <td>2800000</td>
      <td>Under Review</td>
    </tr>
    <tr>
      <th>6</th>
      <td>636685</td>
      <td>Tesla Inc.</td>
      <td>Elon Tusk</td>
      <td>Edward Thorp</td>
      <td>Prediction</td>
      <td>150</td>
      <td>700000</td>
      <td>Presented</td>
    </tr>
    <tr>
      <th>7</th>
      <td>1216870</td>
      <td>Microsoft</td>
      <td>Will Grates</td>
      <td>Edward Thorp</td>
      <td>Tracking</td>
      <td>300</td>
      <td>350000</td>
      <td>Under Review</td>
    </tr>
    <tr>
      <th>8</th>
      <td>2200450</td>
      <td>Walmart</td>
      <td>Will Grates</td>
      <td>Edward Thorp</td>
      <td>Analytics</td>
      <td>150</td>
      <td>2450000</td>
      <td>Lost</td>
    </tr>
    <tr>
      <th>9</th>
      <td>405886</td>
      <td>Apple</td>
      <td>Cindy Phoner</td>
      <td>Claude Shannon</td>
      <td>Analytics</td>
      <td>300</td>
      <td>4550000</td>
      <td>Won</td>
    </tr>
    <tr>
      <th>10</th>
      <td>470248</td>
      <td>Exxon Mobile</td>
      <td>Cindy Phoner</td>
      <td>Claude Shannon</td>
      <td>Analytics</td>
      <td>150</td>
      <td>2100000</td>
      <td>Presented</td>
    </tr>
    <tr>
      <th>11</th>
      <td>698032</td>
      <td>ATT</td>
      <td>Cindy Phoner</td>
      <td>Claude Shannon</td>
      <td>Tracking</td>
      <td>150</td>
      <td>350000</td>
      <td>Under Review</td>
    </tr>
    <tr>
      <th>12</th>
      <td>698032</td>
      <td>ATT</td>
      <td>Cindy Phoner</td>
      <td>Claude Shannon</td>
      <td>Prediction</td>
      <td>150</td>
      <td>700000</td>
      <td>Presented</td>
    </tr>
    <tr>
      <th>13</th>
      <td>902797</td>
      <td>CVS Health</td>
      <td>Emma Gordian</td>
      <td>Claude Shannon</td>
      <td>Tracking</td>
      <td>450</td>
      <td>490000</td>
      <td>Won</td>
    </tr>
    <tr>
      <th>14</th>
      <td>2046943</td>
      <td>Salesforce</td>
      <td>Emma Gordian</td>
      <td>Claude Shannon</td>
      <td>Analytics</td>
      <td>750</td>
      <td>7000000</td>
      <td>Won</td>
    </tr>
    <tr>
      <th>15</th>
      <td>2169499</td>
      <td>Cisco</td>
      <td>Emma Gordian</td>
      <td>Claude Shannon</td>
      <td>Analytics</td>
      <td>300</td>
      <td>4550000</td>
      <td>Lost</td>
    </tr>
    <tr>
      <th>16</th>
      <td>2169499</td>
      <td>Cisco</td>
      <td>Emma Gordian</td>
      <td>Claude Shannon</td>
      <td>GPS Positioning</td>
      <td>300</td>
      <td>350000</td>
      <td>Presented</td>
    </tr>
  </tbody>
</table>
</div>




```python
# Notice Account Number sum() doesn't make sense to keep/use
pd.pivot_table(df,index="Company",aggfunc='sum')
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
      <th>Account Number</th>
      <th>Licenses</th>
      <th>Sale Price</th>
    </tr>
    <tr>
      <th>Company</th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Google</th>
      <td>6370194</td>
      <td>600</td>
      <td>3150000</td>
    </tr>
    <tr>
      <th>ATT</th>
      <td>1396064</td>
      <td>300</td>
      <td>1050000</td>
    </tr>
    <tr>
      <th>Apple</th>
      <td>405886</td>
      <td>300</td>
      <td>4550000</td>
    </tr>
    <tr>
      <th>BOBO</th>
      <td>2192650</td>
      <td>150</td>
      <td>2450000</td>
    </tr>
    <tr>
      <th>CVS Health</th>
      <td>902797</td>
      <td>450</td>
      <td>490000</td>
    </tr>
    <tr>
      <th>Cisco</th>
      <td>4338998</td>
      <td>600</td>
      <td>4900000</td>
    </tr>
    <tr>
      <th>Exxon Mobile</th>
      <td>470248</td>
      <td>150</td>
      <td>2100000</td>
    </tr>
    <tr>
      <th>IKEA</th>
      <td>420496</td>
      <td>300</td>
      <td>4550000</td>
    </tr>
    <tr>
      <th>Microsoft</th>
      <td>1216870</td>
      <td>300</td>
      <td>350000</td>
    </tr>
    <tr>
      <th>Salesforce</th>
      <td>2046943</td>
      <td>750</td>
      <td>7000000</td>
    </tr>
    <tr>
      <th>Tesla Inc.</th>
      <td>1273370</td>
      <td>450</td>
      <td>3500000</td>
    </tr>
    <tr>
      <th>Walmart</th>
      <td>2200450</td>
      <td>150</td>
      <td>2450000</td>
    </tr>
  </tbody>
</table>
</div>




```python
# Either grab the columns
pd.pivot_table(df,index="Company",aggfunc='sum')[['Licenses','Sale Price']]
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
      <th>Licenses</th>
      <th>Sale Price</th>
    </tr>
    <tr>
      <th>Company</th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Google</th>
      <td>600</td>
      <td>3150000</td>
    </tr>
    <tr>
      <th>ATT</th>
      <td>300</td>
      <td>1050000</td>
    </tr>
    <tr>
      <th>Apple</th>
      <td>300</td>
      <td>4550000</td>
    </tr>
    <tr>
      <th>BOBO</th>
      <td>150</td>
      <td>2450000</td>
    </tr>
    <tr>
      <th>CVS Health</th>
      <td>450</td>
      <td>490000</td>
    </tr>
    <tr>
      <th>Cisco</th>
      <td>600</td>
      <td>4900000</td>
    </tr>
    <tr>
      <th>Exxon Mobile</th>
      <td>150</td>
      <td>2100000</td>
    </tr>
    <tr>
      <th>IKEA</th>
      <td>300</td>
      <td>4550000</td>
    </tr>
    <tr>
      <th>Microsoft</th>
      <td>300</td>
      <td>350000</td>
    </tr>
    <tr>
      <th>Salesforce</th>
      <td>750</td>
      <td>7000000</td>
    </tr>
    <tr>
      <th>Tesla Inc.</th>
      <td>450</td>
      <td>3500000</td>
    </tr>
    <tr>
      <th>Walmart</th>
      <td>150</td>
      <td>2450000</td>
    </tr>
  </tbody>
</table>
</div>




```python
# Or state them as wanted values
pd.pivot_table(df,index="Company",aggfunc='sum',values=['Licenses','Sale Price'])
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
      <th>Licenses</th>
      <th>Sale Price</th>
    </tr>
    <tr>
      <th>Company</th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Google</th>
      <td>600</td>
      <td>3150000</td>
    </tr>
    <tr>
      <th>ATT</th>
      <td>300</td>
      <td>1050000</td>
    </tr>
    <tr>
      <th>Apple</th>
      <td>300</td>
      <td>4550000</td>
    </tr>
    <tr>
      <th>BOBO</th>
      <td>150</td>
      <td>2450000</td>
    </tr>
    <tr>
      <th>CVS Health</th>
      <td>450</td>
      <td>490000</td>
    </tr>
    <tr>
      <th>Cisco</th>
      <td>600</td>
      <td>4900000</td>
    </tr>
    <tr>
      <th>Exxon Mobile</th>
      <td>150</td>
      <td>2100000</td>
    </tr>
    <tr>
      <th>IKEA</th>
      <td>300</td>
      <td>4550000</td>
    </tr>
    <tr>
      <th>Microsoft</th>
      <td>300</td>
      <td>350000</td>
    </tr>
    <tr>
      <th>Salesforce</th>
      <td>750</td>
      <td>7000000</td>
    </tr>
    <tr>
      <th>Tesla Inc.</th>
      <td>450</td>
      <td>3500000</td>
    </tr>
    <tr>
      <th>Walmart</th>
      <td>150</td>
      <td>2450000</td>
    </tr>
  </tbody>
</table>
</div>




```python
df.groupby('Company').sum()[['Licenses','Sale Price']]
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
      <th>Licenses</th>
      <th>Sale Price</th>
    </tr>
    <tr>
      <th>Company</th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Google</th>
      <td>600</td>
      <td>3150000</td>
    </tr>
    <tr>
      <th>ATT</th>
      <td>300</td>
      <td>1050000</td>
    </tr>
    <tr>
      <th>Apple</th>
      <td>300</td>
      <td>4550000</td>
    </tr>
    <tr>
      <th>BOBO</th>
      <td>150</td>
      <td>2450000</td>
    </tr>
    <tr>
      <th>CVS Health</th>
      <td>450</td>
      <td>490000</td>
    </tr>
    <tr>
      <th>Cisco</th>
      <td>600</td>
      <td>4900000</td>
    </tr>
    <tr>
      <th>Exxon Mobile</th>
      <td>150</td>
      <td>2100000</td>
    </tr>
    <tr>
      <th>IKEA</th>
      <td>300</td>
      <td>4550000</td>
    </tr>
    <tr>
      <th>Microsoft</th>
      <td>300</td>
      <td>350000</td>
    </tr>
    <tr>
      <th>Salesforce</th>
      <td>750</td>
      <td>7000000</td>
    </tr>
    <tr>
      <th>Tesla Inc.</th>
      <td>450</td>
      <td>3500000</td>
    </tr>
    <tr>
      <th>Walmart</th>
      <td>150</td>
      <td>2450000</td>
    </tr>
  </tbody>
</table>
</div>




```python
pd.pivot_table(df,index=["Account Manager","Contact"],values=['Sale Price'],aggfunc='sum')
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
      <th></th>
      <th>Sale Price</th>
    </tr>
    <tr>
      <th>Account Manager</th>
      <th>Contact</th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th rowspan="2" valign="top">Claude Shannon</th>
      <th>Cindy Phoner</th>
      <td>7700000</td>
    </tr>
    <tr>
      <th>Emma Gordian</th>
      <td>12390000</td>
    </tr>
    <tr>
      <th rowspan="3" valign="top">Edward Thorp</th>
      <th>Elon Tusk</th>
      <td>8050000</td>
    </tr>
    <tr>
      <th>Larry Pager</th>
      <td>5600000</td>
    </tr>
    <tr>
      <th>Will Grates</th>
      <td>2800000</td>
    </tr>
  </tbody>
</table>
</div>



Columns are optional - they provide an additional way to segment the actual values you care about. The aggregation functions are applied to the values you list.


```python
pd.pivot_table(df,index=["Account Manager","Contact"],values=["Sale Price"],columns=["Product"],aggfunc=[np.sum])
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead tr th {
        text-align: left;
    }

    .dataframe thead tr:last-of-type th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr>
      <th></th>
      <th></th>
      <th colspan="4" halign="left">sum</th>
    </tr>
    <tr>
      <th></th>
      <th></th>
      <th colspan="4" halign="left">Sale Price</th>
    </tr>
    <tr>
      <th></th>
      <th>Product</th>
      <th>Analytics</th>
      <th>GPS Positioning</th>
      <th>Prediction</th>
      <th>Tracking</th>
    </tr>
    <tr>
      <th>Account Manager</th>
      <th>Contact</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th rowspan="2" valign="top">Claude Shannon</th>
      <th>Cindy Phoner</th>
      <td>6650000.0</td>
      <td>NaN</td>
      <td>700000.0</td>
      <td>350000.0</td>
    </tr>
    <tr>
      <th>Emma Gordian</th>
      <td>11550000.0</td>
      <td>350000.0</td>
      <td>NaN</td>
      <td>490000.0</td>
    </tr>
    <tr>
      <th rowspan="3" valign="top">Edward Thorp</th>
      <th>Elon Tusk</th>
      <td>7350000.0</td>
      <td>NaN</td>
      <td>700000.0</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>Larry Pager</th>
      <td>4550000.0</td>
      <td>NaN</td>
      <td>700000.0</td>
      <td>350000.0</td>
    </tr>
    <tr>
      <th>Will Grates</th>
      <td>2450000.0</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>350000.0</td>
    </tr>
  </tbody>
</table>
</div>




```python
pd.pivot_table(df,index=["Account Manager","Contact"],values=["Sale Price"],columns=["Product"],aggfunc=[np.sum],fill_value=0)
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead tr th {
        text-align: left;
    }

    .dataframe thead tr:last-of-type th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr>
      <th></th>
      <th></th>
      <th colspan="4" halign="left">sum</th>
    </tr>
    <tr>
      <th></th>
      <th></th>
      <th colspan="4" halign="left">Sale Price</th>
    </tr>
    <tr>
      <th></th>
      <th>Product</th>
      <th>Analytics</th>
      <th>GPS Positioning</th>
      <th>Prediction</th>
      <th>Tracking</th>
    </tr>
    <tr>
      <th>Account Manager</th>
      <th>Contact</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th rowspan="2" valign="top">Claude Shannon</th>
      <th>Cindy Phoner</th>
      <td>6650000</td>
      <td>0</td>
      <td>700000</td>
      <td>350000</td>
    </tr>
    <tr>
      <th>Emma Gordian</th>
      <td>11550000</td>
      <td>350000</td>
      <td>0</td>
      <td>490000</td>
    </tr>
    <tr>
      <th rowspan="3" valign="top">Edward Thorp</th>
      <th>Elon Tusk</th>
      <td>7350000</td>
      <td>0</td>
      <td>700000</td>
      <td>0</td>
    </tr>
    <tr>
      <th>Larry Pager</th>
      <td>4550000</td>
      <td>0</td>
      <td>700000</td>
      <td>350000</td>
    </tr>
    <tr>
      <th>Will Grates</th>
      <td>2450000</td>
      <td>0</td>
      <td>0</td>
      <td>350000</td>
    </tr>
  </tbody>
</table>
</div>




```python
# Can add multiple agg functions
pd.pivot_table(df,index=["Account Manager","Contact"],values=["Sale Price"],columns=["Product"],
               aggfunc=[np.sum,np.mean],fill_value=0)
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead tr th {
        text-align: left;
    }

    .dataframe thead tr:last-of-type th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr>
      <th></th>
      <th></th>
      <th colspan="4" halign="left">sum</th>
      <th colspan="4" halign="left">mean</th>
    </tr>
    <tr>
      <th></th>
      <th></th>
      <th colspan="4" halign="left">Sale Price</th>
      <th colspan="4" halign="left">Sale Price</th>
    </tr>
    <tr>
      <th></th>
      <th>Product</th>
      <th>Analytics</th>
      <th>GPS Positioning</th>
      <th>Prediction</th>
      <th>Tracking</th>
      <th>Analytics</th>
      <th>GPS Positioning</th>
      <th>Prediction</th>
      <th>Tracking</th>
    </tr>
    <tr>
      <th>Account Manager</th>
      <th>Contact</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th rowspan="2" valign="top">Claude Shannon</th>
      <th>Cindy Phoner</th>
      <td>6650000</td>
      <td>0</td>
      <td>700000</td>
      <td>350000</td>
      <td>3325000</td>
      <td>0</td>
      <td>700000</td>
      <td>350000</td>
    </tr>
    <tr>
      <th>Emma Gordian</th>
      <td>11550000</td>
      <td>350000</td>
      <td>0</td>
      <td>490000</td>
      <td>5775000</td>
      <td>350000</td>
      <td>0</td>
      <td>490000</td>
    </tr>
    <tr>
      <th rowspan="3" valign="top">Edward Thorp</th>
      <th>Elon Tusk</th>
      <td>7350000</td>
      <td>0</td>
      <td>700000</td>
      <td>0</td>
      <td>3675000</td>
      <td>0</td>
      <td>700000</td>
      <td>0</td>
    </tr>
    <tr>
      <th>Larry Pager</th>
      <td>4550000</td>
      <td>0</td>
      <td>700000</td>
      <td>350000</td>
      <td>2275000</td>
      <td>0</td>
      <td>700000</td>
      <td>350000</td>
    </tr>
    <tr>
      <th>Will Grates</th>
      <td>2450000</td>
      <td>0</td>
      <td>0</td>
      <td>350000</td>
      <td>2450000</td>
      <td>0</td>
      <td>0</td>
      <td>350000</td>
    </tr>
  </tbody>
</table>
</div>




```python
# Can add on multiple columns
pd.pivot_table(df,index=["Account Manager","Contact"],values=["Sale Price","Licenses"],columns=["Product"],
               aggfunc=[np.sum],fill_value=0)
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead tr th {
        text-align: left;
    }

    .dataframe thead tr:last-of-type th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr>
      <th></th>
      <th></th>
      <th colspan="8" halign="left">sum</th>
    </tr>
    <tr>
      <th></th>
      <th></th>
      <th colspan="4" halign="left">Licenses</th>
      <th colspan="4" halign="left">Sale Price</th>
    </tr>
    <tr>
      <th></th>
      <th>Product</th>
      <th>Analytics</th>
      <th>GPS Positioning</th>
      <th>Prediction</th>
      <th>Tracking</th>
      <th>Analytics</th>
      <th>GPS Positioning</th>
      <th>Prediction</th>
      <th>Tracking</th>
    </tr>
    <tr>
      <th>Account Manager</th>
      <th>Contact</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th rowspan="2" valign="top">Claude Shannon</th>
      <th>Cindy Phoner</th>
      <td>450</td>
      <td>0</td>
      <td>150</td>
      <td>150</td>
      <td>6650000</td>
      <td>0</td>
      <td>700000</td>
      <td>350000</td>
    </tr>
    <tr>
      <th>Emma Gordian</th>
      <td>1050</td>
      <td>300</td>
      <td>0</td>
      <td>450</td>
      <td>11550000</td>
      <td>350000</td>
      <td>0</td>
      <td>490000</td>
    </tr>
    <tr>
      <th rowspan="3" valign="top">Edward Thorp</th>
      <th>Elon Tusk</th>
      <td>600</td>
      <td>0</td>
      <td>150</td>
      <td>0</td>
      <td>7350000</td>
      <td>0</td>
      <td>700000</td>
      <td>0</td>
    </tr>
    <tr>
      <th>Larry Pager</th>
      <td>300</td>
      <td>0</td>
      <td>150</td>
      <td>300</td>
      <td>4550000</td>
      <td>0</td>
      <td>700000</td>
      <td>350000</td>
    </tr>
    <tr>
      <th>Will Grates</th>
      <td>150</td>
      <td>0</td>
      <td>0</td>
      <td>300</td>
      <td>2450000</td>
      <td>0</td>
      <td>0</td>
      <td>350000</td>
    </tr>
  </tbody>
</table>
</div>




```python
# Can add on multiple columns
pd.pivot_table(df,index=["Account Manager","Contact","Product"],values=["Sale Price","Licenses"],
               aggfunc=[np.sum],fill_value=0)
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead tr th {
        text-align: left;
    }

    .dataframe thead tr:last-of-type th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr>
      <th></th>
      <th></th>
      <th></th>
      <th colspan="2" halign="left">sum</th>
    </tr>
    <tr>
      <th></th>
      <th></th>
      <th></th>
      <th>Licenses</th>
      <th>Sale Price</th>
    </tr>
    <tr>
      <th>Account Manager</th>
      <th>Contact</th>
      <th>Product</th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th rowspan="6" valign="top">Claude Shannon</th>
      <th rowspan="3" valign="top">Cindy Phoner</th>
      <th>Analytics</th>
      <td>450</td>
      <td>6650000</td>
    </tr>
    <tr>
      <th>Prediction</th>
      <td>150</td>
      <td>700000</td>
    </tr>
    <tr>
      <th>Tracking</th>
      <td>150</td>
      <td>350000</td>
    </tr>
    <tr>
      <th rowspan="3" valign="top">Emma Gordian</th>
      <th>Analytics</th>
      <td>1050</td>
      <td>11550000</td>
    </tr>
    <tr>
      <th>GPS Positioning</th>
      <td>300</td>
      <td>350000</td>
    </tr>
    <tr>
      <th>Tracking</th>
      <td>450</td>
      <td>490000</td>
    </tr>
    <tr>
      <th rowspan="7" valign="top">Edward Thorp</th>
      <th rowspan="2" valign="top">Elon Tusk</th>
      <th>Analytics</th>
      <td>600</td>
      <td>7350000</td>
    </tr>
    <tr>
      <th>Prediction</th>
      <td>150</td>
      <td>700000</td>
    </tr>
    <tr>
      <th rowspan="3" valign="top">Larry Pager</th>
      <th>Analytics</th>
      <td>300</td>
      <td>4550000</td>
    </tr>
    <tr>
      <th>Prediction</th>
      <td>150</td>
      <td>700000</td>
    </tr>
    <tr>
      <th>Tracking</th>
      <td>300</td>
      <td>350000</td>
    </tr>
    <tr>
      <th rowspan="2" valign="top">Will Grates</th>
      <th>Analytics</th>
      <td>150</td>
      <td>2450000</td>
    </tr>
    <tr>
      <th>Tracking</th>
      <td>300</td>
      <td>350000</td>
    </tr>
  </tbody>
</table>
</div>




```python
# get Final "ALL" with margins = True
# Can add on multiple columns
pd.pivot_table(df,index=["Account Manager","Contact","Product"],values=["Sale Price","Licenses"],
               aggfunc=[np.sum],fill_value=0,margins=True)
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead tr th {
        text-align: left;
    }

    .dataframe thead tr:last-of-type th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr>
      <th></th>
      <th></th>
      <th></th>
      <th colspan="2" halign="left">sum</th>
    </tr>
    <tr>
      <th></th>
      <th></th>
      <th></th>
      <th>Licenses</th>
      <th>Sale Price</th>
    </tr>
    <tr>
      <th>Account Manager</th>
      <th>Contact</th>
      <th>Product</th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th rowspan="6" valign="top">Claude Shannon</th>
      <th rowspan="3" valign="top">Cindy Phoner</th>
      <th>Analytics</th>
      <td>450</td>
      <td>6650000</td>
    </tr>
    <tr>
      <th>Prediction</th>
      <td>150</td>
      <td>700000</td>
    </tr>
    <tr>
      <th>Tracking</th>
      <td>150</td>
      <td>350000</td>
    </tr>
    <tr>
      <th rowspan="3" valign="top">Emma Gordian</th>
      <th>Analytics</th>
      <td>1050</td>
      <td>11550000</td>
    </tr>
    <tr>
      <th>GPS Positioning</th>
      <td>300</td>
      <td>350000</td>
    </tr>
    <tr>
      <th>Tracking</th>
      <td>450</td>
      <td>490000</td>
    </tr>
    <tr>
      <th rowspan="7" valign="top">Edward Thorp</th>
      <th rowspan="2" valign="top">Elon Tusk</th>
      <th>Analytics</th>
      <td>600</td>
      <td>7350000</td>
    </tr>
    <tr>
      <th>Prediction</th>
      <td>150</td>
      <td>700000</td>
    </tr>
    <tr>
      <th rowspan="3" valign="top">Larry Pager</th>
      <th>Analytics</th>
      <td>300</td>
      <td>4550000</td>
    </tr>
    <tr>
      <th>Prediction</th>
      <td>150</td>
      <td>700000</td>
    </tr>
    <tr>
      <th>Tracking</th>
      <td>300</td>
      <td>350000</td>
    </tr>
    <tr>
      <th rowspan="2" valign="top">Will Grates</th>
      <th>Analytics</th>
      <td>150</td>
      <td>2450000</td>
    </tr>
    <tr>
      <th>Tracking</th>
      <td>300</td>
      <td>350000</td>
    </tr>
    <tr>
      <th>All</th>
      <th></th>
      <th></th>
      <td>4500</td>
      <td>36540000</td>
    </tr>
  </tbody>
</table>
</div>




```python
pd.pivot_table(df,index=["Account Manager","Status"],values=["Sale Price"],
               aggfunc=[np.sum],fill_value=0,margins=True)
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead tr th {
        text-align: left;
    }

    .dataframe thead tr:last-of-type th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr>
      <th></th>
      <th></th>
      <th>sum</th>
    </tr>
    <tr>
      <th></th>
      <th></th>
      <th>Sale Price</th>
    </tr>
    <tr>
      <th>Account Manager</th>
      <th>Status</th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th rowspan="4" valign="top">Claude Shannon</th>
      <th>Lost</th>
      <td>4550000</td>
    </tr>
    <tr>
      <th>Presented</th>
      <td>3150000</td>
    </tr>
    <tr>
      <th>Under Review</th>
      <td>350000</td>
    </tr>
    <tr>
      <th>Won</th>
      <td>12040000</td>
    </tr>
    <tr>
      <th rowspan="4" valign="top">Edward Thorp</th>
      <th>Lost</th>
      <td>4900000</td>
    </tr>
    <tr>
      <th>Presented</th>
      <td>3500000</td>
    </tr>
    <tr>
      <th>Under Review</th>
      <td>3500000</td>
    </tr>
    <tr>
      <th>Won</th>
      <td>4550000</td>
    </tr>
    <tr>
      <th>All</th>
      <th></th>
      <td>36540000</td>
    </tr>
  </tbody>
</table>
</div>



----
