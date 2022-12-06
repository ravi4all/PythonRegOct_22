Python 3.10.4 (tags/v3.10.4:9d38120, Mar 23 2022, 23:13:41) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
import numpy as np
x = np.array([4,3,5,7,1,6])
x
array([4, 3, 5, 7, 1, 6])
x = [4,3,5,7,3,6,7]
x
[4, 3, 5, 7, 3, 6, 7]
x = [4,3,5,7,3,6,7,'hello']
x = np.array([4,3,5,7,1,6,'hello'])
x
array(['4', '3', '5', '7', '1', '6', 'hello'], dtype='<U11')
x = np.arange(1,10)
x
array([1, 2, 3, 4, 5, 6, 7, 8, 9])
np.random.random(5)
array([0.81195561, 0.14510286, 0.44893084, 0.15877016, 0.18278727])
x = np.random.randint(1,50,8)
x
array([40, 37, 20,  3, 16, 11, 32, 49])
x[0]
40
x[:-1]
array([40, 37, 20,  3, 16, 11, 32])
x[::-1]
array([49, 32, 11, 16,  3, 20, 37, 40])
x[3:6]
array([ 3, 16, 11])
x
array([40, 37, 20,  3, 16, 11, 32, 49])
x = np.random.randint(1,50,(4,6))
x
array([[16, 45, 12, 19,  7, 13],
       [ 4,  4, 38, 24, 32, 47],
       [39, 34,  4, 14, 14, 45],
       [ 3, 45,  1, 33,  4,  7]])
x.shape
(4, 6)
x.ndim
2
x[0]
array([16, 45, 12, 19,  7, 13])
x[1]
array([ 4,  4, 38, 24, 32, 47])
x[:,0]
array([16,  4, 39,  3])
x[:,0:1]
array([[16],
       [ 4],
       [39],
       [ 3]])
x[:,0:3]
array([[16, 45, 12],
       [ 4,  4, 38],
       [39, 34,  4],
       [ 3, 45,  1]])
x[:,2:4]
array([[12, 19],
       [38, 24],
       [ 4, 14],
       [ 1, 33]])
x[2:4,3:5]
array([[14, 14],
       [33,  4]])
x
array([[16, 45, 12, 19,  7, 13],
       [ 4,  4, 38, 24, 32, 47],
       [39, 34,  4, 14, 14, 45],
       [ 3, 45,  1, 33,  4,  7]])
x[0][0]
16
x[0][4]
7
x[2][3]
14
x.shape
(4, 6)
x.T
array([[16,  4, 39,  3],
       [45,  4, 34, 45],
       [12, 38,  4,  1],
       [19, 24, 14, 33],
       [ 7, 32, 14,  4],
       [13, 47, 45,  7]])
x.reshape((3,8))
array([[16, 45, 12, 19,  7, 13,  4,  4],
       [38, 24, 32, 47, 39, 34,  4, 14],
       [14, 45,  3, 45,  1, 33,  4,  7]])
x
array([[16, 45, 12, 19,  7, 13],
       [ 4,  4, 38, 24, 32, 47],
       [39, 34,  4, 14, 14, 45],
       [ 3, 45,  1, 33,  4,  7]])
x + 5
array([[21, 50, 17, 24, 12, 18],
       [ 9,  9, 43, 29, 37, 52],
       [44, 39,  9, 19, 19, 50],
       [ 8, 50,  6, 38,  9, 12]])
x- 5
array([[11, 40,  7, 14,  2,  8],
       [-1, -1, 33, 19, 27, 42],
       [34, 29, -1,  9,  9, 40],
       [-2, 40, -4, 28, -1,  2]])
x * 2
array([[32, 90, 24, 38, 14, 26],
       [ 8,  8, 76, 48, 64, 94],
       [78, 68,  8, 28, 28, 90],
       [ 6, 90,  2, 66,  8, 14]])
x.sum()
504
x
array([[16, 45, 12, 19,  7, 13],
       [ 4,  4, 38, 24, 32, 47],
       [39, 34,  4, 14, 14, 45],
       [ 3, 45,  1, 33,  4,  7]])
x.min()
1
x.max()
47
x.sum(axis=0)
array([ 62, 128,  55,  90,  57, 112])
x.sum(axis=1)
array([112, 149, 150,  93])
x.min(axis=0)
array([ 3,  4,  1, 14,  4,  7])
x.max(axis=1)
array([45, 47, 45, 45])
x.mean()
21.0
x.mean(axis=0)
array([15.5 , 32.  , 13.75, 22.5 , 14.25, 28.  ])
x.mean(axis=1)
array([18.66666667, 24.83333333, 25.        , 15.5       ])
x
array([[16, 45, 12, 19,  7, 13],
       [ 4,  4, 38, 24, 32, 47],
       [39, 34,  4, 14, 14, 45],
       [ 3, 45,  1, 33,  4,  7]])
np.hstack((x, [4,5,3,2,1,6]))
Traceback (most recent call last):
  File "<pyshell#52>", line 1, in <module>
    np.hstack((x, [4,5,3,2,1,6]))
  File "<__array_function__ internals>", line 180, in hstack
  File "C:\Python310\lib\site-packages\numpy\core\shape_base.py", line 345, in hstack
    return _nx.concatenate(arrs, 1)
  File "<__array_function__ internals>", line 180, in concatenate
