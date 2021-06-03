<h1>Table of Contents<span class="tocSkip"></span></h1>
<div class="toc"><ul class="toc-item"><li><span><a href="#Groupby-Operations-and-Multi-level-Index" data-toc-modified-id="Groupby-Operations-and-Multi-level-Index-1"><span class="toc-item-num">1&nbsp;&nbsp;</span>Groupby Operations and Multi-level Index</a></span><ul class="toc-item"><li><span><a href="#Data" data-toc-modified-id="Data-1.1"><span class="toc-item-num">1.1&nbsp;&nbsp;</span>Data</a></span></li><li><span><a href="#groupby()-method" data-toc-modified-id="groupby()-method-1.2"><span class="toc-item-num">1.2&nbsp;&nbsp;</span>groupby() method</a></span><ul class="toc-item"><li><ul class="toc-item"><li><span><a href="#Adding-an-aggregate-method-call.-To-use-a-grouped-object,-you-need-to-tell-pandas-how-you-want-to-aggregate-the-data." data-toc-modified-id="Adding-an-aggregate-method-call.-To-use-a-grouped-object,-you-need-to-tell-pandas-how-you-want-to-aggregate-the-data.-1.2.0.1"><span class="toc-item-num">1.2.0.1&nbsp;&nbsp;</span>Adding an aggregate method call. To use a grouped object, you need to tell pandas how you want to aggregate the data.</a></span></li></ul></li></ul></li><li><span><a href="#Groupby-Multiple-Columns" data-toc-modified-id="Groupby-Multiple-Columns-1.3"><span class="toc-item-num">1.3&nbsp;&nbsp;</span>Groupby Multiple Columns</a></span></li></ul></li><li><span><a href="#MultiIndex" data-toc-modified-id="MultiIndex-2"><span class="toc-item-num">2&nbsp;&nbsp;</span>MultiIndex</a></span><ul class="toc-item"><li><span><a href="#The-MultiIndex-Object" data-toc-modified-id="The-MultiIndex-Object-2.1"><span class="toc-item-num">2.1&nbsp;&nbsp;</span>The MultiIndex Object</a></span></li></ul></li><li><span><a href="#Indexing-with-the-Hierarchical-Index" data-toc-modified-id="Indexing-with-the-Hierarchical-Index-3"><span class="toc-item-num">3&nbsp;&nbsp;</span>Indexing with the Hierarchical Index</a></span><ul class="toc-item"><li><span><a href="#Grab-Based-on-Outside-Index" data-toc-modified-id="Grab-Based-on-Outside-Index-3.1"><span class="toc-item-num">3.1&nbsp;&nbsp;</span>Grab Based on Outside Index</a></span></li><li><span><a href="#Grab-a-Single-Row" data-toc-modified-id="Grab-a-Single-Row-3.2"><span class="toc-item-num">3.2&nbsp;&nbsp;</span>Grab a Single Row</a></span></li></ul></li><li><span><a href="#Grab-Based-on-Cross-section-with-.xs()" data-toc-modified-id="Grab-Based-on-Cross-section-with-.xs()-4"><span class="toc-item-num">4&nbsp;&nbsp;</span>Grab Based on Cross-section with .xs()</a></span><ul class="toc-item"><li><span><a href="#Parameters" data-toc-modified-id="Parameters-4.1"><span class="toc-item-num">4.1&nbsp;&nbsp;</span>Parameters</a></span><ul class="toc-item"><li><span><a href="#Careful-note!" data-toc-modified-id="Careful-note!-4.1.1"><span class="toc-item-num">4.1.1&nbsp;&nbsp;</span>Careful note!</a></span></li></ul></li><li><span><a href="#Swap-Levels" data-toc-modified-id="Swap-Levels-4.2"><span class="toc-item-num">4.2&nbsp;&nbsp;</span>Swap Levels</a></span></li><li><span><a href="#Sorting-MultiIndex" data-toc-modified-id="Sorting-MultiIndex-4.3"><span class="toc-item-num">4.3&nbsp;&nbsp;</span>Sorting MultiIndex</a></span></li></ul></li><li><span><a href="#Advanced:-agg()-method" data-toc-modified-id="Advanced:-agg()-method-5"><span class="toc-item-num">5&nbsp;&nbsp;</span>Advanced: agg() method</a></span><ul class="toc-item"><li><span><a href="#agg()-on-a-DataFrame" data-toc-modified-id="agg()-on-a-DataFrame-5.1"><span class="toc-item-num">5.1&nbsp;&nbsp;</span>agg() on a DataFrame</a></span><ul class="toc-item"><li><span><a href="#Specify-aggregate-methods-per-column" data-toc-modified-id="Specify-aggregate-methods-per-column-5.1.1"><span class="toc-item-num">5.1.1&nbsp;&nbsp;</span>Specify aggregate methods per column</a></span></li></ul></li><li><span><a href="#agg()-with-groupby()" data-toc-modified-id="agg()-with-groupby()-5.2"><span class="toc-item-num">5.2&nbsp;&nbsp;</span>agg() with groupby()</a></span></li></ul></li></ul></div>

# Groupby Operations and Multi-level Index


```python
import numpy as np
import pandas as pd
```

## Data


```python
df = pd.read_csv('mpg.csv')
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
      <th>mpg</th>
      <th>cylinders</th>
      <th>displacement</th>
      <th>horsepower</th>
      <th>weight</th>
      <th>acceleration</th>
      <th>model_year</th>
      <th>origin</th>
      <th>name</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>18.0</td>
      <td>8</td>
      <td>307.0</td>
      <td>130</td>
      <td>3504</td>
      <td>12.0</td>
      <td>70</td>
      <td>1</td>
      <td>chevrolet chevelle malibu</td>
    </tr>
    <tr>
      <th>1</th>
      <td>15.0</td>
      <td>8</td>
      <td>350.0</td>
      <td>165</td>
      <td>3693</td>
      <td>11.5</td>
      <td>70</td>
      <td>1</td>
      <td>buick skylark 320</td>
    </tr>
    <tr>
      <th>2</th>
      <td>18.0</td>
      <td>8</td>
      <td>318.0</td>
      <td>150</td>
      <td>3436</td>
      <td>11.0</td>
      <td>70</td>
      <td>1</td>
      <td>plymouth satellite</td>
    </tr>
    <tr>
      <th>3</th>
      <td>16.0</td>
      <td>8</td>
      <td>304.0</td>
      <td>150</td>
      <td>3433</td>
      <td>12.0</td>
      <td>70</td>
      <td>1</td>
      <td>amc rebel sst</td>
    </tr>
    <tr>
      <th>4</th>
      <td>17.0</td>
      <td>8</td>
      <td>302.0</td>
      <td>140</td>
      <td>3449</td>
      <td>10.5</td>
      <td>70</td>
      <td>1</td>
      <td>ford torino</td>
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
    </tr>
    <tr>
      <th>393</th>
      <td>27.0</td>
      <td>4</td>
      <td>140.0</td>
      <td>86</td>
      <td>2790</td>
      <td>15.6</td>
      <td>82</td>
      <td>1</td>
      <td>ford mustang gl</td>
    </tr>
    <tr>
      <th>394</th>
      <td>44.0</td>
      <td>4</td>
      <td>97.0</td>
      <td>52</td>
      <td>2130</td>
      <td>24.6</td>
      <td>82</td>
      <td>2</td>
      <td>vw pickup</td>
    </tr>
    <tr>
      <th>395</th>
      <td>32.0</td>
      <td>4</td>
      <td>135.0</td>
      <td>84</td>
      <td>2295</td>
      <td>11.6</td>
      <td>82</td>
      <td>1</td>
      <td>dodge rampage</td>
    </tr>
    <tr>
      <th>396</th>
      <td>28.0</td>
      <td>4</td>
      <td>120.0</td>
      <td>79</td>
      <td>2625</td>
      <td>18.6</td>
      <td>82</td>
      <td>1</td>
      <td>ford ranger</td>
    </tr>
    <tr>
      <th>397</th>
      <td>31.0</td>
      <td>4</td>
      <td>119.0</td>
      <td>82</td>
      <td>2720</td>
      <td>19.4</td>
      <td>82</td>
      <td>1</td>
      <td>chevy s-10</td>
    </tr>
  </tbody>
</table>
<p>398 rows × 9 columns</p>
</div>



## groupby() method


```python
# Creates a groupby object waiting for an aggregate method
df.groupby('model_year')
```




    <pandas.core.groupby.generic.DataFrameGroupBy object at 0x000002B143697A30>



#### Adding an aggregate method call. To use a grouped object, you need to tell pandas how you want to aggregate the data.

Common Options:

    mean(): Compute mean of groups
    sum(): Compute sum of group values
    size(): Compute group sizes
    count(): Compute count of group
    std(): Standard deviation of groups
    var(): Compute variance of groups
    sem(): Standard error of the mean of groups
    describe(): Generates descriptive statistics
    first(): Compute first of group values
    last(): Compute last of group values
    nth() : Take nth value, or a subset if n is a list
    min(): Compute min of group values
    max(): Compute max of group values
    
Full List at the Online Documentation: https://pandas.pydata.org/docs/reference/groupby.html


```python
# model_year becomes the index! It is NOT a column name,it is now the name of the index
df.groupby('model_year').mean()
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
      <th>mpg</th>
      <th>cylinders</th>
      <th>displacement</th>
      <th>weight</th>
      <th>acceleration</th>
      <th>origin</th>
    </tr>
    <tr>
      <th>model_year</th>
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
      <th>70</th>
      <td>17.689655</td>
      <td>6.758621</td>
      <td>281.413793</td>
      <td>3372.793103</td>
      <td>12.948276</td>
      <td>1.310345</td>
    </tr>
    <tr>
      <th>71</th>
      <td>21.250000</td>
      <td>5.571429</td>
      <td>209.750000</td>
      <td>2995.428571</td>
      <td>15.142857</td>
      <td>1.428571</td>
    </tr>
    <tr>
      <th>72</th>
      <td>18.714286</td>
      <td>5.821429</td>
      <td>218.375000</td>
      <td>3237.714286</td>
      <td>15.125000</td>
      <td>1.535714</td>
    </tr>
    <tr>
      <th>73</th>
      <td>17.100000</td>
      <td>6.375000</td>
      <td>256.875000</td>
      <td>3419.025000</td>
      <td>14.312500</td>
      <td>1.375000</td>
    </tr>
    <tr>
      <th>74</th>
      <td>22.703704</td>
      <td>5.259259</td>
      <td>171.740741</td>
      <td>2877.925926</td>
      <td>16.203704</td>
      <td>1.666667</td>
    </tr>
    <tr>
      <th>75</th>
      <td>20.266667</td>
      <td>5.600000</td>
      <td>205.533333</td>
      <td>3176.800000</td>
      <td>16.050000</td>
      <td>1.466667</td>
    </tr>
    <tr>
      <th>76</th>
      <td>21.573529</td>
      <td>5.647059</td>
      <td>197.794118</td>
      <td>3078.735294</td>
      <td>15.941176</td>
      <td>1.470588</td>
    </tr>
    <tr>
      <th>77</th>
      <td>23.375000</td>
      <td>5.464286</td>
      <td>191.392857</td>
      <td>2997.357143</td>
      <td>15.435714</td>
      <td>1.571429</td>
    </tr>
    <tr>
      <th>78</th>
      <td>24.061111</td>
      <td>5.361111</td>
      <td>177.805556</td>
      <td>2861.805556</td>
      <td>15.805556</td>
      <td>1.611111</td>
    </tr>
    <tr>
      <th>79</th>
      <td>25.093103</td>
      <td>5.827586</td>
      <td>206.689655</td>
      <td>3055.344828</td>
      <td>15.813793</td>
      <td>1.275862</td>
    </tr>
    <tr>
      <th>80</th>
      <td>33.696552</td>
      <td>4.137931</td>
      <td>115.827586</td>
      <td>2436.655172</td>
      <td>16.934483</td>
      <td>2.206897</td>
    </tr>
    <tr>
      <th>81</th>
      <td>30.334483</td>
      <td>4.620690</td>
      <td>135.310345</td>
      <td>2522.931034</td>
      <td>16.306897</td>
      <td>1.965517</td>
    </tr>
    <tr>
      <th>82</th>
      <td>31.709677</td>
      <td>4.193548</td>
      <td>128.870968</td>
      <td>2453.548387</td>
      <td>16.638710</td>
      <td>1.645161</td>
    </tr>
  </tbody>
</table>
</div>




```python
avg_year = df.groupby('model_year').mean()
```


```python
avg_year.index
```




    Int64Index([70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82], dtype='int64', name='model_year')




```python
avg_year.columns
```




    Index(['mpg', 'cylinders', 'displacement', 'weight', 'acceleration', 'origin'], dtype='object')




```python
avg_year['mpg']
```




    model_year
    70    17.689655
    71    21.250000
    72    18.714286
    73    17.100000
    74    22.703704
    75    20.266667
    76    21.573529
    77    23.375000
    78    24.061111
    79    25.093103
    80    33.696552
    81    30.334483
    82    31.709677
    Name: mpg, dtype: float64




```python
df.groupby('model_year').mean()['mpg']
```




    model_year
    70    17.689655
    71    21.250000
    72    18.714286
    73    17.100000
    74    22.703704
    75    20.266667
    76    21.573529
    77    23.375000
    78    24.061111
    79    25.093103
    80    33.696552
    81    30.334483
    82    31.709677
    Name: mpg, dtype: float64




