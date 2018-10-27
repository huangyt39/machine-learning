
## Numpy


```python
from numpy import *
```


```python
data = array([[0.85, 0.2, 0.69],[0.52, 0.25, 0.56]])
data + data
```




    array([[1.7 , 0.4 , 1.38],
           [1.04, 0.5 , 1.12]])




```python
data*10
```




    array([[8.5, 2. , 6.9],
           [5.2, 2.5, 5.6]])




```python
data ** 0.5
```




    array([[0.92195445, 0.4472136 , 0.83066239],
           [0.72111026, 0.5       , 0.74833148]])




```python
data.shape
```




    (2, 3)




```python
data.dtype
```




    dtype('float64')




```python
zeros((3,6))
```




    array([[0., 0., 0., 0., 0., 0.],
           [0., 0., 0., 0., 0., 0.],
           [0., 0., 0., 0., 0., 0.]])




```python
eye(4)
```




    array([[1., 0., 0., 0.],
           [0., 1., 0., 0.],
           [0., 0., 1., 0.],
           [0., 0., 0., 1.]])




```python
arr = array([1,2,3],dtype=float64)
arr
```




    array([1., 2., 3.])




```python
arr += [0.4,0.4,0.4]
int_arr = arr.astype(int64)
int_arr
```




    array([1, 2, 3], dtype=int64)




```python
str_arr = arr.astype(string_)
str_arr
```




    array([b'1.4', b'2.4', b'3.4'], dtype='|S32')



类似range，返回一个array


```python
arange(10)
```




    array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])



[,]等价于[][]

标量和数组均可赋值给arr[0]


```python
arr2d = array([[1,2,3],[4,5,6]])
oldarr = arr2d[0].copy()
arr2d[0] = 222
arr2d
```




    array([[222, 222, 222],
           [  4,   5,   6]])




```python
arr2d[0] = oldarr
arr2d[0]
```




    array([1, 2, 3])




```python
ran = random.randn(4,4)
ran
```




    array([[ 2.28116357,  0.42361614,  2.11505224, -0.42446749],
           [-1.36926063, -0.44394285, -1.20299377, -0.16742612],
           [ 0.08534791,  1.36327521,  1.02174783, -1.35361273],
           [-0.45921772,  0.22887775, -0.33502804,  0.62939994]])




```python
names = array(['aaa','bbb','ccc','ddd'])
names == 'aaa'
```




    array([ True, False, False, False])




```python
ran[names=='aaa',2]
```




    array([2.11505224])




```python
array(data<0.5)
```




    array([[False,  True, False],
           [False,  True, False]])




```python
data[data<0.5] = 0
data
```




    array([[0.85, 0.  , 0.69],
           [0.52, 0.  , 0.56]])




```python
arri = array([[i, i, i, i] for i in range(5)])
arri
```




    array([[0, 0, 0, 0],
           [1, 1, 1, 1],
           [2, 2, 2, 2],
           [3, 3, 3, 3],
           [4, 4, 4, 4]])




```python
arri[[2,3,0]]
```




    array([[2, 2, 2, 2],
           [3, 3, 3, 3],
           [0, 0, 0, 0]])




```python
arrr = array([i for i in range(32)])
arrr.reshape(8,4)
```




    array([[ 0,  1,  2,  3],
           [ 4,  5,  6,  7],
           [ 8,  9, 10, 11],
           [12, 13, 14, 15],
           [16, 17, 18, 19],
           [20, 21, 22, 23],
           [24, 25, 26, 27],
           [28, 29, 30, 31]])



花式索引区别于切片，会进行深复制


```python
arrr.reshape(8,4).T
```




    array([[ 0,  4,  8, 12, 16, 20, 24, 28],
           [ 1,  5,  9, 13, 17, 21, 25, 29],
           [ 2,  6, 10, 14, 18, 22, 26, 30],
           [ 3,  7, 11, 15, 19, 23, 27, 31]])



