Python 3.10.4 (tags/v3.10.4:9d38120, Mar 23 2022, 23:13:41) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
x = [3,1,4,5,2]
type(x)
<class 'list'>
x = (3,1,4,5,2)
type(x)
<class 'tuple'>
x = 3,1,4,5,2
type(x)
<class 'tuple'>
del x[0]
Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    del x[0]
TypeError: 'tuple' object doesn't support item deletion
x[0] = 20
Traceback (most recent call last):
  File "<pyshell#7>", line 1, in <module>
    x[0] = 20
TypeError: 'tuple' object does not support item assignment
data = name, age, salary = "Ram", 30, 45000
data
('Ram', 30, 45000)
name
'Ram'
age
30
salary
45000
data
('Ram', 30, 45000)
a,b,c = data
a
'Ram'
b
30
c
45000
