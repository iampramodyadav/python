<h1>Table of Contents<span class="tocSkip"></span></h1>
<div class="toc"><ul class="toc-item"><li><span><a href="#DataFrames" data-toc-modified-id="DataFrames-1"><span class="toc-item-num">1&nbsp;&nbsp;</span>DataFrames</a></span><ul class="toc-item"><li><span><a href="#Imports" data-toc-modified-id="Imports-1.1"><span class="toc-item-num">1.1&nbsp;&nbsp;</span>Imports</a></span><ul class="toc-item"><li><span><a href="#Creating-a-DataFrame-from-Python-Objects" data-toc-modified-id="Creating-a-DataFrame-from-Python-Objects-1.1.1"><span class="toc-item-num">1.1.1&nbsp;&nbsp;</span>Creating a DataFrame from Python Objects</a></span></li></ul></li></ul></li><li><span><a href="#Reading-a-.csv-file-for-a-DataFrame" data-toc-modified-id="Reading-a-.csv-file-for-a-DataFrame-2"><span class="toc-item-num">2&nbsp;&nbsp;</span>Reading a .csv file for a DataFrame</a></span><ul class="toc-item"><li><span><a href="#CSV" data-toc-modified-id="CSV-2.1"><span class="toc-item-num">2.1&nbsp;&nbsp;</span>CSV</a></span><ul class="toc-item"><li><span><a href="#Understanding-File-Paths" data-toc-modified-id="Understanding-File-Paths-2.1.1"><span class="toc-item-num">2.1.1&nbsp;&nbsp;</span>Understanding File Paths</a></span><ul class="toc-item"><li><span><a href="#Print-your-current-directory-file-path-with-pwd" data-toc-modified-id="Print-your-current-directory-file-path-with-pwd-2.1.1.1"><span class="toc-item-num">2.1.1.1&nbsp;&nbsp;</span>Print your current directory file path with pwd</a></span></li><li><span><a href="#List-the-files-in-your-current-directory-with-ls" data-toc-modified-id="List-the-files-in-your-current-directory-with-ls-2.1.1.2"><span class="toc-item-num">2.1.1.2&nbsp;&nbsp;</span>List the files in your current directory with ls</a></span></li></ul></li></ul></li></ul></li><li><span><a href="#DataFrames" data-toc-modified-id="DataFrames-3"><span class="toc-item-num">3&nbsp;&nbsp;</span>DataFrames</a></span><ul class="toc-item"><li><span><a href="#Obtaining-Basic-Information-About-DataFrame" data-toc-modified-id="Obtaining-Basic-Information-About-DataFrame-3.1"><span class="toc-item-num">3.1&nbsp;&nbsp;</span>Obtaining Basic Information About DataFrame</a></span></li><li><span><a href="#Selection-and-Indexing" data-toc-modified-id="Selection-and-Indexing-3.2"><span class="toc-item-num">3.2&nbsp;&nbsp;</span>Selection and Indexing</a></span><ul class="toc-item"><li><span><a href="#COLUMNS" data-toc-modified-id="COLUMNS-3.2.1"><span class="toc-item-num">3.2.1&nbsp;&nbsp;</span>COLUMNS</a></span><ul class="toc-item"><li><span><a href="#Grab-a-Single-Column" data-toc-modified-id="Grab-a-Single-Column-3.2.1.1"><span class="toc-item-num">3.2.1.1&nbsp;&nbsp;</span>Grab a Single Column</a></span></li><li><span><a href="#Grab-Multiple-Columns" data-toc-modified-id="Grab-Multiple-Columns-3.2.1.2"><span class="toc-item-num">3.2.1.2&nbsp;&nbsp;</span>Grab Multiple Columns</a></span></li><li><span><a href="#Create-New-Columns" data-toc-modified-id="Create-New-Columns-3.2.1.3"><span class="toc-item-num">3.2.1.3&nbsp;&nbsp;</span>Create New Columns</a></span></li><li><span><a href="#Adjust-Existing-Columns" data-toc-modified-id="Adjust-Existing-Columns-3.2.1.4"><span class="toc-item-num">3.2.1.4&nbsp;&nbsp;</span>Adjust Existing Columns</a></span></li><li><span><a href="#Remove-Columns" data-toc-modified-id="Remove-Columns-3.2.1.5"><span class="toc-item-num">3.2.1.5&nbsp;&nbsp;</span>Remove Columns</a></span></li></ul></li></ul></li></ul></li><li><span><a href="#Index-Basics" data-toc-modified-id="Index-Basics-4"><span class="toc-item-num">4&nbsp;&nbsp;</span>Index Basics</a></span><ul class="toc-item"><li><ul class="toc-item"><li><span><a href="#ROWS" data-toc-modified-id="ROWS-4.0.1"><span class="toc-item-num">4.0.1&nbsp;&nbsp;</span>ROWS</a></span><ul class="toc-item"><li><span><a href="#Grab-a-Single-Row" data-toc-modified-id="Grab-a-Single-Row-4.0.1.1"><span class="toc-item-num">4.0.1.1&nbsp;&nbsp;</span>Grab a Single Row</a></span></li><li><span><a href="#Grab-Multiple-Rows" data-toc-modified-id="Grab-Multiple-Rows-4.0.1.2"><span class="toc-item-num">4.0.1.2&nbsp;&nbsp;</span>Grab Multiple Rows</a></span></li><li><span><a href="#Remove-Row" data-toc-modified-id="Remove-Row-4.0.1.3"><span class="toc-item-num">4.0.1.3&nbsp;&nbsp;</span>Remove Row</a></span></li><li><span><a href="#Insert-a-New-Row" data-toc-modified-id="Insert-a-New-Row-4.0.1.4"><span class="toc-item-num">4.0.1.4&nbsp;&nbsp;</span>Insert a New Row</a></span></li></ul></li></ul></li></ul></li></ul></div>

