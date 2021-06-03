<h1>Table of Contents<span class="tocSkip"></span></h1>
<div class="toc"><ul class="toc-item"><li><span><a href="#Useful-Methods" data-toc-modified-id="Useful-Methods-1"><span class="toc-item-num">1&nbsp;&nbsp;</span>Useful Methods</a></span><ul class="toc-item"><li><span><a href="#The-.apply()-method" data-toc-modified-id="The-.apply()-method-1.1"><span class="toc-item-num">1.1&nbsp;&nbsp;</span>The .apply() method</a></span><ul class="toc-item"><li><span><a href="#apply-with-a-function" data-toc-modified-id="apply-with-a-function-1.1.1"><span class="toc-item-num">1.1.1&nbsp;&nbsp;</span>apply with a function</a></span></li><li><span><a href="#Using-.apply()-with-more-complex-functions" data-toc-modified-id="Using-.apply()-with-more-complex-functions-1.1.2"><span class="toc-item-num">1.1.2&nbsp;&nbsp;</span>Using .apply() with more complex functions</a></span></li><li><span><a href="#apply-with-lambda" data-toc-modified-id="apply-with-lambda-1.1.3"><span class="toc-item-num">1.1.3&nbsp;&nbsp;</span>apply with lambda</a></span></li></ul></li><li><span><a href="#apply-that-uses-multiple-columns" data-toc-modified-id="apply-that-uses-multiple-columns-1.2"><span class="toc-item-num">1.2&nbsp;&nbsp;</span>apply that uses multiple columns</a></span><ul class="toc-item"><li><span><a href="#df.describe-for-statistical-summaries" data-toc-modified-id="df.describe-for-statistical-summaries-1.2.1"><span class="toc-item-num">1.2.1&nbsp;&nbsp;</span>df.describe for statistical summaries</a></span></li><li><span><a href="#sort_values()" data-toc-modified-id="sort_values()-1.2.2"><span class="toc-item-num">1.2.2&nbsp;&nbsp;</span>sort_values()</a></span></li></ul></li><li><span><a href="#df.corr()-for-correlation-checks" data-toc-modified-id="df.corr()-for-correlation-checks-1.3"><span class="toc-item-num">1.3&nbsp;&nbsp;</span>df.corr() for correlation checks</a></span><ul class="toc-item"><li><span><a href="#idxmin-and-idxmax" data-toc-modified-id="idxmin-and-idxmax-1.3.1"><span class="toc-item-num">1.3.1&nbsp;&nbsp;</span>idxmin and idxmax</a></span></li><li><span><a href="#value_counts" data-toc-modified-id="value_counts-1.3.2"><span class="toc-item-num">1.3.2&nbsp;&nbsp;</span>value_counts</a></span></li><li><span><a href="#replace" data-toc-modified-id="replace-1.3.3"><span class="toc-item-num">1.3.3&nbsp;&nbsp;</span>replace</a></span></li><li><span><a href="#unique" data-toc-modified-id="unique-1.3.4"><span class="toc-item-num">1.3.4&nbsp;&nbsp;</span>unique</a></span></li><li><span><a href="#map" data-toc-modified-id="map-1.3.5"><span class="toc-item-num">1.3.5&nbsp;&nbsp;</span>map</a></span></li></ul></li><li><span><a href="#Duplicates" data-toc-modified-id="Duplicates-1.4"><span class="toc-item-num">1.4&nbsp;&nbsp;</span>Duplicates</a></span><ul class="toc-item"><li><span><a href="#.duplicated()-and-.drop_duplicates()" data-toc-modified-id=".duplicated()-and-.drop_duplicates()-1.4.1"><span class="toc-item-num">1.4.1&nbsp;&nbsp;</span>.duplicated() and .drop_duplicates()</a></span></li></ul></li><li><span><a href="#between" data-toc-modified-id="between-1.5"><span class="toc-item-num">1.5&nbsp;&nbsp;</span>between</a></span></li><li><span><a href="#sample" data-toc-modified-id="sample-1.6"><span class="toc-item-num">1.6&nbsp;&nbsp;</span>sample</a></span></li><li><span><a href="#nlargest-and-nsmallest" data-toc-modified-id="nlargest-and-nsmallest-1.7"><span class="toc-item-num">1.7&nbsp;&nbsp;</span>nlargest and nsmallest</a></span></li></ul></li></ul></div>

# Useful Methods