```python
df.groupby('model_year').describe()
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
      <th colspan="8" halign="left">mpg</th>
      <th colspan="2" halign="left">cylinders</th>
      <th>...</th>
      <th colspan="2" halign="left">acceleration</th>
      <th colspan="8" halign="left">origin</th>
    </tr>
    <tr>
      <th></th>
      <th>count</th>
      <th>mean</th>
      <th>std</th>
      <th>min</th>
      <th>25%</th>
      <th>50%</th>
      <th>75%</th>
      <th>max</th>
      <th>count</th>
      <th>mean</th>
      <th>...</th>
      <th>75%</th>
      <th>max</th>
      <th>count</th>
      <th>mean</th>
      <th>std</th>
      <th>min</th>
      <th>25%</th>
      <th>50%</th>
      <th>75%</th>
      <th>max</th>
    </tr>
    <tr>
      <th>model_year</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
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
      <th>70</th>
      <td>29.0</td>
      <td>17.689655</td>
      <td>5.339231</td>
      <td>9.0</td>
      <td>14.000</td>
      <td>16.00</td>
      <td>22.000</td>
      <td>27.0</td>
      <td>29.0</td>
      <td>6.758621</td>
      <td>...</td>
      <td>15.000</td>
      <td>20.5</td>
      <td>29.0</td>
      <td>1.310345</td>
      <td>0.603765</td>
      <td>1.0</td>
      <td>1.0</td>
      <td>1.0</td>
      <td>1.0</td>
      <td>3.0</td>
    </tr>
    <tr>
      <th>71</th>
      <td>28.0</td>
      <td>21.250000</td>
      <td>6.591942</td>
      <td>12.0</td>
      <td>15.500</td>
      <td>19.00</td>
      <td>27.000</td>
      <td>35.0</td>
      <td>28.0</td>
      <td>5.571429</td>
      <td>...</td>
      <td>16.125</td>
      <td>20.5</td>
      <td>28.0</td>
      <td>1.428571</td>
      <td>0.741798</td>
      <td>1.0</td>
      <td>1.0</td>
      <td>1.0</td>
      <td>2.0</td>
      <td>3.0</td>
    </tr>
    <tr>
      <th>72</th>
      <td>28.0</td>
      <td>18.714286</td>
      <td>5.435529</td>
      <td>11.0</td>
      <td>13.750</td>
      <td>18.50</td>
      <td>23.000</td>
      <td>28.0</td>
      <td>28.0</td>
      <td>5.821429</td>
      <td>...</td>
      <td>16.625</td>
      <td>23.5</td>
      <td>28.0</td>
      <td>1.535714</td>
      <td>0.792658</td>
      <td>1.0</td>
      <td>1.0</td>
      <td>1.0</td>
      <td>2.0</td>
      <td>3.0</td>
    </tr>
    <tr>
      <th>73</th>
      <td>40.0</td>
      <td>17.100000</td>
      <td>4.700245</td>
      <td>11.0</td>
      <td>13.000</td>
      <td>16.00</td>
      <td>20.000</td>
      <td>29.0</td>
      <td>40.0</td>
      <td>6.375000</td>
      <td>...</td>
      <td>16.000</td>
      <td>21.0</td>
      <td>40.0</td>
      <td>1.375000</td>
      <td>0.667467</td>
      <td>1.0</td>
      <td>1.0</td>
      <td>1.0</td>
      <td>2.0</td>
      <td>3.0</td>
    </tr>
    <tr>
      <th>74</th>
      <td>27.0</td>
      <td>22.703704</td>
      <td>6.420010</td>
      <td>13.0</td>
      <td>16.000</td>
      <td>24.00</td>
      <td>27.000</td>
      <td>32.0</td>
      <td>27.0</td>
      <td>5.259259</td>
      <td>...</td>
      <td>17.000</td>
      <td>21.0</td>
      <td>27.0</td>
      <td>1.666667</td>
      <td>0.832050</td>
      <td>1.0</td>
      <td>1.0</td>
      <td>1.0</td>
      <td>2.0</td>
      <td>3.0</td>
    </tr>
    <tr>
      <th>75</th>
      <td>30.0</td>
      <td>20.266667</td>
      <td>4.940566</td>
      <td>13.0</td>
      <td>16.000</td>
      <td>19.50</td>
      <td>23.000</td>
      <td>33.0</td>
      <td>30.0</td>
      <td>5.600000</td>
      <td>...</td>
      <td>17.375</td>
      <td>21.0</td>
      <td>30.0</td>
      <td>1.466667</td>
      <td>0.730297</td>
      <td>1.0</td>
      <td>1.0</td>
      <td>1.0</td>
      <td>2.0</td>
      <td>3.0</td>
    </tr>
    <tr>
      <th>76</th>
      <td>34.0</td>
      <td>21.573529</td>
      <td>5.889297</td>
      <td>13.0</td>
      <td>16.750</td>
      <td>21.00</td>
      <td>26.375</td>
      <td>33.0</td>
      <td>34.0</td>
      <td>5.647059</td>
      <td>...</td>
      <td>17.550</td>
      <td>22.2</td>
      <td>34.0</td>
      <td>1.470588</td>
      <td>0.706476</td>
      <td>1.0</td>
      <td>1.0</td>
      <td>1.0</td>
      <td>2.0</td>
      <td>3.0</td>
    </tr>
    <tr>
      <th>77</th>
      <td>28.0</td>
      <td>23.375000</td>
      <td>6.675862</td>
      <td>15.0</td>
      <td>17.375</td>
      <td>21.75</td>
      <td>30.000</td>
      <td>36.0</td>
      <td>28.0</td>
      <td>5.464286</td>
      <td>...</td>
      <td>16.925</td>
      <td>19.0</td>
      <td>28.0</td>
      <td>1.571429</td>
      <td>0.835711</td>
      <td>1.0</td>
      <td>1.0</td>
      <td>1.0</td>
      <td>2.0</td>
      <td>3.0</td>
    </tr>
    <tr>
      <th>78</th>
      <td>36.0</td>
      <td>24.061111</td>
      <td>6.898044</td>
      <td>16.2</td>
      <td>19.350</td>
      <td>20.70</td>
      <td>28.000</td>
      <td>43.1</td>
      <td>36.0</td>
      <td>5.361111</td>
      <td>...</td>
      <td>16.825</td>
      <td>21.5</td>
      <td>36.0</td>
      <td>1.611111</td>
      <td>0.837608</td>
      <td>1.0</td>
      <td>1.0</td>
      <td>1.0</td>
      <td>2.0</td>
      <td>3.0</td>
    </tr>
    <tr>
      <th>79</th>
      <td>29.0</td>
      <td>25.093103</td>
      <td>6.794217</td>
      <td>15.5</td>
      <td>19.200</td>
      <td>23.90</td>
      <td>31.800</td>
      <td>37.3</td>
      <td>29.0</td>
      <td>5.827586</td>
      <td>...</td>
      <td>17.300</td>
      <td>24.8</td>
      <td>29.0</td>
      <td>1.275862</td>
      <td>0.591400</td>
      <td>1.0</td>
      <td>1.0</td>
      <td>1.0</td>
      <td>1.0</td>
      <td>3.0</td>
    </tr>
    <tr>
      <th>80</th>
      <td>29.0</td>
      <td>33.696552</td>
      <td>7.037983</td>
      <td>19.1</td>
      <td>29.800</td>
      <td>32.70</td>
      <td>38.100</td>
      <td>46.6</td>
      <td>29.0</td>
      <td>4.137931</td>
      <td>...</td>
      <td>18.700</td>
      <td>23.7</td>
      <td>29.0</td>
      <td>2.206897</td>
      <td>0.818505</td>
      <td>1.0</td>
      <td>2.0</td>
      <td>2.0</td>
      <td>3.0</td>
      <td>3.0</td>
    </tr>
    <tr>
      <th>81</th>
      <td>29.0</td>
      <td>30.334483</td>
      <td>5.591465</td>
      <td>17.6</td>
      <td>26.600</td>
      <td>31.60</td>
      <td>34.400</td>
      <td>39.1</td>
      <td>29.0</td>
      <td>4.620690</td>
      <td>...</td>
      <td>17.300</td>
      <td>20.7</td>
      <td>29.0</td>
      <td>1.965517</td>
      <td>0.944259</td>
      <td>1.0</td>
      <td>1.0</td>
      <td>2.0</td>
      <td>3.0</td>
      <td>3.0</td>
    </tr>
    <tr>
      <th>82</th>
      <td>31.0</td>
      <td>31.709677</td>
      <td>5.392548</td>
      <td>22.0</td>
      <td>27.000</td>
      <td>32.00</td>
      <td>36.000</td>
      <td>44.0</td>
      <td>31.0</td>
      <td>4.193548</td>
      <td>...</td>
      <td>18.000</td>
      <td>24.6</td>
      <td>31.0</td>
      <td>1.645161</td>
      <td>0.914636</td>
      <td>1.0</td>
      <td>1.0</td>
      <td>1.0</td>
      <td>3.0</td>
      <td>3.0</td>
    </tr>
  </tbody>
</table>
<p>13 rows × 48 columns</p>
</div>




```python
df.groupby('model_year').describe().transpose()
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
      <th>model_year</th>
      <th>70</th>
      <th>71</th>
      <th>72</th>
      <th>73</th>
      <th>74</th>
      <th>75</th>
      <th>76</th>
      <th>77</th>
      <th>78</th>
      <th>79</th>
      <th>80</th>
      <th>81</th>
      <th>82</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th rowspan="8" valign="top">mpg</th>
      <th>count</th>
      <td>29.000000</td>
      <td>28.000000</td>
      <td>28.000000</td>
      <td>40.000000</td>
      <td>27.000000</td>
      <td>30.000000</td>
      <td>34.000000</td>
      <td>28.000000</td>
      <td>36.000000</td>
      <td>29.000000</td>
      <td>29.000000</td>
      <td>29.000000</td>
      <td>31.000000</td>
    </tr>
    <tr>
      <th>mean</th>
      <td>17.689655</td>
      <td>21.250000</td>
      <td>18.714286</td>
      <td>17.100000</td>
      <td>22.703704</td>
      <td>20.266667</td>
      <td>21.573529</td>
      <td>23.375000</td>
      <td>24.061111</td>
      <td>25.093103</td>
      <td>33.696552</td>
      <td>30.334483</td>
      <td>31.709677</td>
    </tr>
    <tr>
      <th>std</th>
      <td>5.339231</td>
      <td>6.591942</td>
      <td>5.435529</td>
      <td>4.700245</td>
      <td>6.420010</td>
      <td>4.940566</td>
      <td>5.889297</td>
      <td>6.675862</td>
      <td>6.898044</td>
      <td>6.794217</td>
      <td>7.037983</td>
      <td>5.591465</td>
      <td>5.392548</td>
    </tr>
    <tr>
      <th>min</th>
      <td>9.000000</td>
      <td>12.000000</td>
      <td>11.000000</td>
      <td>11.000000</td>
      <td>13.000000</td>
      <td>13.000000</td>
      <td>13.000000</td>
      <td>15.000000</td>
      <td>16.200000</td>
      <td>15.500000</td>
      <td>19.100000</td>
      <td>17.600000</td>
      <td>22.000000</td>
    </tr>
    <tr>
      <th>25%</th>
      <td>14.000000</td>
      <td>15.500000</td>
      <td>13.750000</td>
      <td>13.000000</td>
      <td>16.000000</td>
      <td>16.000000</td>
      <td>16.750000</td>
      <td>17.375000</td>
      <td>19.350000</td>
      <td>19.200000</td>
      <td>29.800000</td>
      <td>26.600000</td>
      <td>27.000000</td>
    </tr>
    <tr>
      <th>50%</th>
      <td>16.000000</td>
      <td>19.000000</td>
      <td>18.500000</td>
      <td>16.000000</td>
      <td>24.000000</td>
      <td>19.500000</td>
      <td>21.000000</td>
      <td>21.750000</td>
      <td>20.700000</td>
      <td>23.900000</td>
      <td>32.700000</td>
      <td>31.600000</td>
      <td>32.000000</td>
    </tr>
    <tr>
      <th>75%</th>
      <td>22.000000</td>
      <td>27.000000</td>
      <td>23.000000</td>
      <td>20.000000</td>
      <td>27.000000</td>
      <td>23.000000</td>
      <td>26.375000</td>
      <td>30.000000</td>
      <td>28.000000</td>
      <td>31.800000</td>
      <td>38.100000</td>
      <td>34.400000</td>
      <td>36.000000</td>
    </tr>
    <tr>
      <th>max</th>
      <td>27.000000</td>
      <td>35.000000</td>
      <td>28.000000</td>
      <td>29.000000</td>
      <td>32.000000</td>
      <td>33.000000</td>
      <td>33.000000</td>
      <td>36.000000</td>
      <td>43.100000</td>
      <td>37.300000</td>
      <td>46.600000</td>
      <td>39.100000</td>
      <td>44.000000</td>
    </tr>
    <tr>
      <th rowspan="8" valign="top">cylinders</th>
      <th>count</th>
      <td>29.000000</td>
      <td>28.000000</td>
      <td>28.000000</td>
      <td>40.000000</td>
      <td>27.000000</td>
      <td>30.000000</td>
      <td>34.000000</td>
      <td>28.000000</td>
      <td>36.000000</td>
      <td>29.000000</td>
      <td>29.000000</td>
      <td>29.000000</td>
      <td>31.000000</td>
    </tr>
    <tr>
      <th>mean</th>
      <td>6.758621</td>
      <td>5.571429</td>
      <td>5.821429</td>
      <td>6.375000</td>
      <td>5.259259</td>
      <td>5.600000</td>
      <td>5.647059</td>
      <td>5.464286</td>
      <td>5.361111</td>
      <td>5.827586</td>
      <td>4.137931</td>
      <td>4.620690</td>
      <td>4.193548</td>
    </tr>
    <tr>
      <th>std</th>
      <td>1.724926</td>
      <td>1.665079</td>
      <td>2.073708</td>
      <td>1.807215</td>
      <td>1.583390</td>
      <td>1.522249</td>
      <td>1.667558</td>
      <td>1.815206</td>
      <td>1.495761</td>
      <td>1.774199</td>
      <td>0.580895</td>
      <td>1.082781</td>
      <td>0.601074</td>
    </tr>
    <tr>
      <th>min</th>
      <td>4.000000</td>
      <td>4.000000</td>
      <td>3.000000</td>
      <td>3.000000</td>
      <td>4.000000</td>
      <td>4.000000</td>
      <td>4.000000</td>
      <td>3.000000</td>
      <td>4.000000</td>
      <td>4.000000</td>
      <td>3.000000</td>
      <td>4.000000</td>
      <td>4.000000</td>
    </tr>
    <tr>
      <th>25%</th>
      <td>6.000000</td>
      <td>4.000000</td>
      <td>4.000000</td>
      <td>4.000000</td>
      <td>4.000000</td>
      <td>4.000000</td>
      <td>4.000000</td>
      <td>4.000000</td>
      <td>4.000000</td>
      <td>4.000000</td>
      <td>4.000000</td>
      <td>4.000000</td>
      <td>4.000000</td>
    </tr>
    <tr>
      <th>50%</th>
      <td>8.000000</td>
      <td>6.000000</td>
      <td>4.000000</td>
      <td>7.000000</td>
      <td>4.000000</td>
      <td>6.000000</td>
      <td>6.000000</td>
      <td>4.000000</td>
      <td>5.500000</td>
      <td>6.000000</td>
      <td>4.000000</td>
      <td>4.000000</td>
      <td>4.000000</td>
    </tr>
    <tr>
      <th>75%</th>
      <td>8.000000</td>
      <td>6.500000</td>
      <td>8.000000</td>
      <td>8.000000</td>
      <td>6.000000</td>
      <td>6.000000</td>
      <td>7.500000</td>
      <td>8.000000</td>
      <td>6.000000</td>
      <td>8.000000</td>
      <td>4.000000</td>
      <td>6.000000</td>
      <td>4.000000</td>
    </tr>
    <tr>
      <th>max</th>
      <td>8.000000</td>
      <td>8.000000</td>
      <td>8.000000</td>
      <td>8.000000</td>
      <td>8.000000</td>
      <td>8.000000</td>
      <td>8.000000</td>
      <td>8.000000</td>
      <td>8.000000</td>
      <td>8.000000</td>
      <td>6.000000</td>
      <td>8.000000</td>
      <td>6.000000</td>
    </tr>
    <tr>
      <th rowspan="8" valign="top">displacement</th>
      <th>count</th>
      <td>29.000000</td>
      <td>28.000000</td>
      <td>28.000000</td>
      <td>40.000000</td>
      <td>27.000000</td>
      <td>30.000000</td>
      <td>34.000000</td>
      <td>28.000000</td>
      <td>36.000000</td>
      <td>29.000000</td>
      <td>29.000000</td>
      <td>29.000000</td>
      <td>31.000000</td>
    </tr>
    <tr>
      <th>mean</th>
      <td>281.413793</td>
      <td>209.750000</td>
      <td>218.375000</td>
      <td>256.875000</td>
      <td>171.740741</td>
      <td>205.533333</td>
      <td>197.794118</td>
      <td>191.392857</td>
      <td>177.805556</td>
      <td>206.689655</td>
      <td>115.827586</td>
      <td>135.310345</td>
      <td>128.870968</td>
    </tr>
    <tr>
      <th>std</th>
      <td>124.421380</td>
      <td>115.102410</td>
      <td>123.781964</td>
      <td>121.722085</td>
      <td>92.601127</td>
      <td>87.669730</td>
      <td>94.422256</td>
      <td>107.813742</td>
      <td>76.012713</td>
      <td>96.307581</td>
      <td>33.744914</td>
      <td>58.387929</td>
      <td>39.352037</td>
    </tr>
    <tr>
      <th>min</th>
      <td>97.000000</td>
      <td>71.000000</td>
      <td>70.000000</td>
      <td>68.000000</td>
      <td>71.000000</td>
      <td>90.000000</td>
      <td>85.000000</td>
      <td>79.000000</td>
      <td>78.000000</td>
      <td>85.000000</td>
      <td>70.000000</td>
      <td>79.000000</td>
      <td>91.000000</td>
    </tr>
    <tr>
      <th>25%</th>
      <td>198.000000</td>
      <td>97.750000</td>
      <td>109.250000</td>
      <td>121.750000</td>
      <td>90.000000</td>
      <td>121.000000</td>
      <td>102.500000</td>
      <td>97.750000</td>
      <td>115.500000</td>
      <td>121.000000</td>
      <td>90.000000</td>
      <td>98.000000</td>
      <td>105.000000</td>
    </tr>
    <tr>
      <th>50%</th>
      <td>307.000000</td>
      <td>228.500000</td>
      <td>131.000000</td>
      <td>276.000000</td>
      <td>122.000000</td>
      <td>228.000000</td>
      <td>184.000000</td>
      <td>143.000000</td>
      <td>159.500000</td>
      <td>183.000000</td>
      <td>107.000000</td>
      <td>119.000000</td>
      <td>119.000000</td>
    </tr>
    <tr>
      <th>75%</th>
      <td>383.000000</td>
      <td>273.000000</td>
      <td>326.000000</td>
      <td>350.250000</td>
      <td>250.000000</td>
      <td>250.000000</td>
      <td>291.000000</td>
      <td>270.500000</td>
      <td>231.000000</td>
      <td>302.000000</td>
      <td>140.000000</td>
      <td>151.000000</td>
      <td>142.000000</td>
    </tr>
    <tr>
      <th>max</th>
      <td>455.000000</td>
      <td>400.000000</td>
      <td>429.000000</td>
      <td>455.000000</td>
      <td>350.000000</td>
      <td>400.000000</td>
      <td>351.000000</td>
      <td>400.000000</td>
      <td>318.000000</td>
      <td>360.000000</td>
      <td>225.000000</td>
      <td>350.000000</td>
      <td>262.000000</td>
    </tr>
    <tr>
      <th rowspan="8" valign="top">weight</th>
      <th>count</th>
      <td>29.000000</td>
      <td>28.000000</td>
      <td>28.000000</td>
      <td>40.000000</td>
      <td>27.000000</td>
      <td>30.000000</td>
      <td>34.000000</td>
      <td>28.000000</td>
      <td>36.000000</td>
      <td>29.000000</td>
      <td>29.000000</td>
      <td>29.000000</td>
      <td>31.000000</td>
    </tr>
    <tr>
      <th>mean</th>
      <td>3372.793103</td>
      <td>2995.428571</td>
      <td>3237.714286</td>
      <td>3419.025000</td>
      <td>2877.925926</td>
      <td>3176.800000</td>
      <td>3078.735294</td>
      <td>2997.357143</td>
      <td>2861.805556</td>
      <td>3055.344828</td>
      <td>2436.655172</td>
      <td>2522.931034</td>
      <td>2453.548387</td>
    </tr>
    <tr>
      <th>std</th>
      <td>852.868663</td>
      <td>1061.830859</td>
      <td>974.520960</td>
      <td>974.809133</td>
      <td>949.308571</td>
      <td>765.179781</td>
      <td>821.371481</td>
      <td>912.825902</td>
      <td>626.023907</td>
      <td>747.881497</td>
      <td>432.235491</td>
      <td>533.600501</td>
      <td>354.276713</td>
    </tr>
    <tr>
      <th>min</th>
      <td>1835.000000</td>
      <td>1613.000000</td>
      <td>2100.000000</td>
      <td>1867.000000</td>
      <td>1649.000000</td>
      <td>1795.000000</td>
      <td>1795.000000</td>
      <td>1825.000000</td>
      <td>1800.000000</td>
      <td>1915.000000</td>
      <td>1835.000000</td>
      <td>1755.000000</td>
      <td>1965.000000</td>
    </tr>
    <tr>
      <th>25%</th>
      <td>2648.000000</td>
      <td>2110.750000</td>
      <td>2285.500000</td>
      <td>2554.500000</td>
      <td>2116.500000</td>
      <td>2676.750000</td>
      <td>2228.750000</td>
      <td>2135.000000</td>
      <td>2282.500000</td>
      <td>2556.000000</td>
      <td>2110.000000</td>
      <td>2065.000000</td>
      <td>2127.500000</td>
    </tr>
    <tr>
      <th>50%</th>
      <td>3449.000000</td>
      <td>2798.000000</td>
      <td>2956.000000</td>
      <td>3338.500000</td>
      <td>2489.000000</td>
      <td>3098.500000</td>
      <td>3171.500000</td>
      <td>2747.500000</td>
      <td>2910.000000</td>
      <td>3190.000000</td>
      <td>2335.000000</td>
      <td>2385.000000</td>
      <td>2525.000000</td>
    </tr>
    <tr>
      <th>75%</th>
      <td>4312.000000</td>
      <td>3603.250000</td>
      <td>4169.750000</td>
      <td>4247.250000</td>
      <td>3622.500000</td>
      <td>3662.250000</td>
      <td>3803.750000</td>
      <td>3925.000000</td>
      <td>3410.000000</td>
      <td>3725.000000</td>
      <td>2800.000000</td>
      <td>2900.000000</td>
      <td>2727.500000</td>
    </tr>
    <tr>
      <th>max</th>
      <td>4732.000000</td>
      <td>5140.000000</td>
      <td>4633.000000</td>
      <td>4997.000000</td>
      <td>4699.000000</td>
      <td>4668.000000</td>
      <td>4380.000000</td>
      <td>4335.000000</td>
      <td>4080.000000</td>
      <td>4360.000000</td>
      <td>3381.000000</td>
      <td>3725.000000</td>
      <td>3035.000000</td>
    </tr>
    <tr>
      <th rowspan="8" valign="top">acceleration</th>
      <th>count</th>
      <td>29.000000</td>
      <td>28.000000</td>
      <td>28.000000</td>
      <td>40.000000</td>
      <td>27.000000</td>
      <td>30.000000</td>
      <td>34.000000</td>
      <td>28.000000</td>
      <td>36.000000</td>
      <td>29.000000</td>
      <td>29.000000</td>
      <td>29.000000</td>
      <td>31.000000</td>
    </tr>
    <tr>
      <th>mean</th>
      <td>12.948276</td>
      <td>15.142857</td>
      <td>15.125000</td>
      <td>14.312500</td>
      <td>16.203704</td>
      <td>16.050000</td>
      <td>15.941176</td>
      <td>15.435714</td>
      <td>15.805556</td>
      <td>15.813793</td>
      <td>16.934483</td>
      <td>16.306897</td>
      <td>16.638710</td>
    </tr>
    <tr>
      <th>std</th>
      <td>3.330982</td>
      <td>2.666171</td>
      <td>2.850032</td>
      <td>2.754222</td>
      <td>1.688532</td>
      <td>2.471737</td>
      <td>2.801419</td>
      <td>2.273391</td>
      <td>2.129915</td>
      <td>2.952931</td>
      <td>2.826694</td>
      <td>2.192509</td>
      <td>2.484844</td>
    </tr>
    <tr>
      <th>min</th>
      <td>8.000000</td>
      <td>11.500000</td>
      <td>11.000000</td>
      <td>9.500000</td>
      <td>13.500000</td>
      <td>11.500000</td>
      <td>12.000000</td>
      <td>11.100000</td>
      <td>11.200000</td>
      <td>11.300000</td>
      <td>11.400000</td>
      <td>12.600000</td>
      <td>11.600000</td>
    </tr>
    <tr>
      <th>25%</th>
      <td>10.000000</td>
      <td>13.375000</td>
      <td>13.375000</td>
      <td>12.500000</td>
      <td>15.250000</td>
      <td>14.125000</td>
      <td>13.925000</td>
      <td>14.000000</td>
      <td>14.475000</td>
      <td>14.000000</td>
      <td>15.100000</td>
      <td>14.800000</td>
      <td>14.850000</td>
    </tr>
    <tr>
      <th>50%</th>
      <td>12.500000</td>
      <td>14.500000</td>
      <td>14.500000</td>
      <td>14.000000</td>
      <td>16.000000</td>
      <td>16.000000</td>
      <td>15.500000</td>
      <td>15.650000</td>
      <td>15.750000</td>
      <td>15.000000</td>
      <td>16.500000</td>
      <td>16.200000</td>
      <td>16.400000</td>
    </tr>
    <tr>
      <th>75%</th>
      <td>15.000000</td>
      <td>16.125000</td>
      <td>16.625000</td>
      <td>16.000000</td>
      <td>17.000000</td>
      <td>17.375000</td>
      <td>17.550000</td>
      <td>16.925000</td>
      <td>16.825000</td>
      <td>17.300000</td>
      <td>18.700000</td>
      <td>17.300000</td>
      <td>18.000000</td>
    </tr>
    <tr>
      <th>max</th>
      <td>20.500000</td>
      <td>20.500000</td>
      <td>23.500000</td>
      <td>21.000000</td>
      <td>21.000000</td>
      <td>21.000000</td>
      <td>22.200000</td>
      <td>19.000000</td>
      <td>21.500000</td>
      <td>24.800000</td>
      <td>23.700000</td>
      <td>20.700000</td>
      <td>24.600000</td>
    </tr>
    <tr>
      <th rowspan="8" valign="top">origin</th>
      <th>count</th>
      <td>29.000000</td>
      <td>28.000000</td>
      <td>28.000000</td>
      <td>40.000000</td>
      <td>27.000000</td>
      <td>30.000000</td>
      <td>34.000000</td>
      <td>28.000000</td>
      <td>36.000000</td>
      <td>29.000000</td>
      <td>29.000000</td>
      <td>29.000000</td>
      <td>31.000000</td>
    </tr>
    <tr>
      <th>mean</th>
      <td>1.310345</td>
      <td>1.428571</td>
      <td>1.535714</td>
      <td>1.375000</td>
      <td>1.666667</td>
      <td>1.466667</td>
      <td>1.470588</td>
      <td>1.571429</td>
      <td>1.611111</td>
      <td>1.275862</td>
      <td>2.206897</td>
      <td>1.965517</td>
      <td>1.645161</td>
    </tr>
    <tr>
      <th>std</th>
      <td>0.603765</td>
      <td>0.741798</td>
      <td>0.792658</td>
      <td>0.667467</td>
      <td>0.832050</td>
      <td>0.730297</td>
      <td>0.706476</td>
      <td>0.835711</td>
      <td>0.837608</td>
      <td>0.591400</td>
      <td>0.818505</td>
      <td>0.944259</td>
      <td>0.914636</td>
    </tr>
    <tr>
      <th>min</th>
      <td>1.000000</td>
      <td>1.000000</td>
      <td>1.000000</td>
      <td>1.000000</td>
      <td>1.000000</td>
      <td>1.000000</td>
      <td>1.000000</td>
      <td>1.000000</td>
      <td>1.000000</td>
      <td>1.000000</td>
      <td>1.000000</td>
      <td>1.000000</td>
      <td>1.000000</td>
    </tr>
    <tr>
      <th>25%</th>
      <td>1.000000</td>
      <td>1.000000</td>
      <td>1.000000</td>
      <td>1.000000</td>
      <td>1.000000</td>
      <td>1.000000</td>
      <td>1.000000</td>
      <td>1.000000</td>
      <td>1.000000</td>
      <td>1.000000</td>
      <td>2.000000</td>
      <td>1.000000</td>
      <td>1.000000</td>
    </tr>
    <tr>
      <th>50%</th>
      <td>1.000000</td>
      <td>1.000000</td>
      <td>1.000000</td>
      <td>1.000000</td>
      <td>1.000000</td>
      <td>1.000000</td>
      <td>1.000000</td>
      <td>1.000000</td>
      <td>1.000000</td>
      <td>1.000000</td>
      <td>2.000000</td>
      <td>2.000000</td>
      <td>1.000000</td>
    </tr>
    <tr>
      <th>75%</th>
      <td>1.000000</td>
      <td>2.000000</td>
      <td>2.000000</td>
      <td>2.000000</td>
      <td>2.000000</td>
      <td>2.000000</td>
      <td>2.000000</td>
      <td>2.000000</td>
      <td>2.000000</td>
      <td>1.000000</td>
      <td>3.000000</td>
      <td>3.000000</td>
      <td>3.000000</td>
    </tr>
    <tr>
      <th>max</th>
      <td>3.000000</td>
      <td>3.000000</td>
      <td>3.000000</td>
      <td>3.000000</td>
      <td>3.000000</td>
      <td>3.000000</td>
      <td>3.000000</td>
      <td>3.000000</td>
      <td>3.000000</td>
      <td>3.000000</td>
      <td>3.000000</td>
      <td>3.000000</td>
      <td>3.000000</td>
    </tr>
  </tbody>