# DataFrames

Throughout the course, most of our data exploration will be done with DataFrames. DataFrames are an extremely powerful tool and a natural extension of the Pandas Series. By definition all a DataFrame is:

**A Pandas DataFrame consists of multiple Pandas Series that share index values.**

## Imports


```python
import numpy as np
import pandas as pd
```

### Creating a DataFrame from Python Objects


```python
# help(pd.DataFrame)
```


```python
# Make sure the seed is in the same cell as the random call
# https://stackoverflow.com/questions/21494489/what-does-numpy-random-seed0-do
np.random.seed(101)
mydata = np.random.randint(0,101,(4,3))
```


```python
mydata
```




    array([[95, 11, 81],
           [70, 63, 87],
           [75,  9, 77],
           [40,  4, 63]])




```python
myindex = ['CA','NY','AZ','TX']
```


```python
mycolumns = ['Jan','Feb','Mar']
```


```python
df = pd.DataFrame(data=mydata)
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
      <th>0</th>
      <th>1</th>
      <th>2</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>95</td>
      <td>11</td>
      <td>81</td>
    </tr>
    <tr>
      <th>1</th>
      <td>70</td>
      <td>63</td>
      <td>87</td>
    </tr>
    <tr>
      <th>2</th>
      <td>75</td>
      <td>9</td>
      <td>77</td>
    </tr>
    <tr>
      <th>3</th>
      <td>40</td>
      <td>4</td>
      <td>63</td>
    </tr>
  </tbody>
</table>
</div>




```python
df = pd.DataFrame(data=mydata,index=myindex)
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
      <th>0</th>
      <th>1</th>
      <th>2</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>CA</th>
      <td>95</td>
      <td>11</td>
      <td>81</td>
    </tr>
    <tr>
      <th>NY</th>
      <td>70</td>
      <td>63</td>
      <td>87</td>
    </tr>
    <tr>
      <th>AZ</th>
      <td>75</td>
      <td>9</td>
      <td>77</td>
    </tr>
    <tr>
      <th>TX</th>
      <td>40</td>
      <td>4</td>
      <td>63</td>
    </tr>
  </tbody>
</table>
</div>




