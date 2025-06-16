# Variable scope   = Where a variable is visible and accessible
# Scope Resolution = (LEGB) Local -> Enclosed -> Global -> Built-in

# Local:
'''
def func1():
    x = 1
    print(x)

def func2():
    x = 2
    print(x)

func1()
func2()

'''

# Enclosed:
'''
def func1():
    x = 1
    def func2():
        x = 2
        print(x)
    func2()
func1()  

'''

# Global:
'''
def func1():
    # x = 1
    print(x)

def func2():
    # x = 2
    print(x)

x = 3
func1()
func2()

'''

# Built-in
'''
import math as m

def func1():
    print(m.e)

func1()

'''
