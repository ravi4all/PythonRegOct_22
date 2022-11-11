Python 3.10.4 (tags/v3.10.4:9d38120, Mar 23 2022, 23:13:41) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
x = []
x = list()
x = [2,3,12,2,54,7,8,3,16]
x = [2,3,12,2,54,7,8,3,16,4.56,"hello",True]
x
[2, 3, 12, 2, 54, 7, 8, 3, 16, 4.56, 'hello', True]
x[::-1]
[True, 'hello', 4.56, 16, 3, 8, 7, 54, 2, 12, 3, 2]
x[0]
2
x[0:4]
[2, 3, 12, 2]
x[4:]
[54, 7, 8, 3, 16, 4.56, 'hello', True]
x = []
x.append(5)
x
[5]
x.append(7)
x
[5, 7]
x.append(3)
x.append(9)
x
[5, 7, 3, 9]
x.append(5,3,6,8)
Traceback (most recent call last):
  File "<pyshell#17>", line 1, in <module>
    x.append(5,3,6,8)
TypeError: list.append() takes exactly one argument (4 given)
x = []
for i in range(1,51):
    x.append(i)

    
x
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50]
x = []
for i in range(1,51):
    if i % 2 == 0:
        x.append(i)

        
x
[2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48, 50]
x = []
x = [4,8,6,7,1,32]
x.append(10)
x
[4, 8, 6, 7, 1, 32, 10]
x.extend(5,2,34,12)
Traceback (most recent call last):
  File "<pyshell#31>", line 1, in <module>
    x.extend(5,2,34,12)
TypeError: list.extend() takes exactly one argument (4 given)
x.extend([5,2,34,12])
x
[4, 8, 6, 7, 1, 32, 10, 5, 2, 34, 12]
x.append([5,2,34,12])
x
[4, 8, 6, 7, 1, 32, 10, 5, 2, 34, 12, [5, 2, 34, 12]]
#Nested List - list inside list
x[-1]
[5, 2, 34, 12]
x.pop()
[5, 2, 34, 12]
x
[4, 8, 6, 7, 1, 32, 10, 5, 2, 34, 12]
x.pop()
12
x
[4, 8, 6, 7, 1, 32, 10, 5, 2, 34]
x.insert(5,11)
x
[4, 8, 6, 7, 1, 11, 32, 10, 5, 2, 34]
x.pop(5)
11
x
[4, 8, 6, 7, 1, 32, 10, 5, 2, 34]
x.count(5)
1
x.count(2)
1
x.index(5)
7
x.index(4)
0
x.remove(0)
Traceback (most recent call last):
  File "<pyshell#50>", line 1, in <module>
    x.remove(0)
ValueError: list.remove(x): x not in list
x.remove(4) # delete by value
x
[8, 6, 7, 1, 32, 10, 5, 2, 34]
x.reverse()
x
[34, 2, 5, 10, 32, 1, 7, 6, 8]
x.sort()
x
[1, 2, 5, 6, 7, 8, 10, 32, 34]
x.sort(reverse=True)
x
[34, 32, 10, 8, 7, 6, 5, 2, 1]
for item in x:
    print(item)

    
34
32
10
8
7
6
5
2
1
names = ["John", "Shawn", "Steve", "Adam"]
for n in names:
    print(n)

    
John
Shawn
Steve
Adam
for i in range(len(names)):
    print(i, ":", names[i])

    
0 : John
1 : Shawn
2 : Steve
3 : Adam
marks = [45,77,55,90,78,26,95,59]
for i in range(len(marks)):
    if marks[i] > 70:
        print(marks[i])

        
77
90
78
95
x = []
x = [i for i in range(1,11)]
x
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
x = [i for i in range(1,11) if i % 2 == 0]
x
[2, 4, 6, 8, 10]
x = [["John","Shawn","Max"],[45000,56000,30000],["IT","HR","IT"]]
x
[['John', 'Shawn', 'Max'], [45000, 56000, 30000], ['IT', 'HR', 'IT']]
x[0]
['John', 'Shawn', 'Max']
x[1]
[45000, 56000, 30000]
x[2]
['IT', 'HR', 'IT']
x[0][0]
'John'
x[0][1]
'Shawn'
x[0][2]
'Max'
x[1][0]
45000
x[1][0]
45000
