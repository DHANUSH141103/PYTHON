
print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L ")
bill=0
check=True
if size=="S":
    bill=15
    check=True
elif size=="M":
    bill=20
    check=True
elif size=="L":
    bill=25
    check=True
else:
    print("wrong input")
    check=False
if check==True:
    add_pepperoni = input("Do you want pepperoni? Y or N ")
    if add_pepperoni=="Y":
        if size=="S":
            bill+=2
            check=True
        else:
            bill+=3
            check=True
    elif add_pepperoni=="N":
        bill+=0
    else:
        print("wrong input")
        check=False
if check==True:
    extra_cheese = input("Do you want extra cheese? Y or N ")
    if extra_cheese=="Y":
        bill+=1
    elif extra_cheese=="N":
        bill+=0
    else:
        print("wrong input")
        check=False
if check==True:
    print(f"Your final bill is: ${bill}.")



    
