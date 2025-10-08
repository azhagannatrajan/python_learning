

# problem 1

n = int(input("enter"))
m = int(input("enter number"))
add = n+m
if add%2==0:
    print("even")
else:
    print("odd")

# problem 2

n=input("enter the value")
f=int(n[0])
m=int(n[1])
add=f+m
mul=f*m
tot=add+mul
if tot==int(n):
    print("great")
else:
    print("not ")

# problem 3

a=input("enter the number")

if a=="Residential":
    print('Residential')
    b=int(input("enter the number"))
    if 0<=b<=100:
        print(3*b)
    elif 101<=b<=200:
        print(5*b)
    elif b>200:
        print(7*b)
if a=="Commercial":
    print('Commercial')
    b=int(input("enter the number"))
    if b>=0 and b<=100:
        print(5*b)
    elif b>=101 and b<=200: 
        print(7*b)
    elif b>200:
        print(10*b)

# problem 4

a=int(input("enter the number"))
if a<=5:
    print(50)
elif a>6 and a<15:
    print(a*8)
elif a>15:
    print(a*6)


# problem 5

a=int(input("enter the number"))
b=int(input("enter the number"))
c=int(input("enter the number"))

if a==b <c or b==c <a or a==c <b:
    print("Not a valid triangle")
elif a==b==c:
    print("Equilateral")
elif a==b and b==a or a==c:
    print("Isosceles ")
else :
    print("Scalene")

# problem 6

a=int(input('ENTER THE NUMBER'))
if a%3==0 and a%5==0:
    print("FizzBuzz")
elif a%3==0:
    print("Fizz")
elif a%5==0:
    print("Buzz")
else:
    print("invalid input")

# problem 7

a=input("science,commerce,arts")
match a:
    case "science":
        b=input("medical/Engineering")
        match b:
            case "medical":
                print("you choosing medical")
            case"Engineering":
                print("you choosing Engineering")

    case "Commerce":
       c=input("CA/B com")
       match c:
           case "CA":
                print("you choosing CA")
           case"B com":
                print("you choosing B com")
           case _:
                print("invalid input")
    case "Arts":
       c=input("History/Literature")
       match c:
           case "History":
                print("you choosing History ")
           case"Literature":
                print("you choosing Literature")
           case _:
                print("invalid input")            
    case _:
        print("invalid input")

# problem 8 

a=int(input("enter the value"))
if a>=9 and a<12:
    print("Morning show")
elif a>=12 and a<4:
    print("Matinee show")   
elif a>=4 and a<7:
    print("Evening Show")  
else:
    print("night show")

# problem 9

a=float(input("enter the value"))
choice=input("start your converstaion")
match choice:
    case "m":
       print(a*1000,"m")
    case "cm":
        print(a*1000000,"cm")
    case "mm":
        print(a*10000000,"mm")   
    case "mi":
        print(a*0.621371,"mi")
    case _:
        print("invalid input")


# problem 10

a=input("select your method")    
if a=="UPI":
    print("You selected UPI payment")
elif a=="Card":
    print("You selected Debit/Credit Card payment")  
elif a=="NetBanking":
    print("You selected Net Banking") 
elif a== "COD":
    print("You selected Cash on Delivery") 
else:
    print("Invalid Payment Mode")