</table>
</div>



## Groupby Multiple Columns
Let's explore average mpg per year per cylinder count


```python
df.groupby(['model_year','cylinders']).mean()
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
      <th>mpg</th>
      <th>displacement</th>
      <th>weight</th>
      <th>acceleration</th>
      <th>origin</th>
    </tr>
    <tr>
      <th>model_year</th>
      <th>cylinders</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th rowspan="3" valign="top">70</th>
      <th>4</th>
      <td>25.285714</td>
      <td>107.000000</td>
      <td>2292.571429</td>
      <td>16.000000</td>
      <td>2.285714</td>
    </tr>
    <tr>
      <th>6</th>
      <td>20.500000</td>
      <td>199.000000</td>
      <td>2710.500000</td>
      <td>15.500000</td>
      <td>1.000000</td>
    </tr>
    <tr>
      <th>8</th>
      <td>14.111111</td>
      <td>367.555556</td>
      <td>3940.055556</td>
      <td>11.194444</td>
      <td>1.000000</td>
    </tr>
    <tr>
      <th rowspan="3" valign="top">71</th>
      <th>4</th>
      <td>27.461538</td>
      <td>101.846154</td>
      <td>2056.384615</td>
      <td>16.961538</td>
      <td>1.923077</td>
    </tr>
    <tr>
      <th>6</th>
      <td>18.000000</td>
      <td>243.375000</td>
      <td>3171.875000</td>
      <td>14.750000</td>
      <td>1.000000</td>
    </tr>
    <tr>
      <th>8</th>
      <td>13.428571</td>
      <td>371.714286</td>
      <td>4537.714286</td>
      <td>12.214286</td>
      <td>1.000000</td>
    </tr>
    <tr>
      <th rowspan="3" valign="top">72</th>
      <th>3</th>
      <td>19.000000</td>
      <td>70.000000</td>
      <td>2330.000000</td>
      <td>13.500000</td>
      <td>3.000000</td>
    </tr>
    <tr>
      <th>4</th>
      <td>23.428571</td>
      <td>111.535714</td>
      <td>2382.642857</td>
      <td>17.214286</td>
      <td>1.928571</td>
    </tr>
    <tr>
      <th>8</th>
      <td>13.615385</td>
      <td>344.846154</td>
      <td>4228.384615</td>
      <td>13.000000</td>
      <td>1.000000</td>
    </tr>
    <tr>
      <th rowspan="4" valign="top">73</th>
      <th>3</th>
      <td>18.000000</td>
      <td>70.000000</td>
      <td>2124.000000</td>
      <td>13.500000</td>
      <td>3.000000</td>
    </tr>
    <tr>
      <th>4</th>
      <td>22.727273</td>
      <td>109.272727</td>
      <td>2338.090909</td>
      <td>17.136364</td>
      <td>2.000000</td>
    </tr>
    <tr>
      <th>6</th>
      <td>19.000000</td>
      <td>212.250000</td>
      <td>2917.125000</td>
      <td>15.687500</td>
      <td>1.250000</td>
    </tr>
    <tr>
      <th>8</th>
      <td>13.200000</td>
      <td>365.250000</td>
      <td>4279.050000</td>
      <td>12.250000</td>
      <td>1.000000</td>
    </tr>
    <tr>
      <th rowspan="3" valign="top">74</th>
      <th>4</th>
      <td>27.800000</td>
      <td>96.533333</td>
      <td>2151.466667</td>
      <td>16.400000</td>
      <td>2.200000</td>
    </tr>
    <tr>
      <th>6</th>
      <td>17.857143</td>
      <td>230.428571</td>
      <td>3320.000000</td>
      <td>16.857143</td>
      <td>1.000000</td>
    </tr>
    <tr>
      <th>8</th>
      <td>14.200000</td>
      <td>315.200000</td>
      <td>4438.400000</td>
      <td>14.700000</td>
      <td>1.000000</td>
    </tr>
    <tr>
      <th rowspan="3" valign="top">75</th>
      <th>4</th>
      <td>25.250000</td>
      <td>114.833333</td>
      <td>2489.250000</td>
      <td>15.833333</td>
      <td>2.166667</td>
    </tr>
    <tr>
      <th>6</th>
      <td>17.583333</td>
      <td>233.750000</td>
      <td>3398.333333</td>
      <td>17.708333</td>
      <td>1.000000</td>
    </tr>
    <tr>
      <th>8</th>
      <td>15.666667</td>
      <td>330.500000</td>
      <td>4108.833333</td>
      <td>13.166667</td>
      <td>1.000000</td>
    </tr>
    <tr>
      <th rowspan="3" valign="top">76</th>
      <th>4</th>
      <td>26.766667</td>
      <td>106.333333</td>
      <td>2306.600000</td>
      <td>16.866667</td>
      <td>1.866667</td>
    </tr>
    <tr>
      <th>6</th>
      <td>20.000000</td>
      <td>221.400000</td>
      <td>3349.600000</td>
      <td>17.000000</td>
      <td>1.300000</td>
    </tr>
    <tr>
      <th>8</th>
      <td>14.666667</td>
      <td>324.000000</td>
      <td>4064.666667</td>
      <td>13.222222</td>
      <td>1.000000</td>
    </tr>
    <tr>
      <th rowspan="4" valign="top">77</th>
      <th>3</th>
      <td>21.500000</td>
      <td>80.000000</td>
      <td>2720.000000</td>
      <td>13.500000</td>
      <td>3.000000</td>
    </tr>
    <tr>
      <th>4</th>
      <td>29.107143</td>
      <td>106.500000</td>
      <td>2205.071429</td>
      <td>16.064286</td>
      <td>1.857143</td>
    </tr>
    <tr>
      <th>6</th>
      <td>19.500000</td>
      <td>220.400000</td>
      <td>3383.000000</td>
      <td>16.900000</td>
      <td>1.400000</td>
    </tr>
    <tr>
      <th>8</th>
      <td>16.000000</td>
      <td>335.750000</td>
      <td>4177.500000</td>
      <td>13.662500</td>
      <td>1.000000</td>
    </tr>
    <tr>
      <th rowspan="4" valign="top">78</th>
      <th>4</th>
      <td>29.576471</td>
      <td>112.117647</td>
      <td>2296.764706</td>
      <td>16.282353</td>
      <td>2.117647</td>
    </tr>
    <tr>
      <th>5</th>
      <td>20.300000</td>
      <td>131.000000</td>
      <td>2830.000000</td>
      <td>15.900000</td>
      <td>2.000000</td>
    </tr>
    <tr>
      <th>6</th>
      <td>19.066667</td>
      <td>213.250000</td>
      <td>3314.166667</td>
      <td>16.391667</td>
      <td>1.166667</td>
    </tr>
    <tr>
      <th>8</th>
      <td>19.050000</td>
      <td>300.833333</td>
      <td>3563.333333</td>
      <td>13.266667</td>
      <td>1.000000</td>
    </tr>
    <tr>
      <th rowspan="4" valign="top">79</th>
      <th>4</th>
      <td>31.525000</td>
      <td>113.583333</td>
      <td>2357.583333</td>
      <td>15.991667</td>
      <td>1.583333</td>
    </tr>
    <tr>
      <th>5</th>
      <td>25.400000</td>
      <td>183.000000</td>
      <td>3530.000000</td>
      <td>20.100000</td>
      <td>2.000000</td>
    </tr>
    <tr>
      <th>6</th>
      <td>22.950000</td>
      <td>205.666667</td>
      <td>3025.833333</td>
      <td>15.433333</td>
      <td>1.000000</td>
    </tr>
    <tr>
      <th>8</th>
      <td>18.630000</td>
      <td>321.400000</td>
      <td>3862.900000</td>
      <td>15.400000</td>
      <td>1.000000</td>
    </tr>
    <tr>
      <th rowspan="4" valign="top">80</th>
      <th>3</th>
      <td>23.700000</td>
      <td>70.000000</td>
      <td>2420.000000</td>
      <td>12.500000</td>
      <td>3.000000</td>
    </tr>
    <tr>
      <th>4</th>
      <td>34.612000</td>
      <td>111.000000</td>
      <td>2360.080000</td>
      <td>17.144000</td>
      <td>2.200000</td>
    </tr>
    <tr>
      <th>5</th>
      <td>36.400000</td>
      <td>121.000000</td>
      <td>2950.000000</td>
      <td>19.900000</td>
      <td>2.000000</td>
    </tr>
    <tr>
      <th>6</th>
      <td>25.900000</td>
      <td>196.500000</td>
      <td>3145.500000</td>
      <td>15.050000</td>
      <td>2.000000</td>
    </tr>
    <tr>
      <th rowspan="3" valign="top">81</th>
      <th>4</th>
      <td>32.814286</td>
      <td>108.857143</td>
      <td>2275.476190</td>
      <td>16.466667</td>
      <td>2.095238</td>
    </tr>
    <tr>
      <th>6</th>
      <td>23.428571</td>
      <td>184.000000</td>
      <td>3093.571429</td>
      <td>15.442857</td>
      <td>1.714286</td>
    </tr>
    <tr>
      <th>8</th>
      <td>26.600000</td>
      <td>350.000000</td>
      <td>3725.000000</td>
      <td>19.000000</td>
      <td>1.000000</td>
    </tr>
    <tr>
      <th rowspan="2" valign="top">82</th>
      <th>4</th>
      <td>32.071429</td>
      <td>118.571429</td>
      <td>2402.321429</td>
      <td>16.703571</td>
      <td>1.714286</td>
    </tr>
    <tr>
      <th>6</th>
      <td>28.333333</td>
      <td>225.000000</td>
      <td>2931.666667</td>
      <td>16.033333</td>
      <td>1.000000</td>
    </tr>
  </tbody>
</table>
</div>




```python
df.groupby(['model_year','cylinders']).mean().index
```




    MultiIndex([(70, 4),
                (70, 6),
                (70, 8),
                (71, 4),
                (71, 6),
                (71, 8),
                (72, 3),
                (72, 4),
                (72, 8),
                (73, 3),
                (73, 4),
                (73, 6),
                (73, 8),
                (74, 4),
                (74, 6),
                (74, 8),
                (75, 4),
                (75, 6),
                (75, 8),
                (76, 4),
                (76, 6),
                (76, 8),
                (77, 3),
                (77, 4),
                (77, 6),
                (77, 8),
                (78, 4),
                (78, 5),
                (78, 6),
                (78, 8),
                (79, 4),
                (79, 5),
                (79, 6),
                (79, 8),
                (80, 3),
                (80, 4),
                (80, 5),
                (80, 6),
                (81, 4),
                (81, 6),
                (81, 8),
                (82, 4),
                (82, 6)],
               names=['model_year', 'cylinders'])



# MultiIndex

## The MultiIndex Object


```python
year_cyl = df.groupby(['model_year','cylinders']).mean()
```


```python
year_cyl
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
      <th>mpg</th>
      <th>displacement</th>
      <th>weight</th>
      <th>acceleration</th>
      <th>origin</th>
    </tr>
    <tr>
      <th>model_year</th>
      <th>cylinders</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th rowspan="3" valign="top">70</th>
      <th>4</th>
      <td>25.285714</td>
      <td>107.000000</td>
      <td>2292.571429</td>
      <td>16.000000</td>
      <td>2.285714</td>
    </tr>
    <tr>
      <th>6</th>
      <td>20.500000</td>
      <td>199.000000</td>
      <td>2710.500000</td>
      <td>15.500000</td>
      <td>1.000000</td>
    </tr>
    <tr>
      <th>8</th>
      <td>14.111111</td>
      <td>367.555556</td>
      <td>3940.055556</td>
      <td>11.194444</td>
      <td>1.000000</td>
    </tr>
    <tr>
      <th rowspan="3" valign="top">71</th>
      <th>4</th>
      <td>27.461538</td>
      <td>101.846154</td>
      <td>2056.384615</td>
      <td>16.961538</td>
      <td>1.923077</td>
    </tr>
    <tr>
      <th>6</th>
      <td>18.000000</td>
      <td>243.375000</td>
      <td>3171.875000</td>
      <td>14.750000</td>
      <td>1.000000</td>
    </tr>
    <tr>
      <th>8</th>
      <td>13.428571</td>
      <td>371.714286</td>
      <td>4537.714286</td>
      <td>12.214286</td>
      <td>1.000000</td>
    </tr>
    <tr>
      <th rowspan="3" valign="top">72</th>
      <th>3</th>
      <td>19.000000</td>
      <td>70.000000</td>
      <td>2330.000000</td>
      <td>13.500000</td>
      <td>3.000000</td>
    </tr>
    <tr>
      <th>4</th>
      <td>23.428571</td>
      <td>111.535714</td>
      <td>2382.642857</td>
      <td>17.214286</td>
      <td>1.928571</td>
    </tr>
    <tr>
      <th>8</th>
      <td>13.615385</td>
      <td>344.846154</td>
      <td>4228.384615</td>
      <td>13.000000</td>
      <td>1.000000</td>
    </tr>
    <tr>
      <th rowspan="4" valign="top">73</th>
      <th>3</th>
      <td>18.000000</td>
      <td>70.000000</td>
      <td>2124.000000</td>
      <td>13.500000</td>
      <td>3.000000</td>
    </tr>
    <tr>
      <th>4</th>
      <td>22.727273</td>
      <td>109.272727</td>
      <td>2338.090909</td>
      <td>17.136364</td>
      <td>2.000000</td>
    </tr>
    <tr>
      <th>6</th>
      <td>19.000000</td>
      <td>212.250000</td>
      <td>2917.125000</td>
      <td>15.687500</td>
      <td>1.250000</td>
    </tr>
    <tr>
      <th>8</th>
      <td>13.200000</td>
      <td>365.250000</td>
      <td>4279.050000</td>
      <td>12.250000</td>
      <td>1.000000</td>
    </tr>
    <tr>
      <th rowspan="3" valign="top">74</th>
      <th>4</th>
      <td>27.800000</td>
      <td>96.533333</td>
      <td>2151.466667</td>
      <td>16.400000</td>
      <td>2.200000</td>
    </tr>
    <tr>
      <th>6</th>
      <td>17.857143</td>
      <td>230.428571</td>
      <td>3320.000000</td>
      <td>16.857143</td>
      <td>1.000000</td>
    </tr>
    <tr>
      <th>8</th>
      <td>14.200000</td>
      <td>315.200000</td>
      <td>4438.400000</td>
      <td>14.700000</td>
      <td>1.000000</td>
    </tr>
    <tr>
      <th rowspan="3" valign="top">75</th>
      <th>4</th>
      <td>25.250000</td>
      <td>114.833333</td>
      <td>2489.250000</td>
      <td>15.833333</td>
      <td>2.166667</td>
    </tr>
    <tr>
      <th>6</th>
      <td>17.583333</td>
      <td>233.750000</td>
      <td>3398.333333</td>
      <td>17.708333</td>
      <td>1.000000</td>
    </tr>
    <tr>
      <th>8</th>
      <td>15.666667</td>
      <td>330.500000</td>
      <td>4108.833333</td>
      <td>13.166667</td>
      <td>1.000000</td>
    </tr>
    <tr>
      <th rowspan="3" valign="top">76</th>
      <th>4</th>
      <td>26.766667</td>
      <td>106.333333</td>
      <td>2306.600000</td>
      <td>16.866667</td>
      <td>1.866667</td>
    </tr>
    <tr>
      <th>6</th>
      <td>20.000000</td>
      <td>221.400000</td>
      <td>3349.600000</td>
      <td>17.000000</td>
      <td>1.300000</td>
    </tr>
    <tr>
      <th>8</th>
      <td>14.666667</td>
      <td>324.000000</td>
      <td>4064.666667</td>
      <td>13.222222</td>
      <td>1.000000</td>
    </tr>
    <tr>
      <th rowspan="4" valign="top">77</th>
      <th>3</th>
      <td>21.500000</td>
      <td>80.000000</td>
      <td>2720.000000</td>
      <td>13.500000</td>
      <td>3.000000</td>
    </tr>
    <tr>
      <th>4</th>
      <td>29.107143</td>
      <td>106.500000</td>
      <td>2205.071429</td>
      <td>16.064286</td>
      <td>1.857143</td>
    </tr>
    <tr>
      <th>6</th>
      <td>19.500000</td>
      <td>220.400000</td>
      <td>3383.000000</td>
      <td>16.900000</td>
      <td>1.400000</td>
    </tr>
    <tr>
      <th>8</th>
      <td>16.000000</td>
      <td>335.750000</td>
      <td>4177.500000</td>
      <td>13.662500</td>
      <td>1.000000</td>
    </tr>
    <tr>
      <th rowspan="4" valign="top">78</th>
      <th>4</th>
      <td>29.576471</td>
      <td>112.117647</td>
      <td>2296.764706</td>
      <td>16.282353</td>
      <td>2.117647</td>
    </tr>
    <tr>
      <th>5</th>
      <td>20.300000</td>
      <td>131.000000</td>
      <td>2830.000000</td>
      <td>15.900000</td>
      <td>2.000000</td>
    </tr>
    <tr>
      <th>6</th>
      <td>19.066667</td>
      <td>213.250000</td>
      <td>3314.166667</td>
      <td>16.391667</td>
      <td>1.166667</td>
    </tr>
    <tr>
      <th>8</th>
      <td>19.050000</td>
      <td>300.833333</td>
      <td>3563.333333</td>
      <td>13.266667</td>
      <td>1.000000</td>
    </tr>
    <tr>
      <th rowspan="4" valign="top">79</th>
      <th>4</th>
      <td>31.525000</td>
      <td>113.583333</td>
      <td>2357.583333</td>
      <td>15.991667</td>
      <td>1.583333</td>
    </tr>
    <tr>
      <th>5</th>
      <td>25.400000</td>
      <td>183.000000</td>
      <td>3530.000000</td>
      <td>20.100000</td>
      <td>2.000000</td>
    </tr>
    <tr>
      <th>6</th>
      <td>22.950000</td>
      <td>205.666667</td>
      <td>3025.833333</td>
      <td>15.433333</td>
      <td>1.000000</td>
    </tr>
    <tr>
      <th>8</th>
      <td>18.630000</td>
      <td>321.400000</td>
      <td>3862.900000</td>
      <td>15.400000</td>
      <td>1.000000</td>
    </tr>
    <tr>
      <th rowspan="4" valign="top">80</th>
      <th>3</th>
      <td>23.700000</td>
      <td>70.000000</td>
      <td>2420.000000</td>
      <td>12.500000</td>
      <td>3.000000</td>
    </tr>
    <tr>
      <th>4</th>
      <td>34.612000</td>
      <td>111.000000</td>
      <td>2360.080000</td>
      <td>17.144000</td>
      <td>2.200000</td>
    </tr>
    <tr>
      <th>5</th>
      <td>36.400000</td>
      <td>121.000000</td>
      <td>2950.000000</td>
      <td>19.900000</td>
      <td>2.000000</td>
    </tr>
    <tr>
      <th>6</th>
      <td>25.900000</td>
      <td>196.500000</td>
      <td>3145.500000</td>
      <td>15.050000</td>
      <td>2.000000</td>
    </tr>
    <tr>
      <th rowspan="3" valign="top">81</th>
      <th>4</th>
      <td>32.814286</td>
      <td>108.857143</td>
      <td>2275.476190</td>
      <td>16.466667</td>
      <td>2.095238</td>
    </tr>
    <tr>
      <th>6</th>
      <td>23.428571</td>
      <td>184.000000</td>
      <td>3093.571429</td>
      <td>15.442857</td>
      <td>1.714286</td>
    </tr>
    <tr>
      <th>8</th>
      <td>26.600000</td>
      <td>350.000000</td>
      <td>3725.000000</td>
      <td>19.000000</td>
      <td>1.000000</td>
    </tr>
    <tr>
      <th rowspan="2" valign="top">82</th>
      <th>4</th>
      <td>32.071429</td>
      <td>118.571429</td>
      <td>2402.321429</td>
      <td>16.703571</td>
      <td>1.714286</td>
    </tr>
    <tr>
      <th>6</th>
      <td>28.333333</td>
      <td>225.000000</td>
      <td>2931.666667</td>
      <td>16.033333</td>
      <td>1.000000</td>
    </tr>
  </tbody>
