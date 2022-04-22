Python 3.8.10 (tags/v3.8.10:3d8993a, May  3 2021, 11:48:03) [MSC v.1928 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> _a=1
>>> _a2=2
>>> _1a=1
>>> 1a=0
SyntaxError: invalid syntax
>>> y='str'
>>> type(y)
<class 'str'>
>>> y=1
>>> type(y)
<class 'int'>
>>> t=1.5
>>> print(type(t))
<class 'float'>
>>> t=1.555555555555555555555
>>> print(type(t))
<class 'float'>
>>> str='hi Inu\nGood morning'
>>> str
'hi Inu\nGood morning'
>>> print(str)
hi Inu
Good morning
>>> s="jj's'
SyntaxError: EOL while scanning string literal
>>> s="jj's"
>>> print(s)
jj's
>>> str1='hi Inu\tGood morning'
>>> print(str1)
hi Inu	Good morning
>>> str1=r'hi Inu\tGood morning'
>>> print(str1)
hi Inu\tGood morning
>>> str1=r'hi Inu\tGood morning'#raw string....
>>> mystr=2*'ab'+'cd'
>>> mystr
'ababcd'
>>> mystr=2*('ab'+'cd')
>>> mystr
'abcdabcd'
>>> mystr=2*('ab'+"cd")
>>> 'abcdabcd'
'abcdabcd'
>>> print("Laya" "Sunil")
LayaSunil
>>> name='LayaSunil'
>>> name[0]
'L'
>>> name[-1]
'l'
>>> name[-2]
'i'
>>> name[-3]
'n'
>>> name[5]
'u'
>>> name[0]+name[4]
'LS'
>>> name='LS'
>>> s='LayaSunil'
>>> s='Laya Sunil'
>>> s[0:4]
'Laya'
>>> s[0:5]
'Laya '
>>> s[-1:]
'l'
>>> s[-1:-3]
''
>>> s[-3:-1]
'ni'
>>> s[-3:0]
''
>>> s[-3:]
'nil'
>>> s='LayaSunil'
>>> s[5]='l'
Traceback (most recent call last):
  File "<pyshell#48>", line 1, in <module>
    s[5]='l'
TypeError: 'str' object does not support item assignment
>>> 'Laya'=='laya'
False
>>> 'Laya'=='Laya'
True
>>> len(s)
9
>>> s='123'
>>> len(s)
3
>>> s="Hello, how are you"
>>> s.
SyntaxError: invalid syntax
>>> 
>>> 
>>> 
>>> s.find("how")
7
>>> s.replace("Hello","Hi")
'Hi, how are you'
>>> s.find("who")
-1
>>> s.capitalize("kaz")
Traceback (most recent call last):
  File "<pyshell#63>", line 1, in <module>
    s.capitalize("kaz")
TypeError: capitalize() takes no arguments (1 given)
>>> s.capitalize()
'Hello, how are you'
>>> s.count(" ")
3
>>> s.count("h")
1
>>> s.count("how")
1
>>> s= la la la la la"
SyntaxError: invalid syntax
>>> s= "la la la la la"
>>> s.len()
Traceback (most recent call last):
  File "<pyshell#71>", line 1, in <module>
    s.len()
AttributeError: 'str' object has no attribute 'len'
>>> len(s)
14
>>> s.count("la")
5
>>> s.count("lii")
0
>>> s.split(" ")
['la', 'la', 'la', 'la', 'la']
>>> s.split(" ")[0]
'la'
>>> s.split(" ")[4]
'la'
>>> s= "aa ba da da ea"
>>> s.split(" ")[4]
'ea'
>>> fruits = "Apple,orange,grapes"
>>> fruits.split(",")
['Apple', 'orange', 'grapes']
>>> gmail = "abc2gmail.com"
>>> gmail = "abc@gmail.com"
>>> gmail.split("@")
['abc', 'gmail.com']
>>> gm = "www.gmail.com"
>>> gm.split(".")
['www', 'gmail', 'com']
>>> sent = "its a great day"
>>> s.upper()
'AA BA DA DA EA'
>>> sent.upper()
'ITS A GREAT DAY'
>>> sent.lower()
'its a great day'
>>> sent.title()
'Its A Great Day'
>>> sent.capitalize()
'Its a great day'
>>> sent.swapcase()
'ITS A GREAT DAY'
>>> sent.title()
'Its A Great Day'
>>> sent.swapcase()
'ITS A GREAT DAY'
>>> s="aBc"
>>> s.swapcase()
'AbC'
>>> sent
'its a great day'
>>> s1="abc"
>>> s22=" abc"
>>> s1==s222
Traceback (most recent call last):
  File "<pyshell#101>", line 1, in <module>
    s1==s222
NameError: name 's222' is not defined
>>> s1==s22
False
>>> s22.strip()
'abc'
>>> s22.rstrip()
' abc'
>>> S22.lstrip()
Traceback (most recent call last):
  File "<pyshell#105>", line 1, in <module>
    S22.lstrip()
NameError: name 'S22' is not defined
>>> s22.lstrip()
'abc'
>>> " ".join(s22)
'  a b c'
>>> "#".join(s22)
' #a#b#c'
>>> "#".join(s22).strip()
'#a#b#c'
>>> "".join(reversed(s22))
'cba '
>>> s="hello world"
>>> s[::-1}
SyntaxError: closing parenthesis '}' does not match opening parenthesis '['
>>> s[::-1]
'dlrow olleh'
>>> s[::-1] #reverse short cut
'dlrow olleh'
>>> # format==>  string_name[start:stop:step]
>>> s[0:5:2]
'hlo'
>>> proverb = "A picture is worth athou