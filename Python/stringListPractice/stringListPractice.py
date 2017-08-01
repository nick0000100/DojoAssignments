Python 2.7.13 (v2.7.13:a06454b1afa1, Dec 17 2016, 20:42:59) [MSC v.1500 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> words = "It's thanksgiving day. It's my birthday,too!"
>>> print words
It's thanksgiving day. It's my birthday,too!
>>> words.find("day")
18
>>> words.replace("day", "month")
"It's thanksgiving month. It's my birthmonth,too!"
>>> x = [2,54,-2,7,12,98]
>>> print x
[2, 54, -2, 7, 12, 98]
>>> min(x)
-2
>>> max(x)
98
>>> x = ["hello",2,54,-2,7,12,98,"world"]
>>> print x
['hello', 2, 54, -2, 7, 12, 98, 'world']
>>> print x[0]
hello
>>> printx[x.length-1]

Traceback (most recent call last):
  File "<pyshell#11>", line 1, in <module>
    printx[x.length-1]
NameError: name 'printx' is not defined
>>> print x[x.length-1]

Traceback (most recent call last):
  File "<pyshell#12>", line 1, in <module>
    print x[x.length-1]
AttributeError: 'list' object has no attribute 'length'
>>> print x[7]
world
>>> x = [19,2,54,-2,7,12,98,32,10,-3,6]
>>> sort(x)

Traceback (most recent call last):
  File "<pyshell#15>", line 1, in <module>
    sort(x)
NameError: name 'sort' is not defined
>>> x.sort()
>>> print x
[-3, -2, 2, 6, 7, 10, 12, 19, 32, 54, 98]
>>> x.len() = x.len() / 2
SyntaxError: can't assign to function call
>>> 
