<h1>Table of Contents<span class="tocSkip"></span></h1>
<div class="toc"><ul class="toc-item"><li><span><a href="#Inputs-and-Outputs" data-toc-modified-id="Inputs-and-Outputs-1"><span class="toc-item-num">1&nbsp;&nbsp;</span>Inputs and Outputs</a></span><ul class="toc-item"><li><span><a href="#Data-Input-and-Output" data-toc-modified-id="Data-Input-and-Output-1.1"><span class="toc-item-num">1.1&nbsp;&nbsp;</span>Data Input and Output</a></span></li><li><span><a href="#Check-out-the-references-here!" data-toc-modified-id="Check-out-the-references-here!-1.2"><span class="toc-item-num">1.2&nbsp;&nbsp;</span>Check out the references here!</a></span></li></ul></li><li><span><a href="#Reading-in-a--CSV" data-toc-modified-id="Reading-in-a--CSV-2"><span class="toc-item-num">2&nbsp;&nbsp;</span>Reading in a  CSV</a></span><ul class="toc-item"><li><span><a href="#Understanding-File-Paths" data-toc-modified-id="Understanding-File-Paths-2.1"><span class="toc-item-num">2.1&nbsp;&nbsp;</span>Understanding File Paths</a></span><ul class="toc-item"><li><ul class="toc-item"><li><span><a href="#Print-your-current-directory-file-path-with-pwd" data-toc-modified-id="Print-your-current-directory-file-path-with-pwd-2.1.0.1"><span class="toc-item-num">2.1.0.1&nbsp;&nbsp;</span>Print your current directory file path with pwd</a></span></li><li><span><a href="#List-the-files-in-your-current-directory-with-ls" data-toc-modified-id="List-the-files-in-your-current-directory-with-ls-2.1.0.2"><span class="toc-item-num">2.1.0.2&nbsp;&nbsp;</span>List the files in your current directory with ls</a></span></li><li><span><a href="#NOTE!" data-toc-modified-id="NOTE!-2.1.0.3"><span class="toc-item-num">2.1.0.3&nbsp;&nbsp;</span>NOTE!</a></span></li></ul></li><li><span><a href="#CSV-Input" data-toc-modified-id="CSV-Input-2.1.1"><span class="toc-item-num">2.1.1&nbsp;&nbsp;</span>CSV Input</a></span></li><li><span><a href="#CSV-Output" data-toc-modified-id="CSV-Output-2.1.2"><span class="toc-item-num">2.1.2&nbsp;&nbsp;</span>CSV Output</a></span></li></ul></li><li><span><a href="#HTML" data-toc-modified-id="HTML-2.2"><span class="toc-item-num">2.2&nbsp;&nbsp;</span>HTML</a></span></li><li><span><a href="#read_html" data-toc-modified-id="read_html-2.3"><span class="toc-item-num">2.3&nbsp;&nbsp;</span>read_html</a></span><ul class="toc-item"><li><span><a href="#HTML-Input" data-toc-modified-id="HTML-Input-2.3.1"><span class="toc-item-num">2.3.1&nbsp;&nbsp;</span>HTML Input</a></span></li><li><span><a href="#Not-Useful-Tables" data-toc-modified-id="Not-Useful-Tables-2.3.2"><span class="toc-item-num">2.3.2&nbsp;&nbsp;</span>Not Useful Tables</a></span></li><li><span><a href="#Tables-that-need-formatting" data-toc-modified-id="Tables-that-need-formatting-2.3.3"><span class="toc-item-num">2.3.3&nbsp;&nbsp;</span>Tables that need formatting</a></span></li><li><span><a href="#Tables-that-are-intact" data-toc-modified-id="Tables-that-are-intact-2.3.4"><span class="toc-item-num">2.3.4&nbsp;&nbsp;</span>Tables that are intact</a></span></li></ul></li><li><span><a href="#Write-to-html-Output" data-toc-modified-id="Write-to-html-Output-2.4"><span class="toc-item-num">2.4&nbsp;&nbsp;</span>Write to html Output</a></span></li></ul></li><li><span><a href="#Excel-Files" data-toc-modified-id="Excel-Files-3"><span class="toc-item-num">3&nbsp;&nbsp;</span>Excel Files</a></span><ul class="toc-item"><li><ul class="toc-item"><li><ul class="toc-item"><li><span><a href="#NOTE:" data-toc-modified-id="NOTE:-3.0.0.1"><span class="toc-item-num">3.0.0.1&nbsp;&nbsp;</span>NOTE:</a></span></li></ul></li></ul></li><li><span><a href="#Excel-file-input-with-read_excel()" data-toc-modified-id="Excel-file-input-with-read_excel()-3.1"><span class="toc-item-num">3.1&nbsp;&nbsp;</span>Excel file input with read_excel()</a></span><ul class="toc-item"><li><span><a href="#What-if" data-toc-modified-id="What-if-3.1.1"><span class="toc-item-num">3.1.1&nbsp;&nbsp;</span>What if</a></span><ul class="toc-item"><li><span><a href="#Grab-all-sheets" data-toc-modified-id="Grab-all-sheets-3.1.1.1"><span class="toc-item-num">3.1.1.1&nbsp;&nbsp;</span>Grab all sheets</a></span></li></ul></li><li><span><a href="#Write-to-Excel-File" data-toc-modified-id="Write-to-Excel-File-3.1.2"><span class="toc-item-num">3.1.2&nbsp;&nbsp;</span>Write to Excel File</a></span></li></ul></li></ul></li><li><span><a href="#SQL-Connections" data-toc-modified-id="SQL-Connections-4"><span class="toc-item-num">4&nbsp;&nbsp;</span>SQL Connections</a></span><ul class="toc-item"><li><ul class="toc-item"><li><ul class="toc-item"><li><span><a href="#NOTE:" data-toc-modified-id="NOTE:-4.0.0.1"><span class="toc-item-num">4.0.0.1&nbsp;&nbsp;</span>NOTE:</a></span></li></ul></li></ul></li><li><span><a href="#Example-SQL-Database-(temporary-in-your-RAM)" data-toc-modified-id="Example-SQL-Database-(temporary-in-your-RAM)-4.1"><span class="toc-item-num">4.1&nbsp;&nbsp;</span>Example SQL Database (temporary in your RAM)</a></span><ul class="toc-item"><li><span><a href="#Write-to-Database" data-toc-modified-id="Write-to-Database-4.1.1"><span class="toc-item-num">4.1.1&nbsp;&nbsp;</span>Write to Database</a></span></li><li><span><a href="#Read-from-SQL-Database" data-toc-modified-id="Read-from-SQL-Database-4.1.2"><span class="toc-item-num">4.1.2&nbsp;&nbsp;</span>Read from SQL Database</a></span></li></ul></li></ul></li></ul></div>