</table>
</div>




```python
year_cyl.index
```




    MultiIndex([(70, 4),
                (70, 6),
                (70, 8),
                (71, 4),
                (71, 6),
                (71, 8),
                (72, 3),
                (72, 4),
                (72, 8),
                (73, 3),
                (73, 4),
                (73, 6),
                (73, 8),
                (74, 4),
                (74, 6),
                (74, 8),
                (75, 4),
                (75, 6),
                (75, 8),
                (76, 4),
                (76, 6),
                (76, 8),
                (77, 3),
                (77, 4),
                (77, 6),
                (77, 8),
                (78, 4),
                (78, 5),
                (78, 6),
                (78, 8),
                (79, 4),
                (79, 5),
                (79, 6),
                (79, 8),
                (80, 3),
                (80, 4),
                (80, 5),
                (80, 6),
                (81, 4),
                (81, 6),
                (81, 8),
                (82, 4),
                (82, 6)],
               names=['model_year', 'cylinders'])




```python
year_cyl.index.levels
```




    FrozenList([[70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82], [3, 4, 5, 6, 8]])




```python
year_cyl.index.names
```




    FrozenList(['model_year', 'cylinders'])



# Indexing with the Hierarchical Index

Full Documentation: https://pandas.pydata.org/pandas-docs/stable/user_guide/advanced.html


