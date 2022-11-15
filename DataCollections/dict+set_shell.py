Python 3.10.4 (tags/v3.10.4:9d38120, Mar 23 2022, 23:13:41) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
data = ["John",1022,"HR",45000]
data = {"name" : "John", "id" : 1022, "dept" : "HR", "salary" : 45000}
data
{'name': 'John', 'id': 1022, 'dept': 'HR', 'salary': 45000}
data[0]
Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    data[0]
KeyError: 0
data.keys()
dict_keys(['name', 'id', 'dept', 'salary'])
data.values()
dict_values(['John', 1022, 'HR', 45000])
data.items()
dict_items([('name', 'John'), ('id', 1022), ('dept', 'HR'), ('salary', 45000)])
data["name"]
'John'
data["id"]
1022
data["salary"]
45000
data
{'name': 'John', 'id': 1022, 'dept': 'HR', 'salary': 45000}
data["address"] = "Delhi"
data
{'name': 'John', 'id': 1022, 'dept': 'HR', 'salary': 45000, 'address': 'Delhi'}
data["id"] = 1011
data
{'name': 'John', 'id': 1011, 'dept': 'HR', 'salary': 45000, 'address': 'Delhi'}
x = {"name" : "John", "name" : "Mac"}
x
{'name': 'Mac'}
data["phone"]
Traceback (most recent call last):
  File "<pyshell#17>", line 1, in <module>
    data["phone"]
KeyError: 'phone'
data.get("name")
'John'
data.get("phone")
data.get("phone","Not Available")
'Not Available'
data.get("name")
'John'
data.get("phone","Not Available")
'Not Available'
data.popitem()
('address', 'Delhi')
data.pop("id")
1011
data
{'name': 'John', 'dept': 'HR', 'salary': 45000}
x = {"id" : 101, "phone" : 8987635643, "address" : "Delhi"}
data.update(x)
data
{'name': 'John', 'dept': 'HR', 'salary': 45000, 'id': 101, 'phone': 8987635643, 'address': 'Delhi'}
for item in data:
    print(item)

    
name
dept
salary
id
phone
address
for item in data:
    print(item, data[item])

    
name John
dept HR
salary 45000
id 101
phone 8987635643
address Delhi

= RESTART: D:/Batches/2022/PythonOctRegEve/DataCollections/dict_exercise_p1.py
['John', 'Max', 'Nick', 'Shawn']
['IT', 'IT', 'HR', 'IT']
[45000, 80000, 55000, 25000]

= RESTART: D:/Batches/2022/PythonOctRegEve/DataCollections/dict_exercise_p1.py
John IT 45000
Max IT 80000
Nick HR 55000
Shawn IT 25000

= RESTART: D:/Batches/2022/PythonOctRegEve/DataCollections/dict_exercise_p1.py
John IT 45000
Max IT 80000
Nick HR 55000
Shawn IT 25000
John IT 45000
Max IT 80000
Shawn IT 25000

= RESTART: D:/Batches/2022/PythonOctRegEve/DataCollections/dict_exercise_p1.py
John IT 45000
Max IT 80000
Shawn IT 25000

= RESTART: D:/Batches/2022/PythonOctRegEve/DataCollections/dict_exercise_p1.py
John IT 45000
Max IT 80000
Shawn IT 25000
Total salary of IT : 150000
data = {3,4,1,4,6,8,12,3,6,8,9,0,12,34}
data
{0, 1, 34, 3, 4, 6, 8, 9, 12}
x = {3,4,1,4,6,8,12,3,6,8,9,0,12,34}
x
{0, 1, 34, 3, 4, 6, 8, 9, 12}
y = {4,2,5,9,0,6,5,1,2,4,12,45,67,8,31}
y
{0, 1, 2, 67, 4, 5, 6, 8, 9, 12, 45, 31}
x & y
{0, 1, 4, 6, 8, 9, 12}
x.intersection(y)
{0, 1, 4, 6, 8, 9, 12}
x | y
{0, 1, 2, 3, 4, 67, 6, 5, 8, 9, 12, 31, 34, 45}
x.union(y)
{0, 1, 2, 3, 4, 67, 6, 5, 8, 9, 12, 31, 34, 45}
x - y
{34, 3}
x.difference(y)
{34, 3}
x[0]
Traceback (most recent call last):
  File "<pyshell#46>", line 1, in <module>
    x[0]
TypeError: 'set' object is not subscriptable
x.add(100)
x
{0, 1, 34, 3, 4, 100, 6, 8, 9, 12}
