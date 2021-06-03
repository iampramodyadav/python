<h1>Table of Contents<span class="tocSkip"></span></h1>
<div class="toc"><ul class="toc-item"><li><span><a href="#Conditional-Filtering" data-toc-modified-id="Conditional-Filtering-1"><span class="toc-item-num">1&nbsp;&nbsp;</span>Conditional Filtering</a></span><ul class="toc-item"><li><span><a href="#Imports" data-toc-modified-id="Imports-1.1"><span class="toc-item-num">1.1&nbsp;&nbsp;</span>Imports</a></span></li><li><span><a href="#Conditions" data-toc-modified-id="Conditions-1.2"><span class="toc-item-num">1.2&nbsp;&nbsp;</span>Conditions</a></span></li><li><span><a href="#Multiple-Conditions" data-toc-modified-id="Multiple-Conditions-1.3"><span class="toc-item-num">1.3&nbsp;&nbsp;</span>Multiple Conditions</a></span></li><li><span><a href="#Conditional-Operator-isin()" data-toc-modified-id="Conditional-Operator-isin()-1.4"><span class="toc-item-num">1.4&nbsp;&nbsp;</span>Conditional Operator isin()</a></span></li></ul></li></ul></div>

# Conditional Filtering

## Imports


```python
import numpy as np
import pandas as pd
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



## Conditions


```python
# df['total_bill'] > 30
```


```python
bool_series = df['total_bill'] > 30
```


```python
df[bool_series]
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
      <th>11</th>
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
      <td>Sun6686</td>
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
    </tr>
    <tr>
      <th>44</th>
      <td>30.40</td>
      <td>5.60</td>
      <td>Male</td>
      <td>No</td>
      <td>Sun</td>
      <td>Dinner</td>
      <td>4</td>
      <td>7.60</td>
      <td>Todd Cooper</td>
      <td>503846761263</td>
      <td>Sun2274</td>
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
    </tr>
    <tr>
      <th>52</th>
      <td>34.81</td>
      <td>5.20</td>
      <td>Female</td>
      <td>No</td>
      <td>Sun</td>
      <td>Dinner</td>
      <td>4</td>
      <td>8.70</td>
      <td>Emily Daniel</td>
      <td>4291280793094374</td>
      <td>Sun6165</td>
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
    </tr>
    <tr>
      <th>83</th>
      <td>32.68</td>
      <td>5.00</td>
      <td>Male</td>
      <td>Yes</td>
      <td>Thur</td>
      <td>Lunch</td>
      <td>2</td>
      <td>16.34</td>
      <td>Daniel Murphy</td>
      <td>5356177501009133</td>
      <td>Thur8801</td>
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
    </tr>
    <tr>
      <th>95</th>
      <td>40.17</td>
      <td>4.73</td>
      <td>Male</td>
      <td>Yes</td>
      <td>Fri</td>
      <td>Dinner</td>
      <td>4</td>
      <td>10.04</td>
      <td>Aaron Bentley</td>
      <td>180026611638690</td>
      <td>Fri9628</td>
    </tr>
    <tr>
      <th>102</th>
      <td>44.30</td>
      <td>2.50</td>
      <td>Female</td>
      <td>Yes</td>
      <td>Sat</td>
      <td>Dinner</td>
      <td>3</td>
      <td>14.77</td>
      <td>Heather Cohen</td>
      <td>379771118886604</td>
      <td>Sat6240</td>
    </tr>
    <tr>
      <th>112</th>
      <td>38.07</td>
      <td>4.00</td>
      <td>Male</td>
      <td>No</td>
      <td>Sun</td>
      <td>Dinner</td>
      <td>3</td>
      <td>12.69</td>
      <td>Jeff Lopez</td>
      <td>3572865915176463</td>
      <td>Sun591</td>
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
    </tr>
    <tr>
      <th>142</th>
      <td>41.19</td>
      <td>5.00</td>
      <td>Male</td>
      <td>No</td>
      <td>Thur</td>
      <td>Lunch</td>
      <td>5</td>
      <td>8.24</td>
      <td>Eric Andrews</td>
      <td>4356531761046453</td>
      <td>Thur3621</td>
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
    </tr>
    <tr>
      <th>167</th>
      <td>31.71</td>
      <td>4.50</td>
      <td>Male</td>
      <td>No</td>
      <td>Sun</td>
      <td>Dinner</td>
      <td>4</td>
      <td>7.93</td>
      <td>Michael Lawson</td>
      <td>3566285921227119</td>
      <td>Sun3719</td>
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
    </tr>
    <tr>
      <th>173</th>
      <td>31.85</td>
      <td>3.18</td>
      <td>Male</td>
      <td>Yes</td>
      <td>Sun</td>
      <td>Dinner</td>
      <td>2</td>
      <td>15.92</td>
      <td>Scott Perez</td>
      <td>3577115550328507</td>
      <td>Sun9335</td>
    </tr>
    <tr>
      <th>175</th>
      <td>32.90</td>
      <td>3.11</td>
      <td>Male</td>
      <td>Yes</td>
      <td>Sun</td>
      <td>Dinner</td>
      <td>2</td>
      <td>16.45</td>
      <td>Nathan Reynolds</td>
      <td>370307040837149</td>
      <td>Sun5109</td>
    </tr>
    <tr>
      <th>179</th>
      <td>34.63</td>
      <td>3.55</td>
      <td>Male</td>
      <td>Yes</td>
      <td>Sun</td>
      <td>Dinner</td>
      <td>2</td>
      <td>17.32</td>
      <td>Brian Bailey</td>
      <td>346656312114848</td>
      <td>Sun9851</td>
    </tr>
    <tr>
      <th>180</th>
      <td>34.65</td>
      <td>3.68</td>
      <td>Male</td>
      <td>Yes</td>
      <td>Sun</td>
      <td>Dinner</td>
      <td>4</td>
      <td>8.66</td>
      <td>James Hebert DDS</td>
      <td>676168737648</td>
      <td>Sun7544</td>
    </tr>
    <tr>
      <th>182</th>
      <td>45.35</td>
      <td>3.50</td>
      <td>Male</td>
      <td>Yes</td>
      <td>Sun</td>
      <td>Dinner</td>
      <td>3</td>
      <td>15.12</td>
      <td>Jose Parsons</td>
      <td>4112207559459910</td>
      <td>Sun2337</td>
    </tr>
    <tr>
      <th>184</th>
      <td>40.55</td>
      <td>3.00</td>
      <td>Male</td>
      <td>Yes</td>
      <td>Sun</td>
      <td>Dinner</td>
      <td>2</td>
      <td>20.27</td>
      <td>Stephen Cox</td>
      <td>3547798222044029</td>
      <td>Sun5140</td>
    </tr>
    <tr>
      <th>187</th>
      <td>30.46</td>
      <td>2.00</td>
      <td>Male</td>
      <td>Yes</td>
      <td>Sun</td>
      <td>Dinner</td>
      <td>5</td>
      <td>6.09</td>
      <td>David Barrett</td>
      <td>4792882899700988</td>
      <td>Sun9987</td>
    </tr>
    <tr>
      <th>197</th>
      <td>43.11</td>
      <td>5.00</td>
      <td>Female</td>
      <td>Yes</td>
      <td>Thur</td>
      <td>Lunch</td>
      <td>4</td>
      <td>10.78</td>
      <td>Brooke Soto</td>
      <td>5544902205760175</td>
      <td>Thur9313</td>
    </tr>
    <tr>
      <th>207</th>
      <td>38.73</td>
      <td>3.00</td>
      <td>Male</td>
      <td>Yes</td>
      <td>Sat</td>
      <td>Dinner</td>
      <td>4</td>
      <td>9.68</td>
      <td>Ricky Ramirez</td>
      <td>347817964484033</td>
      <td>Sat4505</td>
    </tr>
    <tr>
      <th>210</th>
      <td>30.06</td>
      <td>2.00</td>
      <td>Male</td>
      <td>Yes</td>
      <td>Sat</td>
      <td>Dinner</td>
      <td>3</td>
      <td>10.02</td>
      <td>Shawn Mendoza</td>
      <td>30184049218122</td>
      <td>Sat8361</td>
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
    </tr>
    <tr>
      <th>219</th>
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
      <td>Sat8863</td>
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
    </tr>
    <tr>
      <th>238</th>
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
      <td>Sat9777</td>
    </tr>
  </tbody>