```python
year_cyl.head()
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
      <th>mpg</th>
      <th>displacement</th>
      <th>weight</th>
      <th>acceleration</th>
      <th>origin</th>
    </tr>
    <tr>
      <th>model_year</th>
      <th>cylinders</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th rowspan="3" valign="top">70</th>
      <th>4</th>
      <td>25.285714</td>
      <td>107.000000</td>
      <td>2292.571429</td>
      <td>16.000000</td>
      <td>2.285714</td>
    </tr>
    <tr>
      <th>6</th>
      <td>20.500000</td>
      <td>199.000000</td>
      <td>2710.500000</td>
      <td>15.500000</td>
      <td>1.000000</td>
    </tr>
    <tr>
      <th>8</th>
      <td>14.111111</td>
      <td>367.555556</td>
      <td>3940.055556</td>
      <td>11.194444</td>
      <td>1.000000</td>
    </tr>
    <tr>
      <th rowspan="2" valign="top">71</th>
      <th>4</th>
      <td>27.461538</td>
      <td>101.846154</td>
      <td>2056.384615</td>
      <td>16.961538</td>
      <td>1.923077</td>
    </tr>
    <tr>
      <th>6</th>
      <td>18.000000</td>
      <td>243.375000</td>
      <td>3171.875000</td>
      <td>14.750000</td>
      <td>1.000000</td>
    </tr>
  </tbody>
</table>
</div>



## Grab Based on Outside Index


```python
year_cyl.loc[70]
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
      <th>mpg</th>
      <th>displacement</th>
      <th>weight</th>
      <th>acceleration</th>
      <th>origin</th>
    </tr>
    <tr>
      <th>cylinders</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>4</th>
      <td>25.285714</td>
      <td>107.000000</td>
      <td>2292.571429</td>
      <td>16.000000</td>
      <td>2.285714</td>
    </tr>
    <tr>
      <th>6</th>
      <td>20.500000</td>
      <td>199.000000</td>
      <td>2710.500000</td>
      <td>15.500000</td>
      <td>1.000000</td>
    </tr>
    <tr>
      <th>8</th>
      <td>14.111111</td>
      <td>367.555556</td>
      <td>3940.055556</td>
      <td>11.194444</td>
      <td>1.000000</td>
    </tr>
  </tbody>