ValueError: all the input arrays must have same number of dimensions, but the array at index 0 has 2 dimension(s) and the array at index 1 has 1 dimension(s)
np.vstack((x, [4,5,3,2,1,6]))
array([[16, 45, 12, 19,  7, 13],
       [ 4,  4, 38, 24, 32, 47],
       [39, 34,  4, 14, 14, 45],
       [ 3, 45,  1, 33,  4,  7],
       [ 4,  5,  3,  2,  1,  6]])
np.hstack((x, [4,5,3,2]))
Traceback (most recent call last):
  File "<pyshell#54>", line 1, in <module>
    np.hstack((x, [4,5,3,2]))
  File "<__array_function__ internals>", line 180, in hstack
  File "C:\Python310\lib\site-packages\numpy\core\shape_base.py", line 345, in hstack
    return _nx.concatenate(arrs, 1)
  File "<__array_function__ internals>", line 180, in concatenate
ValueError: all the input arrays must have same number of dimensions, but the array at index 0 has 2 dimension(s) and the array at index 1 has 1 dimension(s)
x
array([[16, 45, 12, 19,  7, 13],
       [ 4,  4, 38, 24, 32, 47],
       [39, 34,  4, 14, 14, 45],
       [ 3, 45,  1, 33,  4,  7]])
np.vstack((x, [4,5,3,2,1,6]))
array([[16, 45, 12, 19,  7, 13],
       [ 4,  4, 38, 24, 32, 47],
       [39, 34,  4, 14, 14, 45],
       [ 3, 45,  1, 33,  4,  7],
       [ 4,  5,  3,  2,  1,  6]])
x1 = np.array([[5],[10],[15],[20]])
x
array([[16, 45, 12, 19,  7, 13],
       [ 4,  4, 38, 24, 32, 47],
       [39, 34,  4, 14, 14, 45],
       [ 3, 45,  1, 33,  4,  7]])
x1
array([[ 5],
       [10],
       [15],
       [20]])
np.hstack((x,x1))
array([[16, 45, 12, 19,  7, 13,  5],
       [ 4,  4, 38, 24, 32, 47, 10],
       [39, 34,  4, 14, 14, 45, 15],
       [ 3, 45,  1, 33,  4,  7, 20]])
x = np.array([4,3,5,7,1,6])
x = np.array([[1,2,4],[4,6,7],[21,45,8],[2,46,8]])
x
array([[ 1,  2,  4],
       [ 4,  6,  7],
       [21, 45,  8],
       [ 2, 46,  8]])
np.r_[x, [3,4,6,2]]
Traceback (most recent call last):
  File "<pyshell#64>", line 1, in <module>
    np.r_[x, [3,4,6,2]]
  File "C:\Python310\lib\site-packages\numpy\lib\index_tricks.py", line 412, in __getitem__
    res = self.concatenate(tuple(objs), axis=axis)
  File "<__array_function__ internals>", line 180, in concatenate
ValueError: all the input arrays must have same number of dimensions, but the array at index 0 has 2 dimension(s) and the array at index 1 has 1 dimension(s)
np.r_[x, [3,4,6]]
Traceback (most recent call last):
  File "<pyshell#65>", line 1, in <module>
    np.r_[x, [3,4,6]]
  File "C:\Python310\lib\site-packages\numpy\lib\index_tricks.py", line 412, in __getitem__
    res = self.concatenate(tuple(objs), axis=axis)
  File "<__array_function__ internals>", line 180, in concatenate
ValueError: all the input arrays must have same number of dimensions, but the array at index 0 has 2 dimension(s) and the array at index 1 has 1 dimension(s)
np.r_[x, [[3,4,6,2]]]
Traceback (most recent call last):
  File "<pyshell#66>", line 1, in <module>
    np.r_[x, [[3,4,6,2]]]
  File "C:\Python310\lib\site-packages\numpy\lib\index_tricks.py", line 412, in __getitem__
    res = self.concatenate(tuple(objs), axis=axis)
  File "<__array_function__ internals>", line 180, in concatenate
ValueError: all the input array dimensions for the concatenation axis must match exactly, but along dimension 1, the array at index 0 has size 3 and the array at index 1 has size 4
x
array([[ 1,  2,  4],
       [ 4,  6,  7],
       [21, 45,  8],
       [ 2, 46,  8]])
x.shape
(4, 3)
x[0]
array([1, 2, 4])
np.r_[x, [[2],[5],[5]]]
Traceback (most recent call last):
  File "<pyshell#70>", line 1, in <module>
    np.r_[x, [[2],[5],[5]]]
  File "C:\Python310\lib\site-packages\numpy\lib\index_tricks.py", line 412, in __getitem__
    res = self.concatenate(tuple(objs), axis=axis)
  File "<__array_function__ internals>", line 180, in concatenate
ValueError: all the input array dimensions for the concatenation axis must match exactly, but along dimension 1, the array at index 0 has size 3 and the array at index 1 has size 1
np.r_[x, [[2,5,7]]]
array([[ 1,  2,  4],
       [ 4,  6,  7],
       [21, 45,  8],
       [ 2, 46,  8],
       [ 2,  5,  7]])