```python
df = pd.DataFrame(data=mydata,index=myindex,columns=mycolumns)
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
      <th>Jan</th>
      <th>Feb</th>
      <th>Mar</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>CA</th>
      <td>95</td>
      <td>11</td>
      <td>81</td>
    </tr>
    <tr>
      <th>NY</th>
      <td>70</td>
      <td>63</td>
      <td>87</td>
    </tr>
    <tr>
      <th>AZ</th>
      <td>75</td>
      <td>9</td>
      <td>77</td>
    </tr>
    <tr>
      <th>TX</th>
      <td>40</td>
      <td>4</td>
      <td>63</td>
    </tr>
  </tbody>
</table>
</div>




```python
df.info()
```

    <class 'pandas.core.frame.DataFrame'>
    Index: 4 entries, CA to TX
    Data columns (total 3 columns):
    Jan    4 non-null int32
    Feb    4 non-null int32
    Mar    4 non-null int32
    dtypes: int32(3)
    memory usage: 80.0+ bytes
    


# Reading a .csv file for a DataFrame

----

 Note:**We will go over all kinds of data inputs and outputs (.html, .csv, .xlxs , etc...) later on in the course! For now we just need to read in a simple .csv file.**

----

## CSV
Comma Separated Values files are text files that use commas as field delimeters.<br>
Unless you're running the virtual environment included with the course, you may need to install <tt>xlrd</tt> and <tt>openpyxl</tt>.<br>
In your terminal/command prompt run:

    conda install xlrd
    conda install openpyxl

Then restart Jupyter Notebook.
(or use pip install if you aren't using the Anaconda Distribution)

### Understanding File Paths

You have two options when reading a file with pandas:

1. If your .py file or .ipynb notebook is located in the **exact** same folder location as the .csv file you want to read, simply pass in the file name as a string, for example:
    
        df = pd.read_csv('some_file.csv')
        
2. Pass in the entire file path if you are located in a different directory. The file path must be 100% correct in order for this to work. For example:

        df = pd.read_csv("C:\\Users\\myself\\files\\some_file.csv")

#### Print your current directory file path with pwd


```python
pwd
```




    'C:\\Users\\PRAMOD\\Desktop\\ML-Udemy\\03-Pandas'



#### List the files in your current directory with ls


```python
ls
```

     Volume in drive C has no label.
     Volume Serial Number is 2E8A-6B5E
    
     Directory of C:\Users\PRAMOD\Desktop\ML-Udemy\03-Pandas
    
    06/01/2021  06:23 PM    <DIR>          .
    06/01/2021  06:23 PM    <DIR>          ..
    09/28/2020  02:22 AM    <DIR>          .ipynb_checkpoints
    07/13/2020  12:37 AM    <DIR>          __pycache__
    06/01/2021  03:55 PM            14,311 00-Series.ipynb
    06/01/2021  06:23 PM           214,402 01-DataFrames.ipynb
    09/08/2020  11:29 PM           194,591 02-Conditional-Filtering.ipynb
    08/13/2020  06:19 AM           196,385 03-Useful-Methods.ipynb
    07/02/2020  04:02 AM            64,227 04-Missing-Data.ipynb
    07/05/2020  01:58 AM           219,627 05-Groupby-Operations-and-MultiIndex.ipynb
    07/05/2020  03:49 AM            62,966 06-Combining-DataFrames.ipynb
    09/25/2020  11:34 PM            32,972 07-Text-Methods.ipynb
    09/08/2020  11:29 PM            93,392 08-Time-Methods.ipynb
    09/26/2020  05:18 AM            65,234 09-Inputs-and-Outputs.ipynb
    09/26/2020  05:16 AM           101,081 10-Pivot-Tables.ipynb
    09/28/2020  02:04 AM            47,135 11-Pandas-Project-Exercise .ipynb
    09/28/2020  02:04 AM            52,576 12-Pandas-Project-Exercise-Solution.ipynb
    07/05/2020  06:09 AM                51 example.csv
    09/27/2020  12:44 AM             5,022 example.xlsx
    07/13/2020  01:11 AM        25,112,317 hotel_booking_data.csv
    02/08/2020  12:56 AM               177 movie_scores.csv
    07/02/2020  04:26 AM            17,727 mpg.csv
    07/05/2020  06:28 AM             5,022 my_excel_file.xlsx
    07/05/2020  06:40 AM                51 new_file.csv
    09/27/2020  12:35 AM             5,021 new_workbook.xlsx
    09/26/2020  05:46 AM                51 newfile.csv
    07/12/2020  12:44 AM            52,132 reshaping_pivot.png
    07/03/2020  06:26 AM             5,459 RetailSales_BeerWineLiquor.csv
    07/07/2020  05:40 AM             1,320 Sales_Funnel_CRM.csv
    09/26/2020  11:10 PM             1,330 sample_table.html
    07/05/2020  06:40 AM               555 simple.html
    01/28/2020  02:58 AM            18,752 tips.csv
                  28 File(s)     26,583,886 bytes
                   4 Dir(s)  18,530,562,048 bytes free
    


```python
df = pd.read_csv('tips.csv')
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
    </tr>
    <tr>
      <th>240</th>
      <td>27.18</td>
      <td>2.00</td>
      <td>Female</td>
      <td>Yes</td>
      <td>Sat</td>
      <td>Dinner</td>
      <td>2</td>
      <td>13.59</td>
      <td>Monica Sanders</td>
      <td>3506806155565404</td>
      <td>Sat1766</td>
    </tr>
    <tr>
      <th>241</th>
      <td>22.67</td>
      <td>2.00</td>
      <td>Male</td>
      <td>Yes</td>
      <td>Sat</td>
      <td>Dinner</td>
      <td>2</td>
      <td>11.34</td>
      <td>Keith Wong</td>
      <td>6011891618747196</td>
      <td>Sat3880</td>
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
    </tr>
  </tbody>
</table>
<p>244 rows × 11 columns</p>
</div>



----
About this DataSet (in case you are interested)

* Description
    * One waiter recorded information about each tip he received over a period of a few months working in one restaurant. He collected several variables:

* Format
    * A data frame with 244 rows and 7 variables

* Details
    * tip in dollars,
    * bill in dollars,
    * sex of the bill payer,
    * whether there were smokers in the party,
    * day of the week,
    * time of day,
    * size of the party.

In all he recorded 244 tips. The data was reported in a collection of case studies for business statistics (Bryant & Smith 1995).

* References
    * Bryant, P. G. and Smith, M (1995) Practical Data Analysis: Case Studies in Business Statistics. Homewood, IL: Richard D. Irwin Publishing:
    
* Note: We created some additional columns with Fake data, including Name, CC Number, and Payment ID.

----

# DataFrames

## Obtaining Basic Information About DataFrame


```python
df.columns
```




    Index(['total_bill', 'tip', 'sex', 'smoker', 'day', 'time', 'size',
           'price_per_person', 'Payer Name', 'CC Number', 'Payment ID'],
          dtype='object')




```python
df.index
```




    RangeIndex(start=0, stop=244, step=1)




```python
df.head(3)
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
  </tbody>
</table>
</div>




```python
df.tail(3)
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
      <th>241</th>
      <td>22.67</td>
      <td>2.00</td>
      <td>Male</td>
      <td>Yes</td>
      <td>Sat</td>
      <td>Dinner</td>
      <td>2</td>
      <td>11.34</td>
      <td>Keith Wong</td>
      <td>6011891618747196</td>
      <td>Sat3880</td>
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
    </tr>
  </tbody>
</table>
</div>




```python
df.info()
```

    <class 'pandas.core.frame.DataFrame'>
    RangeIndex: 244 entries, 0 to 243
    Data columns (total 11 columns):
    total_bill          244 non-null float64
    tip                 244 non-null float64
    sex                 244 non-null object
    smoker              244 non-null object
    day                 244 non-null object
    time                244 non-null object
    size                244 non-null int64
    price_per_person    244 non-null float64
    Payer Name          244 non-null object
    CC Number           244 non-null int64
    Payment ID          244 non-null object
    dtypes: float64(3), int64(2), object(6)
    memory usage: 21.0+ KB
    