</table>
</div>




```python
year_cyl.loc[[70,72]]
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
      <th>mpg</th>
      <th>displacement</th>
      <th>weight</th>
      <th>acceleration</th>
      <th>origin</th>
    </tr>
    <tr>
      <th>model_year</th>
      <th>cylinders</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th rowspan="3" valign="top">70</th>
      <th>4</th>
      <td>25.285714</td>
      <td>107.000000</td>
      <td>2292.571429</td>
      <td>16.000000</td>
      <td>2.285714</td>
    </tr>
    <tr>
      <th>6</th>
      <td>20.500000</td>
      <td>199.000000</td>
      <td>2710.500000</td>
      <td>15.500000</td>
      <td>1.000000</td>
    </tr>
    <tr>
      <th>8</th>
      <td>14.111111</td>
      <td>367.555556</td>
      <td>3940.055556</td>
      <td>11.194444</td>
      <td>1.000000</td>
    </tr>
    <tr>
      <th rowspan="3" valign="top">72</th>
      <th>3</th>
      <td>19.000000</td>
      <td>70.000000</td>
      <td>2330.000000</td>
      <td>13.500000</td>
      <td>3.000000</td>
    </tr>
    <tr>
      <th>4</th>
      <td>23.428571</td>
      <td>111.535714</td>
      <td>2382.642857</td>
      <td>17.214286</td>
      <td>1.928571</td>
    </tr>
    <tr>
      <th>8</th>
      <td>13.615385</td>
      <td>344.846154</td>
      <td>4228.384615</td>
      <td>13.000000</td>
      <td>1.000000</td>
    </tr>
  </tbody>
</table>
</div>



## Grab a Single Row


```python
year_cyl.loc[(70,8)]
```




    mpg               14.111111
    displacement     367.555556
    weight          3940.055556
    acceleration      11.194444
    origin             1.000000
    Name: (70, 8), dtype: float64



# Grab Based on Cross-section with .xs()

This method takes a `key` argument to select data at a particular
level of a MultiIndex.

Parameters
----------
    key : label or tuple of label
        Label contained in the index, or partially in a MultiIndex.
    axis : {0 or 'index', 1 or 'columns'}, default 0
        Axis to retrieve cross-section on.
    level : object, defaults to first n levels (n=1 or len(key))
        In case of a key partially contained in a MultiIndex, indicate
        which levels are used. Levels can be referred by label or position.


```python
year_cyl.xs(key=70,axis=0,level='model_year')
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
      <th>mpg</th>
      <th>displacement</th>
      <th>weight</th>
      <th>acceleration</th>
      <th>origin</th>
    </tr>
    <tr>
      <th>cylinders</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>4</th>
      <td>25.285714</td>
      <td>107.000000</td>
      <td>2292.571429</td>
      <td>16.000000</td>
      <td>2.285714</td>
    </tr>
    <tr>
      <th>6</th>
      <td>20.500000</td>
      <td>199.000000</td>
      <td>2710.500000</td>
      <td>15.500000</td>
      <td>1.000000</td>
    </tr>
    <tr>
      <th>8</th>
      <td>14.111111</td>
      <td>367.555556</td>
      <td>3940.055556</td>
      <td>11.194444</td>
      <td>1.000000</td>
    </tr>
  </tbody>
</table>
</div>




```python
# Mean column values for 4 cylinders per year
year_cyl.xs(key=4,axis=0,level='cylinders')
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
      <th>mpg</th>
      <th>displacement</th>
      <th>weight</th>
      <th>acceleration</th>
      <th>origin</th>
    </tr>
    <tr>
      <th>model_year</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>70</th>
      <td>25.285714</td>
      <td>107.000000</td>
      <td>2292.571429</td>
      <td>16.000000</td>
      <td>2.285714</td>
    </tr>
    <tr>
      <th>71</th>
      <td>27.461538</td>
      <td>101.846154</td>
      <td>2056.384615</td>
      <td>16.961538</td>
      <td>1.923077</td>
    </tr>
    <tr>
      <th>72</th>
      <td>23.428571</td>
      <td>111.535714</td>
      <td>2382.642857</td>
      <td>17.214286</td>
      <td>1.928571</td>
    </tr>
    <tr>
      <th>73</th>
      <td>22.727273</td>
      <td>109.272727</td>
      <td>2338.090909</td>
      <td>17.136364</td>
      <td>2.000000</td>
    </tr>
    <tr>
      <th>74</th>
      <td>27.800000</td>
      <td>96.533333</td>
      <td>2151.466667</td>
      <td>16.400000</td>
      <td>2.200000</td>
    </tr>
    <tr>
      <th>75</th>
      <td>25.250000</td>
      <td>114.833333</td>
      <td>2489.250000</td>
      <td>15.833333</td>
      <td>2.166667</td>
    </tr>
    <tr>
      <th>76</th>
      <td>26.766667</td>
      <td>106.333333</td>
      <td>2306.600000</td>
      <td>16.866667</td>
      <td>1.866667</td>
    </tr>
    <tr>
      <th>77</th>
      <td>29.107143</td>
      <td>106.500000</td>
      <td>2205.071429</td>
      <td>16.064286</td>
      <td>1.857143</td>
    </tr>
    <tr>
      <th>78</th>
      <td>29.576471</td>
      <td>112.117647</td>
      <td>2296.764706</td>
      <td>16.282353</td>
      <td>2.117647</td>
    </tr>
    <tr>
      <th>79</th>
      <td>31.525000</td>
      <td>113.583333</td>
      <td>2357.583333</td>
      <td>15.991667</td>
      <td>1.583333</td>
    </tr>
    <tr>
      <th>80</th>
      <td>34.612000</td>
      <td>111.000000</td>
      <td>2360.080000</td>
      <td>17.144000</td>
      <td>2.200000</td>
    </tr>
    <tr>
      <th>81</th>
      <td>32.814286</td>
      <td>108.857143</td>
      <td>2275.476190</td>
      <td>16.466667</td>
      <td>2.095238</td>
    </tr>
    <tr>
      <th>82</th>
      <td>32.071429</td>
      <td>118.571429</td>
      <td>2402.321429</td>
      <td>16.703571</td>
      <td>1.714286</td>
    </tr>
  </tbody>
</table>
</div>



### Careful note!

Keep in mind, its usually much easier to filter out values **before** running a groupby() call, so you should attempt to filter out any values/categories you don't want to use. For example, its much easier to remove **4** cylinder cars before the groupby() call, very difficult to this sort of thing after a group by.


```python
df[df['cylinders'].isin([6,8])].groupby(['model_year','cylinders']).mean()
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
      <th>mpg</th>
      <th>displacement</th>
      <th>weight</th>
      <th>acceleration</th>
      <th>origin</th>
    </tr>
    <tr>
      <th>model_year</th>
      <th>cylinders</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th rowspan="2" valign="top">70</th>
      <th>6</th>
      <td>20.500000</td>
      <td>199.000000</td>
      <td>2710.500000</td>
      <td>15.500000</td>
      <td>1.000000</td>
    </tr>
    <tr>
      <th>8</th>
      <td>14.111111</td>
      <td>367.555556</td>
      <td>3940.055556</td>
      <td>11.194444</td>
      <td>1.000000</td>
    </tr>
    <tr>
      <th rowspan="2" valign="top">71</th>
      <th>6</th>
      <td>18.000000</td>
      <td>243.375000</td>
      <td>3171.875000</td>
      <td>14.750000</td>
      <td>1.000000</td>
    </tr>
    <tr>
      <th>8</th>
      <td>13.428571</td>
      <td>371.714286</td>
      <td>4537.714286</td>
      <td>12.214286</td>
      <td>1.000000</td>
    </tr>
    <tr>
      <th>72</th>
      <th>8</th>
      <td>13.615385</td>
      <td>344.846154</td>
      <td>4228.384615</td>
      <td>13.000000</td>
      <td>1.000000</td>
    </tr>
    <tr>
      <th rowspan="2" valign="top">73</th>
      <th>6</th>
      <td>19.000000</td>
      <td>212.250000</td>
      <td>2917.125000</td>
      <td>15.687500</td>
      <td>1.250000</td>
    </tr>
    <tr>
      <th>8</th>
      <td>13.200000</td>
      <td>365.250000</td>
      <td>4279.050000</td>
      <td>12.250000</td>
      <td>1.000000</td>
    </tr>
    <tr>
      <th rowspan="2" valign="top">74</th>
      <th>6</th>
      <td>17.857143</td>
      <td>230.428571</td>
      <td>3320.000000</td>
      <td>16.857143</td>
      <td>1.000000</td>
    </tr>
    <tr>
      <th>8</th>
      <td>14.200000</td>
      <td>315.200000</td>
      <td>4438.400000</td>
      <td>14.700000</td>
      <td>1.000000</td>
    </tr>
    <tr>
      <th rowspan="2" valign="top">75</th>
      <th>6</th>
      <td>17.583333</td>
      <td>233.750000</td>
      <td>3398.333333</td>
      <td>17.708333</td>
      <td>1.000000</td>
    </tr>
    <tr>
      <th>8</th>
      <td>15.666667</td>
      <td>330.500000</td>
      <td>4108.833333</td>
      <td>13.166667</td>
      <td>1.000000</td>
    </tr>
    <tr>
      <th rowspan="2" valign="top">76</th>
      <th>6</th>
      <td>20.000000</td>
      <td>221.400000</td>
      <td>3349.600000</td>
      <td>17.000000</td>
      <td>1.300000</td>
    </tr>
    <tr>
      <th>8</th>
      <td>14.666667</td>
      <td>324.000000</td>
      <td>4064.666667</td>
      <td>13.222222</td>
      <td>1.000000</td>
    </tr>
    <tr>
      <th rowspan="2" valign="top">77</th>
      <th>6</th>
      <td>19.500000</td>
      <td>220.400000</td>
      <td>3383.000000</td>
      <td>16.900000</td>
      <td>1.400000</td>
    </tr>
    <tr>
      <th>8</th>
      <td>16.000000</td>
      <td>335.750000</td>
      <td>4177.500000</td>
      <td>13.662500</td>
      <td>1.000000</td>
    </tr>
    <tr>
      <th rowspan="2" valign="top">78</th>
      <th>6</th>
      <td>19.066667</td>
      <td>213.250000</td>
      <td>3314.166667</td>
      <td>16.391667</td>
      <td>1.166667</td>
    </tr>
    <tr>
      <th>8</th>
      <td>19.050000</td>
      <td>300.833333</td>
      <td>3563.333333</td>
      <td>13.266667</td>
      <td>1.000000</td>
    </tr>
    <tr>
      <th rowspan="2" valign="top">79</th>
      <th>6</th>
      <td>22.950000</td>
      <td>205.666667</td>
      <td>3025.833333</td>
      <td>15.433333</td>
      <td>1.000000</td>
    </tr>
    <tr>
      <th>8</th>
      <td>18.630000</td>
      <td>321.400000</td>
      <td>3862.900000</td>
      <td>15.400000</td>
      <td>1.000000</td>
    </tr>
    <tr>
      <th>80</th>
      <th>6</th>
      <td>25.900000</td>
      <td>196.500000</td>
      <td>3145.500000</td>
      <td>15.050000</td>
      <td>2.000000</td>
    </tr>
    <tr>
      <th rowspan="2" valign="top">81</th>
      <th>6</th>
      <td>23.428571</td>
      <td>184.000000</td>
      <td>3093.571429</td>
      <td>15.442857</td>
      <td>1.714286</td>
    </tr>
    <tr>
      <th>8</th>
      <td>26.600000</td>
      <td>350.000000</td>
      <td>3725.000000</td>
      <td>19.000000</td>
      <td>1.000000</td>
    </tr>
    <tr>
      <th>82</th>
      <th>6</th>
      <td>28.333333</td>
      <td>225.000000</td>
      <td>2931.666667</td>
      <td>16.033333</td>
      <td>1.000000</td>
    </tr>
  </tbody>
</table>
</div>



## Swap Levels

* Swapping Levels: https://pandas.pydata.org/pandas-docs/stable/user_guide/advanced.html#swapping-levels-with-swaplevel
* Generalized Method is reorder_levels: https://pandas.pydata.org/pandas-docs/stable/user_guide/advanced.html#reordering-levels-with-reorder-levels