</table>
</div>




```python
df[df['total_bill']>30]
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
      <th>11</th>
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
      <td>Sun6686</td>
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
    </tr>
    <tr>
      <th>44</th>
      <td>30.40</td>
      <td>5.60</td>
      <td>Male</td>
      <td>No</td>
      <td>Sun</td>
      <td>Dinner</td>
      <td>4</td>
      <td>7.60</td>
      <td>Todd Cooper</td>
      <td>503846761263</td>
      <td>Sun2274</td>
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
    </tr>
    <tr>
      <th>52</th>
      <td>34.81</td>
      <td>5.20</td>
      <td>Female</td>
      <td>No</td>
      <td>Sun</td>
      <td>Dinner</td>
      <td>4</td>
      <td>8.70</td>
      <td>Emily Daniel</td>
      <td>4291280793094374</td>
      <td>Sun6165</td>
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
    </tr>
    <tr>
      <th>83</th>
      <td>32.68</td>
      <td>5.00</td>
      <td>Male</td>
      <td>Yes</td>
      <td>Thur</td>
      <td>Lunch</td>
      <td>2</td>
      <td>16.34</td>
      <td>Daniel Murphy</td>
      <td>5356177501009133</td>
      <td>Thur8801</td>
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
    </tr>
    <tr>
      <th>95</th>
      <td>40.17</td>
      <td>4.73</td>
      <td>Male</td>
      <td>Yes</td>
      <td>Fri</td>
      <td>Dinner</td>
      <td>4</td>
      <td>10.04</td>
      <td>Aaron Bentley</td>
      <td>180026611638690</td>
      <td>Fri9628</td>
    </tr>
    <tr>
      <th>102</th>
      <td>44.30</td>
      <td>2.50</td>
      <td>Female</td>
      <td>Yes</td>
      <td>Sat</td>
      <td>Dinner</td>
      <td>3</td>
      <td>14.77</td>
      <td>Heather Cohen</td>
      <td>379771118886604</td>
      <td>Sat6240</td>
    </tr>
    <tr>
      <th>112</th>
      <td>38.07</td>
      <td>4.00</td>
      <td>Male</td>
      <td>No</td>
      <td>Sun</td>
      <td>Dinner</td>
      <td>3</td>
      <td>12.69</td>
      <td>Jeff Lopez</td>
      <td>3572865915176463</td>
      <td>Sun591</td>
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
    </tr>
    <tr>
      <th>142</th>
      <td>41.19</td>
      <td>5.00</td>
      <td>Male</td>
      <td>No</td>
      <td>Thur</td>
      <td>Lunch</td>
      <td>5</td>
      <td>8.24</td>
      <td>Eric Andrews</td>
      <td>4356531761046453</td>
      <td>Thur3621</td>
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
    </tr>
    <tr>
      <th>167</th>
      <td>31.71</td>
      <td>4.50</td>
      <td>Male</td>
      <td>No</td>
      <td>Sun</td>
      <td>Dinner</td>
      <td>4</td>
      <td>7.93</td>
      <td>Michael Lawson</td>
      <td>3566285921227119</td>
      <td>Sun3719</td>
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
    </tr>
    <tr>
      <th>173</th>
      <td>31.85</td>
      <td>3.18</td>
      <td>Male</td>
      <td>Yes</td>
      <td>Sun</td>
      <td>Dinner</td>
      <td>2</td>
      <td>15.92</td>
      <td>Scott Perez</td>
      <td>3577115550328507</td>
      <td>Sun9335</td>
    </tr>
    <tr>
      <th>175</th>
      <td>32.90</td>
      <td>3.11</td>
      <td>Male</td>
      <td>Yes</td>
      <td>Sun</td>
      <td>Dinner</td>
      <td>2</td>
      <td>16.45</td>
      <td>Nathan Reynolds</td>
      <td>370307040837149</td>
      <td>Sun5109</td>
    </tr>
    <tr>
      <th>179</th>
      <td>34.63</td>
      <td>3.55</td>
      <td>Male</td>
      <td>Yes</td>
      <td>Sun</td>
      <td>Dinner</td>
      <td>2</td>
      <td>17.32</td>
      <td>Brian Bailey</td>
      <td>346656312114848</td>
      <td>Sun9851</td>
    </tr>
    <tr>
      <th>180</th>
      <td>34.65</td>
      <td>3.68</td>
      <td>Male</td>
      <td>Yes</td>
      <td>Sun</td>
      <td>Dinner</td>
      <td>4</td>
      <td>8.66</td>
      <td>James Hebert DDS</td>
      <td>676168737648</td>
      <td>Sun7544</td>
    </tr>
    <tr>
      <th>182</th>
      <td>45.35</td>
      <td>3.50</td>
      <td>Male</td>
      <td>Yes</td>
      <td>Sun</td>
      <td>Dinner</td>
      <td>3</td>
      <td>15.12</td>
      <td>Jose Parsons</td>
      <td>4112207559459910</td>
      <td>Sun2337</td>
    </tr>
    <tr>
      <th>184</th>
      <td>40.55</td>
      <td>3.00</td>
      <td>Male</td>
      <td>Yes</td>
      <td>Sun</td>
      <td>Dinner</td>
      <td>2</td>
      <td>20.27</td>
      <td>Stephen Cox</td>
      <td>3547798222044029</td>
      <td>Sun5140</td>
    </tr>
    <tr>
      <th>187</th>
      <td>30.46</td>
      <td>2.00</td>
      <td>Male</td>
      <td>Yes</td>
      <td>Sun</td>
      <td>Dinner</td>
      <td>5</td>
      <td>6.09</td>
      <td>David Barrett</td>
      <td>4792882899700988</td>
      <td>Sun9987</td>
    </tr>
    <tr>
      <th>197</th>
      <td>43.11</td>
      <td>5.00</td>
      <td>Female</td>
      <td>Yes</td>
      <td>Thur</td>
      <td>Lunch</td>
      <td>4</td>
      <td>10.78</td>
      <td>Brooke Soto</td>
      <td>5544902205760175</td>
      <td>Thur9313</td>
    </tr>
    <tr>
      <th>207</th>
      <td>38.73</td>
      <td>3.00</td>
      <td>Male</td>
      <td>Yes</td>
      <td>Sat</td>
      <td>Dinner</td>
      <td>4</td>
      <td>9.68</td>
      <td>Ricky Ramirez</td>
      <td>347817964484033</td>
      <td>Sat4505</td>
    </tr>
    <tr>
      <th>210</th>
      <td>30.06</td>
      <td>2.00</td>
      <td>Male</td>
      <td>Yes</td>
      <td>Sat</td>
      <td>Dinner</td>
      <td>3</td>
      <td>10.02</td>
      <td>Shawn Mendoza</td>
      <td>30184049218122</td>
      <td>Sat8361</td>
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
    </tr>
    <tr>
      <th>219</th>
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
      <td>Sat8863</td>
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
    </tr>
    <tr>
      <th>238</th>
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
      <td>Sat9777</td>
    </tr>
  </tbody>
</table>
</div>




```python
df[df['sex'] == 'Male']
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
    </tr>
    <tr>
      <th>6</th>
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
      <td>Sun5985</td>
    </tr>
    <tr>
      <th>7</th>
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
      <td>Sun8157</td>
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
    </tr>
    <tr>
      <th>15</th>
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
      <td>Sun1878</td>
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
    </tr>
    <tr>
      <th>19</th>
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
      <td>Sat9213</td>
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
    </tr>
    <tr>
      <th>28</th>
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
      <td>Sat3697</td>
    </tr>
    <tr>
      <th>30</th>
      <td>9.55</td>
      <td>1.45</td>
      <td>Male</td>
      <td>No</td>
      <td>Sat</td>
      <td>Dinner</td>
      <td>2</td>
      <td>4.78</td>
      <td>Grant Hall</td>
      <td>30196517521548</td>
      <td>Sat4099</td>
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
    </tr>
    <tr>
      <th>35</th>
      <td>24.06</td>
      <td>3.60</td>
      <td>Male</td>
      <td>No</td>
      <td>Sat</td>
      <td>Dinner</td>
      <td>3</td>
      <td>8.02</td>
      <td>Joseph Mullins</td>
      <td>5519770449260299</td>
      <td>Sat632</td>
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
      <th>195</th>
      <td>7.56</td>
      <td>1.44</td>
      <td>Male</td>
      <td>No</td>
      <td>Thur</td>
      <td>Lunch</td>
      <td>2</td>
      <td>3.78</td>
      <td>Michael White</td>
      <td>4865390263095532</td>
      <td>Thur697</td>
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
    </tr>
    <tr>
      <th>204</th>
      <td>20.53</td>
      <td>4.00</td>
      <td>Male</td>
      <td>Yes</td>
      <td>Thur</td>
      <td>Lunch</td>
      <td>4</td>
      <td>5.13</td>
      <td>Scott Kim</td>
      <td>3570611756827620</td>
      <td>Thur2160</td>
    </tr>
    <tr>
      <th>206</th>
      <td>26.59</td>
      <td>3.41</td>
      <td>Male</td>
      <td>Yes</td>
      <td>Sat</td>
      <td>Dinner</td>
      <td>3</td>
      <td>8.86</td>
      <td>Daniel Owens</td>
      <td>38971087967574</td>
      <td>Sat1</td>
    </tr>
    <tr>
      <th>207</th>
      <td>38.73</td>
      <td>3.00</td>
      <td>Male</td>
      <td>Yes</td>
      <td>Sat</td>
      <td>Dinner</td>
      <td>4</td>
      <td>9.68</td>
      <td>Ricky Ramirez</td>
      <td>347817964484033</td>
      <td>Sat4505</td>
    </tr>
    <tr>
      <th>208</th>
      <td>24.27</td>
      <td>2.03</td>
      <td>Male</td>
      <td>Yes</td>
      <td>Sat</td>
      <td>Dinner</td>
      <td>2</td>
      <td>12.14</td>
      <td>Jason Carter</td>
      <td>4268942915626180</td>
      <td>Sat6048</td>
    </tr>
    <tr>
      <th>210</th>
      <td>30.06</td>
      <td>2.00</td>
      <td>Male</td>
      <td>Yes</td>
      <td>Sat</td>
      <td>Dinner</td>
      <td>3</td>
      <td>10.02</td>
      <td>Shawn Mendoza</td>
      <td>30184049218122</td>
      <td>Sat8361</td>
    </tr>
    <tr>
      <th>211</th>
      <td>25.89</td>
      <td>5.16</td>
      <td>Male</td>
      <td>Yes</td>
      <td>Sat</td>
      <td>Dinner</td>
      <td>4</td>
      <td>6.47</td>
      <td>Christopher Li</td>
      <td>6011962464150569</td>
      <td>Sat6735</td>
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
    </tr>
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
    </tr>
    <tr>
      <th>218</th>
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
      <td>Sat4772</td>
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
    </tr>
    <tr>
      <th>222</th>
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
      <td>Fri6624</td>
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
    </tr>
    <tr>
      <th>227</th>
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
      <td>Sat4319</td>
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
    </tr>
    <tr>
      <th>230</th>
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
      <td>Sat7872</td>
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
  </tbody>
