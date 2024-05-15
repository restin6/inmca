'''
def add (x,y):
    print(x+y)

def sub(x,y):
    print(x-y)

def mul(x,y):
    print(x*y)

def div(x,y):
    print(x/y)

print("Menu driven Calculator")
x=int(input("Enter 1st Number: "))
y=int(input("Enter 2nd Number: "))
print("1- Addition\n2- Substraction\n3- Multiplication\n4- Division")
p=int(input("Enter Option: "))
if p==1:
        add(x,y)
elif p==2:
        sub(x,y)
elif p==3:
        mul(x,y)
elif p==4:
        div(x,y)
else:
        print("Invalid Option")
'''
def ra (x,y):
    print(x, "and ",y)

def ka(x,y):
    print(x, "and ",y)

def da(x,y=8):
    print(x, "and ",y)

def vla(*x):
    print(x, "and ",y)

print("Function Demonstrate")
x=int(input("Enter 1st Number: "))
y=int(input("Enter 2nd Number: "))
print("1- Required Argument")
ra(x,y)
print("2-Keyword Argument")
ka(x,5)
print("3-Default Argument")
da(x,y)
da(x)
print("4-Variable Length Argument")
vla(x,y)