```python
year_cyl.swaplevel().head()
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
      <th>mpg</th>
      <th>displacement</th>
      <th>weight</th>
      <th>acceleration</th>
      <th>origin</th>
    </tr>
    <tr>
      <th>cylinders</th>
      <th>model_year</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>4</th>
      <th>70</th>
      <td>25.285714</td>
      <td>107.000000</td>
      <td>2292.571429</td>
      <td>16.000000</td>
      <td>2.285714</td>
    </tr>
    <tr>
      <th>6</th>
      <th>70</th>
      <td>20.500000</td>
      <td>199.000000</td>
      <td>2710.500000</td>
      <td>15.500000</td>
      <td>1.000000</td>
    </tr>
    <tr>
      <th>8</th>
      <th>70</th>
      <td>14.111111</td>
      <td>367.555556</td>
      <td>3940.055556</td>
      <td>11.194444</td>
      <td>1.000000</td>
    </tr>
    <tr>
      <th>4</th>
      <th>71</th>
      <td>27.461538</td>
      <td>101.846154</td>
      <td>2056.384615</td>
      <td>16.961538</td>
      <td>1.923077</td>
    </tr>
    <tr>
      <th>6</th>
      <th>71</th>
      <td>18.000000</td>
      <td>243.375000</td>
      <td>3171.875000</td>
      <td>14.750000</td>
      <td>1.000000</td>
    </tr>
  </tbody>
</table>
</div>



## Sorting MultiIndex

* https://pandas.pydata.org/pandas-docs/stable/user_guide/advanced.html#sorting-a-multiindex 


```python
year_cyl.sort_index(level='model_year',ascending=False)
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
      <th>mpg</th>
      <th>displacement</th>
      <th>weight</th>
      <th>acceleration</th>
      <th>origin</th>
    </tr>
    <tr>
      <th>model_year</th>
      <th>cylinders</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th rowspan="2" valign="top">82</th>
      <th>6</th>
      <td>28.333333</td>
      <td>225.000000</td>
      <td>2931.666667</td>
      <td>16.033333</td>
      <td>1.000000</td>
    </tr>
    <tr>
      <th>4</th>
      <td>32.071429</td>
      <td>118.571429</td>
      <td>2402.321429</td>
      <td>16.703571</td>
      <td>1.714286</td>
    </tr>
    <tr>
      <th rowspan="3" valign="top">81</th>
      <th>8</th>
      <td>26.600000</td>
      <td>350.000000</td>
      <td>3725.000000</td>
      <td>19.000000</td>
      <td>1.000000</td>
    </tr>
    <tr>
      <th>6</th>
      <td>23.428571</td>
      <td>184.000000</td>
      <td>3093.571429</td>
      <td>15.442857</td>
      <td>1.714286</td>
    </tr>
    <tr>
      <th>4</th>
      <td>32.814286</td>
      <td>108.857143</td>
      <td>2275.476190</td>
      <td>16.466667</td>
      <td>2.095238</td>
    </tr>
    <tr>
      <th rowspan="4" valign="top">80</th>
      <th>6</th>
      <td>25.900000</td>
      <td>196.500000</td>
      <td>3145.500000</td>
      <td>15.050000</td>
      <td>2.000000</td>
    </tr>
    <tr>
      <th>5</th>
      <td>36.400000</td>
      <td>121.000000</td>
      <td>2950.000000</td>
      <td>19.900000</td>
      <td>2.000000</td>
    </tr>
    <tr>
      <th>4</th>
      <td>34.612000</td>
      <td>111.000000</td>
      <td>2360.080000</td>
      <td>17.144000</td>
      <td>2.200000</td>
    </tr>
    <tr>
      <th>3</th>
      <td>23.700000</td>
      <td>70.000000</td>
      <td>2420.000000</td>
      <td>12.500000</td>
      <td>3.000000</td>
    </tr>
    <tr>
      <th rowspan="4" valign="top">79</th>
      <th>8</th>
      <td>18.630000</td>
      <td>321.400000</td>
      <td>3862.900000</td>
      <td>15.400000</td>
      <td>1.000000</td>
    </tr>
    <tr>
      <th>6</th>
      <td>22.950000</td>
      <td>205.666667</td>
      <td>3025.833333</td>
      <td>15.433333</td>
      <td>1.000000</td>
    </tr>
    <tr>
      <th>5</th>
      <td>25.400000</td>
      <td>183.000000</td>
      <td>3530.000000</td>
      <td>20.100000</td>
      <td>2.000000</td>
    </tr>
    <tr>
      <th>4</th>
      <td>31.525000</td>
      <td>113.583333</td>
      <td>2357.583333</td>
      <td>15.991667</td>
      <td>1.583333</td>
    </tr>
    <tr>
      <th rowspan="4" valign="top">78</th>
      <th>8</th>
      <td>19.050000</td>
      <td>300.833333</td>
      <td>3563.333333</td>
      <td>13.266667</td>
      <td>1.000000</td>
    </tr>
    <tr>
      <th>6</th>
      <td>19.066667</td>
      <td>213.250000</td>
      <td>3314.166667</td>
      <td>16.391667</td>
      <td>1.166667</td>
    </tr>
    <tr>
      <th>5</th>
      <td>20.300000</td>
      <td>131.000000</td>
      <td>2830.000000</td>
      <td>15.900000</td>
      <td>2.000000</td>
    </tr>
    <tr>
      <th>4</th>
      <td>29.576471</td>
      <td>112.117647</td>
      <td>2296.764706</td>
      <td>16.282353</td>
      <td>2.117647</td>
    </tr>
    <tr>
      <th rowspan="4" valign="top">77</th>
      <th>8</th>
      <td>16.000000</td>
      <td>335.750000</td>
      <td>4177.500000</td>
      <td>13.662500</td>
      <td>1.000000</td>
    </tr>
    <tr>
      <th>6</th>
      <td>19.500000</td>
      <td>220.400000</td>
      <td>3383.000000</td>
      <td>16.900000</td>
      <td>1.400000</td>
    </tr>
    <tr>
      <th>4</th>
      <td>29.107143</td>
      <td>106.500000</td>
      <td>2205.071429</td>
      <td>16.064286</td>
      <td>1.857143</td>
    </tr>
    <tr>
      <th>3</th>
      <td>21.500000</td>
      <td>80.000000</td>
      <td>2720.000000</td>
      <td>13.500000</td>
      <td>3.000000</td>
    </tr>
    <tr>
      <th rowspan="3" valign="top">76</th>
      <th>8</th>
      <td>14.666667</td>
      <td>324.000000</td>
      <td>4064.666667</td>
      <td>13.222222</td>
      <td>1.000000</td>
    </tr>
    <tr>
      <th>6</th>
      <td>20.000000</td>
      <td>221.400000</td>
      <td>3349.600000</td>
      <td>17.000000</td>
      <td>1.300000</td>
    </tr>
    <tr>
      <th>4</th>
      <td>26.766667</td>
      <td>106.333333</td>
      <td>2306.600000</td>
      <td>16.866667</td>
      <td>1.866667</td>
    </tr>
    <tr>
      <th rowspan="3" valign="top">75</th>
      <th>8</th>
      <td>15.666667</td>
      <td>330.500000</td>
      <td>4108.833333</td>
      <td>13.166667</td>
      <td>1.000000</td>
    </tr>
    <tr>
      <th>6</th>
      <td>17.583333</td>
      <td>233.750000</td>
      <td>3398.333333</td>
      <td>17.708333</td>
      <td>1.000000</td>
    </tr>
    <tr>
      <th>4</th>
      <td>25.250000</td>
      <td>114.833333</td>
      <td>2489.250000</td>
      <td>15.833333</td>
      <td>2.166667</td>
    </tr>
    <tr>
      <th rowspan="3" valign="top">74</th>
      <th>8</th>
      <td>14.200000</td>
      <td>315.200000</td>
      <td>4438.400000</td>
      <td>14.700000</td>
      <td>1.000000</td>
    </tr>
    <tr>
      <th>6</th>
      <td>17.857143</td>
      <td>230.428571</td>
      <td>3320.000000</td>
      <td>16.857143</td>
      <td>1.000000</td>
    </tr>
    <tr>
      <th>4</th>
      <td>27.800000</td>
      <td>96.533333</td>
      <td>2151.466667</td>
      <td>16.400000</td>
      <td>2.200000</td>
    </tr>
    <tr>
      <th rowspan="4" valign="top">73</th>
      <th>8</th>
      <td>13.200000</td>
      <td>365.250000</td>
      <td>4279.050000</td>
      <td>12.250000</td>
      <td>1.000000</td>
    </tr>
    <tr>
      <th>6</th>
      <td>19.000000</td>
      <td>212.250000</td>
      <td>2917.125000</td>
      <td>15.687500</td>
      <td>1.250000</td>
    </tr>
    <tr>
      <th>4</th>
      <td>22.727273</td>
      <td>109.272727</td>
      <td>2338.090909</td>
      <td>17.136364</td>
      <td>2.000000</td>
    </tr>
    <tr>
      <th>3</th>
      <td>18.000000</td>
      <td>70.000000</td>
      <td>2124.000000</td>
      <td>13.500000</td>
      <td>3.000000</td>
    </tr>
    <tr>
      <th rowspan="3" valign="top">72</th>
      <th>8</th>
      <td>13.615385</td>
      <td>344.846154</td>
      <td>4228.384615</td>
      <td>13.000000</td>
      <td>1.000000</td>
    </tr>
    <tr>
      <th>4</th>
      <td>23.428571</td>
      <td>111.535714</td>
      <td>2382.642857</td>
      <td>17.214286</td>
      <td>1.928571</td>
    </tr>
    <tr>
      <th>3</th>
      <td>19.000000</td>
      <td>70.000000</td>
      <td>2330.000000</td>
      <td>13.500000</td>
      <td>3.000000</td>
    </tr>
    <tr>
      <th rowspan="3" valign="top">71</th>
      <th>8</th>
      <td>13.428571</td>
      <td>371.714286</td>
      <td>4537.714286</td>
      <td>12.214286</td>
      <td>1.000000</td>
    </tr>
    <tr>
      <th>6</th>
      <td>18.000000</td>
      <td>243.375000</td>
      <td>3171.875000</td>
      <td>14.750000</td>
      <td>1.000000</td>
    </tr>
    <tr>
      <th>4</th>
      <td>27.461538</td>
      <td>101.846154</td>
      <td>2056.384615</td>
      <td>16.961538</td>
      <td>1.923077</td>
    </tr>
    <tr>
      <th rowspan="3" valign="top">70</th>
      <th>8</th>
      <td>14.111111</td>
      <td>367.555556</td>
      <td>3940.055556</td>
      <td>11.194444</td>
      <td>1.000000</td>
    </tr>
    <tr>
      <th>6</th>
      <td>20.500000</td>
      <td>199.000000</td>
      <td>2710.500000</td>
      <td>15.500000</td>
      <td>1.000000</td>
    </tr>
    <tr>
      <th>4</th>
      <td>25.285714</td>
      <td>107.000000</td>
      <td>2292.571429</td>
      <td>16.000000</td>
      <td>2.285714</td>
    </tr>
  </tbody>
</table>
</div>