</table>
<p>157 rows × 11 columns</p>
</div>



## Multiple Conditions

Recall the steps:

* Get the conditions
* Wrap each condition in parenthesis
* Use the | or & operator, depending if you want an 
    * OR | (either condition is True)
    * AND & (both conditions must be True)
* You can also use the ~ operator as a NOT operation


```python
df[(df['total_bill'] > 30) & (df['sex']=='Male')]
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
    </tr>
    <tr>
      <th>44</th>
      <td>30.40</td>
      <td>5.60</td>
      <td>Male</td>
      <td>No</td>
      <td>Sun</td>
      <td>Dinner</td>
      <td>4</td>
      <td>7.60</td>
      <td>Todd Cooper</td>
      <td>503846761263</td>
      <td>Sun2274</td>
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
    </tr>
    <tr>
      <th>83</th>
      <td>32.68</td>
      <td>5.00</td>
      <td>Male</td>
      <td>Yes</td>
      <td>Thur</td>
      <td>Lunch</td>
      <td>2</td>
      <td>16.34</td>
      <td>Daniel Murphy</td>
      <td>5356177501009133</td>
      <td>Thur8801</td>
    </tr>
    <tr>
      <th>95</th>
      <td>40.17</td>
      <td>4.73</td>
      <td>Male</td>
      <td>Yes</td>
      <td>Fri</td>
      <td>Dinner</td>
      <td>4</td>
      <td>10.04</td>
      <td>Aaron Bentley</td>
      <td>180026611638690</td>
      <td>Fri9628</td>
    </tr>
    <tr>
      <th>112</th>
      <td>38.07</td>
      <td>4.00</td>
      <td>Male</td>
      <td>No</td>
      <td>Sun</td>
      <td>Dinner</td>
      <td>3</td>
      <td>12.69</td>
      <td>Jeff Lopez</td>
      <td>3572865915176463</td>
      <td>Sun591</td>
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
    </tr>
    <tr>
      <th>142</th>
      <td>41.19</td>
      <td>5.00</td>
      <td>Male</td>
      <td>No</td>
      <td>Thur</td>
      <td>Lunch</td>
      <td>5</td>
      <td>8.24</td>
      <td>Eric Andrews</td>
      <td>4356531761046453</td>
      <td>Thur3621</td>
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
    </tr>
    <tr>
      <th>167</th>
      <td>31.71</td>
      <td>4.50</td>
      <td>Male</td>
      <td>No</td>
      <td>Sun</td>
      <td>Dinner</td>
      <td>4</td>
      <td>7.93</td>
      <td>Michael Lawson</td>
      <td>3566285921227119</td>
      <td>Sun3719</td>
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
    </tr>
    <tr>
      <th>173</th>
      <td>31.85</td>
      <td>3.18</td>
      <td>Male</td>
      <td>Yes</td>
      <td>Sun</td>
      <td>Dinner</td>
      <td>2</td>
      <td>15.92</td>
      <td>Scott Perez</td>
      <td>3577115550328507</td>
      <td>Sun9335</td>
    </tr>
    <tr>
      <th>175</th>
      <td>32.90</td>
      <td>3.11</td>
      <td>Male</td>
      <td>Yes</td>
      <td>Sun</td>
      <td>Dinner</td>
      <td>2</td>
      <td>16.45</td>
      <td>Nathan Reynolds</td>
      <td>370307040837149</td>
      <td>Sun5109</td>
    </tr>
    <tr>
      <th>179</th>
      <td>34.63</td>
      <td>3.55</td>
      <td>Male</td>
      <td>Yes</td>
      <td>Sun</td>
      <td>Dinner</td>
      <td>2</td>
      <td>17.32</td>
      <td>Brian Bailey</td>
      <td>346656312114848</td>
      <td>Sun9851</td>
    </tr>
    <tr>
      <th>180</th>
      <td>34.65</td>
      <td>3.68</td>
      <td>Male</td>
      <td>Yes</td>
      <td>Sun</td>
      <td>Dinner</td>
      <td>4</td>
      <td>8.66</td>
      <td>James Hebert DDS</td>
      <td>676168737648</td>
      <td>Sun7544</td>
    </tr>
    <tr>
      <th>182</th>
      <td>45.35</td>
      <td>3.50</td>
      <td>Male</td>
      <td>Yes</td>
      <td>Sun</td>
      <td>Dinner</td>
      <td>3</td>
      <td>15.12</td>
      <td>Jose Parsons</td>
      <td>4112207559459910</td>
      <td>Sun2337</td>
    </tr>
    <tr>
      <th>184</th>
      <td>40.55</td>
      <td>3.00</td>
      <td>Male</td>
      <td>Yes</td>
      <td>Sun</td>
      <td>Dinner</td>
      <td>2</td>
      <td>20.27</td>
      <td>Stephen Cox</td>
      <td>3547798222044029</td>
      <td>Sun5140</td>
    </tr>
    <tr>
      <th>187</th>
      <td>30.46</td>
      <td>2.00</td>
      <td>Male</td>
      <td>Yes</td>
      <td>Sun</td>
      <td>Dinner</td>
      <td>5</td>
      <td>6.09</td>
      <td>David Barrett</td>
      <td>4792882899700988</td>
      <td>Sun9987</td>
    </tr>
    <tr>
      <th>207</th>
      <td>38.73</td>
      <td>3.00</td>
      <td>Male</td>
      <td>Yes</td>
      <td>Sat</td>
      <td>Dinner</td>
      <td>4</td>
      <td>9.68</td>
      <td>Ricky Ramirez</td>
      <td>347817964484033</td>
      <td>Sat4505</td>
    </tr>
    <tr>
      <th>210</th>
      <td>30.06</td>
      <td>2.00</td>
      <td>Male</td>
      <td>Yes</td>
      <td>Sat</td>
      <td>Dinner</td>
      <td>3</td>
      <td>10.02</td>
      <td>Shawn Mendoza</td>
      <td>30184049218122</td>
      <td>Sat8361</td>
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
    </tr>
  </tbody>
</table>
</div>




```python
df[(df['total_bill'] > 30) & ~(df['sex']=='Male')]
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
      <th>11</th>
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
      <td>Sun6686</td>
    </tr>
    <tr>
      <th>52</th>
      <td>34.81</td>
      <td>5.20</td>
      <td>Female</td>
      <td>No</td>
      <td>Sun</td>
      <td>Dinner</td>
      <td>4</td>
      <td>8.70</td>
      <td>Emily Daniel</td>
      <td>4291280793094374</td>
      <td>Sun6165</td>
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
    </tr>
    <tr>
      <th>102</th>
      <td>44.30</td>
      <td>2.50</td>
      <td>Female</td>
      <td>Yes</td>
      <td>Sat</td>
      <td>Dinner</td>
      <td>3</td>
      <td>14.77</td>
      <td>Heather Cohen</td>
      <td>379771118886604</td>
      <td>Sat6240</td>
    </tr>
    <tr>
      <th>197</th>
      <td>43.11</td>
      <td>5.00</td>
      <td>Female</td>
      <td>Yes</td>
      <td>Thur</td>
      <td>Lunch</td>
      <td>4</td>
      <td>10.78</td>
      <td>Brooke Soto</td>
      <td>5544902205760175</td>
      <td>Thur9313</td>
    </tr>
    <tr>
      <th>219</th>
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
      <td>Sat8863</td>
    </tr>
    <tr>
      <th>238</th>
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
      <td>Sat9777</td>
    </tr>
  </tbody>
