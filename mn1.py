1.#calculator
import math 
def sum():
    a=int(input("enter value of a:"))
    b=int(input("enter value of b:"))
    sum =a+b
    return sum
def sub():
    a=int(input("enter value of a:"))
    b=int(input("enter value of b:"))
    sub =a-b
    return sub
def mul():
    a=int(input("enter value of a:"))
    b=int(input("enter value of b:"))
    mul =a*b
    return mul
def div():
    a=int(input("enter value of a:"))
    b=int(input("enter value of b:"))
    div =a/b
    return div
def sqrt():
    a=int(input("enter value of a:"))
    sqrt =math.sqrt(a)
    return sqrt
def pow():
    a=int(input("enter value of a:"))
    b=int(input("enter value of b:"))
    pow =a**b
    return pow
def log():
    a=int(input("enter value of a:"))
    log =math.log(a)
    return log
def sin():
    a=int(input("enter the value of a:"))
    sin =math.sin(a)
    return sin
def cos():
    a=int(input("enter the value a:"))
    cos =math.cos(a)
    return cos
def tan():
    a=int(input("enter the value a:"))
    tan =math.tan(a)
    return tan
def exp():
    a=int(input("enter the value a:"))
    
    exp =math.exp(a)
    return exp
def fact():
    a=int(input("enter the value a:"))
    fact =math.factorial(a)
    return fact
def mod():
    a=int(input("enter the value a:"))
    b=int(input("enter the value b:"))
    mod =a%b
    return mod
def sqr():
    a=int(input("enter the value a:"))
    sqr =a**2
    return sqr
def cube():
    a=int(input("enter the value a:"))
    cube =a**3
    return cube

    
while True:
    print('''
          1-Addition
          2-Subtract
          3-Division
          4-Multiply
          5-Square root
          6-Power
          7-Logarithm
          8-sin(0)
          9-cos(0)
          10-tan(0)
          11-Exp
          12-Factorial
          13-Remaider
          14-Square of no.
          15-Cube of no.
          16-Exit''')
    choice=int(input("enter your choice:"))
    if choice==1:
       print(sum())
    elif choice==2:
       print(sub())
    elif choice==3:
        print(div())
    elif choice==4:
        print(mul())
    elif choice==5:
        print(sqrt())
    elif choice==6:
        print(pow())
    elif choice==7:
        print(log())
    elif choice==8:
        print(sin())
    elif choice==9:
        print(cos())
    elif choice==10:
        print(tan())
    elif choice==11:
        print(exp())
    elif choice==12:
        print(fact())
    elif choice==13:
        print(mod())
    elif choice==14:
        print(sqr())
    elif choice==15:
        print(cube())
    elif choice==16:
        break
    else:
        print("invalid choice")

