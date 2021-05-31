<h1>Table of Contents<span class="tocSkip"></span></h1>
<div class="toc"><ul class="toc-item"><li><span><a href="#NumPy" data-toc-modified-id="NumPy-1"><span class="toc-item-num">1&nbsp;&nbsp;</span>NumPy</a></span><ul class="toc-item"><li><span><a href="#Array-creation-functions" data-toc-modified-id="Array-creation-functions-1.1"><span class="toc-item-num">1.1&nbsp;&nbsp;</span>Array creation functions</a></span><ul class="toc-item"><li><span><a href="#From-list" data-toc-modified-id="From-list-1.1.1"><span class="toc-item-num">1.1.1&nbsp;&nbsp;</span>From list</a></span></li><li><span><a href="#Array-creation-using-array-functions" data-toc-modified-id="Array-creation-using-array-functions-1.1.2"><span class="toc-item-num">1.1.2&nbsp;&nbsp;</span>Array creation using array functions</a></span></li><li><span><a href="#Array-creation-using-numpy-methods" data-toc-modified-id="Array-creation-using-numpy-methods-1.1.3"><span class="toc-item-num">1.1.3&nbsp;&nbsp;</span>Array creation using numpy methods</a></span></li><li><span><a href="#arange" data-toc-modified-id="arange-1.1.4"><span class="toc-item-num">1.1.4&nbsp;&nbsp;</span>arange</a></span></li><li><span><a href="#zeros" data-toc-modified-id="zeros-1.1.5"><span class="toc-item-num">1.1.5&nbsp;&nbsp;</span>zeros</a></span></li><li><span><a href="#ones" data-toc-modified-id="ones-1.1.6"><span class="toc-item-num">1.1.6&nbsp;&nbsp;</span>ones</a></span></li><li><span><a href="#linspace" data-toc-modified-id="linspace-1.1.7"><span class="toc-item-num">1.1.7&nbsp;&nbsp;</span>linspace</a></span></li><li><span><a href="#eye" data-toc-modified-id="eye-1.1.8"><span class="toc-item-num">1.1.8&nbsp;&nbsp;</span>eye</a></span></li><li><span><a href="#random" data-toc-modified-id="random-1.1.9"><span class="toc-item-num">1.1.9&nbsp;&nbsp;</span>random</a></span></li><li><span><a href="#reshape" data-toc-modified-id="reshape-1.1.10"><span class="toc-item-num">1.1.10&nbsp;&nbsp;</span>reshape</a></span></li></ul></li><li><span><a href="#max,-min,-argmax,-argmin" data-toc-modified-id="max,-min,-argmax,-argmin-1.2"><span class="toc-item-num">1.2&nbsp;&nbsp;</span>max, min, argmax, argmin</a></span></li><li><span><a href="#shape,-dtype" data-toc-modified-id="shape,-dtype-1.3"><span class="toc-item-num">1.3&nbsp;&nbsp;</span>shape, dtype</a></span></li><li><span><a href="#NumPy-Indexing-and-Selection" data-toc-modified-id="NumPy-Indexing-and-Selection-1.4"><span class="toc-item-num">1.4&nbsp;&nbsp;</span>NumPy Indexing and Selection</a></span><ul class="toc-item"><li><span><a href="#Broadcasting" data-toc-modified-id="Broadcasting-1.4.1"><span class="toc-item-num">1.4.1&nbsp;&nbsp;</span>Broadcasting</a></span></li><li><span><a href="#indexing-in-2D-array" data-toc-modified-id="indexing-in-2D-array-1.4.2"><span class="toc-item-num">1.4.2&nbsp;&nbsp;</span>indexing in 2D array</a></span></li><li><span><a href="#Conditional-selection" data-toc-modified-id="Conditional-selection-1.4.3"><span class="toc-item-num">1.4.3&nbsp;&nbsp;</span>Conditional selection</a></span></li></ul></li><li><span><a href="#NumPy-Operations" data-toc-modified-id="NumPy-Operations-1.5"><span class="toc-item-num">1.5&nbsp;&nbsp;</span>NumPy Operations</a></span></li></ul></li></ul></div>

