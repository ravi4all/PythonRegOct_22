Python 3.10.4 (tags/v3.10.4:9d38120, Mar 23 2022, 23:13:41) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
text = "Hello how are you...??"
text.lower()
'hello how are you...??'
text.upper()
'HELLO HOW ARE YOU...??'
text.title()
'Hello How Are You...??'
text.capitalize()
'Hello how are you...??'
text.swapcase()
'hELLO HOW ARE YOU...??'
text.count('a')
1
text.count('o')
3
text.find('o')
4
text.find('o', 5)
7
text.startswith("o")
False
text.startswith("H")
True
text.endswith("o")
False
text.endswith("o.")
False
text.endswith(".")
False
text.endswith("?")
True
text.isalnum()
False
text.isalpha()
False
text.isascii()
True
text.islower()
False
text = "   Hello World..."
text.removeprefix()
Traceback (most recent call last):
  File "<pyshell#21>", line 1, in <module>
    text.removeprefix()
TypeError: str.removeprefix() takes exactly one argument (0 given)
text.removeprefix(" ")
'  Hello World...'
text.removesuffix(".")
'   Hello World..'
text.strip()
'Hello World...'
text.rstrip(".")
'   Hello World'
text.lstrip(" ")
'Hello World...'
text
'   Hello World...'
text.find('o')
7
text.rfind('o')
10