```python
len(df)
```




    244




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



## Selection and Indexing

Let's learn how to retrieve information from a DataFrame.

### COLUMNS

We will begin be learning how to extract information based on the columns


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



#### Grab a Single Column


```python
df['total_bill']
```




    0      16.99
    1      10.34
    2      21.01
    3      23.68
    4      24.59
    5      25.29
    6       8.77
    7      26.88
    8      15.04
    9      14.78
    10     10.27
    11     35.26
    12     15.42
    13     18.43
    14     14.83
    15     21.58
    16     10.33
    17     16.29
    18     16.97
    19     20.65
    20     17.92
    21     20.29
    22     15.77
    23     39.42
    24     19.82
    25     17.81
    26     13.37
    27     12.69
    28     21.70
    29     19.65
           ...  
    214    28.17
    215    12.90
    216    28.15
    217    11.59
    218     7.74
    219    30.14
    220    12.16
    221    13.42
    222     8.58
    223    15.98
    224    13.42
    225    16.27
    226    10.09
    227    20.45
    228    13.28
    229    22.12
    230    24.01
    231    15.69
    232    11.61
    233    10.77
    234    15.53
    235    10.07
    236    12.60
    237    32.83
    238    35.83
    239    29.03
    240    27.18
    241    22.67
    242    17.82
    243    18.78
    Name: total_bill, Length: 244, dtype: float64




```python
type(df['total_bill'])
```




    pandas.core.series.Series



#### Grab Multiple Columns


```python
# Note how its a python list of column names! Thus the double brackets.
df[['total_bill','tip']]
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
      <th>0</th>
      <td>16.99</td>
      <td>1.01</td>
    </tr>
    <tr>
      <th>1</th>
      <td>10.34</td>
      <td>1.66</td>
    </tr>
    <tr>
      <th>2</th>
      <td>21.01</td>
      <td>3.50</td>
    </tr>
    <tr>
      <th>3</th>
      <td>23.68</td>
      <td>3.31</td>
    </tr>
    <tr>
      <th>4</th>
      <td>24.59</td>
      <td>3.61</td>
    </tr>
    <tr>
      <th>5</th>
      <td>25.29</td>
      <td>4.71</td>
    </tr>
    <tr>
      <th>6</th>
      <td>8.77</td>
      <td>2.00</td>
    </tr>
    <tr>
      <th>7</th>
      <td>26.88</td>
      <td>3.12</td>
    </tr>
    <tr>
      <th>8</th>
      <td>15.04</td>
      <td>1.96</td>
    </tr>
    <tr>
      <th>9</th>
      <td>14.78</td>
      <td>3.23</td>
    </tr>
    <tr>
      <th>10</th>
      <td>10.27</td>
      <td>1.71</td>
    </tr>
    <tr>
      <th>11</th>
      <td>35.26</td>
      <td>5.00</td>
    </tr>
    <tr>
      <th>12</th>
      <td>15.42</td>
      <td>1.57</td>
    </tr>
    <tr>
      <th>13</th>
      <td>18.43</td>
      <td>3.00</td>
    </tr>
    <tr>
      <th>14</th>
      <td>14.83</td>
      <td>3.02</td>
    </tr>
    <tr>
      <th>15</th>
      <td>21.58</td>
      <td>3.92</td>
    </tr>
    <tr>
      <th>16</th>
      <td>10.33</td>
      <td>1.67</td>
    </tr>
    <tr>
      <th>17</th>
      <td>16.29</td>
      <td>3.71</td>
    </tr>
    <tr>
      <th>18</th>
      <td>16.97</td>
      <td>3.50</td>
    </tr>
    <tr>
      <th>19</th>
      <td>20.65</td>
      <td>3.35</td>
    </tr>
    <tr>
      <th>20</th>
      <td>17.92</td>
      <td>4.08</td>
    </tr>
    <tr>
      <th>21</th>
      <td>20.29</td>
      <td>2.75</td>
    </tr>
    <tr>
      <th>22</th>
      <td>15.77</td>
      <td>2.23</td>
    </tr>
    <tr>
      <th>23</th>
      <td>39.42</td>
      <td>7.58</td>
    </tr>
    <tr>
      <th>24</th>
      <td>19.82</td>
      <td>3.18</td>
    </tr>
    <tr>
      <th>25</th>
      <td>17.81</td>
      <td>2.34</td>
    </tr>
    <tr>
      <th>26</th>
      <td>13.37</td>
      <td>2.00</td>
    </tr>
    <tr>
      <th>27</th>
      <td>12.69</td>
      <td>2.00</td>
    </tr>
    <tr>
      <th>28</th>
      <td>21.70</td>
      <td>4.30</td>
    </tr>
    <tr>
      <th>29</th>
      <td>19.65</td>
      <td>3.00</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>214</th>
      <td>28.17</td>
      <td>6.50</td>
    </tr>
    <tr>
      <th>215</th>
      <td>12.90</td>
      <td>1.10</td>
    </tr>
    <tr>
      <th>216</th>
      <td>28.15</td>
      <td>3.00</td>
    </tr>
    <tr>
      <th>217</th>
      <td>11.59</td>
      <td>1.50</td>
    </tr>
    <tr>
      <th>218</th>
      <td>7.74</td>
      <td>1.44</td>
    </tr>
    <tr>
      <th>219</th>
      <td>30.14</td>
      <td>3.09</td>
    </tr>
    <tr>
      <th>220</th>
      <td>12.16</td>
      <td>2.20</td>
    </tr>
    <tr>
      <th>221</th>
      <td>13.42</td>
      <td>3.48</td>
    </tr>
    <tr>
      <th>222</th>
      <td>8.58</td>
      <td>1.92</td>
    </tr>
    <tr>
      <th>223</th>
      <td>15.98</td>
      <td>3.00</td>
    </tr>
    <tr>
      <th>224</th>
      <td>13.42</td>
      <td>1.58</td>
    </tr>
    <tr>
      <th>225</th>
      <td>16.27</td>
      <td>2.50</td>
    </tr>
    <tr>
      <th>226</th>
      <td>10.09</td>
      <td>2.00</td>
    </tr>
    <tr>
      <th>227</th>
      <td>20.45</td>
      <td>3.00</td>
    </tr>
    <tr>
      <th>228</th>
      <td>13.28</td>
      <td>2.72</td>
    </tr>
    <tr>
      <th>229</th>
      <td>22.12</td>
      <td>2.88</td>
    </tr>
    <tr>
      <th>230</th>
      <td>24.01</td>
      <td>2.00</td>
    </tr>
    <tr>
      <th>231</th>
      <td>15.69</td>
      <td>3.00</td>
    </tr>
    <tr>
      <th>232</th>
      <td>11.61</td>
      <td>3.39</td>
    </tr>
    <tr>
      <th>233</th>
      <td>10.77</td>
      <td>1.47</td>
    </tr>
    <tr>
      <th>234</th>
      <td>15.53</td>
      <td>3.00</td>
    </tr>
    <tr>
      <th>235</th>
      <td>10.07</td>
      <td>1.25</td>
    </tr>
    <tr>
      <th>236</th>
      <td>12.60</td>
      <td>1.00</td>
    </tr>
    <tr>
      <th>237</th>
      <td>32.83</td>
      <td>1.17</td>
    </tr>
    <tr>
      <th>238</th>
      <td>35.83</td>
      <td>4.67</td>
    </tr>
    <tr>
      <th>239</th>
      <td>29.03</td>
      <td>5.92</td>
    </tr>
    <tr>
      <th>240</th>
      <td>27.18</td>
      <td>2.00</td>
    </tr>
    <tr>
      <th>241</th>
      <td>22.67</td>
      <td>2.00</td>
    </tr>
    <tr>
      <th>242</th>
      <td>17.82</td>
      <td>1.75</td>
    </tr>
    <tr>
      <th>243</th>
      <td>18.78</td>
      <td>3.00</td>
    </tr>
  </tbody>
</table>
<p>244 rows × 2 columns</p>
</div>



#### Create New Columns


```python
df['tip_percentage'] = 100* df['tip'] / df['total_bill']
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
      <th>tip_percentage</th>
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
      <td>5.944673</td>
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
      <td>16.054159</td>
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
      <td>16.658734</td>
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
      <td>13.978041</td>
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
      <td>14.680765</td>
    </tr>
  </tbody>
