""" this module is a copy from Gerry Jenkins code in the next Video:
https://www.youtube.com/watch?v=myTz-ZDkO6Q"""
# how to get the line number and other source file contect at tuntime

import inspect
import os

# prints basic info: Line, Module and Method:
def print_info(msg = ""):
    f = inspect.currentframe()
    i = inspect.getframeinfo(f.f_back)
    if i.function == "<module>":
        print(f"line {i.lineno}, at {os.path.basename(i.filename)} --> {msg}")
    else:
        print(f"line {i.lineno} at {os.path.basename(i.filename)}, method: {i.function} --> {msg}")



def another_function():
    print_info("this is another function called another function")

if __name__ == "__main__":
    p = 3*3
    print_info("type(p):  {}".format(type(p)))    # new way of printing for debugging
    # note that it needs to print only one var, so if we need it to print multiple vars, we would have to 
    # use formatting options so all the printings are one var. I.e., use '.format()'
    another_function()
