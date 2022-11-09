Python 3.10.4 (tags/v3.10.4:9d38120, Mar 23 2022, 23:13:41) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
text = "Hello World"
text[0]
'H'
text[1]
'e'
text[2]
'l'
len(text)
11
text[10]
'd'
text[11]
Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    text[11]
IndexError: string index out of range
tetx[-1]
Traceback (most recent call last):
  File "<pyshell#7>", line 1, in <module>
    tetx[-1]
NameError: name 'tetx' is not defined
text[-1]
'd'
text[-2]
'l'
text
'Hello World'
text[0:4]
'Hell'
text[5:10]
' Worl'
text[5:]
' World'
text[:6]
'Hello '
text[:]
'Hello World'
text[5:]
' World'
text[:5]
'Hello'
text[-1]
'd'
text[1:7]
'ello W'
text[7:1]
''
#text[upperbound : lowerbound]
text[0:10]
'Hello Worl'
text[0:10:2]
'HloWr'
text
'Hello World'
text[7:1:-1]
'oW oll'
text[10:1:-1]
'dlroW oll'
text[-1:-10]
''
text[-10:-1]
'ello Worl'
text[-1:-10:-1]
'dlroW oll'
text[::-1]
'dlroW olleH'
dir(text)
['__add__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getnewargs__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mod__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__rmod__', '__rmul__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 'capitalize', 'casefold', 'center', 'count', 'encode', 'endswith', 'expandtabs', 'find', 'format', 'format_map', 'index', 'isalnum', 'isalpha', 'isascii', 'isdecimal', 'isdigit', 'isidentifier', 'islower', 'isnumeric', 'isprintable', 'isspace', 'istitle', 'isupper', 'join', 'ljust', 'lower', 'lstrip', 'maketrans', 'partition', 'removeprefix', 'removesuffix', 'replace', 'rfind', 'rindex', 'rjust', 'rpartition', 'rsplit', 'rstrip', 'split', 'splitlines', 'startswith', 'strip', 'swapcase', 'title', 'translate', 'upper', 'zfill']
text.lower()
'hello world'
text.upper()
'HELLO WORLD'
text.title()
'Hello World'
text.capitalize()
'Hello world'
text.swapcase()
'hELLO wORLD'
text = "Hello how are you...? I am fine thankyou"
len(text)
40
text.split()
['Hello', 'how', 'are', 'you...?', 'I', 'am', 'fine', 'thankyou']
text.split("?")
['Hello how are you...', ' I am fine thankyou']
len(text.split())
8
len(text.split("?"))
2
text.count('o')
4
text.count('e')
3
text.index('o')
4
text.index('o',0)
4
text.index('o',5)
7
text.index('o',8)
15
text.index('o',16)
38
text.index('o',39)
Traceback (most recent call last):
  File "<pyshell#50>", line 1, in <module>
    text.index('o',39)
ValueError: substring not found
text.index('z')
Traceback (most recent call last):
  File "<pyshell#51>", line 1, in <module>
    text.index('z')
ValueError: substring not found
text.find('z')
-1
text.find('o')
4
text.find('o',5)
7
text.find('o',8)
15
text.find('o',39)
-1
count = text.count('o')
index = 0
for i in range(count):
    index = text.find('o', index)
    print(index)
    index += 1

    
4
7
15
38