# NumPy
NumPy, short for Numerical Python, is one of the most important foundational pack‐
ages for numerical computing in Python. Most computational packages providing
scientific functionality use NumPy’s array objects as the lingua franca for data
exchange


```python
import numpy as np
```

## Array creation functions

|Function |Description |
|:-----------|:-----------|
|**array**| Convert input data (list, tuple, array, or other sequence type) to an ndarray either by inferring a dtype or explicitly specifying a dtype; copies the input data by default |
|**asarray**| Convert input to ndarray, but do not copy if the input is already an ndarray|
|**arange**| Like the built-in range but returns an ndarray instead of a list|
|**ones,ones_like**|Produce an array of all 1s with the given shape and dtype; ones_like takes another array and produces a ones array of the same shape and dtype|
|**zeros,zeros_like**| Like ones and ones_like but producing arrays of 0s instead|
|**empty,empty_like**| Create new arrays by allocating new memory, but do not populate with any values like ones and zeros|
|**full,full_like**|Produce an array of the given shape and dtype with all values set to the indicated “fill value” full_like takes another array and produces a filled array of the same shape and dtype|
|**eye, identity**| Create a square N × N identity matrix (1s on the diagonal and 0s elsewhere)|


### From list 


```python
MyList = [1, 2, 3]
type(MyList)
```




    list




```python
MyArr=np.array(MyList)

```


```python
type(MyArr)
```




    numpy.ndarray




```python
My_Matrix = [[1, 2, 2], [5, 6, 8], [1, 5, 6]]
My_Matrix
```




    [[1, 2, 2], [5, 6, 8], [1, 5, 6]]




```python
np.array(My_Matrix)
```




    array([[1, 2, 2],
           [5, 6, 8],
           [1, 5, 6]])



### Array creation using array functions 
`array(data type, value list)` function is used to create an array with data type and value list specified in its arguments.


```python
import array
  
# initializing array with array values
# initializes array with signed integers
arr = array.array('i', [1, 2, 3]) 
arr
```




    array('i', [1, 2, 3])



### Array creation using numpy methods 
**`numpy.empty(shape, dtype = float, order = ‘C’)`** : Return a new array of given shape and type, with random values.


```python
import numpy as np

b = np.empty(2, dtype=int)
print("Matrix b : \n", b)

a = np.empty([2, 2], dtype=int)
print("\nMatrix a : \n", a)

c = np.empty([3, 3])
print("\nMatrix c : \n", c)
```

    Matrix b : 
     [1065353216 1065353216]
    
    Matrix a : 
     [[1118797009 1919926152]
     [1706021002  505578125]]
    
    Matrix c : 
     [[0.00000000e+000 0.00000000e+000 0.00000000e+000]
     [0.00000000e+000 0.00000000e+000 6.24498976e-321]
     [1.03977794e-312 8.70018274e-313 4.45038538e-308]]
    

### arange
`arange([start,] stop[, step,][, dtype])`

    start : [optional] start of interval range. By default start = 0
    stop  : end of interval range
    step  : [optional] step size of interval. By default step size = 1,  
    For any output out, this is the distance between two adjacent values, out[i+1] - out[i]. 
    dtype : type of output array


```python
np.arange(10)
```




    array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])




```python
np.arange(0,10)
```




    array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])




```python
np.arange(0,10,2)
```




    array([0, 2, 4, 6, 8])




```python
np.arange(1,101)
```




    array([  1,   2,   3,   4,   5,   6,   7,   8,   9,  10,  11,  12,  13,
            14,  15,  16,  17,  18,  19,  20,  21,  22,  23,  24,  25,  26,
            27,  28,  29,  30,  31,  32,  33,  34,  35,  36,  37,  38,  39,
            40,  41,  42,  43,  44,  45,  46,  47,  48,  49,  50,  51,  52,
            53,  54,  55,  56,  57,  58,  59,  60,  61,  62,  63,  64,  65,
            66,  67,  68,  69,  70,  71,  72,  73,  74,  75,  76,  77,  78,
            79,  80,  81,  82,  83,  84,  85,  86,  87,  88,  89,  90,  91,
            92,  93,  94,  95,  96,  97,  98,  99, 100])