Let's cover some useful methods and functions built in to pandas. This is actually just a small sampling of the functions and methods available in Pandas, but they are some of the most commonly used.
The [documentation](https://pandas.pydata.org/pandas-docs/stable/reference/index.html) is a great resource to continue exploring more methods and functions (we will introduce more further along in the course).
Here is a list of functions and methods we'll cover here (click on one to jump to that section in this notebook.):

* [apply() method](#apply_method)
* [apply() with a function](#apply_function)
* [apply() with a lambda expression](#apply_lambda)
* [apply() on multiple columns](#apply_multiple)
* [describe()](#describe)
* [sort_values()](#sort)
* [corr()](#corr)
* [idxmin and idxmax](#idx)
* [value_counts](#v_c)
* [replace](#replace)
* [unique and nunique](#uni)
* [map](#map)
* [duplicated and drop_duplicates](#dup)
* [between](#bet)
* [sample](#sample)
* [nlargest](#n)

Make sure to view the video lessons to get the full explanation!

<a id='apply_method'></a>

## The .apply() method

Here we will learn about a very useful method known as **apply** on a DataFrame. This allows us to apply and broadcast custom functions on a DataFrame column


```python
import pandas as pd
import numpy as np
```


```python
df = pd.read_csv('tips.csv')
```


```python
df.head()
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
      <th>total_bill</th>
      <th>tip</th>
      <th>sex</th>
      <th>smoker</th>
      <th>day</th>
      <th>time</th>
      <th>size</th>
      <th>price_per_person</th>
      <th>Payer Name</th>
      <th>CC Number</th>
      <th>Payment ID</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>16.99</td>
      <td>1.01</td>
      <td>Female</td>
      <td>No</td>
      <td>Sun</td>
      <td>Dinner</td>
      <td>2</td>
      <td>8.49</td>
      <td>Christy Cunningham</td>
      <td>3560325168603410</td>
      <td>Sun2959</td>
    </tr>
    <tr>
      <th>1</th>
      <td>10.34</td>
      <td>1.66</td>
      <td>Male</td>
      <td>No</td>
      <td>Sun</td>
      <td>Dinner</td>
      <td>3</td>
      <td>3.45</td>
      <td>Douglas Tucker</td>
      <td>4478071379779230</td>
      <td>Sun4608</td>
    </tr>
    <tr>
      <th>2</th>
      <td>21.01</td>
      <td>3.50</td>
      <td>Male</td>
      <td>No</td>
      <td>Sun</td>
      <td>Dinner</td>
      <td>3</td>
      <td>7.00</td>
      <td>Travis Walters</td>
      <td>6011812112971322</td>
      <td>Sun4458</td>
    </tr>
    <tr>
      <th>3</th>
      <td>23.68</td>
      <td>3.31</td>
      <td>Male</td>
      <td>No</td>
      <td>Sun</td>
      <td>Dinner</td>
      <td>2</td>
      <td>11.84</td>
      <td>Nathaniel Harris</td>
      <td>4676137647685994</td>
      <td>Sun5260</td>
    </tr>
    <tr>
      <th>4</th>
      <td>24.59</td>
      <td>3.61</td>
      <td>Female</td>
      <td>No</td>
      <td>Sun</td>
      <td>Dinner</td>
      <td>4</td>
      <td>6.15</td>
      <td>Tonya Carter</td>
      <td>4832732618637221</td>
      <td>Sun2251</td>
    </tr>
  </tbody>
</table>
</div>



<a id='apply_function'></a>
### apply with a function


```python
df.info()
```

    <class 'pandas.core.frame.DataFrame'>
    RangeIndex: 244 entries, 0 to 243
    Data columns (total 11 columns):
     #   Column            Non-Null Count  Dtype  
    ---  ------            --------------  -----  
     0   total_bill        244 non-null    float64
     1   tip               244 non-null    float64
     2   sex               244 non-null    object 
     3   smoker            244 non-null    object 
     4   day               244 non-null    object 
     5   time              244 non-null    object 
     6   size              244 non-null    int64  
     7   price_per_person  244 non-null    float64
     8   Payer Name        244 non-null    object 
     9   CC Number         244 non-null    int64  
     10  Payment ID        244 non-null    object 
    dtypes: float64(3), int64(2), object(6)
    memory usage: 21.1+ KB
    


```python
def last_four(num):
    return str(num)[-4:]
```


```python
df['CC Number'][0]
```




    3560325168603410




```python
last_four(3560325168603410)
```




    '3410'




```python
df['last_four'] = df['CC Number'].apply(last_four)
```


```python
df.head()
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
      <th>total_bill</th>
      <th>tip</th>
      <th>sex</th>
      <th>smoker</th>
      <th>day</th>
      <th>time</th>
      <th>size</th>
      <th>price_per_person</th>
      <th>Payer Name</th>
      <th>CC Number</th>
      <th>Payment ID</th>
      <th>last_four</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>16.99</td>
      <td>1.01</td>
      <td>Female</td>
      <td>No</td>
      <td>Sun</td>
      <td>Dinner</td>
      <td>2</td>
      <td>8.49</td>
      <td>Christy Cunningham</td>
      <td>3560325168603410</td>
      <td>Sun2959</td>
      <td>3410</td>
    </tr>
    <tr>
      <th>1</th>
      <td>10.34</td>
      <td>1.66</td>
      <td>Male</td>
      <td>No</td>
      <td>Sun</td>
      <td>Dinner</td>
      <td>3</td>
      <td>3.45</td>
      <td>Douglas Tucker</td>
      <td>4478071379779230</td>
      <td>Sun4608</td>
      <td>9230</td>
    </tr>
    <tr>
      <th>2</th>
      <td>21.01</td>
      <td>3.50</td>
      <td>Male</td>
      <td>No</td>
      <td>Sun</td>
      <td>Dinner</td>
      <td>3</td>
      <td>7.00</td>
      <td>Travis Walters</td>
      <td>6011812112971322</td>
      <td>Sun4458</td>
      <td>1322</td>
    </tr>
    <tr>
      <th>3</th>
      <td>23.68</td>
      <td>3.31</td>
      <td>Male</td>
      <td>No</td>
      <td>Sun</td>
      <td>Dinner</td>
      <td>2</td>
      <td>11.84</td>
      <td>Nathaniel Harris</td>
      <td>4676137647685994</td>
      <td>Sun5260</td>
      <td>5994</td>
    </tr>
    <tr>
      <th>4</th>
      <td>24.59</td>
      <td>3.61</td>
      <td>Female</td>
      <td>No</td>
      <td>Sun</td>
      <td>Dinner</td>
      <td>4</td>
      <td>6.15</td>
      <td>Tonya Carter</td>
      <td>4832732618637221</td>
      <td>Sun2251</td>
      <td>7221</td>
    </tr>
  </tbody>
</table>
</div>



### Using .apply() with more complex functions


```python
df['total_bill'].mean()
```




    19.78594262295082




```python
def yelp(price):
    if price < 10:
        return '$'
    elif price >= 10 and price < 30:
        return '$$'
    else:
        return '$$$'
```


```python
df['Expensive'] = df['total_bill'].apply(yelp)
```


```python
# df
```

<a id='apply_lambda'></a>
### apply with lambda


```python
def simple(num):
    return num*2
```


```python
lambda num: num*2
```




    <function __main__.<lambda>(num)>




```python
df['total_bill'].apply(lambda bill:bill*0.18)
```




    0      3.0582
    1      1.8612
    2      3.7818
    3      4.2624
    4      4.4262
            ...  
    239    5.2254
    240    4.8924
    241    4.0806
    242    3.2076
    243    3.3804
    Name: total_bill, Length: 244, dtype: float64



<a id='apply_multiple'></a>
## apply that uses multiple columns

Note, there are several ways to do this:

https://stackoverflow.com/questions/19914937/applying-function-with-multiple-arguments-to-create-a-new-pandas-column


```python
df.head()
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
      <th>total_bill</th>
      <th>tip</th>
      <th>sex</th>
      <th>smoker</th>
      <th>day</th>
      <th>time</th>
      <th>size</th>
      <th>price_per_person</th>
      <th>Payer Name</th>
      <th>CC Number</th>
      <th>Payment ID</th>
      <th>last_four</th>
      <th>Expensive</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>16.99</td>
      <td>1.01</td>
      <td>Female</td>
      <td>No</td>
      <td>Sun</td>
      <td>Dinner</td>
      <td>2</td>
      <td>8.49</td>
      <td>Christy Cunningham</td>
      <td>3560325168603410</td>
      <td>Sun2959</td>
      <td>3410</td>
      <td>$$</td>
    </tr>
    <tr>
      <th>1</th>
      <td>10.34</td>
      <td>1.66</td>
      <td>Male</td>
      <td>No</td>
      <td>Sun</td>
      <td>Dinner</td>
      <td>3</td>
      <td>3.45</td>
      <td>Douglas Tucker</td>
      <td>4478071379779230</td>
      <td>Sun4608</td>
      <td>9230</td>
      <td>$$</td>
    </tr>
    <tr>
      <th>2</th>
      <td>21.01</td>
      <td>3.50</td>
      <td>Male</td>
      <td>No</td>
      <td>Sun</td>
      <td>Dinner</td>
      <td>3</td>
      <td>7.00</td>
      <td>Travis Walters</td>
      <td>6011812112971322</td>
      <td>Sun4458</td>
      <td>1322</td>
      <td>$$</td>
    </tr>
    <tr>
      <th>3</th>
      <td>23.68</td>
      <td>3.31</td>
      <td>Male</td>
      <td>No</td>
      <td>Sun</td>
      <td>Dinner</td>
      <td>2</td>
      <td>11.84</td>
      <td>Nathaniel Harris</td>
      <td>4676137647685994</td>
      <td>Sun5260</td>
      <td>5994</td>
      <td>$$</td>
    </tr>
    <tr>
      <th>4</th>
      <td>24.59</td>
      <td>3.61</td>
      <td>Female</td>
      <td>No</td>
      <td>Sun</td>
      <td>Dinner</td>
      <td>4</td>
      <td>6.15</td>
      <td>Tonya Carter</td>
      <td>4832732618637221</td>
      <td>Sun2251</td>
      <td>7221</td>
      <td>$$</td>
    </tr>
  </tbody>
</table>
</div>




```python
def quality(total_bill,tip):
    if tip/total_bill  > 0.25:
        return "Generous"
    else:
        return "Other"
```


```python
df['Tip Quality'] = df[['total_bill','tip']].apply(lambda df: quality(df['total_bill'],df['tip']),axis=1)
```


```python
df.head()
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
      <th>total_bill</th>
      <th>tip</th>
      <th>sex</th>
      <th>smoker</th>
      <th>day</th>
      <th>time</th>
      <th>size</th>
      <th>price_per_person</th>
      <th>Payer Name</th>
      <th>CC Number</th>
      <th>Payment ID</th>
      <th>last_four</th>
      <th>Expensive</th>
      <th>Tip Quality</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>16.99</td>
      <td>1.01</td>
      <td>Female</td>
      <td>No</td>
      <td>Sun</td>
      <td>Dinner</td>
      <td>2</td>
      <td>8.49</td>
      <td>Christy Cunningham</td>
      <td>3560325168603410</td>
      <td>Sun2959</td>
      <td>3410</td>
      <td>$$</td>
      <td>Other</td>
    </tr>
    <tr>
      <th>1</th>
      <td>10.34</td>
      <td>1.66</td>
      <td>Male</td>
      <td>No</td>
      <td>Sun</td>
      <td>Dinner</td>
      <td>3</td>
      <td>3.45</td>
      <td>Douglas Tucker</td>
      <td>4478071379779230</td>
      <td>Sun4608</td>
      <td>9230</td>
      <td>$$</td>
      <td>Other</td>
    </tr>
    <tr>
      <th>2</th>
      <td>21.01</td>
      <td>3.50</td>
      <td>Male</td>
      <td>No</td>
      <td>Sun</td>
      <td>Dinner</td>
      <td>3</td>
      <td>7.00</td>
      <td>Travis Walters</td>
      <td>6011812112971322</td>
      <td>Sun4458</td>
      <td>1322</td>
      <td>$$</td>
      <td>Other</td>
    </tr>
    <tr>
      <th>3</th>
      <td>23.68</td>
      <td>3.31</td>
      <td>Male</td>
      <td>No</td>
      <td>Sun</td>
      <td>Dinner</td>
      <td>2</td>
      <td>11.84</td>
      <td>Nathaniel Harris</td>
      <td>4676137647685994</td>
      <td>Sun5260</td>
      <td>5994</td>
      <td>$$</td>
      <td>Other</td>
    </tr>
    <tr>
      <th>4</th>
      <td>24.59</td>
      <td>3.61</td>
      <td>Female</td>
      <td>No</td>
      <td>Sun</td>
      <td>Dinner</td>
      <td>4</td>
      <td>6.15</td>
      <td>Tonya Carter</td>
      <td>4832732618637221</td>
      <td>Sun2251</td>
      <td>7221</td>
      <td>$$</td>
      <td>Other</td>
    </tr>
  </tbody>
</table>
</div>




```python
import numpy as np
```


```python
df['Tip Quality'] = np.vectorize(quality)(df['total_bill'], df['tip'])
```


```python
df.head()
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
      <th>total_bill</th>
      <th>tip</th>
      <th>sex</th>
      <th>smoker</th>
      <th>day</th>
      <th>time</th>
      <th>size</th>
      <th>price_per_person</th>
      <th>Payer Name</th>
      <th>CC Number</th>
      <th>Payment ID</th>
      <th>last_four</th>
      <th>Expensive</th>
      <th>Tip Quality</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>16.99</td>
      <td>1.01</td>
      <td>Female</td>
      <td>No</td>
      <td>Sun</td>
      <td>Dinner</td>
      <td>2</td>
      <td>8.49</td>
      <td>Christy Cunningham</td>
      <td>3560325168603410</td>
      <td>Sun2959</td>
      <td>3410</td>
      <td>$$</td>
      <td>Other</td>
    </tr>
    <tr>
      <th>1</th>
      <td>10.34</td>
      <td>1.66</td>
      <td>Male</td>
      <td>No</td>
      <td>Sun</td>
      <td>Dinner</td>
      <td>3</td>
      <td>3.45</td>
      <td>Douglas Tucker</td>
      <td>4478071379779230</td>
      <td>Sun4608</td>
      <td>9230</td>
      <td>$$</td>
      <td>Other</td>
    </tr>
    <tr>
      <th>2</th>
      <td>21.01</td>
      <td>3.50</td>
      <td>Male</td>
      <td>No</td>
      <td>Sun</td>
      <td>Dinner</td>
      <td>3</td>
      <td>7.00</td>
      <td>Travis Walters</td>
      <td>6011812112971322</td>
      <td>Sun4458</td>
      <td>1322</td>
      <td>$$</td>
      <td>Other</td>
    </tr>
    <tr>
      <th>3</th>
      <td>23.68</td>
      <td>3.31</td>
      <td>Male</td>
      <td>No</td>
      <td>Sun</td>
      <td>Dinner</td>
      <td>2</td>
      <td>11.84</td>
      <td>Nathaniel Harris</td>
      <td>4676137647685994</td>
      <td>Sun5260</td>
      <td>5994</td>
      <td>$$</td>
      <td>Other</td>
    </tr>
    <tr>
      <th>4</th>
      <td>24.59</td>
      <td>3.61</td>
      <td>Female</td>
      <td>No</td>
      <td>Sun</td>
      <td>Dinner</td>
      <td>4</td>
      <td>6.15</td>
      <td>Tonya Carter</td>
      <td>4832732618637221</td>
      <td>Sun2251</td>
      <td>7221</td>
      <td>$$</td>
      <td>Other</td>
    </tr>
  </tbody>
</table>
</div>



So, which one is faster?


```python
import timeit 
  
# code snippet to be executed only once 
setup = '''
import numpy as np
import pandas as pd
df = pd.read_csv('tips.csv')
def quality(total_bill,tip):
    if tip/total_bill  > 0.25:
        return "Generous"
    else:
        return "Other"
'''
  
# code snippet whose execution time is to be measured 
stmt_one = ''' 
df['Tip Quality'] = df[['total_bill','tip']].apply(lambda df: quality(df['total_bill'],df['tip']),axis=1)
'''

stmt_two = '''
df['Tip Quality'] = np.vectorize(quality)(df['total_bill'], df['tip'])
'''
  
```


```python
timeit.timeit(setup = setup, 
                    stmt = stmt_one, 
                    number = 1000) 
```




    5.0198852999999986




```python
timeit.timeit(setup = setup, 
                    stmt = stmt_two, 
                    number = 1000) 
```




    0.21840849999999534



Wow! Vectorization is much faster! Keep **np.vectorize()** in mind for the future.

Full Details:
https://docs.scipy.org/doc/numpy/reference/generated/numpy.vectorize.html

<a id='describe'></a>
### df.describe for statistical summaries


```python
df.describe()
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
      <th>total_bill</th>
      <th>tip</th>
      <th>size</th>
      <th>price_per_person</th>
      <th>CC Number</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>count</th>
      <td>244.000000</td>
      <td>244.000000</td>
      <td>244.000000</td>
      <td>244.000000</td>
      <td>2.440000e+02</td>
    </tr>
    <tr>
      <th>mean</th>
      <td>19.785943</td>
      <td>2.998279</td>
      <td>2.569672</td>
      <td>7.888197</td>
      <td>2.563496e+15</td>
    </tr>
    <tr>
      <th>std</th>
      <td>8.902412</td>
      <td>1.383638</td>
      <td>0.951100</td>
      <td>2.914234</td>
      <td>2.369340e+15</td>
    </tr>
    <tr>
      <th>min</th>
      <td>3.070000</td>
      <td>1.000000</td>
      <td>1.000000</td>
      <td>2.880000</td>
      <td>6.040679e+10</td>
    </tr>
    <tr>
      <th>25%</th>
      <td>13.347500</td>
      <td>2.000000</td>
      <td>2.000000</td>
      <td>5.800000</td>
      <td>3.040731e+13</td>
    </tr>
    <tr>
      <th>50%</th>
      <td>17.795000</td>
      <td>2.900000</td>
      <td>2.000000</td>
      <td>7.255000</td>
      <td>3.525318e+15</td>
    </tr>
    <tr>
      <th>75%</th>
      <td>24.127500</td>
      <td>3.562500</td>
      <td>3.000000</td>
      <td>9.390000</td>
      <td>4.553675e+15</td>
    </tr>
    <tr>
      <th>max</th>
      <td>50.810000</td>
      <td>10.000000</td>
      <td>6.000000</td>
      <td>20.270000</td>
      <td>6.596454e+15</td>
    </tr>
  </tbody>
</table>
</div>




```python
df.describe().transpose()
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
      <th>count</th>
      <th>mean</th>
      <th>std</th>
      <th>min</th>
      <th>25%</th>
      <th>50%</th>
      <th>75%</th>
      <th>max</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>total_bill</th>
      <td>244.0</td>
      <td>1.978594e+01</td>
      <td>8.902412e+00</td>
      <td>3.070000e+00</td>
      <td>1.334750e+01</td>
      <td>1.779500e+01</td>
      <td>2.412750e+01</td>
      <td>5.081000e+01</td>
    </tr>
    <tr>
      <th>tip</th>
      <td>244.0</td>
      <td>2.998279e+00</td>
      <td>1.383638e+00</td>
      <td>1.000000e+00</td>
      <td>2.000000e+00</td>
      <td>2.900000e+00</td>
      <td>3.562500e+00</td>
      <td>1.000000e+01</td>
    </tr>
    <tr>
      <th>size</th>
      <td>244.0</td>
      <td>2.569672e+00</td>
      <td>9.510998e-01</td>
      <td>1.000000e+00</td>
      <td>2.000000e+00</td>
      <td>2.000000e+00</td>
      <td>3.000000e+00</td>
      <td>6.000000e+00</td>
    </tr>
    <tr>
      <th>price_per_person</th>
      <td>244.0</td>
      <td>7.888197e+00</td>
      <td>2.914234e+00</td>
      <td>2.880000e+00</td>
      <td>5.800000e+00</td>
      <td>7.255000e+00</td>
      <td>9.390000e+00</td>
      <td>2.027000e+01</td>
    </tr>
    <tr>
      <th>CC Number</th>
      <td>244.0</td>
      <td>2.563496e+15</td>
      <td>2.369340e+15</td>
      <td>6.040679e+10</td>
      <td>3.040731e+13</td>
      <td>3.525318e+15</td>
      <td>4.553675e+15</td>
      <td>6.596454e+15</td>
    </tr>
  </tbody>
</table>
</div>



<a id='sort'></a>
### sort_values()


```python
df.sort_values('tip')
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
      <th>total_bill</th>
      <th>tip</th>
      <th>sex</th>
      <th>smoker</th>
      <th>day</th>
      <th>time</th>
      <th>size</th>
      <th>price_per_person</th>
      <th>Payer Name</th>
      <th>CC Number</th>
      <th>Payment ID</th>
      <th>last_four</th>
      <th>Expensive</th>
      <th>Tip Quality</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>67</th>
      <td>3.07</td>
      <td>1.00</td>
      <td>Female</td>
      <td>Yes</td>
      <td>Sat</td>
      <td>Dinner</td>
      <td>1</td>
      <td>3.07</td>
      <td>Tiffany Brock</td>
      <td>4359488526995267</td>
      <td>Sat3455</td>
      <td>5267</td>
      <td>$</td>
      <td>Generous</td>
    </tr>
    <tr>
      <th>236</th>
      <td>12.60</td>
      <td>1.00</td>
      <td>Male</td>
      <td>Yes</td>
      <td>Sat</td>
      <td>Dinner</td>
      <td>2</td>
      <td>6.30</td>
      <td>Matthew Myers</td>
      <td>3543676378973965</td>
      <td>Sat5032</td>
      <td>3965</td>
      <td>$$</td>
      <td>Other</td>
    </tr>
    <tr>
      <th>92</th>
      <td>5.75</td>
      <td>1.00</td>
      <td>Female</td>
      <td>Yes</td>
      <td>Fri</td>
      <td>Dinner</td>
      <td>2</td>
      <td>2.88</td>
      <td>Leah Ramirez</td>
      <td>3508911676966392</td>
      <td>Fri3780</td>
      <td>6392</td>
      <td>$</td>
      <td>Other</td>
    </tr>
    <tr>
      <th>111</th>
      <td>7.25</td>
      <td>1.00</td>
      <td>Female</td>
      <td>No</td>
      <td>Sat</td>
      <td>Dinner</td>
      <td>1</td>
      <td>7.25</td>
      <td>Terri Jones</td>
      <td>3559221007826887</td>
      <td>Sat4801</td>
      <td>6887</td>
      <td>$</td>
      <td>Other</td>
    </tr>
    <tr>
      <th>0</th>
      <td>16.99</td>
      <td>1.01</td>
      <td>Female</td>
      <td>No</td>
      <td>Sun</td>
      <td>Dinner</td>
      <td>2</td>
      <td>8.49</td>
      <td>Christy Cunningham</td>
      <td>3560325168603410</td>
      <td>Sun2959</td>
      <td>3410</td>
      <td>$$</td>
      <td>Other</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>141</th>
      <td>34.30</td>
      <td>6.70</td>
      <td>Male</td>
      <td>No</td>
      <td>Thur</td>
      <td>Lunch</td>
      <td>6</td>
      <td>5.72</td>
      <td>Steven Carlson</td>
      <td>3526515703718508</td>
      <td>Thur1025</td>
      <td>8508</td>
      <td>$$$</td>
      <td>Other</td>
    </tr>
    <tr>
      <th>59</th>
      <td>48.27</td>
      <td>6.73</td>
      <td>Male</td>
      <td>No</td>
      <td>Sat</td>
      <td>Dinner</td>
      <td>4</td>
      <td>12.07</td>
      <td>Brian Ortiz</td>
      <td>6596453823950595</td>
      <td>Sat8139</td>
      <td>0595</td>
      <td>$$$</td>
      <td>Other</td>
    </tr>
    <tr>
      <th>23</th>
      <td>39.42</td>
      <td>7.58</td>
      <td>Male</td>
      <td>No</td>
      <td>Sat</td>
      <td>Dinner</td>
      <td>4</td>
      <td>9.86</td>
      <td>Lance Peterson</td>
      <td>3542584061609808</td>
      <td>Sat239</td>
      <td>9808</td>
      <td>$$$</td>
      <td>Other</td>
    </tr>
    <tr>
      <th>212</th>
      <td>48.33</td>
      <td>9.00</td>
      <td>Male</td>
      <td>No</td>
      <td>Sat</td>
      <td>Dinner</td>
      <td>4</td>
      <td>12.08</td>
      <td>Alex Williamson</td>
      <td>676218815212</td>
      <td>Sat4590</td>
      <td>5212</td>
      <td>$$$</td>
      <td>Other</td>
    </tr>
    <tr>
      <th>170</th>
      <td>50.81</td>
      <td>10.00</td>
      <td>Male</td>
      <td>Yes</td>
      <td>Sat</td>
      <td>Dinner</td>
      <td>3</td>
      <td>16.94</td>
      <td>Gregory Clark</td>
      <td>5473850968388236</td>
      <td>Sat1954</td>
      <td>8236</td>
      <td>$$$</td>
      <td>Other</td>
    </tr>
  </tbody>
</table>
<p>244 rows × 14 columns</p>
</div>




```python
# Helpful if you want to reorder after a sort
# https://stackoverflow.com/questions/13148429/how-to-change-the-order-of-dataframe-columns
df.sort_values(['tip','size'])
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
      <th>total_bill</th>
      <th>tip</th>
      <th>sex</th>
      <th>smoker</th>
      <th>day</th>
      <th>time</th>
      <th>size</th>
      <th>price_per_person</th>
      <th>Payer Name</th>
      <th>CC Number</th>
      <th>Payment ID</th>
      <th>last_four</th>
      <th>Expensive</th>
      <th>Tip Quality</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>67</th>
      <td>3.07</td>
      <td>1.00</td>
      <td>Female</td>
      <td>Yes</td>
      <td>Sat</td>
      <td>Dinner</td>
      <td>1</td>
      <td>3.07</td>
      <td>Tiffany Brock</td>
      <td>4359488526995267</td>
      <td>Sat3455</td>
      <td>5267</td>
      <td>$</td>
      <td>Generous</td>
    </tr>
    <tr>
      <th>111</th>
      <td>7.25</td>
      <td>1.00</td>
      <td>Female</td>
      <td>No</td>
      <td>Sat</td>
      <td>Dinner</td>
      <td>1</td>
      <td>7.25</td>
      <td>Terri Jones</td>
      <td>3559221007826887</td>
      <td>Sat4801</td>
      <td>6887</td>
      <td>$</td>
      <td>Other</td>
    </tr>
    <tr>
      <th>92</th>
      <td>5.75</td>
      <td>1.00</td>
      <td>Female</td>
      <td>Yes</td>
      <td>Fri</td>
      <td>Dinner</td>
      <td>2</td>
      <td>2.88</td>
      <td>Leah Ramirez</td>
      <td>3508911676966392</td>
      <td>Fri3780</td>
      <td>6392</td>
      <td>$</td>
      <td>Other</td>
    </tr>
    <tr>
      <th>236</th>
      <td>12.60</td>
      <td>1.00</td>
      <td>Male</td>
      <td>Yes</td>
      <td>Sat</td>
      <td>Dinner</td>
      <td>2</td>
      <td>6.30</td>
      <td>Matthew Myers</td>
      <td>3543676378973965</td>
      <td>Sat5032</td>
      <td>3965</td>
      <td>$$</td>
      <td>Other</td>
    </tr>
    <tr>
      <th>0</th>
      <td>16.99</td>
      <td>1.01</td>
      <td>Female</td>
      <td>No</td>
      <td>Sun</td>
      <td>Dinner</td>
      <td>2</td>
      <td>8.49</td>
      <td>Christy Cunningham</td>
      <td>3560325168603410</td>
      <td>Sun2959</td>
      <td>3410</td>
      <td>$$</td>
      <td>Other</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>141</th>
      <td>34.30</td>
      <td>6.70</td>
      <td>Male</td>
      <td>No</td>
      <td>Thur</td>
      <td>Lunch</td>
      <td>6</td>
      <td>5.72</td>
      <td>Steven Carlson</td>
      <td>3526515703718508</td>
      <td>Thur1025</td>
      <td>8508</td>
      <td>$$$</td>
      <td>Other</td>
    </tr>
    <tr>
      <th>59</th>
      <td>48.27</td>
      <td>6.73</td>
      <td>Male</td>
      <td>No</td>
      <td>Sat</td>
      <td>Dinner</td>
      <td>4</td>
      <td>12.07</td>
      <td>Brian Ortiz</td>
      <td>6596453823950595</td>
      <td>Sat8139</td>
      <td>0595</td>
      <td>$$$</td>
      <td>Other</td>
    </tr>
    <tr>
      <th>23</th>
      <td>39.42</td>
      <td>7.58</td>
      <td>Male</td>
      <td>No</td>
      <td>Sat</td>
      <td>Dinner</td>
      <td>4</td>
      <td>9.86</td>
      <td>Lance Peterson</td>
      <td>3542584061609808</td>
      <td>Sat239</td>
      <td>9808</td>
      <td>$$$</td>
      <td>Other</td>
    </tr>
    <tr>
      <th>212</th>
      <td>48.33</td>
      <td>9.00</td>
      <td>Male</td>
      <td>No</td>
      <td>Sat</td>
      <td>Dinner</td>
      <td>4</td>
      <td>12.08</td>
      <td>Alex Williamson</td>
      <td>676218815212</td>
      <td>Sat4590</td>
      <td>5212</td>
      <td>$$$</td>
      <td>Other</td>
    </tr>
    <tr>
      <th>170</th>
      <td>50.81</td>
      <td>10.00</td>
      <td>Male</td>
      <td>Yes</td>
      <td>Sat</td>
      <td>Dinner</td>
      <td>3</td>
      <td>16.94</td>
      <td>Gregory Clark</td>
      <td>5473850968388236</td>
      <td>Sat1954</td>
      <td>8236</td>
      <td>$$$</td>
      <td>Other</td>
    </tr>
  </tbody>
</table>
<p>244 rows × 14 columns</p>
</div>



<a id='corr'></a>
## df.corr() for correlation checks

[Wikipedia on Correlation](https://en.wikipedia.org/wiki/Correlation_and_dependence)


```python
df.corr()
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
      <th>total_bill</th>
      <th>tip</th>
      <th>size</th>
      <th>price_per_person</th>
      <th>CC Number</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>total_bill</th>
      <td>1.000000</td>
      <td>0.675734</td>
      <td>0.598315</td>
      <td>0.647554</td>
      <td>0.104576</td>
    </tr>
    <tr>
      <th>tip</th>
      <td>0.675734</td>
      <td>1.000000</td>
      <td>0.489299</td>
      <td>0.347405</td>
      <td>0.110857</td>
    </tr>
    <tr>
      <th>size</th>
      <td>0.598315</td>
      <td>0.489299</td>
      <td>1.000000</td>
      <td>-0.175359</td>
      <td>-0.030239</td>
    </tr>
    <tr>
      <th>price_per_person</th>
      <td>0.647554</td>
      <td>0.347405</td>
      <td>-0.175359</td>
      <td>1.000000</td>
      <td>0.135240</td>
    </tr>
    <tr>
      <th>CC Number</th>
      <td>0.104576</td>
      <td>0.110857</td>
      <td>-0.030239</td>
      <td>0.135240</td>
      <td>1.000000</td>
    </tr>
  </tbody>
</table>
</div>




```python
df[['total_bill','tip']].corr()
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
      <th>total_bill</th>
      <th>tip</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>total_bill</th>
      <td>1.000000</td>
      <td>0.675734</td>
    </tr>
    <tr>
      <th>tip</th>
      <td>0.675734</td>
      <td>1.000000</td>
    </tr>
  </tbody>
</table>
</div>



<a id='idx'></a>
### idxmin and idxmax


```python
df.head()
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
      <th>total_bill</th>
      <th>tip</th>
      <th>sex</th>
      <th>smoker</th>
      <th>day</th>
      <th>time</th>
      <th>size</th>
      <th>price_per_person</th>
      <th>Payer Name</th>
      <th>CC Number</th>
      <th>Payment ID</th>
      <th>last_four</th>
      <th>Expensive</th>
      <th>Tip Quality</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>16.99</td>
      <td>1.01</td>
      <td>Female</td>
      <td>No</td>
      <td>Sun</td>
      <td>Dinner</td>
      <td>2</td>
      <td>8.49</td>
      <td>Christy Cunningham</td>
      <td>3560325168603410</td>
      <td>Sun2959</td>
      <td>3410</td>
      <td>$$</td>
      <td>Other</td>
    </tr>
    <tr>
      <th>1</th>
      <td>10.34</td>
      <td>1.66</td>
      <td>Male</td>
      <td>No</td>
      <td>Sun</td>
      <td>Dinner</td>
      <td>3</td>
      <td>3.45</td>
      <td>Douglas Tucker</td>
      <td>4478071379779230</td>
      <td>Sun4608</td>
      <td>9230</td>
      <td>$$</td>
      <td>Other</td>
    </tr>
    <tr>
      <th>2</th>
      <td>21.01</td>
      <td>3.50</td>
      <td>Male</td>
      <td>No</td>
      <td>Sun</td>
      <td>Dinner</td>
      <td>3</td>
      <td>7.00</td>
      <td>Travis Walters</td>
      <td>6011812112971322</td>
      <td>Sun4458</td>
      <td>1322</td>
      <td>$$</td>
      <td>Other</td>
    </tr>
    <tr>
      <th>3</th>
      <td>23.68</td>
      <td>3.31</td>
      <td>Male</td>
      <td>No</td>
      <td>Sun</td>
      <td>Dinner</td>
      <td>2</td>
      <td>11.84</td>
      <td>Nathaniel Harris</td>
      <td>4676137647685994</td>
      <td>Sun5260</td>
      <td>5994</td>
      <td>$$</td>
      <td>Other</td>
    </tr>
    <tr>
      <th>4</th>
      <td>24.59</td>
      <td>3.61</td>
      <td>Female</td>
      <td>No</td>
      <td>Sun</td>
      <td>Dinner</td>
      <td>4</td>
      <td>6.15</td>
      <td>Tonya Carter</td>
      <td>4832732618637221</td>
      <td>Sun2251</td>
      <td>7221</td>
      <td>$$</td>
      <td>Other</td>
    </tr>
  </tbody>
</table>
</div>




```python
df['total_bill'].max()
```




    50.81




```python
df['total_bill'].idxmax()
```




    170




```python
df['total_bill'].idxmin()
```




    67




```python
df.iloc[67]
```




    total_bill                      3.07
    tip                                1
    sex                           Female
    smoker                           Yes
    day                              Sat
    time                          Dinner
    size                               1
    price_per_person                3.07
    Payer Name             Tiffany Brock
    CC Number           4359488526995267
    Payment ID                   Sat3455
    last_four                       5267
    Expensive                          $
    Tip Quality                 Generous
    Name: 67, dtype: object




```python
df.iloc[170]
```




    total_bill                     50.81
    tip                               10
    sex                             Male
    smoker                           Yes
    day                              Sat
    time                          Dinner
    size                               3
    price_per_person               16.94
    Payer Name             Gregory Clark
    CC Number           5473850968388236
    Payment ID                   Sat1954
    last_four                       8236
    Expensive                        $$$
    Tip Quality                    Other
    Name: 170, dtype: object



<a id='v_c'></a>
### value_counts

Nice method to quickly get a count per category. Only makes sense on categorical columns.


```python
df.head()
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
      <th>total_bill</th>
      <th>tip</th>
      <th>sex</th>
      <th>smoker</th>
      <th>day</th>
      <th>time</th>
      <th>size</th>
      <th>price_per_person</th>
      <th>Payer Name</th>
      <th>CC Number</th>
      <th>Payment ID</th>
      <th>last_four</th>
      <th>Expensive</th>
      <th>Tip Quality</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>16.99</td>
      <td>1.01</td>
      <td>Female</td>
      <td>No</td>
      <td>Sun</td>
      <td>Dinner</td>
      <td>2</td>
      <td>8.49</td>
      <td>Christy Cunningham</td>
      <td>3560325168603410</td>
      <td>Sun2959</td>
      <td>3410</td>
      <td>$$</td>
      <td>Other</td>
    </tr>
    <tr>
      <th>1</th>
      <td>10.34</td>
      <td>1.66</td>
      <td>Male</td>
      <td>No</td>
      <td>Sun</td>
      <td>Dinner</td>
      <td>3</td>
      <td>3.45</td>
      <td>Douglas Tucker</td>
      <td>4478071379779230</td>
      <td>Sun4608</td>
      <td>9230</td>
      <td>$$</td>
      <td>Other</td>
    </tr>
    <tr>
      <th>2</th>
      <td>21.01</td>
      <td>3.50</td>
      <td>Male</td>
      <td>No</td>
      <td>Sun</td>
      <td>Dinner</td>
      <td>3</td>
      <td>7.00</td>
      <td>Travis Walters</td>
      <td>6011812112971322</td>
      <td>Sun4458</td>
      <td>1322</td>
      <td>$$</td>
      <td>Other</td>
    </tr>
    <tr>
      <th>3</th>
      <td>23.68</td>
      <td>3.31</td>
      <td>Male</td>
      <td>No</td>
      <td>Sun</td>
      <td>Dinner</td>
      <td>2</td>
      <td>11.84</td>
      <td>Nathaniel Harris</td>
      <td>4676137647685994</td>
      <td>Sun5260</td>
      <td>5994</td>
      <td>$$</td>
      <td>Other</td>
    </tr>
    <tr>
      <th>4</th>
      <td>24.59</td>
      <td>3.61</td>
      <td>Female</td>
      <td>No</td>
      <td>Sun</td>
      <td>Dinner</td>
      <td>4</td>
      <td>6.15</td>
      <td>Tonya Carter</td>
      <td>4832732618637221</td>
      <td>Sun2251</td>
      <td>7221</td>
      <td>$$</td>
      <td>Other</td>
    </tr>
  </tbody>
</table>
</div>




```python
df['sex'].value_counts()
```




    Male      157
    Female     87
    Name: sex, dtype: int64



<a id='replace'></a>

### replace

Quickly replace values with another one.


```python
df.head()
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
      <th>total_bill</th>
      <th>tip</th>
      <th>sex</th>
      <th>smoker</th>
      <th>day</th>
      <th>time</th>
      <th>size</th>
      <th>price_per_person</th>
      <th>Payer Name</th>
      <th>CC Number</th>
      <th>Payment ID</th>
      <th>last_four</th>
      <th>Expensive</th>
      <th>Tip Quality</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>16.99</td>
      <td>1.01</td>
      <td>Female</td>
      <td>No</td>
      <td>Sun</td>
      <td>Dinner</td>
      <td>2</td>
      <td>8.49</td>
      <td>Christy Cunningham</td>
      <td>3560325168603410</td>
      <td>Sun2959</td>
      <td>3410</td>
      <td>$$</td>
      <td>Other</td>
    </tr>
    <tr>
      <th>1</th>
      <td>10.34</td>
      <td>1.66</td>
      <td>Male</td>
      <td>No</td>
      <td>Sun</td>
      <td>Dinner</td>
      <td>3</td>
      <td>3.45</td>
      <td>Douglas Tucker</td>
      <td>4478071379779230</td>
      <td>Sun4608</td>
      <td>9230</td>
      <td>$$</td>
      <td>Other</td>
    </tr>
    <tr>
      <th>2</th>
      <td>21.01</td>
      <td>3.50</td>
      <td>Male</td>
      <td>No</td>
      <td>Sun</td>
      <td>Dinner</td>
      <td>3</td>
      <td>7.00</td>
      <td>Travis Walters</td>
      <td>6011812112971322</td>
      <td>Sun4458</td>
      <td>1322</td>
      <td>$$</td>
      <td>Other</td>
    </tr>
    <tr>
      <th>3</th>
      <td>23.68</td>
      <td>3.31</td>
      <td>Male</td>
      <td>No</td>
      <td>Sun</td>
      <td>Dinner</td>
      <td>2</td>
      <td>11.84</td>
      <td>Nathaniel Harris</td>
      <td>4676137647685994</td>
      <td>Sun5260</td>
      <td>5994</td>
      <td>$$</td>
      <td>Other</td>
    </tr>
    <tr>
      <th>4</th>
      <td>24.59</td>
      <td>3.61</td>
      <td>Female</td>
      <td>No</td>
      <td>Sun</td>
      <td>Dinner</td>
      <td>4</td>
      <td>6.15</td>
      <td>Tonya Carter</td>
      <td>4832732618637221</td>
      <td>Sun2251</td>
      <td>7221</td>
      <td>$$</td>
      <td>Other</td>
    </tr>
  </tbody>
</table>
</div>




```python
df['Tip Quality'].replace(to_replace='Other',value='Ok')
```




    0            Ok
    1            Ok
    2            Ok
    3            Ok
    4            Ok
    5            Ok
    6            Ok
    7            Ok
    8            Ok
    9            Ok
    10           Ok
    11           Ok
    12           Ok
    13           Ok
    14           Ok
    15           Ok
    16           Ok
    17           Ok
    18           Ok
    19           Ok
    20           Ok
    21           Ok
    22           Ok
    23           Ok
    24           Ok
    25           Ok
    26           Ok
    27           Ok
    28           Ok
    29           Ok
             ...   
    214          Ok
    215          Ok
    216          Ok
    217          Ok
    218          Ok
    219          Ok
    220          Ok
    221    Generous
    222          Ok
    223          Ok
    224          Ok
    225          Ok
    226          Ok
    227          Ok
    228          Ok
    229          Ok
    230          Ok
    231          Ok
    232    Generous
    233          Ok
    234          Ok
    235          Ok
    236          Ok
    237          Ok
    238          Ok
    239          Ok
    240          Ok
    241          Ok
    242          Ok
    243          Ok
    Name: Tip Quality, Length: 244, dtype: object




```python
df['Tip Quality'] = df['Tip Quality'].replace(to_replace='Other',value='Ok')
```


```python
df.head()
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
      <th>total_bill</th>
      <th>tip</th>
      <th>sex</th>
      <th>smoker</th>
      <th>day</th>
      <th>time</th>
      <th>size</th>
      <th>price_per_person</th>
      <th>Payer Name</th>
      <th>CC Number</th>
      <th>Payment ID</th>
      <th>last_four</th>
      <th>Expensive</th>
      <th>Tip Quality</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>16.99</td>
      <td>1.01</td>
      <td>Female</td>
      <td>No</td>
      <td>Sun</td>
      <td>Dinner</td>
      <td>2</td>
      <td>8.49</td>
      <td>Christy Cunningham</td>
      <td>3560325168603410</td>
      <td>Sun2959</td>
      <td>3410</td>
      <td>$$</td>
      <td>Ok</td>
    </tr>
    <tr>
      <th>1</th>
      <td>10.34</td>
      <td>1.66</td>
      <td>Male</td>
      <td>No</td>
      <td>Sun</td>
      <td>Dinner</td>
      <td>3</td>
      <td>3.45</td>
      <td>Douglas Tucker</td>
      <td>4478071379779230</td>
      <td>Sun4608</td>
      <td>9230</td>
      <td>$$</td>
      <td>Ok</td>
    </tr>
    <tr>
      <th>2</th>
      <td>21.01</td>
      <td>3.50</td>
      <td>Male</td>
      <td>No</td>
      <td>Sun</td>
      <td>Dinner</td>
      <td>3</td>
      <td>7.00</td>
      <td>Travis Walters</td>
      <td>6011812112971322</td>
      <td>Sun4458</td>
      <td>1322</td>
      <td>$$</td>
      <td>Ok</td>
    </tr>
    <tr>
      <th>3</th>
      <td>23.68</td>
      <td>3.31</td>
      <td>Male</td>
      <td>No</td>
      <td>Sun</td>
      <td>Dinner</td>
      <td>2</td>
      <td>11.84</td>
      <td>Nathaniel Harris</td>
      <td>4676137647685994</td>
      <td>Sun5260</td>
      <td>5994</td>
      <td>$$</td>
      <td>Ok</td>
    </tr>
    <tr>
      <th>4</th>
      <td>24.59</td>
      <td>3.61</td>
      <td>Female</td>
      <td>No</td>
      <td>Sun</td>
      <td>Dinner</td>
      <td>4</td>
      <td>6.15</td>
      <td>Tonya Carter</td>
      <td>4832732618637221</td>
      <td>Sun2251</td>
      <td>7221</td>
      <td>$$</td>
      <td>Ok</td>
    </tr>
  </tbody>
</table>
</div>



<a id='uni'></a>
### unique


```python
df['size'].unique()
```




    array([2, 3, 4, 1, 6, 5], dtype=int64)




```python
df['size'].nunique()
```




    6




```python
df['time'].unique()
```




    array(['Dinner', 'Lunch'], dtype=object)



<a id='map'></a>
### map


```python
my_map = {'Dinner':'D','Lunch':'L'}
```


```python
df['time'].map(my_map)
```




    0      D
    1      D
    2      D
    3      D
    4      D
    5      D
    6      D
    7      D
    8      D
    9      D
    10     D
    11     D
    12     D
    13     D
    14     D
    15     D
    16     D
    17     D
    18     D
    19     D
    20     D
    21     D
    22     D
    23     D
    24     D
    25     D
    26     D
    27     D
    28     D
    29     D
          ..
    214    D
    215    D
    216    D
    217    D
    218    D
    219    D
    220    L
    221    L
    222    L
    223    L
    224    L
    225    L
    226    L
    227    D
    228    D
    229    D
    230    D
    231    D
    232    D
    233    D
    234    D
    235    D
    236    D
    237    D
    238    D
    239    D
    240    D
    241    D
    242    D
    243    D
    Name: time, Length: 244, dtype: object




```python
df.head()
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
      <th>total_bill</th>
      <th>tip</th>
      <th>sex</th>
      <th>smoker</th>
      <th>day</th>
      <th>time</th>
      <th>size</th>
      <th>price_per_person</th>
      <th>Payer Name</th>
      <th>CC Number</th>
      <th>Payment ID</th>
      <th>last_four</th>
      <th>Expensive</th>
      <th>Tip Quality</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>16.99</td>
      <td>1.01</td>
      <td>Female</td>
      <td>No</td>
      <td>Sun</td>
      <td>Dinner</td>
      <td>2</td>
      <td>8.49</td>
      <td>Christy Cunningham</td>
      <td>3560325168603410</td>
      <td>Sun2959</td>
      <td>3410</td>
      <td>$$</td>
      <td>Ok</td>
    </tr>
    <tr>
      <th>1</th>
      <td>10.34</td>
      <td>1.66</td>
      <td>Male</td>
      <td>No</td>
      <td>Sun</td>
      <td>Dinner</td>
      <td>3</td>
      <td>3.45</td>
      <td>Douglas Tucker</td>
      <td>4478071379779230</td>
      <td>Sun4608</td>
      <td>9230</td>
      <td>$$</td>
      <td>Ok</td>
    </tr>
    <tr>
      <th>2</th>
      <td>21.01</td>
      <td>3.50</td>
      <td>Male</td>
      <td>No</td>
      <td>Sun</td>
      <td>Dinner</td>
      <td>3</td>
      <td>7.00</td>
      <td>Travis Walters</td>
      <td>6011812112971322</td>
      <td>Sun4458</td>
      <td>1322</td>
      <td>$$</td>
      <td>Ok</td>
    </tr>
    <tr>
      <th>3</th>
      <td>23.68</td>
      <td>3.31</td>
      <td>Male</td>
      <td>No</td>
      <td>Sun</td>
      <td>Dinner</td>
      <td>2</td>
      <td>11.84</td>
      <td>Nathaniel Harris</td>
      <td>4676137647685994</td>
      <td>Sun5260</td>
      <td>5994</td>
      <td>$$</td>
      <td>Ok</td>
    </tr>
    <tr>
      <th>4</th>
      <td>24.59</td>
      <td>3.61</td>
      <td>Female</td>
      <td>No</td>
      <td>Sun</td>
      <td>Dinner</td>
      <td>4</td>
      <td>6.15</td>
      <td>Tonya Carter</td>
      <td>4832732618637221</td>
      <td>Sun2251</td>
      <td>7221</td>
      <td>$$</td>
      <td>Ok</td>
    </tr>
  </tbody>
</table>
</div>



<a id='dup'></a>
## Duplicates

### .duplicated() and .drop_duplicates()


```python
# Returns True for the 1st instance of a duplicated row
df.duplicated()
```




    0      False
    1      False
    2      False
    3      False
    4      False
    5      False
    6      False
    7      False
    8      False
    9      False
    10     False
    11     False
    12     False
    13     False
    14     False
    15     False
    16     False
    17     False
    18     False
    19     False
    20     False
    21     False
    22     False
    23     False
    24     False
    25     False
    26     False
    27     False
    28     False
    29     False
           ...  
    214    False
    215    False
    216    False
    217    False
    218    False
    219    False
    220    False
    221    False
    222    False
    223    False
    224    False
    225    False
    226    False
    227    False
    228    False
    229    False
    230    False
    231    False
    232    False
    233    False
    234    False
    235    False
    236    False
    237    False
    238    False
    239    False
    240    False
    241    False
    242    False
    243    False
    Length: 244, dtype: bool




```python
simple_df = pd.DataFrame([1,2,2],['a','b','c'])
```


```python
simple_df
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
      <th>0</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>a</th>
      <td>1</td>
    </tr>
    <tr>
      <th>b</th>
      <td>2</td>
    </tr>
    <tr>
      <th>c</th>
      <td>2</td>
    </tr>
  </tbody>
</table>
</div>




```python
simple_df.duplicated()
```




    a    False
    b    False
    c     True
    dtype: bool




```python
simple_df.drop_duplicates()
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
      <th>0</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>a</th>
      <td>1</td>
    </tr>
    <tr>
      <th>b</th>
      <td>2</td>
    </tr>
  </tbody>
</table>
</div>



<a id='bet'></a>
## between

left: A scalar value that defines the left boundary
right: A scalar value that defines the right boundary
inclusive: A Boolean value which is True by default. If False, it excludes the two passed arguments while checking.


```python
df['total_bill'].between(10,20,inclusive=True)
```




    0       True
    1       True
    2      False
    3      False
    4      False
    5      False
    6      False
    7      False
    8       True
    9       True
    10      True
    11     False
    12      True
    13      True
    14      True
    15     False
    16      True
    17      True
    18      True
    19     False
    20      True
    21     False
    22      True
    23     False
    24      True
    25      True
    26      True
    27      True
    28     False
    29      True
           ...  
    214    False
    215     True
    216    False
    217     True
    218    False
    219    False
    220     True
    221     True
    222    False
    223     True
    224     True
    225     True
    226     True
    227    False
    228     True
    229    False
    230    False
    231     True
    232     True
    233     True
    234     True
    235     True
    236     True
    237    False
    238    False
    239    False
    240    False
    241    False
    242     True
    243     True
    Name: total_bill, Length: 244, dtype: bool




```python
df[df['total_bill'].between(10,20,inclusive=True)]
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
      <th>total_bill</th>
      <th>tip</th>
      <th>sex</th>
      <th>smoker</th>
      <th>day</th>
      <th>time</th>
      <th>size</th>
      <th>price_per_person</th>
      <th>Payer Name</th>
      <th>CC Number</th>
      <th>Payment ID</th>
      <th>last_four</th>
      <th>Expensive</th>
      <th>Tip Quality</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>16.99</td>
      <td>1.01</td>
      <td>Female</td>
      <td>No</td>
      <td>Sun</td>
      <td>Dinner</td>
      <td>2</td>
      <td>8.49</td>
      <td>Christy Cunningham</td>
      <td>3560325168603410</td>
      <td>Sun2959</td>
      <td>3410</td>
      <td>$$</td>
      <td>Ok</td>
    </tr>
    <tr>
      <th>1</th>
      <td>10.34</td>
      <td>1.66</td>
      <td>Male</td>
      <td>No</td>
      <td>Sun</td>
      <td>Dinner</td>
      <td>3</td>
      <td>3.45</td>
      <td>Douglas Tucker</td>
      <td>4478071379779230</td>
      <td>Sun4608</td>
      <td>9230</td>
      <td>$$</td>
      <td>Ok</td>
    </tr>
    <tr>
      <th>8</th>
      <td>15.04</td>
      <td>1.96</td>
      <td>Male</td>
      <td>No</td>
      <td>Sun</td>
      <td>Dinner</td>
      <td>2</td>
      <td>7.52</td>
      <td>Joseph Mcdonald</td>
      <td>3522866365840377</td>
      <td>Sun6820</td>
      <td>0377</td>
      <td>$$</td>
      <td>Ok</td>
    </tr>
    <tr>
      <th>9</th>
      <td>14.78</td>
      <td>3.23</td>
      <td>Male</td>
      <td>No</td>
      <td>Sun</td>
      <td>Dinner</td>
      <td>2</td>
      <td>7.39</td>
      <td>Jerome Abbott</td>
      <td>3532124519049786</td>
      <td>Sun3775</td>
      <td>9786</td>
      <td>$$</td>
      <td>Ok</td>
    </tr>
    <tr>
      <th>10</th>
      <td>10.27</td>
      <td>1.71</td>
      <td>Male</td>
      <td>No</td>
      <td>Sun</td>
      <td>Dinner</td>
      <td>2</td>
      <td>5.14</td>
      <td>William Riley</td>
      <td>566287581219</td>
      <td>Sun2546</td>
      <td>1219</td>
      <td>$$</td>
      <td>Ok</td>
    </tr>
    <tr>
      <th>12</th>
      <td>15.42</td>
      <td>1.57</td>
      <td>Male</td>
      <td>No</td>
      <td>Sun</td>
      <td>Dinner</td>
      <td>2</td>
      <td>7.71</td>
      <td>Chad Harrington</td>
      <td>577040572932</td>
      <td>Sun1300</td>
      <td>2932</td>
      <td>$$</td>
      <td>Ok</td>
    </tr>
    <tr>
      <th>13</th>
      <td>18.43</td>
      <td>3.00</td>
      <td>Male</td>
      <td>No</td>
      <td>Sun</td>
      <td>Dinner</td>
      <td>4</td>
      <td>4.61</td>
      <td>Joshua Jones</td>
      <td>6011163105616890</td>
      <td>Sun2971</td>
      <td>6890</td>
      <td>$$</td>
      <td>Ok</td>
    </tr>
    <tr>
      <th>14</th>
      <td>14.83</td>
      <td>3.02</td>
      <td>Female</td>
      <td>No</td>
      <td>Sun</td>
      <td>Dinner</td>
      <td>2</td>
      <td>7.42</td>
      <td>Vanessa Jones</td>
      <td>30016702287574</td>
      <td>Sun3848</td>
      <td>7574</td>
      <td>$$</td>
      <td>Ok</td>
    </tr>
    <tr>
      <th>16</th>
      <td>10.33</td>
      <td>1.67</td>
      <td>Female</td>
      <td>No</td>
      <td>Sun</td>
      <td>Dinner</td>
      <td>3</td>
      <td>3.44</td>
      <td>Elizabeth Foster</td>
      <td>4240025044626033</td>
      <td>Sun9715</td>
      <td>6033</td>
      <td>$$</td>
      <td>Ok</td>
    </tr>
    <tr>
      <th>17</th>
      <td>16.29</td>
      <td>3.71</td>
      <td>Male</td>
      <td>No</td>
      <td>Sun</td>
      <td>Dinner</td>
      <td>3</td>
      <td>5.43</td>
      <td>John Pittman</td>
      <td>6521340257218708</td>
      <td>Sun2998</td>
      <td>8708</td>
      <td>$$</td>
      <td>Ok</td>
    </tr>
    <tr>
      <th>18</th>
      <td>16.97</td>
      <td>3.50</td>
      <td>Female</td>
      <td>No</td>
      <td>Sun</td>
      <td>Dinner</td>
      <td>3</td>
      <td>5.66</td>
      <td>Laura Martinez</td>
      <td>30422275171379</td>
      <td>Sun2789</td>
      <td>1379</td>
      <td>$$</td>
      <td>Ok</td>
    </tr>
    <tr>
      <th>20</th>
      <td>17.92</td>
      <td>4.08</td>
      <td>Male</td>
      <td>No</td>
      <td>Sat</td>
      <td>Dinner</td>
      <td>2</td>
      <td>8.96</td>
      <td>Thomas Rice</td>
      <td>4403296224639756</td>
      <td>Sat1709</td>
      <td>9756</td>
      <td>$$</td>
      <td>Ok</td>
    </tr>
    <tr>
      <th>22</th>
      <td>15.77</td>
      <td>2.23</td>
      <td>Female</td>
      <td>No</td>
      <td>Sat</td>
      <td>Dinner</td>
      <td>2</td>
      <td>7.88</td>
      <td>Ashley Shelton</td>
      <td>3524119516293213</td>
      <td>Sat9786</td>
      <td>3213</td>
      <td>$$</td>
      <td>Ok</td>
    </tr>
    <tr>
      <th>24</th>
      <td>19.82</td>
      <td>3.18</td>
      <td>Male</td>
      <td>No</td>
      <td>Sat</td>
      <td>Dinner</td>
      <td>2</td>
      <td>9.91</td>
      <td>Christopher Ross</td>
      <td>36739148167928</td>
      <td>Sat6236</td>
      <td>7928</td>
      <td>$$</td>
      <td>Ok</td>
    </tr>
    <tr>
      <th>25</th>
      <td>17.81</td>
      <td>2.34</td>
      <td>Male</td>
      <td>No</td>
      <td>Sat</td>
      <td>Dinner</td>
      <td>4</td>
      <td>4.45</td>
      <td>Robert Perkins</td>
      <td>30502930499388</td>
      <td>Sat907</td>
      <td>9388</td>
      <td>$$</td>
      <td>Ok</td>
    </tr>
    <tr>
      <th>26</th>
      <td>13.37</td>
      <td>2.00</td>
      <td>Male</td>
      <td>No</td>
      <td>Sat</td>
      <td>Dinner</td>
      <td>2</td>
      <td>6.68</td>
      <td>Kyle Avery</td>
      <td>6531339539615499</td>
      <td>Sat6651</td>
      <td>5499</td>
      <td>$$</td>
      <td>Ok</td>
    </tr>
    <tr>
      <th>27</th>
      <td>12.69</td>
      <td>2.00</td>
      <td>Male</td>
      <td>No</td>
      <td>Sat</td>
      <td>Dinner</td>
      <td>2</td>
      <td>6.34</td>
      <td>Patrick Barber</td>
      <td>30155551880343</td>
      <td>Sat394</td>
      <td>0343</td>
      <td>$$</td>
      <td>Ok</td>
    </tr>
    <tr>
      <th>29</th>
      <td>19.65</td>
      <td>3.00</td>
      <td>Female</td>
      <td>No</td>
      <td>Sat</td>
      <td>Dinner</td>
      <td>2</td>
      <td>9.82</td>
      <td>Melinda Murphy</td>
      <td>5489272944576051</td>
      <td>Sat2467</td>
      <td>6051</td>
      <td>$$</td>
      <td>Ok</td>
    </tr>
    <tr>
      <th>31</th>
      <td>18.35</td>
      <td>2.50</td>
      <td>Male</td>
      <td>No</td>
      <td>Sat</td>
      <td>Dinner</td>
      <td>4</td>
      <td>4.59</td>
      <td>Danny Santiago</td>
      <td>630415546013</td>
      <td>Sat4947</td>
      <td>6013</td>
      <td>$$</td>
      <td>Ok</td>
    </tr>
    <tr>
      <th>32</th>
      <td>15.06</td>
      <td>3.00</td>
      <td>Female</td>
      <td>No</td>
      <td>Sat</td>
      <td>Dinner</td>
      <td>2</td>
      <td>7.53</td>
      <td>Amanda Wilson</td>
      <td>213186304291560</td>
      <td>Sat1327</td>
      <td>1560</td>
      <td>$$</td>
      <td>Ok</td>
    </tr>
    <tr>
      <th>34</th>
      <td>17.78</td>
      <td>3.27</td>
      <td>Male</td>
      <td>No</td>
      <td>Sat</td>
      <td>Dinner</td>
      <td>2</td>
      <td>8.89</td>
      <td>Jacob Castillo</td>
      <td>3551492000704805</td>
      <td>Sat8124</td>
      <td>4805</td>
      <td>$$</td>
      <td>Ok</td>
    </tr>
    <tr>
      <th>36</th>
      <td>16.31</td>
      <td>2.00</td>
      <td>Male</td>
      <td>No</td>
      <td>Sat</td>
      <td>Dinner</td>
      <td>3</td>
      <td>5.44</td>
      <td>William Ford</td>
      <td>3527691170179398</td>
      <td>Sat9139</td>
      <td>9398</td>
      <td>$$</td>
      <td>Ok</td>
    </tr>
    <tr>
      <th>37</th>
      <td>16.93</td>
      <td>3.07</td>
      <td>Female</td>
      <td>No</td>
      <td>Sat</td>
      <td>Dinner</td>
      <td>3</td>
      <td>5.64</td>
      <td>Erin Lewis</td>
      <td>5161695527390786</td>
      <td>Sat6406</td>
      <td>0786</td>
      <td>$$</td>
      <td>Ok</td>
    </tr>
    <tr>
      <th>38</th>
      <td>18.69</td>
      <td>2.31</td>
      <td>Male</td>
      <td>No</td>
      <td>Sat</td>
      <td>Dinner</td>
      <td>3</td>
      <td>6.23</td>
      <td>Brandon Bradley</td>
      <td>4427601595688633</td>
      <td>Sat4056</td>
      <td>8633</td>
      <td>$$</td>
      <td>Ok</td>
    </tr>
    <tr>
      <th>40</th>
      <td>16.04</td>
      <td>2.24</td>
      <td>Male</td>
      <td>No</td>
      <td>Sat</td>
      <td>Dinner</td>
      <td>3</td>
      <td>5.35</td>
      <td>Adam Edwards</td>
      <td>3544447755679420</td>
      <td>Sat8549</td>
      <td>9420</td>
      <td>$$</td>
      <td>Ok</td>
    </tr>
    <tr>
      <th>41</th>
      <td>17.46</td>
      <td>2.54</td>
      <td>Male</td>
      <td>No</td>
      <td>Sun</td>
      <td>Dinner</td>
      <td>2</td>
      <td>8.73</td>
      <td>David Boyer</td>
      <td>3536678244278149</td>
      <td>Sun9460</td>
      <td>8149</td>
      <td>$$</td>
      <td>Ok</td>
    </tr>
    <tr>
      <th>42</th>
      <td>13.94</td>
      <td>3.06</td>
      <td>Male</td>
      <td>No</td>
      <td>Sun</td>
      <td>Dinner</td>
      <td>2</td>
      <td>6.97</td>
      <td>Bryan Brown</td>
      <td>36231182760859</td>
      <td>Sun1699</td>
      <td>0859</td>
      <td>$$</td>
      <td>Ok</td>
    </tr>
    <tr>
      <th>45</th>
      <td>18.29</td>
      <td>3.00</td>
      <td>Male</td>
      <td>No</td>
      <td>Sun</td>
      <td>Dinner</td>
      <td>2</td>
      <td>9.14</td>
      <td>Richard Fitzgerald</td>
      <td>375156610762053</td>
      <td>Sun8643</td>
      <td>2053</td>
      <td>$$</td>
      <td>Ok</td>
    </tr>
    <tr>
      <th>49</th>
      <td>18.04</td>
      <td>3.00</td>
      <td>Male</td>
      <td>No</td>
      <td>Sun</td>
      <td>Dinner</td>
      <td>2</td>
      <td>9.02</td>
      <td>William Roth</td>
      <td>6573923967142503</td>
      <td>Sun9774</td>
      <td>2503</td>
      <td>$$</td>
      <td>Ok</td>
    </tr>
    <tr>
      <th>50</th>
      <td>12.54</td>
      <td>2.50</td>
      <td>Male</td>
      <td>No</td>
      <td>Sun</td>
      <td>Dinner</td>
      <td>2</td>
      <td>6.27</td>
      <td>Jeremiah Neal</td>
      <td>2225400829691416</td>
      <td>Sun2021</td>
      <td>1416</td>
      <td>$$</td>
      <td>Ok</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>191</th>
      <td>19.81</td>
      <td>4.19</td>
      <td>Female</td>
      <td>Yes</td>
      <td>Thur</td>
      <td>Lunch</td>
      <td>2</td>
      <td>9.90</td>
      <td>Kristy Boyd</td>
      <td>4317015327600068</td>
      <td>Thur967</td>
      <td>0068</td>
      <td>$$</td>
      <td>Ok</td>
    </tr>
    <tr>
      <th>193</th>
      <td>15.48</td>
      <td>2.02</td>
      <td>Male</td>
      <td>Yes</td>
      <td>Thur</td>
      <td>Lunch</td>
      <td>2</td>
      <td>7.74</td>
      <td>Raymond Sullivan</td>
      <td>180068856139315</td>
      <td>Thur606</td>
      <td>9315</td>
      <td>$$</td>
      <td>Ok</td>
    </tr>
    <tr>
      <th>194</th>
      <td>16.58</td>
      <td>4.00</td>
      <td>Male</td>
      <td>Yes</td>
      <td>Thur</td>
      <td>Lunch</td>
      <td>2</td>
      <td>8.29</td>
      <td>Benjamin Weber</td>
      <td>676210011505</td>
      <td>Thur9318</td>
      <td>1505</td>
      <td>$$</td>
      <td>Ok</td>
    </tr>
    <tr>
      <th>196</th>
      <td>10.34</td>
      <td>2.00</td>
      <td>Male</td>
      <td>Yes</td>
      <td>Thur</td>
      <td>Lunch</td>
      <td>2</td>
      <td>5.17</td>
      <td>Eric Martin</td>
      <td>30442491190342</td>
      <td>Thur9862</td>
      <td>0342</td>
      <td>$$</td>
      <td>Ok</td>
    </tr>
    <tr>
      <th>198</th>
      <td>13.00</td>
      <td>2.00</td>
      <td>Female</td>
      <td>Yes</td>
      <td>Thur</td>
      <td>Lunch</td>
      <td>2</td>
      <td>6.50</td>
      <td>Katherine Bond</td>
      <td>4926725945192</td>
      <td>Thur437</td>
      <td>5192</td>
      <td>$$</td>
      <td>Ok</td>
    </tr>
    <tr>
      <th>199</th>
      <td>13.51</td>
      <td>2.00</td>
      <td>Male</td>
      <td>Yes</td>
      <td>Thur</td>
      <td>Lunch</td>
      <td>2</td>
      <td>6.76</td>
      <td>Joseph Murphy MD</td>
      <td>6547218923471275</td>
      <td>Thur2428</td>
      <td>1275</td>
      <td>$$</td>
      <td>Ok</td>
    </tr>
    <tr>
      <th>200</th>
      <td>18.71</td>
      <td>4.00</td>
      <td>Male</td>
      <td>Yes</td>
      <td>Thur</td>
      <td>Lunch</td>
      <td>3</td>
      <td>6.24</td>
      <td>Jason Conrad</td>
      <td>4581233003487</td>
      <td>Thur6048</td>
      <td>3487</td>
      <td>$$</td>
      <td>Ok</td>
    </tr>
    <tr>
      <th>201</th>
      <td>12.74</td>
      <td>2.01</td>
      <td>Female</td>
      <td>Yes</td>
      <td>Thur</td>
      <td>Lunch</td>
      <td>2</td>
      <td>6.37</td>
      <td>Abigail Parks</td>
      <td>3586645396220590</td>
      <td>Thur2544</td>
      <td>0590</td>
      <td>$$</td>
      <td>Ok</td>
    </tr>
    <tr>
      <th>202</th>
      <td>13.00</td>
      <td>2.00</td>
      <td>Female</td>
      <td>Yes</td>
      <td>Thur</td>
      <td>Lunch</td>
      <td>2</td>
      <td>6.50</td>
      <td>Ashley Shaw</td>
      <td>180088043008041</td>
      <td>Thur1301</td>
      <td>8041</td>
      <td>$$</td>
      <td>Ok</td>
    </tr>
    <tr>
      <th>203</th>
      <td>16.40</td>
      <td>2.50</td>
      <td>Female</td>
      <td>Yes</td>
      <td>Thur</td>
      <td>Lunch</td>
      <td>2</td>
      <td>8.20</td>
      <td>Toni Brooks</td>
      <td>3582289985920239</td>
      <td>Thur7770</td>
      <td>0239</td>
      <td>$$</td>
      <td>Ok</td>
    </tr>
    <tr>
      <th>205</th>
      <td>16.47</td>
      <td>3.23</td>
      <td>Female</td>
      <td>Yes</td>
      <td>Thur</td>
      <td>Lunch</td>
      <td>3</td>
      <td>5.49</td>
      <td>Carly Reyes</td>
      <td>4787787236486</td>
      <td>Thur8084</td>
      <td>6486</td>
      <td>$$</td>
      <td>Ok</td>
    </tr>
    <tr>
      <th>209</th>
      <td>12.76</td>
      <td>2.23</td>
      <td>Female</td>
      <td>Yes</td>
      <td>Sat</td>
      <td>Dinner</td>
      <td>2</td>
      <td>6.38</td>
      <td>Sarah Cunningham</td>
      <td>341876516331163</td>
      <td>Sat1274</td>
      <td>1163</td>
      <td>$$</td>
      <td>Ok</td>
    </tr>
    <tr>
      <th>213</th>
      <td>13.27</td>
      <td>2.50</td>
      <td>Female</td>
      <td>Yes</td>
      <td>Sat</td>
      <td>Dinner</td>
      <td>2</td>
      <td>6.64</td>
      <td>Robin Andersen</td>
      <td>580140531089</td>
      <td>Sat1374</td>
      <td>1089</td>
      <td>$$</td>
      <td>Ok</td>
    </tr>
    <tr>
      <th>215</th>
      <td>12.90</td>
      <td>1.10</td>
      <td>Female</td>
      <td>Yes</td>
      <td>Sat</td>
      <td>Dinner</td>
      <td>2</td>
      <td>6.45</td>
      <td>Jessica Owen</td>
      <td>4726904879471</td>
      <td>Sat6983</td>
      <td>9471</td>
      <td>$$</td>
      <td>Ok</td>
    </tr>
    <tr>
      <th>217</th>
      <td>11.59</td>
      <td>1.50</td>
      <td>Male</td>
      <td>Yes</td>
      <td>Sat</td>
      <td>Dinner</td>
      <td>2</td>
      <td>5.80</td>
      <td>Gary Orr</td>
      <td>30324521283406</td>
      <td>Sat8489</td>
      <td>3406</td>
      <td>$$</td>
      <td>Ok</td>
    </tr>
    <tr>
      <th>220</th>
      <td>12.16</td>
      <td>2.20</td>
      <td>Male</td>
      <td>Yes</td>
      <td>Fri</td>
      <td>Lunch</td>
      <td>2</td>
      <td>6.08</td>
      <td>Ricky Johnson</td>
      <td>213109508670736</td>
      <td>Fri4607</td>
      <td>0736</td>
      <td>$$</td>
      <td>Ok</td>
    </tr>
    <tr>
      <th>221</th>
      <td>13.42</td>
      <td>3.48</td>
      <td>Female</td>
      <td>Yes</td>
      <td>Fri</td>
      <td>Lunch</td>
      <td>2</td>
      <td>6.71</td>
      <td>Leslie Kaufman</td>
      <td>379437981958785</td>
      <td>Fri7511</td>
      <td>8785</td>
      <td>$$</td>
      <td>Generous</td>
    </tr>
    <tr>
      <th>223</th>
      <td>15.98</td>
      <td>3.00</td>
      <td>Female</td>
      <td>No</td>
      <td>Fri</td>
      <td>Lunch</td>
      <td>3</td>
      <td>5.33</td>
      <td>Mary Rivera</td>
      <td>5343428579353069</td>
      <td>Fri6014</td>
      <td>3069</td>
      <td>$$</td>
      <td>Ok</td>
    </tr>
    <tr>
      <th>224</th>
      <td>13.42</td>
      <td>1.58</td>
      <td>Male</td>
      <td>Yes</td>
      <td>Fri</td>
      <td>Lunch</td>
      <td>2</td>
      <td>6.71</td>
      <td>Ronald Vaughn DVM</td>
      <td>341503466406403</td>
      <td>Fri5959</td>
      <td>6403</td>
      <td>$$</td>
      <td>Ok</td>
    </tr>
    <tr>
      <th>225</th>
      <td>16.27</td>
      <td>2.50</td>
      <td>Female</td>
      <td>Yes</td>
      <td>Fri</td>
      <td>Lunch</td>
      <td>2</td>
      <td>8.14</td>
      <td>Whitney Arnold</td>
      <td>3579111947217428</td>
      <td>Fri6665</td>
      <td>7428</td>
      <td>$$</td>
      <td>Ok</td>
    </tr>
    <tr>
      <th>226</th>
      <td>10.09</td>
      <td>2.00</td>
      <td>Female</td>
      <td>Yes</td>
      <td>Fri</td>
      <td>Lunch</td>
      <td>2</td>
      <td>5.04</td>
      <td>Ruth Weiss</td>
      <td>5268689490381635</td>
      <td>Fri6359</td>
      <td>1635</td>
      <td>$$</td>
      <td>Ok</td>
    </tr>
    <tr>
      <th>228</th>
      <td>13.28</td>
      <td>2.72</td>
      <td>Male</td>
      <td>No</td>
      <td>Sat</td>
      <td>Dinner</td>
      <td>2</td>
      <td>6.64</td>
      <td>Glenn Jones</td>
      <td>502061651712</td>
      <td>Sat2937</td>
      <td>1712</td>
      <td>$$</td>
      <td>Ok</td>
    </tr>
    <tr>
      <th>231</th>
      <td>15.69</td>
      <td>3.00</td>
      <td>Male</td>
      <td>Yes</td>
      <td>Sat</td>
      <td>Dinner</td>
      <td>3</td>
      <td>5.23</td>
      <td>Jason Parks</td>
      <td>4812333796161</td>
      <td>Sat6334</td>
      <td>6161</td>
      <td>$$</td>
      <td>Ok</td>
    </tr>
    <tr>
      <th>232</th>
      <td>11.61</td>
      <td>3.39</td>
      <td>Male</td>
      <td>No</td>
      <td>Sat</td>
      <td>Dinner</td>
      <td>2</td>
      <td>5.80</td>
      <td>James Taylor</td>
      <td>6011482917327995</td>
      <td>Sat2124</td>
      <td>7995</td>
      <td>$$</td>
      <td>Generous</td>
    </tr>
    <tr>
      <th>233</th>
      <td>10.77</td>
      <td>1.47</td>
      <td>Male</td>
      <td>No</td>
      <td>Sat</td>
      <td>Dinner</td>
      <td>2</td>
      <td>5.38</td>
      <td>Paul Novak</td>
      <td>6011698897610858</td>
      <td>Sat1467</td>
      <td>0858</td>
      <td>$$</td>
      <td>Ok</td>
    </tr>
    <tr>
      <th>234</th>
      <td>15.53</td>
      <td>3.00</td>
      <td>Male</td>
      <td>Yes</td>
      <td>Sat</td>
      <td>Dinner</td>
      <td>2</td>
      <td>7.76</td>
      <td>Tracy Douglas</td>
      <td>4097938155941930</td>
      <td>Sat7220</td>
      <td>1930</td>
      <td>$$</td>
      <td>Ok</td>
    </tr>
    <tr>
      <th>235</th>
      <td>10.07</td>
      <td>1.25</td>
      <td>Male</td>
      <td>No</td>
      <td>Sat</td>
      <td>Dinner</td>
      <td>2</td>
      <td>5.04</td>
      <td>Sean Gonzalez</td>
      <td>3534021246117605</td>
      <td>Sat4615</td>
      <td>7605</td>
      <td>$$</td>
      <td>Ok</td>
    </tr>
    <tr>
      <th>236</th>
      <td>12.60</td>
      <td>1.00</td>
      <td>Male</td>
      <td>Yes</td>
      <td>Sat</td>
      <td>Dinner</td>
      <td>2</td>
      <td>6.30</td>
      <td>Matthew Myers</td>
      <td>3543676378973965</td>
      <td>Sat5032</td>
      <td>3965</td>
      <td>$$</td>
      <td>Ok</td>
    </tr>
    <tr>
      <th>242</th>
      <td>17.82</td>
      <td>1.75</td>
      <td>Male</td>
      <td>No</td>
      <td>Sat</td>
      <td>Dinner</td>
      <td>2</td>
      <td>8.91</td>
      <td>Dennis Dixon</td>
      <td>4375220550950</td>
      <td>Sat17</td>
      <td>0950</td>
      <td>$$</td>
      <td>Ok</td>
    </tr>
    <tr>
      <th>243</th>
      <td>18.78</td>
      <td>3.00</td>
      <td>Female</td>
      <td>No</td>
      <td>Thur</td>
      <td>Dinner</td>
      <td>2</td>
      <td>9.39</td>
      <td>Michelle Hardin</td>
      <td>3511451626698139</td>
      <td>Thur672</td>
      <td>8139</td>
      <td>$$</td>
      <td>Ok</td>
    </tr>
  </tbody>
</table>
<p>130 rows × 14 columns</p>
</div>



<a id='sample'></a>
## sample


```python
df.sample(5)
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
      <th>total_bill</th>
      <th>tip</th>
      <th>sex</th>
      <th>smoker</th>
      <th>day</th>
      <th>time</th>
      <th>size</th>
      <th>price_per_person</th>
      <th>Payer Name</th>
      <th>CC Number</th>
      <th>Payment ID</th>
      <th>last_four</th>
      <th>Expensive</th>
      <th>Tip Quality</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>216</th>
      <td>28.15</td>
      <td>3.00</td>
      <td>Male</td>
      <td>Yes</td>
      <td>Sat</td>
      <td>Dinner</td>
      <td>5</td>
      <td>5.63</td>
      <td>Shawn Barnett PhD</td>
      <td>4590982568244</td>
      <td>Sat7320</td>
      <td>8244</td>
      <td>$$</td>
      <td>Ok</td>
    </tr>
    <tr>
      <th>136</th>
      <td>10.33</td>
      <td>2.00</td>
      <td>Female</td>
      <td>No</td>
      <td>Thur</td>
      <td>Lunch</td>
      <td>2</td>
      <td>5.16</td>
      <td>Donna Kelly</td>
      <td>180048553626376</td>
      <td>Thur1393</td>
      <td>6376</td>
      <td>$$</td>
      <td>Ok</td>
    </tr>
    <tr>
      <th>13</th>
      <td>18.43</td>
      <td>3.00</td>
      <td>Male</td>
      <td>No</td>
      <td>Sun</td>
      <td>Dinner</td>
      <td>4</td>
      <td>4.61</td>
      <td>Joshua Jones</td>
      <td>6011163105616890</td>
      <td>Sun2971</td>
      <td>6890</td>
      <td>$$</td>
      <td>Ok</td>
    </tr>
    <tr>
      <th>146</th>
      <td>18.64</td>
      <td>1.36</td>
      <td>Female</td>
      <td>No</td>
      <td>Thur</td>
      <td>Lunch</td>
      <td>3</td>
      <td>6.21</td>
      <td>Kelly Estrada</td>
      <td>60463302327</td>
      <td>Thur3941</td>
      <td>2327</td>
      <td>$$</td>
      <td>Ok</td>
    </tr>
    <tr>
      <th>56</th>
      <td>38.01</td>
      <td>3.00</td>
      <td>Male</td>
      <td>Yes</td>
      <td>Sat</td>
      <td>Dinner</td>
      <td>4</td>
      <td>9.50</td>
      <td>James Christensen DDS</td>
      <td>349793629453226</td>
      <td>Sat8903</td>
      <td>3226</td>
      <td>$$$</td>
      <td>Ok</td>
    </tr>
  </tbody>
</table>
</div>




```python
df.sample(frac=0.1)
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
      <th>total_bill</th>
      <th>tip</th>
      <th>sex</th>
      <th>smoker</th>
      <th>day</th>
      <th>time</th>
      <th>size</th>
      <th>price_per_person</th>
      <th>Payer Name</th>
      <th>CC Number</th>
      <th>Payment ID</th>
      <th>last_four</th>
      <th>Expensive</th>
      <th>Tip Quality</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>73</th>
      <td>25.28</td>
      <td>5.00</td>
      <td>Female</td>
      <td>Yes</td>
      <td>Sat</td>
      <td>Dinner</td>
      <td>2</td>
      <td>12.64</td>
      <td>Julie Holmes</td>
      <td>5418689346409571</td>
      <td>Sat6065</td>
      <td>9571</td>
      <td>$$</td>
      <td>Ok</td>
    </tr>
    <tr>
      <th>141</th>
      <td>34.30</td>
      <td>6.70</td>
      <td>Male</td>
      <td>No</td>
      <td>Thur</td>
      <td>Lunch</td>
      <td>6</td>
      <td>5.72</td>
      <td>Steven Carlson</td>
      <td>3526515703718508</td>
      <td>Thur1025</td>
      <td>8508</td>
      <td>$$$</td>
      <td>Ok</td>
    </tr>
    <tr>
      <th>239</th>
      <td>29.03</td>
      <td>5.92</td>
      <td>Male</td>
      <td>No</td>
      <td>Sat</td>
      <td>Dinner</td>
      <td>3</td>
      <td>9.68</td>
      <td>Michael Avila</td>
      <td>5296068606052842</td>
      <td>Sat2657</td>
      <td>2842</td>
      <td>$$</td>
      <td>Ok</td>
    </tr>
    <tr>
      <th>237</th>
      <td>32.83</td>
      <td>1.17</td>
      <td>Male</td>
      <td>Yes</td>
      <td>Sat</td>
      <td>Dinner</td>
      <td>2</td>
      <td>16.42</td>
      <td>Thomas Brown</td>
      <td>4284722681265508</td>
      <td>Sat2929</td>
      <td>5508</td>
      <td>$$$</td>
      <td>Ok</td>
    </tr>
    <tr>
      <th>69</th>
      <td>15.01</td>
      <td>2.09</td>
      <td>Male</td>
      <td>Yes</td>
      <td>Sat</td>
      <td>Dinner</td>
      <td>2</td>
      <td>7.50</td>
      <td>Adam Hall</td>
      <td>4700924377057571</td>
      <td>Sat855</td>
      <td>7571</td>
      <td>$$</td>
      <td>Ok</td>
    </tr>
    <tr>
      <th>108</th>
      <td>18.24</td>
      <td>3.76</td>
      <td>Male</td>
      <td>No</td>
      <td>Sat</td>
      <td>Dinner</td>
      <td>2</td>
      <td>9.12</td>
      <td>Steven Grant</td>
      <td>4112810433473856</td>
      <td>Sat6376</td>
      <td>3856</td>
      <td>$$</td>
      <td>Ok</td>
    </tr>
    <tr>
      <th>85</th>
      <td>34.83</td>
      <td>5.17</td>
      <td>Female</td>
      <td>No</td>
      <td>Thur</td>
      <td>Lunch</td>
      <td>4</td>
      <td>8.71</td>
      <td>Shawna Cook</td>
      <td>6011787464177340</td>
      <td>Thur7972</td>
      <td>7340</td>
      <td>$$$</td>
      <td>Ok</td>
    </tr>
    <tr>
      <th>156</th>
      <td>48.17</td>
      <td>5.00</td>
      <td>Male</td>
      <td>No</td>
      <td>Sun</td>
      <td>Dinner</td>
      <td>6</td>
      <td>8.03</td>
      <td>Ryan Gonzales</td>
      <td>3523151482063321</td>
      <td>Sun7518</td>
      <td>3321</td>
      <td>$$$</td>
      <td>Ok</td>
    </tr>
    <tr>
      <th>196</th>
      <td>10.34</td>
      <td>2.00</td>
      <td>Male</td>
      <td>Yes</td>
      <td>Thur</td>
      <td>Lunch</td>
      <td>2</td>
      <td>5.17</td>
      <td>Eric Martin</td>
      <td>30442491190342</td>
      <td>Thur9862</td>
      <td>0342</td>
      <td>$$</td>
      <td>Ok</td>
    </tr>
    <tr>
      <th>41</th>
      <td>17.46</td>
      <td>2.54</td>
      <td>Male</td>
      <td>No</td>
      <td>Sun</td>
      <td>Dinner</td>
      <td>2</td>
      <td>8.73</td>
      <td>David Boyer</td>
      <td>3536678244278149</td>
      <td>Sun9460</td>
      <td>8149</td>
      <td>$$</td>
      <td>Ok</td>
    </tr>
    <tr>
      <th>236</th>
      <td>12.60</td>
      <td>1.00</td>
      <td>Male</td>
      <td>Yes</td>
      <td>Sat</td>
      <td>Dinner</td>
      <td>2</td>
      <td>6.30</td>
      <td>Matthew Myers</td>
      <td>3543676378973965</td>
      <td>Sat5032</td>
      <td>3965</td>
      <td>$$</td>
      <td>Ok</td>
    </tr>
    <tr>
      <th>225</th>
      <td>16.27</td>
      <td>2.50</td>
      <td>Female</td>
      <td>Yes</td>
      <td>Fri</td>
      <td>Lunch</td>
      <td>2</td>
      <td>8.14</td>
      <td>Whitney Arnold</td>
      <td>3579111947217428</td>
      <td>Fri6665</td>
      <td>7428</td>
      <td>$$</td>
      <td>Ok</td>
    </tr>
    <tr>
      <th>61</th>
      <td>13.81</td>
      <td>2.00</td>
      <td>Male</td>
      <td>Yes</td>
      <td>Sat</td>
      <td>Dinner</td>
      <td>2</td>
      <td>6.90</td>
      <td>Ryan Hernandez</td>
      <td>4766834726806</td>
      <td>Sat3030</td>
      <td>6806</td>
      <td>$$</td>
      <td>Ok</td>
    </tr>
    <tr>
      <th>203</th>
      <td>16.40</td>
      <td>2.50</td>
      <td>Female</td>
      <td>Yes</td>
      <td>Thur</td>
      <td>Lunch</td>
      <td>2</td>
      <td>8.20</td>
      <td>Toni Brooks</td>
      <td>3582289985920239</td>
      <td>Thur7770</td>
      <td>0239</td>
      <td>$$</td>
      <td>Ok</td>
    </tr>
    <tr>
      <th>5</th>
      <td>25.29</td>
      <td>4.71</td>
      <td>Male</td>
      <td>No</td>
      <td>Sun</td>
      <td>Dinner</td>
      <td>4</td>
      <td>6.32</td>
      <td>Erik Smith</td>
      <td>213140353657882</td>
      <td>Sun9679</td>
      <td>7882</td>
      <td>$$</td>
      <td>Ok</td>
    </tr>
    <tr>
      <th>220</th>
      <td>12.16</td>
      <td>2.20</td>
      <td>Male</td>
      <td>Yes</td>
      <td>Fri</td>
      <td>Lunch</td>
      <td>2</td>
      <td>6.08</td>
      <td>Ricky Johnson</td>
      <td>213109508670736</td>
      <td>Fri4607</td>
      <td>0736</td>
      <td>$$</td>
      <td>Ok</td>
    </tr>
    <tr>
      <th>119</th>
      <td>24.08</td>
      <td>2.92</td>
      <td>Female</td>
      <td>No</td>
      <td>Thur</td>
      <td>Lunch</td>
      <td>4</td>
      <td>6.02</td>
      <td>Melanie Jordan</td>
      <td>676212062720</td>
      <td>Thur8063</td>
      <td>2720</td>
      <td>$$</td>
      <td>Ok</td>
    </tr>
    <tr>
      <th>96</th>
      <td>27.28</td>
      <td>4.00</td>
      <td>Male</td>
      <td>Yes</td>
      <td>Fri</td>
      <td>Dinner</td>
      <td>2</td>
      <td>13.64</td>
      <td>Eric Carter</td>
      <td>4563054452787961</td>
      <td>Fri3159</td>
      <td>7961</td>
      <td>$$</td>
      <td>Ok</td>
    </tr>
    <tr>
      <th>159</th>
      <td>16.49</td>
      <td>2.00</td>
      <td>Male</td>
      <td>No</td>
      <td>Sun</td>
      <td>Dinner</td>
      <td>4</td>
      <td>4.12</td>
      <td>Christopher Soto</td>
      <td>30501814271434</td>
      <td>Sun1781</td>
      <td>1434</td>
      <td>$$</td>
      <td>Ok</td>
    </tr>
    <tr>
      <th>26</th>
      <td>13.37</td>
      <td>2.00</td>
      <td>Male</td>
      <td>No</td>
      <td>Sat</td>
      <td>Dinner</td>
      <td>2</td>
      <td>6.68</td>
      <td>Kyle Avery</td>
      <td>6531339539615499</td>
      <td>Sat6651</td>
      <td>5499</td>
      <td>$$</td>
      <td>Ok</td>
    </tr>
    <tr>
      <th>129</th>
      <td>22.82</td>
      <td>2.18</td>
      <td>Male</td>
      <td>No</td>
      <td>Thur</td>
      <td>Lunch</td>
      <td>3</td>
      <td>7.61</td>
      <td>Raymond Torres</td>
      <td>4855776744024</td>
      <td>Thur9424</td>
      <td>4024</td>
      <td>$$</td>
      <td>Ok</td>
    </tr>
    <tr>
      <th>21</th>
      <td>20.29</td>
      <td>2.75</td>
      <td>Female</td>
      <td>No</td>
      <td>Sat</td>
      <td>Dinner</td>
      <td>2</td>
      <td>10.14</td>
      <td>Natalie Gardner</td>
      <td>5448125351489749</td>
      <td>Sat9618</td>
      <td>9749</td>
      <td>$$</td>
      <td>Ok</td>
    </tr>
    <tr>
      <th>94</th>
      <td>22.75</td>
      <td>3.25</td>
      <td>Female</td>
      <td>No</td>
      <td>Fri</td>
      <td>Dinner</td>
      <td>2</td>
      <td>11.38</td>
      <td>Jamie Garza</td>
      <td>676318332068</td>
      <td>Fri2318</td>
      <td>2068</td>
      <td>$$</td>
      <td>Ok</td>
    </tr>
    <tr>
      <th>39</th>
      <td>31.27</td>
      <td>5.00</td>
      <td>Male</td>
      <td>No</td>
      <td>Sat</td>
      <td>Dinner</td>
      <td>3</td>
      <td>10.42</td>
      <td>Mr. Brandon Berry</td>
      <td>6011525851069856</td>
      <td>Sat6373</td>
      <td>9856</td>
      <td>$$$</td>
      <td>Ok</td>
    </tr>
  </tbody>
</table>
</div>



<a id='n'></a>
## nlargest and nsmallest


```python
df.nlargest(10,'tip')
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
      <th>total_bill</th>
      <th>tip</th>
      <th>sex</th>
      <th>smoker</th>
      <th>day</th>
      <th>time</th>
      <th>size</th>
      <th>price_per_person</th>
      <th>Payer Name</th>
      <th>CC Number</th>
      <th>Payment ID</th>
      <th>last_four</th>
      <th>Expensive</th>
      <th>Tip Quality</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>170</th>
      <td>50.81</td>
      <td>10.00</td>
      <td>Male</td>
      <td>Yes</td>
      <td>Sat</td>
      <td>Dinner</td>
      <td>3</td>
      <td>16.94</td>
      <td>Gregory Clark</td>
      <td>5473850968388236</td>
      <td>Sat1954</td>
      <td>8236</td>
      <td>$$$</td>
      <td>Ok</td>
    </tr>
    <tr>
      <th>212</th>
      <td>48.33</td>
      <td>9.00</td>
      <td>Male</td>
      <td>No</td>
      <td>Sat</td>
      <td>Dinner</td>
      <td>4</td>
      <td>12.08</td>
      <td>Alex Williamson</td>
      <td>676218815212</td>
      <td>Sat4590</td>
      <td>5212</td>
      <td>$$$</td>
      <td>Ok</td>
    </tr>
    <tr>
      <th>23</th>
      <td>39.42</td>
      <td>7.58</td>
      <td>Male</td>
      <td>No</td>
      <td>Sat</td>
      <td>Dinner</td>
      <td>4</td>
      <td>9.86</td>
      <td>Lance Peterson</td>
      <td>3542584061609808</td>
      <td>Sat239</td>
      <td>9808</td>
      <td>$$$</td>
      <td>Ok</td>
    </tr>
    <tr>
      <th>59</th>
      <td>48.27</td>
      <td>6.73</td>
      <td>Male</td>
      <td>No</td>
      <td>Sat</td>
      <td>Dinner</td>
      <td>4</td>
      <td>12.07</td>
      <td>Brian Ortiz</td>
      <td>6596453823950595</td>
      <td>Sat8139</td>
      <td>0595</td>
      <td>$$$</td>
      <td>Ok</td>
    </tr>
    <tr>
      <th>141</th>
      <td>34.30</td>
      <td>6.70</td>
      <td>Male</td>
      <td>No</td>
      <td>Thur</td>
      <td>Lunch</td>
      <td>6</td>
      <td>5.72</td>
      <td>Steven Carlson</td>
      <td>3526515703718508</td>
      <td>Thur1025</td>
      <td>8508</td>
      <td>$$$</td>
      <td>Ok</td>
    </tr>
    <tr>
      <th>183</th>
      <td>23.17</td>
      <td>6.50</td>
      <td>Male</td>
      <td>Yes</td>
      <td>Sun</td>
      <td>Dinner</td>
      <td>4</td>
      <td>5.79</td>
      <td>Dr. Michael James</td>
      <td>4718501859162</td>
      <td>Sun6059</td>
      <td>9162</td>
      <td>$$</td>
      <td>Generous</td>
    </tr>
    <tr>
      <th>214</th>
      <td>28.17</td>
      <td>6.50</td>
      <td>Female</td>
      <td>Yes</td>
      <td>Sat</td>
      <td>Dinner</td>
      <td>3</td>
      <td>9.39</td>
      <td>Marissa Jackson</td>
      <td>4922302538691962</td>
      <td>Sat3374</td>
      <td>1962</td>
      <td>$$</td>
      <td>Ok</td>
    </tr>
    <tr>
      <th>47</th>
      <td>32.40</td>
      <td>6.00</td>
      <td>Male</td>
      <td>No</td>
      <td>Sun</td>
      <td>Dinner</td>
      <td>4</td>
      <td>8.10</td>
      <td>James Barnes</td>
      <td>3552002592874186</td>
      <td>Sun9677</td>
      <td>4186</td>
      <td>$$$</td>
      <td>Ok</td>
    </tr>
    <tr>
      <th>239</th>
      <td>29.03</td>
      <td>5.92</td>
      <td>Male</td>
      <td>No</td>
      <td>Sat</td>
      <td>Dinner</td>
      <td>3</td>
      <td>9.68</td>
      <td>Michael Avila</td>
      <td>5296068606052842</td>
      <td>Sat2657</td>
      <td>2842</td>
      <td>$$</td>
      <td>Ok</td>
    </tr>
    <tr>
      <th>88</th>
      <td>24.71</td>
      <td>5.85</td>
      <td>Male</td>
      <td>No</td>
      <td>Thur</td>
      <td>Lunch</td>
      <td>2</td>
      <td>12.36</td>
      <td>Roger Taylor</td>
      <td>4410248629955</td>
      <td>Thur9003</td>
      <td>9955</td>
      <td>$$</td>
      <td>Ok</td>
    </tr>
  </tbody>
</table>
</div>



----