</table>
</div>




```python
df[(df['total_bill'] > 30) & (df['sex']!='Male')]
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
      <th>11</th>
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
      <td>Sun6686</td>
    </tr>
    <tr>
      <th>52</th>
      <td>34.81</td>
      <td>5.20</td>
      <td>Female</td>
      <td>No</td>
      <td>Sun</td>
      <td>Dinner</td>
      <td>4</td>
      <td>8.70</td>
      <td>Emily Daniel</td>
      <td>4291280793094374</td>
      <td>Sun6165</td>
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
    </tr>
    <tr>
      <th>102</th>
      <td>44.30</td>
      <td>2.50</td>
      <td>Female</td>
      <td>Yes</td>
      <td>Sat</td>
      <td>Dinner</td>
      <td>3</td>
      <td>14.77</td>
      <td>Heather Cohen</td>
      <td>379771118886604</td>
      <td>Sat6240</td>
    </tr>
    <tr>
      <th>197</th>
      <td>43.11</td>
      <td>5.00</td>
      <td>Female</td>
      <td>Yes</td>
      <td>Thur</td>
      <td>Lunch</td>
      <td>4</td>
      <td>10.78</td>
      <td>Brooke Soto</td>
      <td>5544902205760175</td>
      <td>Thur9313</td>
    </tr>
    <tr>
      <th>219</th>
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
      <td>Sat8863</td>
    </tr>
    <tr>
      <th>238</th>
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
      <td>Sat9777</td>
    </tr>
  </tbody>
</table>
</div>




```python
# The Weekend
df[(df['day'] =='Sun') | (df['day']=='Sat')]
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
    </tr>
    <tr>
      <th>6</th>
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
      <td>Sun5985</td>
    </tr>
    <tr>
      <th>7</th>
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
      <td>Sun8157</td>
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
    </tr>
    <tr>
      <th>11</th>
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
      <td>Sun6686</td>
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
    </tr>
    <tr>
      <th>15</th>
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
      <td>Sun1878</td>
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
    </tr>
    <tr>
      <th>19</th>
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
      <td>Sat9213</td>
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
    </tr>
    <tr>
      <th>28</th>
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
      <td>Sat3697</td>
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
      <th>206</th>
      <td>26.59</td>
      <td>3.41</td>
      <td>Male</td>
      <td>Yes</td>
      <td>Sat</td>
      <td>Dinner</td>
      <td>3</td>
      <td>8.86</td>
      <td>Daniel Owens</td>
      <td>38971087967574</td>
      <td>Sat1</td>
    </tr>
    <tr>
      <th>207</th>
      <td>38.73</td>
      <td>3.00</td>
      <td>Male</td>
      <td>Yes</td>
      <td>Sat</td>
      <td>Dinner</td>
      <td>4</td>
      <td>9.68</td>
      <td>Ricky Ramirez</td>
      <td>347817964484033</td>
      <td>Sat4505</td>
    </tr>
    <tr>
      <th>208</th>
      <td>24.27</td>
      <td>2.03</td>
      <td>Male</td>
      <td>Yes</td>
      <td>Sat</td>
      <td>Dinner</td>
      <td>2</td>
      <td>12.14</td>
      <td>Jason Carter</td>
      <td>4268942915626180</td>
      <td>Sat6048</td>
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
    </tr>
    <tr>
      <th>210</th>
      <td>30.06</td>
      <td>2.00</td>
      <td>Male</td>
      <td>Yes</td>
      <td>Sat</td>
      <td>Dinner</td>
      <td>3</td>
      <td>10.02</td>
      <td>Shawn Mendoza</td>
      <td>30184049218122</td>
      <td>Sat8361</td>
    </tr>
    <tr>
      <th>211</th>
      <td>25.89</td>
      <td>5.16</td>
      <td>Male</td>
      <td>Yes</td>
      <td>Sat</td>
      <td>Dinner</td>
      <td>4</td>
      <td>6.47</td>
      <td>Christopher Li</td>
      <td>6011962464150569</td>
      <td>Sat6735</td>
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
    </tr>
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
    </tr>
    <tr>
      <th>218</th>
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
      <td>Sat4772</td>
    </tr>
    <tr>
      <th>219</th>
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
      <td>Sat8863</td>
    </tr>
    <tr>
      <th>227</th>
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
      <td>Sat4319</td>
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
    </tr>
    <tr>
      <th>229</th>
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
      <td>Sat3943</td>
    </tr>
    <tr>
      <th>230</th>
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
      <td>Sat7872</td>
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
    </tr>
    <tr>
      <th>238</th>
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
      <td>Sat9777</td>
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
  </tbody>