```python
np.arange(0,101,20)
```




    array([  0,  20,  40,  60,  80, 100])



### zeros
`numpy.zeros(shape, dtype = None, order = 'C')`

    shape : integer or sequence of integers
    order  : C_contiguous or F_contiguous
         C-contiguous order in memory(last index varies the fastest)
         C order means that operating row-rise on the array will be slightly quicker
         FORTRAN-contiguous order in memory (first index varies the fastest).
         F order means that column-wise operations will be faster. 
    dtype : [optional, float(byDeafult)] Data type of returned array




```python
np.zeros(5)
```




    array([0., 0., 0., 0., 0.])




```python
np.zeros((3,3))
```




    array([[0., 0., 0.],
           [0., 0., 0.],
           [0., 0., 0.]])




```python
np.zeros((2,5))
```




    array([[0., 0., 0., 0., 0.],
           [0., 0., 0., 0., 0.]])



### ones


```python
np.ones((2,5))
```




    array([[1., 1., 1., 1., 1.],
           [1., 1., 1., 1., 1.]])




```python
np.ones(4)
```




    array([1., 1., 1., 1.])



### linspace
The `numpy.linspace()` function returns number spaces evenly w.r.t interval. Similar to `numpy.arange()` function but instead of step it uses sample number.

```numpy.linspace(start,stop,num = 50,endpoint = True,retstep = False,dtype = None)```

    ->start  : [optional] start of interval range. By default start = 0
    ->stop   : end of interval range
    ->restep : If True, return (samples, step). By deflut restep = False
    ->num    : [int, optional] No. of samples to generate
    ->dtype  : type of output array


```python
np.linspace(0,10,3)
```




    array([ 0.,  5., 10.])




```python
np.linspace(0,10,11)
```




    array([ 0.,  1.,  2.,  3.,  4.,  5.,  6.,  7.,  8.,  9., 10.])




```python
np.linspace(10,200,5)
```




    array([ 10. ,  57.5, 105. , 152.5, 200. ])




```python
len(np.linspace(10,200,5))
```




    5



### eye



```python
np.eye(5)
```




    array([[1., 0., 0., 0., 0.],
           [0., 1., 0., 0., 0.],
           [0., 0., 1., 0., 0.],
           [0., 0., 0., 1., 0.],
           [0., 0., 0., 0., 1.]])




```python
np.eye(3)
```




    array([[1., 0., 0.],
           [0., 1., 0.],
           [0., 0., 1.]])



### random
`rand(d0, d1, ..., dn)`
Create an array of the given shape and populate it with random samples from a uniform distribution over ``[0, 1)``.


```python
np.random.rand(1)
```




    array([0.44684956])




```python
np.random.rand(5)
```




    array([0.00409228, 0.58257588, 0.04609696, 0.1081864 , 0.01496536])




```python
np.random.rand(5,5)
```




    array([[0.71297395, 0.81037372, 0.68119351, 0.54086142, 0.96965231],
           [0.17034626, 0.71502332, 0.17963456, 0.84942978, 0.66702249],
           [0.25039683, 0.27667351, 0.54160488, 0.96438044, 0.31963327],
           [0.15218855, 0.32695061, 0.41040314, 0.18581687, 0.20543774],
           [0.99694804, 0.75934926, 0.28764941, 0.06669142, 0.83341272]])



`np.random.randn()` Return a sample (or samples) from the "standard normal" distribution.


```python
np.random.randn(2,3) #Return a sample (or samples) from the "standard normal" distribution.
```




    array([[ 1.79924835, -0.10639448,  1.30960256],
           [ 2.38144296,  0.52566785, -0.16244737]])



`randint(low, high=None, size=None, dtype=int)`

Return random integers from `low` (inclusive) to `high` (exclusive).


```python
np.random.randint(0,101,10)
```




    array([26, 70, 72, 14, 60, 14, 27, 48,  2, 56])




```python
np.random.randint(0,101,(4,5))
```




    array([[27,  5,  0, 16, 48],
           [51, 70, 23, 88, 65],
           [90,  5, 72, 90, 89],
           [78, 38, 16, 80,  5]])