dot:矩阵内积XTX


```python
dot(data.T,data)
```




    array([[0.9929, 0.    , 0.8777],
           [0.    , 0.    , 0.    ],
           [0.8777, 0.    , 0.7897]])



transpose要传入一个由轴编号组成的元祖


```python
arr = arange(16).reshape((2,2,4))
arr
```




    array([[[ 0,  1,  2,  3],
            [ 4,  5,  6,  7]],
    
           [[ 8,  9, 10, 11],
            [12, 13, 14, 15]]])




```python
arr.transpose((1,0,2))
```




    array([[[ 0,  1,  2,  3],
            [ 8,  9, 10, 11]],
    
           [[ 4,  5,  6,  7],
            [12, 13, 14, 15]]])




```python
x = array([1,5,3,1.5,4])
y = array([2,2,2,2,2])
maximum(x,y)
```




    array([2., 5., 3., 2., 4.])



一元ufun:abs fabs sqrt exp rint（四舍五入） ceil（大于等于该值的最小整数） sign（正负号）sincostan...

二元ufun:add divide（丢弃余数） power maximum mod 


```python
x > y
```




    array([False,  True,  True, False,  True])



meshgrid


```python
xnums = arange(4)
ynums = arange(5)
xx,yy = meshgrid(xnums, ynums)
print("xx: ",xx)
print("yy: ",yy)
```

    xx:  [[0 1 2 3]
     [0 1 2 3]
     [0 1 2 3]
     [0 1 2 3]
     [0 1 2 3]]
    yy:  [[0 0 0 0]
     [1 1 1 1]
     [2 2 2 2]
     [3 3 3 3]
     [4 4 4 4]]
    

[(x if c else y) for x,y,c in zip(xarr,yarr,cond)] == 
where(cond, xarr, yarr)

且where的二三个参数不必是数组，可以是标量值

可用于类似：将所有正值替换为2，负值替换为-2

eg where(arr > 0,2, -2)

where(cond1 and cond2, 0 , 

    where(cond1, 1,
    
       where(cond2, 2, 3)))

统计方法:mean sum std var min max sumsum（所有元素的累积和）...

可接受一个axis参数，用于计算该轴上的值，如mean(axis=1)

用于布尔型数组的方法

sum():统计正值的数量

any():是否存在正值

all():是否都是正值


```python
arrra = random.randn(4)
arrra
```




    array([-0.2887347 ,  1.60835297, -0.85117141,  0.67146065])




```python
sort(arrra)
```




    array([-0.85117141, -0.2887347 ,  0.67146065,  1.60835297])




```python
arrra = random.randn(5,3)
arrra
```




    array([[-1.25500558, -0.30907417, -1.06945137],
           [ 0.15746399,  2.21500089, -0.43894227],
           [ 0.1974026 , -0.44326413, -0.68874571],
           [ 0.34834095, -1.66883909,  0.89800544],
           [ 0.72059941,  1.01992621,  0.88948023]])




```python
arrra.sort(1)
arrra
```




    array([[-1.25500558, -1.06945137, -0.30907417],
           [-0.43894227,  0.15746399,  2.21500089],
           [-0.68874571, -0.44326413,  0.1974026 ],
           [-1.66883909,  0.34834095,  0.89800544],
           [ 0.72059941,  0.88948023,  1.01992621]])



计算5%分位数

large_arr.sort()

large_arr[int(0.05 * len(large_arr))]


```python
names = array(['Bob', 'Wynton', 'Cindy', 'Bob', 'Cindy'])
unique(names)
```




    array(['Bob', 'Cindy', 'Wynton'], dtype='<U6')



集合运算:unique, intersect1d（公共元素，返回有序结果） union in1d（元素是否包含于）

读写磁盘数据

save('array',arr)或save('array.npy',arr)

load('array.npy')

savez('array.npz', a=arr, b=arr)

arch = load('array.npz')

arch['b']