</table>
</div>




```python
df['price_per_person'] = df['total_bill'] / df['size']
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
      <th>tip_percentage</th>
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
      <td>8.495000</td>
      <td>Christy Cunningham</td>
      <td>3560325168603410</td>
      <td>Sun2959</td>
      <td>5.944673</td>
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
      <td>3.446667</td>
      <td>Douglas Tucker</td>
      <td>4478071379779230</td>
      <td>Sun4608</td>
      <td>16.054159</td>
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
      <td>7.003333</td>
      <td>Travis Walters</td>
      <td>6011812112971322</td>
      <td>Sun4458</td>
      <td>16.658734</td>
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
      <td>11.840000</td>
      <td>Nathaniel Harris</td>
      <td>4676137647685994</td>
      <td>Sun5260</td>
      <td>13.978041</td>
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
      <td>6.147500</td>
      <td>Tonya Carter</td>
      <td>4832732618637221</td>
      <td>Sun2251</td>
      <td>14.680765</td>
    </tr>
  </tbody>
</table>
</div>




```python
help(np.round)
```

    Help on function round_ in module numpy:
    
    round_(a, decimals=0, out=None)
        Round an array to the given number of decimals.
        
        See Also
        --------
        around : equivalent function; see for details.
    
    

#### Adjust Existing Columns


```python
# Because pandas is based on numpy, we get awesome capabilities with numpy's universal functions!
df['price_per_person'] = np.round(df['price_per_person'],2)
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
      <th>tip_percentage</th>
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
      <td>5.944673</td>
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
      <td>16.054159</td>
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
      <td>16.658734</td>
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
      <td>13.978041</td>
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
      <td>14.680765</td>
    </tr>
  </tbody>
</table>
</div>



#### Remove Columns


```python
# df.drop('tip_percentage',axis=1)
```