```python
year_cyl.sort_index(level='cylinders',ascending=False)
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
      <th>mpg</th>
      <th>displacement</th>
      <th>weight</th>
      <th>acceleration</th>
      <th>origin</th>
    </tr>
    <tr>
      <th>model_year</th>
      <th>cylinders</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>81</th>
      <th>8</th>
      <td>26.600000</td>
      <td>350.000000</td>
      <td>3725.000000</td>
      <td>19.000000</td>
      <td>1.000000</td>
    </tr>
    <tr>
      <th>79</th>
      <th>8</th>
      <td>18.630000</td>
      <td>321.400000</td>
      <td>3862.900000</td>
      <td>15.400000</td>
      <td>1.000000</td>
    </tr>
    <tr>
      <th>78</th>
      <th>8</th>
      <td>19.050000</td>
      <td>300.833333</td>
      <td>3563.333333</td>
      <td>13.266667</td>
      <td>1.000000</td>
    </tr>
    <tr>
      <th>77</th>
      <th>8</th>
      <td>16.000000</td>
      <td>335.750000</td>
      <td>4177.500000</td>
      <td>13.662500</td>
      <td>1.000000</td>
    </tr>
    <tr>
      <th>76</th>
      <th>8</th>
      <td>14.666667</td>
      <td>324.000000</td>
      <td>4064.666667</td>
      <td>13.222222</td>
      <td>1.000000</td>
    </tr>
    <tr>
      <th>75</th>
      <th>8</th>
      <td>15.666667</td>
      <td>330.500000</td>
      <td>4108.833333</td>
      <td>13.166667</td>
      <td>1.000000</td>
    </tr>
    <tr>
      <th>74</th>
      <th>8</th>
      <td>14.200000</td>
      <td>315.200000</td>
      <td>4438.400000</td>
      <td>14.700000</td>
      <td>1.000000</td>
    </tr>
    <tr>
      <th>73</th>
      <th>8</th>
      <td>13.200000</td>
      <td>365.250000</td>
      <td>4279.050000</td>
      <td>12.250000</td>
      <td>1.000000</td>
    </tr>
    <tr>
      <th>72</th>
      <th>8</th>
      <td>13.615385</td>
      <td>344.846154</td>
      <td>4228.384615</td>
      <td>13.000000</td>
      <td>1.000000</td>
    </tr>
    <tr>
      <th>71</th>
      <th>8</th>
      <td>13.428571</td>
      <td>371.714286</td>
      <td>4537.714286</td>
      <td>12.214286</td>
      <td>1.000000</td>
    </tr>
    <tr>
      <th>70</th>
      <th>8</th>
      <td>14.111111</td>
      <td>367.555556</td>
      <td>3940.055556</td>
      <td>11.194444</td>
      <td>1.000000</td>
    </tr>
    <tr>
      <th>82</th>
      <th>6</th>
      <td>28.333333</td>
      <td>225.000000</td>
      <td>2931.666667</td>
      <td>16.033333</td>
      <td>1.000000</td>
    </tr>
    <tr>
      <th>81</th>
      <th>6</th>
      <td>23.428571</td>
      <td>184.000000</td>
      <td>3093.571429</td>
      <td>15.442857</td>
      <td>1.714286</td>
    </tr>
    <tr>
      <th>80</th>
      <th>6</th>
      <td>25.900000</td>
      <td>196.500000</td>
      <td>3145.500000</td>
      <td>15.050000</td>
      <td>2.000000</td>
    </tr>
    <tr>
      <th>79</th>
      <th>6</th>
      <td>22.950000</td>
      <td>205.666667</td>
      <td>3025.833333</td>
      <td>15.433333</td>
      <td>1.000000</td>
    </tr>
    <tr>
      <th>78</th>
      <th>6</th>
      <td>19.066667</td>
      <td>213.250000</td>
      <td>3314.166667</td>
      <td>16.391667</td>
      <td>1.166667</td>
    </tr>
    <tr>
      <th>77</th>
      <th>6</th>
      <td>19.500000</td>
      <td>220.400000</td>
      <td>3383.000000</td>
      <td>16.900000</td>
      <td>1.400000</td>
    </tr>
    <tr>
      <th>76</th>
      <th>6</th>
      <td>20.000000</td>
      <td>221.400000</td>
      <td>3349.600000</td>
      <td>17.000000</td>
      <td>1.300000</td>
    </tr>
    <tr>
      <th>75</th>
      <th>6</th>
      <td>17.583333</td>
      <td>233.750000</td>
      <td>3398.333333</td>
      <td>17.708333</td>
      <td>1.000000</td>
    </tr>
    <tr>
      <th>74</th>
      <th>6</th>
      <td>17.857143</td>
      <td>230.428571</td>
      <td>3320.000000</td>
      <td>16.857143</td>
      <td>1.000000</td>
    </tr>
    <tr>
      <th>73</th>
      <th>6</th>
      <td>19.000000</td>
      <td>212.250000</td>
      <td>2917.125000</td>
      <td>15.687500</td>
      <td>1.250000</td>
    </tr>
    <tr>
      <th>71</th>
      <th>6</th>
      <td>18.000000</td>
      <td>243.375000</td>
      <td>3171.875000</td>
      <td>14.750000</td>
      <td>1.000000</td>
    </tr>
    <tr>
      <th>70</th>
      <th>6</th>
      <td>20.500000</td>
      <td>199.000000</td>
      <td>2710.500000</td>
      <td>15.500000</td>
      <td>1.000000</td>
    </tr>
    <tr>
      <th>80</th>
      <th>5</th>
      <td>36.400000</td>
      <td>121.000000</td>
      <td>2950.000000</td>
      <td>19.900000</td>
      <td>2.000000</td>
    </tr>
    <tr>
      <th>79</th>
      <th>5</th>
      <td>25.400000</td>
      <td>183.000000</td>
      <td>3530.000000</td>
      <td>20.100000</td>
      <td>2.000000</td>
    </tr>
    <tr>
      <th>78</th>
      <th>5</th>
      <td>20.300000</td>
      <td>131.000000</td>
      <td>2830.000000</td>
      <td>15.900000</td>
      <td>2.000000</td>
    </tr>
    <tr>
      <th>82</th>
      <th>4</th>
      <td>32.071429</td>
      <td>118.571429</td>
      <td>2402.321429</td>
      <td>16.703571</td>
      <td>1.714286</td>
    </tr>
    <tr>
      <th>81</th>
      <th>4</th>
      <td>32.814286</td>
      <td>108.857143</td>
      <td>2275.476190</td>
      <td>16.466667</td>
      <td>2.095238</td>
    </tr>
    <tr>
      <th>80</th>
      <th>4</th>
      <td>34.612000</td>
      <td>111.000000</td>
      <td>2360.080000</td>
      <td>17.144000</td>
      <td>2.200000</td>
    </tr>
    <tr>
      <th>79</th>
      <th>4</th>
      <td>31.525000</td>
      <td>113.583333</td>
      <td>2357.583333</td>
      <td>15.991667</td>
      <td>1.583333</td>
    </tr>
    <tr>
      <th>78</th>
      <th>4</th>
      <td>29.576471</td>
      <td>112.117647</td>
      <td>2296.764706</td>
      <td>16.282353</td>
      <td>2.117647</td>
    </tr>
    <tr>
      <th>77</th>
      <th>4</th>
      <td>29.107143</td>
      <td>106.500000</td>
      <td>2205.071429</td>
      <td>16.064286</td>
      <td>1.857143</td>
    </tr>
    <tr>
      <th>76</th>
      <th>4</th>
      <td>26.766667</td>
      <td>106.333333</td>
      <td>2306.600000</td>
      <td>16.866667</td>
      <td>1.866667</td>
    </tr>
    <tr>
      <th>75</th>
      <th>4</th>
      <td>25.250000</td>
      <td>114.833333</td>
      <td>2489.250000</td>
      <td>15.833333</td>
      <td>2.166667</td>
    </tr>
    <tr>
      <th>74</th>
      <th>4</th>
      <td>27.800000</td>
      <td>96.533333</td>
      <td>2151.466667</td>
      <td>16.400000</td>
      <td>2.200000</td>
    </tr>
    <tr>
      <th>73</th>
      <th>4</th>
      <td>22.727273</td>
      <td>109.272727</td>
      <td>2338.090909</td>
      <td>17.136364</td>
      <td>2.000000</td>
    </tr>
    <tr>
      <th>72</th>
      <th>4</th>
      <td>23.428571</td>
      <td>111.535714</td>
      <td>2382.642857</td>
      <td>17.214286</td>
      <td>1.928571</td>
    </tr>
    <tr>
      <th>71</th>
      <th>4</th>
      <td>27.461538</td>
      <td>101.846154</td>
      <td>2056.384615</td>
      <td>16.961538</td>
      <td>1.923077</td>
    </tr>
    <tr>
      <th>70</th>
      <th>4</th>
      <td>25.285714</td>
      <td>107.000000</td>
      <td>2292.571429</td>
      <td>16.000000</td>
      <td>2.285714</td>
    </tr>
    <tr>
      <th>80</th>
      <th>3</th>
      <td>23.700000</td>
      <td>70.000000</td>
      <td>2420.000000</td>
      <td>12.500000</td>
      <td>3.000000</td>
    </tr>
    <tr>
      <th>77</th>
      <th>3</th>
      <td>21.500000</td>
      <td>80.000000</td>
      <td>2720.000000</td>
      <td>13.500000</td>
      <td>3.000000</td>
    </tr>
    <tr>
      <th>73</th>
      <th>3</th>
      <td>18.000000</td>
      <td>70.000000</td>
      <td>2124.000000</td>
      <td>13.500000</td>
      <td>3.000000</td>
    </tr>
    <tr>
      <th>72</th>
      <th>3</th>
      <td>19.000000</td>
      <td>70.000000</td>
      <td>2330.000000</td>
      <td>13.500000</td>
      <td>3.000000</td>
    </tr>
  </tbody>
</table>
</div>



# Advanced: agg() method

The agg() method allows you to customize what aggregate functions you want per category


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
      <th>mpg</th>
      <th>cylinders</th>
      <th>displacement</th>
      <th>horsepower</th>
      <th>weight</th>
      <th>acceleration</th>
      <th>model_year</th>
      <th>origin</th>
      <th>name</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>18.0</td>
      <td>8</td>
      <td>307.0</td>
      <td>130</td>
      <td>3504</td>
      <td>12.0</td>
      <td>70</td>
      <td>1</td>
      <td>chevrolet chevelle malibu</td>
    </tr>
    <tr>
      <th>1</th>
      <td>15.0</td>
      <td>8</td>
      <td>350.0</td>
      <td>165</td>
      <td>3693</td>
      <td>11.5</td>
      <td>70</td>
      <td>1</td>
      <td>buick skylark 320</td>
    </tr>
    <tr>
      <th>2</th>
      <td>18.0</td>
      <td>8</td>
      <td>318.0</td>
      <td>150</td>
      <td>3436</td>
      <td>11.0</td>
      <td>70</td>
      <td>1</td>
      <td>plymouth satellite</td>
    </tr>
    <tr>
      <th>3</th>
      <td>16.0</td>
      <td>8</td>
      <td>304.0</td>
      <td>150</td>
      <td>3433</td>
      <td>12.0</td>
      <td>70</td>
      <td>1</td>
      <td>amc rebel sst</td>
    </tr>
    <tr>
      <th>4</th>
      <td>17.0</td>
      <td>8</td>
      <td>302.0</td>
      <td>140</td>
      <td>3449</td>
      <td>10.5</td>
      <td>70</td>
      <td>1</td>
      <td>ford torino</td>
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
    </tr>
    <tr>
      <th>393</th>
      <td>27.0</td>
      <td>4</td>
      <td>140.0</td>
      <td>86</td>
      <td>2790</td>
      <td>15.6</td>
      <td>82</td>
      <td>1</td>
      <td>ford mustang gl</td>
    </tr>
    <tr>
      <th>394</th>
      <td>44.0</td>
      <td>4</td>
      <td>97.0</td>
      <td>52</td>
      <td>2130</td>
      <td>24.6</td>
      <td>82</td>
      <td>2</td>
      <td>vw pickup</td>
    </tr>
    <tr>
      <th>395</th>
      <td>32.0</td>
      <td>4</td>
      <td>135.0</td>
      <td>84</td>
      <td>2295</td>
      <td>11.6</td>
      <td>82</td>
      <td>1</td>
      <td>dodge rampage</td>
    </tr>
    <tr>
      <th>396</th>
      <td>28.0</td>
      <td>4</td>
      <td>120.0</td>
      <td>79</td>
      <td>2625</td>
      <td>18.6</td>
      <td>82</td>
      <td>1</td>
      <td>ford ranger</td>
    </tr>
    <tr>
      <th>397</th>
      <td>31.0</td>
      <td>4</td>
      <td>119.0</td>
      <td>82</td>
      <td>2720</td>
      <td>19.4</td>
      <td>82</td>
      <td>1</td>
      <td>chevy s-10</td>
    </tr>
  </tbody>
</table>
<p>398 rows × 9 columns</p>
</div>



## agg() on a DataFrame


```python
# These strings need to match up with built-in method names
df.agg(['median','mean'])
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
      <th>mpg</th>
      <th>cylinders</th>
      <th>displacement</th>
      <th>weight</th>
      <th>acceleration</th>
      <th>model_year</th>
      <th>origin</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>median</th>
      <td>23.000000</td>
      <td>4.000000</td>
      <td>148.500000</td>
      <td>2803.500000</td>
      <td>15.50000</td>
      <td>76.00000</td>
      <td>1.000000</td>
    </tr>
    <tr>
      <th>mean</th>
      <td>23.514573</td>
      <td>5.454774</td>
      <td>193.425879</td>
      <td>2970.424623</td>
      <td>15.56809</td>
      <td>76.01005</td>
      <td>1.572864</td>
    </tr>
  </tbody>
</table>
</div>




```python
df.agg(['sum','mean'])[['mpg','weight']]
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
      <th>mpg</th>
      <th>weight</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>sum</th>
      <td>9358.800000</td>
      <td>1.182229e+06</td>
    </tr>
    <tr>
      <th>mean</th>
      <td>23.514573</td>
      <td>2.970425e+03</td>
    </tr>
  </tbody>
</table>
</div>



### Specify aggregate methods per column

**agg()** is very powerful,allowing you to pass in a dictionary where the keys are the columns and the values are a list of aggregate methods.


```python
df.agg({'mpg':['median','mean'],'weight':['mean','std']})
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
      <th>mpg</th>
      <th>weight</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>median</th>
      <td>23.000000</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>mean</th>
      <td>23.514573</td>
      <td>2970.424623</td>
    </tr>
    <tr>
      <th>std</th>
      <td>NaN</td>
      <td>846.841774</td>
    </tr>
  </tbody>
</table>
</div>



## agg() with groupby()


```python
df.groupby('model_year').agg({'mpg':['median','mean'],'weight':['mean','std']})
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
      <th colspan="2" halign="left">mpg</th>
      <th colspan="2" halign="left">weight</th>
    </tr>
    <tr>
      <th></th>
      <th>median</th>
      <th>mean</th>
      <th>mean</th>
      <th>std</th>
    </tr>
    <tr>
      <th>model_year</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>70</th>
      <td>16.00</td>
      <td>17.689655</td>
      <td>3372.793103</td>
      <td>852.868663</td>
    </tr>
    <tr>
      <th>71</th>
      <td>19.00</td>
      <td>21.250000</td>
      <td>2995.428571</td>
      <td>1061.830859</td>
    </tr>
    <tr>
      <th>72</th>
      <td>18.50</td>
      <td>18.714286</td>
      <td>3237.714286</td>
      <td>974.520960</td>
    </tr>
    <tr>
      <th>73</th>
      <td>16.00</td>
      <td>17.100000</td>
      <td>3419.025000</td>
      <td>974.809133</td>
    </tr>
    <tr>
      <th>74</th>
      <td>24.00</td>
      <td>22.703704</td>
      <td>2877.925926</td>
      <td>949.308571</td>
    </tr>
    <tr>
      <th>75</th>
      <td>19.50</td>
      <td>20.266667</td>
      <td>3176.800000</td>
      <td>765.179781</td>
    </tr>
    <tr>
      <th>76</th>
      <td>21.00</td>
      <td>21.573529</td>
      <td>3078.735294</td>
      <td>821.371481</td>
    </tr>
    <tr>
      <th>77</th>
      <td>21.75</td>
      <td>23.375000</td>
      <td>2997.357143</td>
      <td>912.825902</td>
    </tr>
    <tr>
      <th>78</th>
      <td>20.70</td>
      <td>24.061111</td>
      <td>2861.805556</td>
      <td>626.023907</td>
    </tr>
    <tr>
      <th>79</th>
      <td>23.90</td>
      <td>25.093103</td>
      <td>3055.344828</td>
      <td>747.881497</td>
    </tr>
    <tr>
      <th>80</th>
      <td>32.70</td>
      <td>33.696552</td>
      <td>2436.655172</td>
      <td>432.235491</td>
    </tr>
    <tr>
      <th>81</th>
      <td>31.60</td>
      <td>30.334483</td>
      <td>2522.931034</td>
      <td>533.600501</td>
    </tr>
    <tr>
      <th>82</th>
      <td>32.00</td>
      <td>31.709677</td>
      <td>2453.548387</td>
      <td>354.276713</td>
    </tr>
  </tbody>
</table>
</div>


