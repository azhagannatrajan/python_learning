# Problem 1

letter = input("Enter your alphabets here ")

match letter :
    case "a" | "e" | "i" | "o" | "u" :
        print("It is a vowel")
    case _ :
        print("It is a consonant")

# problem 2

age = int(input("Enter your age here : "))
if age>0 and age <=5 :
    print("Free")
elif age>5 and age<=12 :
    print("10")
elif age>12 and age<=64 :
    print("20")
elif age>65 :
    print("15")

# problem 3

monthNumber = int(input("Enter your month (1-12)"))
match monthNumber :
    case 1:
        print("January")
    case 2 :
        print("February")
    case 3 :
        print("March")
    case 4 :
        print("April")
    case 5 :
        print("May")
    case 6 :
        print("June")
    case 7:
        print("July")
    case 8 :
        print("August")
    case 9 :
        print("September")
    case 10 :
        print("October")
    case 11 :
        print("November")
    case 12 :
        print("December")
    case _ :
        print("Invalid month number")


        