```python
np.random.seed(42)
np.random.rand(4)
```




    array([0.37454012, 0.95071431, 0.73199394, 0.59865848])




```python
np.random.seed(42)
np.random.rand(4)
```




    array([0.37454012, 0.95071431, 0.73199394, 0.59865848])




```python
np.random.rand(4)
```




    array([0.15601864, 0.15599452, 0.05808361, 0.86617615])




```python
np.random.seed(101)
np.random.rand(4)
```




    array([0.51639863, 0.57066759, 0.02847423, 0.17152166])




```python
np.random.seed(101)
np.random.rand(4)
```




    array([0.51639863, 0.57066759, 0.02847423, 0.17152166])



### reshape



```python
arr=np.arange(0,25)
arr
```




    array([ 0,  1,  2,  3,  4,  5,  6,  7,  8,  9, 10, 11, 12, 13, 14, 15, 16,
           17, 18, 19, 20, 21, 22, 23, 24])




```python
arr.reshape(5,5)
```




    array([[ 0,  1,  2,  3,  4],
           [ 5,  6,  7,  8,  9],
           [10, 11, 12, 13, 14],
           [15, 16, 17, 18, 19],
           [20, 21, 22, 23, 24]])




```python
arr.reshape(5,4)
```


    ---------------------------------------------------------------------------

    ValueError                                Traceback (most recent call last)

    <ipython-input-48-081adc27730c> in <module>
    ----> 1 arr.reshape(5,4)
    

    ValueError: cannot reshape array of size 25 into shape (5,4)


## max, min, argmax, argmin


```python
ranarr=np.random.randint(0,101,10)
ranarr
```




    array([12, 93, 40, 49, 83,  8, 29, 59, 34, 44])




```python
ranarr.max()
```




    93




```python
ranarr.min()
```




    8




```python
ranarr.argmax()
```




    1




```python
ranarr.argmin()
```




    5



## shape, dtype


```python
ranarr.dtype
```




    dtype('int32')




```python
arr
```




    array([ 0,  1,  2,  3,  4,  5,  6,  7,  8,  9, 10, 11, 12, 13, 14, 15, 16,
           17, 18, 19, 20, 21, 22, 23, 24])




```python
arr.shape
```




    (25,)




```python
arr=arr.reshape(5,5)
arr
```




    array([[ 0,  1,  2,  3,  4],
           [ 5,  6,  7,  8,  9],
           [10, 11, 12, 13, 14],
           [15, 16, 17, 18, 19],
           [20, 21, 22, 23, 24]])




```python
arr.shape
```




    (5, 5)



## NumPy Indexing and Selection
- **Grabbing single element**
- **Grabbing slice of element**
- **Broadcasting selection**
- **Indexing and selection in 2-dimension**
- **Conditional selection**





```python
import numpy as np
```


```python
arr=np.arange(0,11)
arr
```




    array([ 0,  1,  2,  3,  4,  5,  6,  7,  8,  9, 10])




```python
arr[8]
```




    8




```python
arr[1]
```




    1




```python
arr[0]
```




    0




```python
arr[1:8]
```




    array([1, 2, 3, 4, 5, 6, 7])




```python
arr[0:5]
```




    array([0, 1, 2, 3, 4])




```python
arr[:5]
```




    array([0, 1, 2, 3, 4])




```python
arr[5:]
```




    array([ 5,  6,  7,  8,  9, 10])



### Broadcasting


```python
arr[0:5]=100
```


```python
arr
```




    array([100, 100, 100, 100, 100,   5,   6,   7,   8,   9,  10])




```python
arr=np.arange(0,11)
arr
```




    array([ 0,  1,  2,  3,  4,  5,  6,  7,  8,  9, 10])




```python
slice_of_array=arr[0:5]
```


```python
slice_of_array
```




    array([0, 1, 2, 3, 4])




```python
slice_of_array[:]=99
```


```python
slice_of_array
```




    array([99, 99, 99, 99, 99])




```python
arr
```




    array([99, 99, 99, 99, 99,  5,  6,  7,  8,  9, 10])



original array changed

if you want to not change in array you have to make copy


```python
arr_copy=arr.copy()
```


