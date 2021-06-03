<h1>Table of Contents<span class="tocSkip"></span></h1>
<div class="toc"><ul class="toc-item"><li><span><a href="#Series" data-toc-modified-id="Series-1"><span class="toc-item-num">1&nbsp;&nbsp;</span>Series</a></span><ul class="toc-item"><li><span><a href="#Imports" data-toc-modified-id="Imports-1.1"><span class="toc-item-num">1.1&nbsp;&nbsp;</span>Imports</a></span></li><li><span><a href="#Creating-a-Series-from-Python-Objects" data-toc-modified-id="Creating-a-Series-from-Python-Objects-1.2"><span class="toc-item-num">1.2&nbsp;&nbsp;</span>Creating a Series from Python Objects</a></span><ul class="toc-item"><li><span><a href="#Index-and-Data-Lists" data-toc-modified-id="Index-and-Data-Lists-1.2.1"><span class="toc-item-num">1.2.1&nbsp;&nbsp;</span>Index and Data Lists</a></span></li><li><span><a href="#From-a--Dictionary" data-toc-modified-id="From-a--Dictionary-1.2.2"><span class="toc-item-num">1.2.2&nbsp;&nbsp;</span>From a  Dictionary</a></span></li></ul></li></ul></li><li><span><a href="#Key-Ideas-of-a-Series" data-toc-modified-id="Key-Ideas-of-a-Series-2"><span class="toc-item-num">2&nbsp;&nbsp;</span>Key Ideas of a Series</a></span><ul class="toc-item"><li><span><a href="#Named-Index" data-toc-modified-id="Named-Index-2.1"><span class="toc-item-num">2.1&nbsp;&nbsp;</span>Named Index</a></span></li><li><span><a href="#Operations" data-toc-modified-id="Operations-2.2"><span class="toc-item-num">2.2&nbsp;&nbsp;</span>Operations</a></span></li><li><span><a href="#Between-Series" data-toc-modified-id="Between-Series-2.3"><span class="toc-item-num">2.3&nbsp;&nbsp;</span>Between Series</a></span></li></ul></li></ul></div>

# Series

The first main data type we will learn about for pandas is the Series data type. Let's import Pandas and explore the Series object.

A Series is very similar to a NumPy array (in fact it is built on top of the NumPy array object). What differentiates the NumPy array from a Series, is that a Series can have axis labels, meaning it can be indexed by a label, instead of just a number location. It also doesn't need to hold numeric data, it can hold any arbitrary Python Object.

Let's explore this concept through some examples:

## Imports


```python
import numpy as np
import pandas as pd
```

## Creating a Series from Python Objects


```python
#help(pd.Series)
```

### Index and Data Lists

We can create a Series from Python lists (also from NumPy arrays)


```python
myindex = ['USA','Canada','Mexico']
```


```python
mydata = [1776,1867,1821]
```


```python
myser = pd.Series(data=mydata)
```


```python
myser
```




    0    1776
    1    1867
    2    1821
    dtype: int64




```python
pd.Series(data=mydata,index=myindex)
```




    USA       1776
    Canada    1867
    Mexico    1821
    dtype: int64




```python
ran_data = np.random.randint(0,100,4)
```


```python
ran_data
```




    array([39, 35, 37, 23])




```python
names = ['Andrew','Bobo','Claire','David']
```


```python
ages = pd.Series(ran_data,names)
```


```python
ages
```




    Andrew    39
    Bobo      35
    Claire    37
    David     23
    dtype: int32



### From a  Dictionary


```python
ages = {'Sammy':5,'Frank':10,'Spike':7}
```


```python
ages
```




    {'Frank': 10, 'Sammy': 5, 'Spike': 7}




```python
pd.Series(ages)
```




    Sammy     5
    Frank    10
    Spike     7
    dtype: int64



# Key Ideas of a Series

## Named Index


```python
# Imaginary Sales Data for 1st and 2nd Quarters for Global Company
q1 = {'Japan': 80, 'China': 450, 'India': 200, 'USA': 250}
q2 = {'Brazil': 100,'China': 500, 'India': 210,'USA': 260}
```


```python
# Convert into Pandas Series
sales_Q1 = pd.Series(q1)
sales_Q2 = pd.Series(q2)
```


```python
sales_Q1
```




    Japan     80
    China    450
    India    200
    USA      250
    dtype: int64




```python
# Call values based on Named Index
sales_Q1['Japan']
```




    80




```python
# Integer Based Location information also retained!
sales_Q1[0]
```




    80



**Be careful with potential errors!**


```python
# Wrong Name
# sales_Q1['France']
```


```python
# Accidental Extra Space
# sales_Q1['USA ']
```


```python
# Capitalization Mistake
# sales_Q1['usa']
```

## Operations


```python
# Grab just the index keys
sales_Q1.keys()
```




    Index(['Japan', 'China', 'India', 'USA'], dtype='object')




```python
# Can Perform Operations Broadcasted across entire Series
sales_Q1 * 2
```




    Japan    160
    China    900
    India    400
    USA      500
    dtype: int64




```python
sales_Q2 / 100
```




    Brazil    1.0
    China     5.0
    India     2.1
    USA       2.6
    dtype: float64



## Between Series


```python
# Notice how Pandas informs you of mismatch with NaN
sales_Q1 + sales_Q2
```




    Brazil      NaN
    China     950.0
    India     410.0
    Japan       NaN
    USA       510.0
    dtype: float64




```python
# You can fill these with any value you want
sales_Q1.add(sales_Q2,fill_value=0)
```




    Brazil    100.0
    China     950.0
    India     410.0
    Japan      80.0
    USA       510.0
    dtype: float64



That is all we need to know about Series, up next, DataFrames!