```python
df = df.drop("tip_percentage",axis=1)
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



# Index Basics

Before going over the same retrieval tasks for rows, let's build some basic understanding of the pandas DataFrame Index.


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




```python
df.index
```




    RangeIndex(start=0, stop=244, step=1)




```python
df.set_index('Payment ID')
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
    </tr>
    <tr>
      <th>Payment ID</th>
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
      <th>Sun2959</th>
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
    </tr>
    <tr>
      <th>Sun4608</th>
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
    </tr>
    <tr>
      <th>Sun4458</th>
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
    </tr>
    <tr>
      <th>Sun5260</th>
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
    </tr>
    <tr>
      <th>Sun2251</th>
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
    </tr>
    <tr>
      <th>Sun9679</th>
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
    </tr>
    <tr>
      <th>Sun5985</th>
      <td>8.77</td>
      <td>2.00</td>
      <td>Male</td>
      <td>No</td>
      <td>Sun</td>
      <td>Dinner</td>
      <td>2</td>
      <td>4.38</td>
      <td>Kristopher Johnson</td>
      <td>2223727524230344</td>
    </tr>
    <tr>
      <th>Sun8157</th>
      <td>26.88</td>
      <td>3.12</td>
      <td>Male</td>
      <td>No</td>
      <td>Sun</td>
      <td>Dinner</td>
      <td>4</td>
      <td>6.72</td>
      <td>Robert Buck</td>
      <td>3514785077705092</td>
    </tr>
    <tr>
      <th>Sun6820</th>
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
    </tr>
    <tr>
      <th>Sun3775</th>
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
    </tr>
    <tr>
      <th>Sun2546</th>
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
    </tr>
    <tr>
      <th>Sun6686</th>
      <td>35.26</td>
      <td>5.00</td>
      <td>Female</td>
      <td>No</td>
      <td>Sun</td>
      <td>Dinner</td>
      <td>4</td>
      <td>8.82</td>
      <td>Diane Macias</td>
      <td>4577817359320969</td>
    </tr>
    <tr>
      <th>Sun1300</th>
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
    </tr>
    <tr>
      <th>Sun2971</th>
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
    </tr>
    <tr>
      <th>Sun3848</th>
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
    </tr>
    <tr>
      <th>Sun1878</th>
      <td>21.58</td>
      <td>3.92</td>
      <td>Male</td>
      <td>No</td>
      <td>Sun</td>
      <td>Dinner</td>
      <td>2</td>
      <td>10.79</td>
      <td>Matthew Reilly</td>
      <td>180073029785069</td>
    </tr>
    <tr>
      <th>Sun9715</th>
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
    </tr>
    <tr>
      <th>Sun2998</th>
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
    </tr>
    <tr>
      <th>Sun2789</th>
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
    </tr>
    <tr>
      <th>Sat9213</th>
      <td>20.65</td>
      <td>3.35</td>
      <td>Male</td>
      <td>No</td>
      <td>Sat</td>
      <td>Dinner</td>
      <td>3</td>
      <td>6.88</td>
      <td>Timothy Oneal</td>
      <td>6568069240986485</td>
    </tr>
    <tr>
      <th>Sat1709</th>
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
    </tr>
    <tr>
      <th>Sat9618</th>
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
    </tr>
    <tr>
      <th>Sat9786</th>
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
    </tr>
    <tr>
      <th>Sat239</th>
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
    </tr>
    <tr>
      <th>Sat6236</th>
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
    </tr>
    <tr>
      <th>Sat907</th>
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
    </tr>
    <tr>
      <th>Sat6651</th>
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
    </tr>
    <tr>
      <th>Sat394</th>
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
    </tr>
    <tr>
      <th>Sat3697</th>
      <td>21.70</td>
      <td>4.30</td>
      <td>Male</td>
      <td>No</td>
      <td>Sat</td>
      <td>Dinner</td>
      <td>2</td>
      <td>10.85</td>
      <td>David Collier</td>
      <td>5529694315416009</td>
    </tr>
    <tr>
      <th>Sat2467</th>
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
    </tr>
    <tr>
      <th>Sat3374</th>
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
    </tr>
    <tr>
      <th>Sat6983</th>
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
    </tr>
    <tr>
      <th>Sat7320</th>
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
    </tr>
    <tr>
      <th>Sat8489</th>
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
    </tr>
    <tr>
      <th>Sat4772</th>
      <td>7.74</td>
      <td>1.44</td>
      <td>Male</td>
      <td>Yes</td>
      <td>Sat</td>
      <td>Dinner</td>
      <td>2</td>
      <td>3.87</td>
      <td>Nicholas Archer</td>
      <td>340517153733524</td>
    </tr>
    <tr>
      <th>Sat8863</th>
      <td>30.14</td>
      <td>3.09</td>
      <td>Female</td>
      <td>Yes</td>
      <td>Sat</td>
      <td>Dinner</td>
      <td>4</td>
      <td>7.54</td>
      <td>Shelby House</td>
      <td>502097403252</td>
    </tr>
    <tr>
      <th>Fri4607</th>
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
    </tr>
    <tr>
      <th>Fri7511</th>
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
    </tr>
    <tr>
      <th>Fri6624</th>
      <td>8.58</td>
      <td>1.92</td>
      <td>Male</td>
      <td>Yes</td>
      <td>Fri</td>
      <td>Lunch</td>
      <td>1</td>
      <td>8.58</td>
      <td>Jason Lawrence</td>
      <td>3505302934650403</td>
    </tr>
    <tr>
      <th>Fri6014</th>
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
    </tr>
    <tr>
      <th>Fri5959</th>
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
    </tr>
    <tr>
      <th>Fri6665</th>
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
    </tr>
    <tr>
      <th>Fri6359</th>
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
    </tr>
    <tr>
      <th>Sat4319</th>
      <td>20.45</td>
      <td>3.00</td>
      <td>Male</td>
      <td>No</td>
      <td>Sat</td>
      <td>Dinner</td>
      <td>4</td>
      <td>5.11</td>
      <td>Robert Bradley</td>
      <td>213141668145910</td>
    </tr>
    <tr>
      <th>Sat2937</th>
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
    </tr>
    <tr>
      <th>Sat3943</th>
      <td>22.12</td>
      <td>2.88</td>
      <td>Female</td>
      <td>Yes</td>
      <td>Sat</td>
      <td>Dinner</td>
      <td>2</td>
      <td>11.06</td>
      <td>Jennifer Russell</td>
      <td>4793003293608</td>
    </tr>
    <tr>
      <th>Sat7872</th>
      <td>24.01</td>
      <td>2.00</td>
      <td>Male</td>
      <td>Yes</td>
      <td>Sat</td>
      <td>Dinner</td>
      <td>4</td>
      <td>6.00</td>
      <td>Michael Osborne</td>
      <td>4258682154026</td>
    </tr>
    <tr>
      <th>Sat6334</th>
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
    </tr>
    <tr>
      <th>Sat2124</th>
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
    </tr>
    <tr>
      <th>Sat1467</th>
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
    </tr>
    <tr>
      <th>Sat7220</th>
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
    </tr>
    <tr>
      <th>Sat4615</th>
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
    </tr>
    <tr>
      <th>Sat5032</th>
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
    </tr>
    <tr>
      <th>Sat2929</th>
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
    </tr>
    <tr>
      <th>Sat9777</th>
      <td>35.83</td>
      <td>4.67</td>
      <td>Female</td>
      <td>No</td>
      <td>Sat</td>
      <td>Dinner</td>
      <td>3</td>
      <td>11.94</td>
      <td>Kimberly Crane</td>
      <td>676184013727</td>
    </tr>
    <tr>
      <th>Sat2657</th>
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
    </tr>
    <tr>
      <th>Sat1766</th>
      <td>27.18</td>
      <td>2.00</td>
      <td>Female</td>
      <td>Yes</td>
      <td>Sat</td>
      <td>Dinner</td>
      <td>2</td>
      <td>13.59</td>
      <td>Monica Sanders</td>
      <td>3506806155565404</td>
    </tr>
    <tr>
      <th>Sat3880</th>
      <td>22.67</td>
      <td>2.00</td>
      <td>Male</td>
      <td>Yes</td>
      <td>Sat</td>
      <td>Dinner</td>
      <td>2</td>
      <td>11.34</td>
      <td>Keith Wong</td>
      <td>6011891618747196</td>
    </tr>
    <tr>
      <th>Sat17</th>
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
    </tr>
    <tr>
      <th>Thur672</th>
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
    </tr>
  </tbody>