# Inputs and Outputs

**NOTE: Typically we will just be either reading csv files directly or using pandas-datareader to pull data from the web. Consider this lecture just a quick overview of what is possible with pandas (we won't be working with SQL or Excel files in this course)**

## Data Input and Output

This notebook is the reference code for getting input and output, pandas can read a variety of file types using its pd.read_ methods. Let's take a look at the most common data types:


```python
import numpy as np
import pandas as pd
```

## Check out the references here! 

**This is the best online resource for how to read/write to a variety of data sources!**

https://pandas.pydata.org/pandas-docs/stable/user_guide/io.html

----
----

<table border="1" class="colwidths-given docutils">
<colgroup>
<col width="12%" />
<col width="40%" />
<col width="24%" />
<col width="24%" />
</colgroup>
<thead valign="bottom">
<tr class="row-odd"><th class="head">Format Type</th>
<th class="head">Data Description</th>
<th class="head">Reader</th>
<th class="head">Writer</th>
</tr>
</thead>
<tbody valign="top">
<tr class="row-even"><td>text</td>
<td><a class="reference external" href="https://en.wikipedia.org/wiki/Comma-separated_values">CSV</a></td>
<td><a class="reference internal" href="#io-read-csv-table"><span class="std std-ref">read_csv</span></a></td>
<td><a class="reference internal" href="#io-store-in-csv"><span class="std std-ref">to_csv</span></a></td>
</tr>
<tr class="row-odd"><td>text</td>
<td><a class="reference external" href="https://www.json.org/">JSON</a></td>
<td><a class="reference internal" href="#io-json-reader"><span class="std std-ref">read_json</span></a></td>
<td><a class="reference internal" href="#io-json-writer"><span class="std std-ref">to_json</span></a></td>
</tr>
<tr class="row-even"><td>text</td>
<td><a class="reference external" href="https://en.wikipedia.org/wiki/HTML">HTML</a></td>
<td><a class="reference internal" href="#io-read-html"><span class="std std-ref">read_html</span></a></td>
<td><a class="reference internal" href="#io-html"><span class="std std-ref">to_html</span></a></td>
</tr>
<tr class="row-odd"><td>text</td>
<td>Local clipboard</td>
<td><a class="reference internal" href="#io-clipboard"><span class="std std-ref">read_clipboard</span></a></td>
<td><a class="reference internal" href="#io-clipboard"><span class="std std-ref">to_clipboard</span></a></td>
</tr>
<tr class="row-even"><td>binary</td>
<td><a class="reference external" href="https://en.wikipedia.org/wiki/Microsoft_Excel">MS Excel</a></td>
<td><a class="reference internal" href="#io-excel-reader"><span class="std std-ref">read_excel</span></a></td>
<td><a class="reference internal" href="#io-excel-writer"><span class="std std-ref">to_excel</span></a></td>
</tr>
<tr class="row-odd"><td>binary</td>
<td><a class="reference external" href="http://www.opendocumentformat.org">OpenDocument</a></td>
<td><a class="reference internal" href="#io-ods"><span class="std std-ref">read_excel</span></a></td>
<td>&#160;</td>
</tr>
<tr class="row-even"><td>binary</td>
<td><a class="reference external" href="https://support.hdfgroup.org/HDF5/whatishdf5.html">HDF5 Format</a></td>
<td><a class="reference internal" href="#io-hdf5"><span class="std std-ref">read_hdf</span></a></td>
<td><a class="reference internal" href="#io-hdf5"><span class="std std-ref">to_hdf</span></a></td>
</tr>
<tr class="row-odd"><td>binary</td>
<td><a class="reference external" href="https://github.com/wesm/feather">Feather Format</a></td>
<td><a class="reference internal" href="#io-feather"><span class="std std-ref">read_feather</span></a></td>
<td><a class="reference internal" href="#io-feather"><span class="std std-ref">to_feather</span></a></td>
</tr>
<tr class="row-even"><td>binary</td>
<td><a class="reference external" href="https://parquet.apache.org/">Parquet Format</a></td>
<td><a class="reference internal" href="#io-parquet"><span class="std std-ref">read_parquet</span></a></td>
<td><a class="reference internal" href="#io-parquet"><span class="std std-ref">to_parquet</span></a></td>
</tr>
<tr class="row-odd"><td>binary</td>
<td><a class="reference external" href="https://msgpack.org/index.html">Msgpack</a></td>
<td><a class="reference internal" href="#io-msgpack"><span class="std std-ref">read_msgpack</span></a></td>
<td><a class="reference internal" href="#io-msgpack"><span class="std std-ref">to_msgpack</span></a></td>
</tr>
<tr class="row-even"><td>binary</td>
<td><a class="reference external" href="https://en.wikipedia.org/wiki/Stata">Stata</a></td>
<td><a class="reference internal" href="#io-stata-reader"><span class="std std-ref">read_stata</span></a></td>
<td><a class="reference internal" href="#io-stata-writer"><span class="std std-ref">to_stata</span></a></td>
</tr>
<tr class="row-odd"><td>binary</td>
<td><a class="reference external" href="https://en.wikipedia.org/wiki/SAS_(software)">SAS</a></td>
<td><a class="reference internal" href="#io-sas-reader"><span class="std std-ref">read_sas</span></a></td>
<td>&#160;</td>
</tr>
<tr class="row-even"><td>binary</td>
<td><a class="reference external" href="https://docs.python.org/3/library/pickle.html">Python Pickle Format</a></td>
<td><a class="reference internal" href="#io-pickle"><span class="std std-ref">read_pickle</span></a></td>
<td><a class="reference internal" href="#io-pickle"><span class="std std-ref">to_pickle</span></a></td>
</tr>
<tr class="row-odd"><td>SQL</td>
<td><a class="reference external" href="https://en.wikipedia.org/wiki/SQL">SQL</a></td>
<td><a class="reference internal" href="#io-sql"><span class="std std-ref">read_sql</span></a></td>
<td><a class="reference internal" href="#io-sql"><span class="std std-ref">to_sql</span></a></td>
</tr>
<tr class="row-even"><td>SQL</td>
<td><a class="reference external" href="https://en.wikipedia.org/wiki/BigQuery">Google Big Query</a></td>
<td><a class="reference internal" href="#io-bigquery"><span class="std std-ref">read_gbq</span></a></td>
<td><a class="reference internal" href="#io-bigquery"><span class="std std-ref">to_gbq</span></a></td>
</tr>
</tbody>
</table>

-----
----

# Reading in a  CSV
Comma Separated Values files are text files that use commas as field delimeters.<br>
Unless you're running the virtual environment included with the course, you may need to install <tt>xlrd</tt> and <tt>openpyxl</tt>.<br>
In your terminal/command prompt run:

    conda install xlrd
    conda install openpyxl

Then restart Jupyter Notebook.
(or use pip install if you aren't using the Anaconda Distribution)

## Understanding File Paths

You have two options when reading a file with pandas:

1. If your .py file or .ipynb notebook is located in the **exact** same folder location as the .csv file you want to read, simply pass in the file name as a string, for example:
    
        df = pd.read_csv('some_file.csv')
        
2. Pass in the entire file path if you are located in a different directory. The file path must be 100% correct in order for this to work. For example:

        df = pd.read_csv("C:\\Users\\myself\\files\\some_file.csv")

#### Print your current directory file path with pwd


```python
pwd
```




    'C:\\Users\\Marcial\\Pierian-Data-Courses\\Machine-Learning-MasterClass\\03-Pandas'



#### List the files in your current directory with ls


```python
ls
```

     Volume in drive C has no label.
     Volume Serial Number is 3652-BD2F
    
     Directory of C:\Users\Marcial\Pierian-Data-Courses\Machine-Learning-MasterClass\03-Pandas
    
    07/04/2020  06:10 PM    <DIR>          .
    07/04/2020  06:10 PM    <DIR>          ..
    07/02/2020  05:40 PM    <DIR>          .ipynb_checkpoints
    06/30/2020  04:51 PM           565,390 00-Series.ipynb
    07/01/2020  12:48 PM           208,957 01-DataFrames.ipynb
    07/01/2020  12:48 PM           194,591 02-Conditional-Filtering.ipynb
    07/02/2020  07:02 PM           196,047 03-Useful-Methods.ipynb
    07/01/2020  03:32 PM            64,227 04-Missing-Data.ipynb
    07/04/2020  01:28 PM           219,627 05-Groupby-Operations-and-MultiIndex.ipynb
    07/04/2020  03:19 PM            62,966 06-Combining-DataFrames.ipynb
    07/02/2020  07:02 PM            29,356 07-Text-Methods.ipynb
    07/02/2020  06:38 PM            35,705 08-Time-Methods.ipynb
    07/04/2020  06:10 PM            53,097 09-Inputs-and-Outputs.ipynb
    07/02/2020  05:34 PM             1,095 10-Pivot-Tables.ipynb
    07/02/2020  05:34 PM               951 11-Pandas-Project-Exercise.ipynb
    07/02/2020  05:34 PM             1,118 12-Pandas-Project-Exercise-Solution.ipynb
    07/04/2020  05:39 PM                51 example.csv
    07/04/2020  06:02 PM             5,022 example.xlsx
    02/07/2020  12:26 PM               177 movie_scores.csv
    07/01/2020  03:56 PM            17,727 mpg.csv
    07/04/2020  05:58 PM             5,022 my_excel_file.xlsx
    07/04/2020  05:56 PM                51 new_file.csv
    07/02/2020  05:56 PM             5,459 RetailSales_BeerWineLiquor.csv
    07/04/2020  05:56 PM               555 simple.html
    01/27/2020  02:28 PM            18,752 tips.csv
                  22 File(s)      1,685,943 bytes
                   3 Dir(s)  82,818,367,488 bytes free
    

-----
#### NOTE!
***Common confusion point! Take note that all read input methods are called directly from pandas with pd.read_  , all output methods are called directly off the dataframe with df.to_***

-------

### CSV Input


```python
df = pd.read_csv('example.csv')
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
      <th>a</th>
      <th>b</th>
      <th>c</th>
      <th>d</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>0</td>
      <td>1</td>
      <td>2</td>
      <td>3</td>
    </tr>
    <tr>
      <th>1</th>
      <td>4</td>
      <td>5</td>
      <td>6</td>
      <td>7</td>
    </tr>
    <tr>
      <th>2</th>
      <td>8</td>
      <td>9</td>
      <td>10</td>
      <td>11</td>
    </tr>
    <tr>
      <th>3</th>
      <td>12</td>
      <td>13</td>
      <td>14</td>
      <td>15</td>
    </tr>
  </tbody>
</table>
</div>




```python
df = pd.read_csv('example.csv',index_col=0)
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
      <th>b</th>
      <th>c</th>
      <th>d</th>
    </tr>
    <tr>
      <th>a</th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1</td>
      <td>2</td>
      <td>3</td>
    </tr>
    <tr>
      <th>4</th>
      <td>5</td>
      <td>6</td>
      <td>7</td>
    </tr>
    <tr>
      <th>8</th>
      <td>9</td>
      <td>10</td>
      <td>11</td>
    </tr>
    <tr>
      <th>12</th>
      <td>13</td>
      <td>14</td>
      <td>15</td>
    </tr>
  </tbody>
</table>
</div>




```python
df = pd.read_csv('example.csv')
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
      <th>a</th>
      <th>b</th>
      <th>c</th>
      <th>d</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>0</td>
      <td>1</td>
      <td>2</td>
      <td>3</td>
    </tr>
    <tr>
      <th>1</th>
      <td>4</td>
      <td>5</td>
      <td>6</td>
      <td>7</td>
    </tr>
    <tr>
      <th>2</th>
      <td>8</td>
      <td>9</td>
      <td>10</td>
      <td>11</td>
    </tr>
    <tr>
      <th>3</th>
      <td>12</td>
      <td>13</td>
      <td>14</td>
      <td>15</td>
    </tr>
  </tbody>
</table>
</div>



### CSV Output

Set index=False if you do not want to save the index , otherwise it will add a new column to the .csv file that includes your index and call it "Unnamed: 0" if your index did not have a name. If you do want to save your index, simply set it to True (the default value).


```python
df.to_csv('new_file.csv',index=False)
```

## HTML

Pandas can read table tabs off of HTML. This only works if your firewall isn't blocking pandas from accessing the internet!

Unless you're running the virtual environment included with the course, you may need to install <tt>lxml</tt>, <tt>htmllib5</tt>, and <tt>BeautifulSoup4</tt>.<br>
In your terminal/command prompt run:

    conda install lxml
    
    or
    
    pip install lxml
    
Then restart Jupyter Notebook (you may need to restart your computer).
(or use pip install if you aren't using the Anaconda Distribution)

## read_html

### HTML Input

Pandas read_html function will read tables off of a webpage and return a list of DataFrame objects. NOTE: This only works with well defined <table> objects in the html on the page, this can not magically read in tables that are images on a page.


```python
tables = pd.read_html('https://en.wikipedia.org/wiki/World_population')
```


```python
len(tables) #tables
```




    26



### Not Useful Tables
Pandas found 26 tables on that page. Some are not useful:


```python
tables[0]
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
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>NaN</td>
      <td>An editor has expressed concern that this arti...</td>
    </tr>
  </tbody>
</table>
</div>



### Tables that need formatting

Some will be misaligned, meaning you need to do extra work to fix the columns and rows:


```python
tables[1]
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
</style>
<table border="1" class="dataframe">
  <thead>
    <tr>
      <th></th>
      <th colspan="5" halign="left">World population (millions, UN estimates)[14]</th>
    </tr>
    <tr>
      <th></th>
      <th>#</th>
      <th>Top ten most populous countries</th>
      <th>2000</th>
      <th>2015</th>
      <th>2030[A]</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1</td>
      <td>China[B]</td>
      <td>1270</td>
      <td>1376</td>
      <td>1416</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2</td>
      <td>India</td>
      <td>1053</td>
      <td>1311</td>
      <td>1528</td>
    </tr>
    <tr>
      <th>2</th>
      <td>3</td>
      <td>United States</td>
      <td>283</td>
      <td>322</td>
      <td>356</td>
    </tr>
    <tr>
      <th>3</th>
      <td>4</td>
      <td>Indonesia</td>
      <td>212</td>
      <td>258</td>
      <td>295</td>
    </tr>
    <tr>
      <th>4</th>
      <td>5</td>
      <td>Pakistan</td>
      <td>136</td>
      <td>208</td>
      <td>245</td>
    </tr>
    <tr>
      <th>5</th>
      <td>6</td>
      <td>Brazil</td>
      <td>176</td>
      <td>206</td>
      <td>228</td>
    </tr>
    <tr>
      <th>6</th>
      <td>7</td>
      <td>Nigeria</td>
      <td>123</td>
      <td>182</td>
      <td>263</td>
    </tr>
    <tr>
      <th>7</th>
      <td>8</td>
      <td>Bangladesh</td>
      <td>131</td>
      <td>161</td>
      <td>186</td>
    </tr>
    <tr>
      <th>8</th>
      <td>9</td>
      <td>Russia</td>
      <td>146</td>
      <td>146</td>
      <td>149</td>
    </tr>
    <tr>
      <th>9</th>
      <td>10</td>
      <td>Mexico</td>
      <td>103</td>
      <td>127</td>
      <td>148</td>
    </tr>
    <tr>
      <th>10</th>
      <td>NaN</td>
      <td>World total</td>
      <td>6127</td>
      <td>7349</td>
      <td>8501</td>
    </tr>
    <tr>
      <th>11</th>
      <td>Notes: ^ 2030 = Medium variant. ^ China exclud...</td>
      <td>Notes: ^ 2030 = Medium variant. ^ China exclud...</td>
      <td>Notes: ^ 2030 = Medium variant. ^ China exclud...</td>
      <td>Notes: ^ 2030 = Medium variant. ^ China exclud...</td>
      <td>Notes: ^ 2030 = Medium variant. ^ China exclud...</td>
    </tr>
  </tbody>
</table>
</div>




```python
world_pop = tables[1]
```


```python
world_pop.columns
```




    MultiIndex([('World population (millions, UN estimates)[14]', ...),
                ('World population (millions, UN estimates)[14]', ...),
                ('World population (millions, UN estimates)[14]', ...),
                ('World population (millions, UN estimates)[14]', ...),
                ('World population (millions, UN estimates)[14]', ...)],
               )




```python
world_pop = world_pop['World population (millions, UN estimates)[14]'].drop('#',axis=1)
```


```python
world_pop.columns
```




    Index(['Top ten most populous countries', '2000', '2015', '2030[A]'], dtype='object')




```python
world_pop.columns = ['Countries', '2000', '2015', '2030 Est.']
world_pop = world_pop.drop(11,axis=0)
```


```python
world_pop
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
      <th>Countries</th>
      <th>2000</th>
      <th>2015</th>
      <th>2030 Est.</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>China[B]</td>
      <td>1270</td>
      <td>1376</td>
      <td>1416</td>
    </tr>
    <tr>
      <th>1</th>
      <td>India</td>
      <td>1053</td>
      <td>1311</td>
      <td>1528</td>
    </tr>
    <tr>
      <th>2</th>
      <td>United States</td>
      <td>283</td>
      <td>322</td>
      <td>356</td>
    </tr>
    <tr>
      <th>3</th>
      <td>Indonesia</td>
      <td>212</td>
      <td>258</td>
      <td>295</td>
    </tr>
    <tr>
      <th>4</th>
      <td>Pakistan</td>
      <td>136</td>
      <td>208</td>
      <td>245</td>
    </tr>
    <tr>
      <th>5</th>
      <td>Brazil</td>
      <td>176</td>
      <td>206</td>
      <td>228</td>
    </tr>
    <tr>
      <th>6</th>
      <td>Nigeria</td>
      <td>123</td>
      <td>182</td>
      <td>263</td>
    </tr>
    <tr>
      <th>7</th>
      <td>Bangladesh</td>
      <td>131</td>
      <td>161</td>
      <td>186</td>
    </tr>
    <tr>
      <th>8</th>
      <td>Russia</td>
      <td>146</td>
      <td>146</td>
      <td>149</td>
    </tr>
    <tr>
      <th>9</th>
      <td>Mexico</td>
      <td>103</td>
      <td>127</td>
      <td>148</td>
    </tr>
    <tr>
      <th>10</th>
      <td>World total</td>
      <td>6127</td>
      <td>7349</td>
      <td>8501</td>
    </tr>
  </tbody>
</table>
</div>



### Tables that are intact


```python
tables[6]
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
      <th>Rank</th>
      <th>Country</th>
      <th>Population</th>
      <th>Area (km2)</th>
      <th>Density (Pop. per km2)</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1</td>
      <td>Singapore</td>
      <td>5703600</td>
      <td>710</td>
      <td>8033</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2</td>
      <td>Bangladesh</td>
      <td>168870000</td>
      <td>143998</td>
      <td>1173</td>
    </tr>
    <tr>
      <th>2</th>
      <td>3</td>
      <td>Lebanon</td>
      <td>6855713</td>
      <td>10452</td>
      <td>656</td>
    </tr>
    <tr>
      <th>3</th>
      <td>4</td>
      <td>Taiwan</td>
      <td>23604265</td>
      <td>36193</td>
      <td>652</td>
    </tr>
    <tr>
      <th>4</th>
      <td>5</td>
      <td>South Korea</td>
      <td>51780579</td>
      <td>99538</td>
      <td>520</td>
    </tr>
    <tr>
      <th>5</th>
      <td>6</td>
      <td>Rwanda</td>
      <td>12374397</td>
      <td>26338</td>
      <td>470</td>
    </tr>
    <tr>
      <th>6</th>
      <td>7</td>
      <td>Haiti</td>
      <td>11577779</td>
      <td>27065</td>
      <td>428</td>
    </tr>
    <tr>
      <th>7</th>
      <td>8</td>
      <td>Netherlands</td>
      <td>17480000</td>
      <td>41526</td>
      <td>421</td>
    </tr>
    <tr>
      <th>8</th>
      <td>9</td>
      <td>Israel</td>
      <td>9220000</td>
      <td>22072</td>
      <td>418</td>
    </tr>
    <tr>
      <th>9</th>
      <td>10</td>
      <td>India</td>
      <td>1364080000</td>
      <td>3287240</td>
      <td>415</td>
    </tr>
  </tbody>
</table>
</div>



## Write to html Output

If you are working on a website and want to quickly output the .html file, you can use to_html


```python
df.to_html('simple.html',index=False)
```

**read_html** is not perfect, but its quite powerful for such a simple method call!

# Excel Files

Pandas can read in basic excel files (it will get errors if there are macros or extensive formulas relying on outside excel files), in general, pandas can only grab the raw information from an .excel file.

#### NOTE: 
***Requires the openpyxl and xlrd library! Its provided for you in our environment, or simply install with:***

    pip install openpyxl
    pip install xlrd
    
Heavy excel users may want to check out this website: https://www.python-excel.org/

You can think of an excel file as a Workbook containin sheets, which for pandas means each sheet can be a DataFrame.

## Excel file input with read_excel()


```python
df = pd.read_excel('my_excel_file.xlsx',sheet_name='First_Sheet')
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
      <th>a</th>
      <th>b</th>
      <th>c</th>
      <th>d</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>0</td>
      <td>1</td>
      <td>2</td>
      <td>3</td>
    </tr>
    <tr>
      <th>1</th>
      <td>4</td>
      <td>5</td>
      <td>6</td>
      <td>7</td>
    </tr>
    <tr>
      <th>2</th>
      <td>8</td>
      <td>9</td>
      <td>10</td>
      <td>11</td>
    </tr>
    <tr>
      <th>3</th>
      <td>12</td>
      <td>13</td>
      <td>14</td>
      <td>15</td>
    </tr>
  </tbody>
</table>
</div>



### What if
***you don't know the sheet name? Or want to run a for loop for certain sheet names? Or want every sheet?***

Several ways to do this: https://stackoverflow.com/questions/17977540/pandas-looking-up-the-list-of-sheets-in-an-excel-file


```python
# Returns a list of sheet_names
pd.ExcelFile('my_excel_file.xlsx').sheet_names
```




    ['First_Sheet']



#### Grab all sheets


```python
excel_sheets = pd.read_excel('my_excel_file.xlsx',sheet_name=None)
```


```python
type(excel_sheets)
```




    dict




```python
excel_sheets.keys()
```




    dict_keys(['First_Sheet'])




```python
excel_sheets['First_Sheet']
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
      <th>a</th>
      <th>b</th>
      <th>c</th>
      <th>d</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>0</td>
      <td>1</td>
      <td>2</td>
      <td>3</td>
    </tr>
    <tr>
      <th>1</th>
      <td>4</td>
      <td>5</td>
      <td>6</td>
      <td>7</td>
    </tr>
    <tr>
      <th>2</th>
      <td>8</td>
      <td>9</td>
      <td>10</td>
      <td>11</td>
    </tr>
    <tr>
      <th>3</th>
      <td>12</td>
      <td>13</td>
      <td>14</td>
      <td>15</td>
    </tr>
  </tbody>
</table>
</div>



### Write to Excel File


```python
df.to_excel('example.xlsx',sheet_name='First_Sheet',index=False)
```

# SQL Connections

#### NOTE: 
***Highly recommend you explore specific libraries for your specific SQL Engine. Simple search for your database+python in Google and the top results should hopefully include an API.***

* [MySQL](https://www.google.com/search?q=mysql+python)
* [PostgreSQL](https://www.google.com/search?q=postgresql+python)
* [MS SQL Server](https://www.google.com/search?q=MSSQLserver+python)
* [Orcale](https://www.google.com/search?q=oracle+python)
* [MongoDB](https://www.google.com/search?q=mongodb+python)

Let's review pandas capabilities by using SQLite, which comes built in with Python.

## Example SQL Database (temporary in your RAM)

You will need to install sqlalchemy with:

    pip install sqlalchemy
    
to follow along. To understand how to make a connection to your own database, make sure to review: https://docs.sqlalchemy.org/en/13/core/connections.html


```python
from sqlalchemy import create_engine
```


```python
temp_db = create_engine('sqlite:///:memory:')
```

### Write to Database


```python
tables[6]
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
      <th>Rank</th>
      <th>Country</th>
      <th>Population</th>
      <th>Area (km2)</th>
      <th>Density (Pop. per km2)</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1</td>
      <td>Singapore</td>
      <td>5703600</td>
      <td>710</td>
      <td>8033</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2</td>
      <td>Bangladesh</td>
      <td>168870000</td>
      <td>143998</td>
      <td>1173</td>
    </tr>
    <tr>
      <th>2</th>
      <td>3</td>
      <td>Lebanon</td>
      <td>6855713</td>
      <td>10452</td>
      <td>656</td>
    </tr>
    <tr>
      <th>3</th>
      <td>4</td>
      <td>Taiwan</td>
      <td>23604265</td>
      <td>36193</td>
      <td>652</td>
    </tr>
    <tr>
      <th>4</th>
      <td>5</td>
      <td>South Korea</td>
      <td>51780579</td>
      <td>99538</td>
      <td>520</td>
    </tr>
    <tr>
      <th>5</th>
      <td>6</td>
      <td>Rwanda</td>
      <td>12374397</td>
      <td>26338</td>
      <td>470</td>
    </tr>
    <tr>
      <th>6</th>
      <td>7</td>
      <td>Haiti</td>
      <td>11577779</td>
      <td>27065</td>
      <td>428</td>
    </tr>
    <tr>
      <th>7</th>
      <td>8</td>
      <td>Netherlands</td>
      <td>17480000</td>
      <td>41526</td>
      <td>421</td>
    </tr>
    <tr>
      <th>8</th>
      <td>9</td>
      <td>Israel</td>
      <td>9220000</td>
      <td>22072</td>
      <td>418</td>
    </tr>
    <tr>
      <th>9</th>
      <td>10</td>
      <td>India</td>
      <td>1364080000</td>
      <td>3287240</td>
      <td>415</td>
    </tr>
  </tbody>
</table>
</div>




```python
pop = tables[6]
```


```python
pop.to_sql(name='populations',con=temp_db)
```

### Read from SQL Database


```python
# Read in an entire table
pd.read_sql(sql='populations',con=temp_db)
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
      <th>Rank</th>
      <th>Country</th>
      <th>Population</th>
      <th>Area (km2)</th>
      <th>Density (Pop. per km2)</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>0</td>
      <td>1</td>
      <td>Singapore</td>
      <td>5703600</td>
      <td>710</td>
      <td>8033</td>
    </tr>
    <tr>
      <th>1</th>
      <td>1</td>
      <td>2</td>
      <td>Bangladesh</td>
      <td>168870000</td>
      <td>143998</td>
      <td>1173</td>
    </tr>
    <tr>
      <th>2</th>
      <td>2</td>
      <td>3</td>
      <td>Lebanon</td>
      <td>6855713</td>
      <td>10452</td>
      <td>656</td>
    </tr>
    <tr>
      <th>3</th>
      <td>3</td>
      <td>4</td>
      <td>Taiwan</td>
      <td>23604265</td>
      <td>36193</td>
      <td>652</td>
    </tr>
    <tr>
      <th>4</th>
      <td>4</td>
      <td>5</td>
      <td>South Korea</td>
      <td>51780579</td>
      <td>99538</td>
      <td>520</td>
    </tr>
    <tr>
      <th>5</th>
      <td>5</td>
      <td>6</td>
      <td>Rwanda</td>
      <td>12374397</td>
      <td>26338</td>
      <td>470</td>
    </tr>
    <tr>
      <th>6</th>
      <td>6</td>
      <td>7</td>
      <td>Haiti</td>
      <td>11577779</td>
      <td>27065</td>
      <td>428</td>
    </tr>
    <tr>
      <th>7</th>
      <td>7</td>
      <td>8</td>
      <td>Netherlands</td>
      <td>17480000</td>
      <td>41526</td>
      <td>421</td>
    </tr>
    <tr>
      <th>8</th>
      <td>8</td>
      <td>9</td>
      <td>Israel</td>
      <td>9220000</td>
      <td>22072</td>
      <td>418</td>
    </tr>
    <tr>
      <th>9</th>
      <td>9</td>
      <td>10</td>
      <td>India</td>
      <td>1364080000</td>
      <td>3287240</td>
      <td>415</td>
    </tr>
  </tbody>
</table>
</div>




```python
# Read in with a SQL Query
pd.read_sql_query(sql="SELECT Country FROM populations",con=temp_db)
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
      <th>Country</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Singapore</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Bangladesh</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Lebanon</td>
    </tr>
    <tr>
      <th>3</th>
      <td>Taiwan</td>
    </tr>
    <tr>
      <th>4</th>
      <td>South Korea</td>
    </tr>
    <tr>
      <th>5</th>
      <td>Rwanda</td>
    </tr>
    <tr>
      <th>6</th>
      <td>Haiti</td>
    </tr>
    <tr>
      <th>7</th>
      <td>Netherlands</td>
    </tr>
    <tr>
      <th>8</th>
      <td>Israel</td>
    </tr>
    <tr>
      <th>9</th>
      <td>India</td>
    </tr>
  </tbody>
</table>
</div>



It is difficult to generalize pandas and SQL, due to a wide array of issues, including permissions,security, online access, varying SQL engines, etc... Use these ideas as a starting off point, and you will most likely need to do your own research for your own situation.
