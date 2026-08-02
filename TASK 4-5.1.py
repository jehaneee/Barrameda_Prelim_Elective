Python 3.13.1 (tags/v3.13.1:0671451, Dec  3 2024, 19:06:28) [MSC v.1942 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> print"Hello WOrld"
SyntaxError: Missing parentheses in call to 'print'. Did you mean print(...)?
>>> print("Hello WOrld");
Hello WOrld
>>> Print("Hello World")
Traceback (most recent call last):
  File "<pyshell#2>", line 1, in <module>
    Print("Hello World")
NameError: name 'Print' is not defined. Did you mean: 'print'?
>>> print("Hel World")
Hel World
>>> prin(Hello World
...      
SyntaxError: '(' was never closed
