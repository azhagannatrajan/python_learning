income = int(input("Enter your amount = "))
if income>0 and income <= 250000 :
    print("No tax")
elif income > 250000 and income <= 500000 :
    tax1 = (income*5/100)
    print(tax1)
elif income>500000 and income<=1000000:
    tax2 = (income*20/100)
    print(tax2)
elif income > 1000000 :
    tax3 = (income*30/100)
    print(tax3)
else : 
    print("Invalid amount")