</table>
<p>163 rows × 11 columns</p>
</div>



## Conditional Operator isin()

We can use .isin() operator to filter by a list of options.


```python
options = ['Sat','Sun']
df['day'].isin(options)
```




    0       True
    1       True
    2       True
    3       True
    4       True
    5       True
    6       True
    7       True
    8       True
    9       True
    10      True
    11      True
    12      True
    13      True
    14      True
    15      True
    16      True
    17      True
    18      True
    19      True
    20      True
    21      True
    22      True
    23      True
    24      True
    25      True
    26      True
    27      True
    28      True
    29      True
           ...  
    214     True
    215     True
    216     True
    217     True
    218     True
    219     True
    220    False
    221    False
    222    False
    223    False
    224    False
    225    False
    226    False
    227     True
    228     True
    229     True
    230     True
    231     True
    232     True
    233     True
    234     True
    235     True
    236     True
    237     True
    238     True
    239     True
    240     True
    241     True
    242     True
    243    False
    Name: day, Length: 244, dtype: bool




```python
df[df['day'].isin(['Sat','Sun'])]
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
    </tr>
    <tr>
      <th>6</th>
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
      <td>Sun5985</td>
    </tr>
    <tr>
      <th>7</th>
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
      <td>Sun8157</td>
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
    </tr>
    <tr>
      <th>11</th>
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
      <td>Sun6686</td>
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
    </tr>
    <tr>
      <th>15</th>
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
      <td>Sun1878</td>
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
    </tr>
    <tr>
      <th>19</th>
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
      <td>Sat9213</td>
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
    </tr>
    <tr>
      <th>28</th>
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
      <td>Sat3697</td>
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
      <th>206</th>
      <td>26.59</td>
      <td>3.41</td>
      <td>Male</td>
      <td>Yes</td>
      <td>Sat</td>
      <td>Dinner</td>
      <td>3</td>
      <td>8.86</td>
      <td>Daniel Owens</td>
      <td>38971087967574</td>
      <td>Sat1</td>
    </tr>
    <tr>
      <th>207</th>
      <td>38.73</td>
      <td>3.00</td>
      <td>Male</td>
      <td>Yes</td>
      <td>Sat</td>
      <td>Dinner</td>
      <td>4</td>
      <td>9.68</td>
      <td>Ricky Ramirez</td>
      <td>347817964484033</td>
      <td>Sat4505</td>
    </tr>
    <tr>
      <th>208</th>
      <td>24.27</td>
      <td>2.03</td>
      <td>Male</td>
      <td>Yes</td>
      <td>Sat</td>
      <td>Dinner</td>
      <td>2</td>
      <td>12.14</td>
      <td>Jason Carter</td>
      <td>4268942915626180</td>
      <td>Sat6048</td>
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
    </tr>
    <tr>
      <th>210</th>
      <td>30.06</td>
      <td>2.00</td>
      <td>Male</td>
      <td>Yes</td>
      <td>Sat</td>
      <td>Dinner</td>
      <td>3</td>
      <td>10.02</td>
      <td>Shawn Mendoza</td>
      <td>30184049218122</td>
      <td>Sat8361</td>
    </tr>
    <tr>
      <th>211</th>
      <td>25.89</td>
      <td>5.16</td>
      <td>Male</td>
      <td>Yes</td>
      <td>Sat</td>
      <td>Dinner</td>
      <td>4</td>
      <td>6.47</td>
      <td>Christopher Li</td>
      <td>6011962464150569</td>
      <td>Sat6735</td>
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
    </tr>
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
    </tr>
    <tr>
      <th>218</th>
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
      <td>Sat4772</td>
    </tr>
    <tr>
      <th>219</th>
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
      <td>Sat8863</td>
    </tr>
    <tr>
      <th>227</th>
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
      <td>Sat4319</td>
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
    </tr>
    <tr>
      <th>229</th>
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
      <td>Sat3943</td>
    </tr>
    <tr>
      <th>230</th>
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
      <td>Sat7872</td>
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
    </tr>
    <tr>
      <th>238</th>
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
      <td>Sat9777</td>
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
  </tbody>
</table>
<p>163 rows × 11 columns</p>
</div>




```python

```