```python
arr_copy[:]=99
arr_copy
```




    array([99, 99, 99, 99, 99, 99, 99, 99, 99, 99, 99])




```python
arr
```




    array([99, 99, 99, 99, 99,  5,  6,  7,  8,  9, 10])



### indexing in 2D array


```python
import numpy as np
arr_2d=np.array([[1,2,3],[4,5,6],[7,8,9]])
arr_2d
```




    array([[1, 2, 3],
           [4, 5, 6],
           [7, 8, 9]])




```python
arr_2d.shape
```




    (3, 3)




```python
arr_2d[0]
```




    array([1, 2, 3])




```python
arr_2d[2]
```




    array([7, 8, 9])




```python
arr_2d[1,1]
```




    5




```python
arr_2d[0,0]
```




    1




```python
arr_2d[:2]
```




    array([[1, 2, 3],
           [4, 5, 6]])




```python
arr_2d[0:2,1:]
```




    array([[2, 3],
           [5, 6]])



### Conditional selection


```python
arr=np.arange(1,11)
arr
```




    array([ 1,  2,  3,  4,  5,  6,  7,  8,  9, 10])




```python
arr>4
```




    array([False, False, False, False,  True,  True,  True,  True,  True,
            True])




```python
bool_arr=arr>4
```


```python
bool_arr
```




    array([False, False, False, False,  True,  True,  True,  True,  True,
            True])




```python
arr[bool_arr]
```




    array([ 5,  6,  7,  8,  9, 10])




```python
arr[arr>4]
```




    array([ 5,  6,  7,  8,  9, 10])



## NumPy Operations


```python
import numpy as np

```


```python
arr=np.arange(0,10)
arr
```




    array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])




```python
arr+5
```




    array([ 5,  6,  7,  8,  9, 10, 11, 12, 13, 14])




```python
arr-2
```




    array([-2, -1,  0,  1,  2,  3,  4,  5,  6,  7])




```python
arr+arr
```




    array([ 0,  2,  4,  6,  8, 10, 12, 14, 16, 18])




```python
arr*arr
```




    array([ 0,  1,  4,  9, 16, 25, 36, 49, 64, 81])




```python
arr-arr
```




    array([0, 0, 0, 0, 0, 0, 0, 0, 0, 0])




```python
arr/arr
```

    <ipython-input-31-50b4ced5627e>:1: RuntimeWarning: invalid value encountered in true_divide
      arr/arr
    




    array([nan,  1.,  1.,  1.,  1.,  1.,  1.,  1.,  1.,  1.])




```python
1/arr
```

    <ipython-input-33-016353831300>:1: RuntimeWarning: divide by zero encountered in true_divide
      1/arr
    




    array([       inf, 1.        , 0.5       , 0.33333333, 0.25      ,
           0.2       , 0.16666667, 0.14285714, 0.125     , 0.11111111])




```python
np.sqrt(arr)
```




    array([0.        , 1.        , 1.41421356, 1.73205081, 2.        ,
           2.23606798, 2.44948974, 2.64575131, 2.82842712, 3.        ])




```python
np.log(arr)
```

    <ipython-input-35-a67b4ae04e95>:1: RuntimeWarning: divide by zero encountered in log
      np.log(arr)
    




    array([      -inf, 0.        , 0.69314718, 1.09861229, 1.38629436,
           1.60943791, 1.79175947, 1.94591015, 2.07944154, 2.19722458])




```python
arr.sum()
```




    45




```python
arr.mean()
```




    4.5




```python
arr.var()
```




    8.25




```python
arr.std()
```




    2.8722813232690143




```python
arr_2d=np.arange(0,25).reshape(5,5)
```


```python
arr_2d
```




    array([[ 0,  1,  2,  3,  4],
           [ 5,  6,  7,  8,  9],
           [10, 11, 12, 13, 14],
           [15, 16, 17, 18, 19],
           [20, 21, 22, 23, 24]])




```python
arr_2d.sum()
```




    300




```python
arr_2d.sum(axis=0) #across rows or sum of columns
```




    array([50, 55, 60, 65, 70])




```python
arr_2d.sum(axis=1) #across column or sum of rows
```




    array([ 10,  35,  60,  85, 110])



---
