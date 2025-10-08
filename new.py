# def get_animal_sound (animal) :

#     if animal == "dog" :
#         print("Woof!")
#     elif animal == "cat" :
#         print("Meow!")
#     elif animal == "cow" :
#         print("Moo!")
    
# get_animal_sound("dog")

# month = int(input("enter your month"))
# match month  :
#         case 12 | 1 | 2 :
#                 print("It is Winter")
#         case 3 | 4 | 5 :
#                 print("It is Summer")
#         case 6 | 7 | 8 | 9  :
#                 print("It is Monsoon")
#         case 10 | 11 :
#                 print("It is Autumn")
#         case _ :
#                 print("Invalid Input")


X = int(input("enter your mark"))
match X :
    case _ if X <= 100 and X >= 80 :
        print("A")
    case _ if X>= 60 and X <= 79 :
        print("B")
    case _ if X <=50 and X <=59 :
        print("C")