</table>
<p>244 rows × 10 columns</p>
</div>




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




```python
df = df.set_index('Payment ID')
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
    </tr>
    <tr>
      <th>Payment ID</th>
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
      <th>Sun2959</th>
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
    </tr>
    <tr>
      <th>Sun4608</th>
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
    </tr>
    <tr>
      <th>Sun4458</th>
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
    </tr>
    <tr>
      <th>Sun5260</th>
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
    </tr>
    <tr>
      <th>Sun2251</th>
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
    </tr>
  </tbody>
</table>
</div>




```python
df = df.reset_index()
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
      <th>Payment ID</th>
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
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Sun2959</td>
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
    </tr>
    <tr>
      <th>1</th>
      <td>Sun4608</td>
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
    </tr>
    <tr>
      <th>2</th>
      <td>Sun4458</td>
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
    </tr>
    <tr>
      <th>3</th>
      <td>Sun5260</td>
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
    </tr>
    <tr>
      <th>4</th>
      <td>Sun2251</td>
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
    </tr>
  </tbody>
</table>
</div>



### ROWS

Let's now explore these same concepts but with Rows.


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
      <th>Payment ID</th>
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
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Sun2959</td>
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
    </tr>
    <tr>
      <th>1</th>
      <td>Sun4608</td>
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
    </tr>
    <tr>
      <th>2</th>
      <td>Sun4458</td>
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
    </tr>
    <tr>
      <th>3</th>
      <td>Sun5260</td>
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
    </tr>
    <tr>
      <th>4</th>
      <td>Sun2251</td>
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
    </tr>
  </tbody>
</table>
</div>




