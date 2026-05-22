import functions as fun #This will automatically print the output of the functions.py file

fun.sub() #This will print only output of sub() function in the module functions#

"""
When you use this module, .pyc file get generated under folder _pycache_ with module name
Why?
- Makes future imports faster
Python does not need to recompile the .py file every time

Note:
_pycache_ is generally created for your own module, now always for built in modules like math,boto3
It gets generated when the module is imported/executed
Safe to delete-python recreates it when needed
"""