```python
df = df.set_index('Payment ID')
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
    </tr>
    <tr>
      <th>Payment ID</th>
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
      <th>Sun2959</th>
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
    </tr>
    <tr>
      <th>Sun4608</th>
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
    </tr>
    <tr>
      <th>Sun4458</th>
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
    </tr>
    <tr>
      <th>Sun5260</th>
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
    </tr>
    <tr>
      <th>Sun2251</th>
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
    </tr>
  </tbody>
</table>
</div>



#### Grab a Single Row


```python
# Integer Based
df.iloc[0]
```




    total_bill                       16.99
    tip                               1.01
    sex                             Female
    smoker                              No
    day                                Sun
    time                            Dinner
    size                                 2
    price_per_person                  8.49
    Payer Name          Christy Cunningham
    CC Number             3560325168603410
    Name: Sun2959, dtype: object




```python
# Name Based
df.loc['Sun2959']
```




    total_bill                       16.99
    tip                               1.01
    sex                             Female
    smoker                              No
    day                                Sun
    time                            Dinner
    size                                 2
    price_per_person                  8.49
    Payer Name          Christy Cunningham
    CC Number             3560325168603410
    Name: Sun2959, dtype: object



#### Grab Multiple Rows


```python
df.iloc[0:4]
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
    </tr>
    <tr>
      <th>Payment ID</th>
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
      <th>Sun2959</th>
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
    </tr>
    <tr>
      <th>Sun4608</th>
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
    </tr>
    <tr>
      <th>Sun4458</th>
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
    </tr>
    <tr>
      <th>Sun5260</th>
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
    </tr>
  </tbody>
</table>
</div>




```python
df.loc[['Sun2959','Sun5260']]
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
    </tr>
    <tr>
      <th>Payment ID</th>
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
      <th>Sun2959</th>
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
    </tr>
    <tr>
      <th>Sun5260</th>
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
    </tr>
  </tbody>
</table>
</div>



#### Remove Row

Typically are datasets will be large enough that we won't remove rows like this since we won't know thier row location for some specific condition, instead, we drop rows based on conditions such as missing data or column values. The next lecture will cover this in a lot more detail.


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
    </tr>
    <tr>
      <th>Payment ID</th>
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
      <th>Sun2959</th>
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
    </tr>
    <tr>
      <th>Sun4608</th>
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
    </tr>
    <tr>
      <th>Sun4458</th>
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
    </tr>
    <tr>
      <th>Sun5260</th>
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
    </tr>
    <tr>
      <th>Sun2251</th>
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
    </tr>
  </tbody>
</table>
</div>




```python
df.drop('Sun2959',axis=0).head()
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
    </tr>
    <tr>
      <th>Payment ID</th>
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
      <th>Sun4608</th>
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
    </tr>
    <tr>
      <th>Sun4458</th>
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
    </tr>
    <tr>
      <th>Sun5260</th>
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
    </tr>
    <tr>
      <th>Sun2251</th>
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
    </tr>
    <tr>
      <th>Sun9679</th>
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
    </tr>
  </tbody>
</table>
</div>




```python
# Error if you have a named index!
# df.drop(0,axis=0).head()
```

#### Insert a New Row

Pretty rare to add a single row like this. Usually you use pd.concat() to add many rows at once. You could use the .append() method with a list of pd.Series() objects, but you won't see us do this with realistic real-world data.


```python
one_row = df.iloc[0]
```


```python
one_row
```




    total_bill                       16.99
    tip                               1.01
    sex                             Female
    smoker                              No
    day                                Sun
    time                            Dinner
    size                                 2
    price_per_person                  8.49
    Payer Name          Christy Cunningham
    CC Number             3560325168603410
    Name: Sun2959, dtype: object




```python
type(one_row)
```




    pandas.core.series.Series




```python
df.tail()
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
    </tr>
    <tr>
      <th>Payment ID</th>
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
      <th>Sat2657</th>
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
    </tr>
    <tr>
      <th>Sat1766</th>
      <td>27.18</td>
      <td>2.00</td>
      <td>Female</td>
      <td>Yes</td>
      <td>Sat</td>
      <td>Dinner</td>
      <td>2</td>
      <td>13.59</td>
      <td>Monica Sanders</td>
      <td>3506806155565404</td>
    </tr>
    <tr>
      <th>Sat3880</th>
      <td>22.67</td>
      <td>2.00</td>
      <td>Male</td>
      <td>Yes</td>
      <td>Sat</td>
      <td>Dinner</td>
      <td>2</td>
      <td>11.34</td>
      <td>Keith Wong</td>
      <td>6011891618747196</td>
    </tr>
    <tr>
      <th>Sat17</th>
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
    </tr>
    <tr>
      <th>Thur672</th>
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
    </tr>
  </tbody>
</table>
</div>




```python
df.append(one_row).tail()
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
    </tr>
    <tr>
      <th>Payment ID</th>
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
      <th>Sat1766</th>
      <td>27.18</td>
      <td>2.00</td>
      <td>Female</td>
      <td>Yes</td>
      <td>Sat</td>
      <td>Dinner</td>
      <td>2</td>
      <td>13.59</td>
      <td>Monica Sanders</td>
      <td>3506806155565404</td>
    </tr>
    <tr>
      <th>Sat3880</th>
      <td>22.67</td>
      <td>2.00</td>
      <td>Male</td>
      <td>Yes</td>
      <td>Sat</td>
      <td>Dinner</td>
      <td>2</td>
      <td>11.34</td>
      <td>Keith Wong</td>
      <td>6011891618747196</td>
    </tr>
    <tr>
      <th>Sat17</th>
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
    </tr>
    <tr>
      <th>Thur672</th>
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
    </tr>
    <tr>
      <th>Sun2959</th>
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
    </tr>
  </tbody>
</table>
</div>



--------
