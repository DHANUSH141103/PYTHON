# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
lname1=name1.lower()
lname2=name2.lower()
t=lname1.count("t")+lname2.count("t")
r=lname1.count("r")+lname2.count("r")
u=lname1.count("u")+lname2.count("u")
e=lname1.count("e")+lname2.count("e")
total_of_true=t+r+u+e
l=lname1.count("l")+lname2.count("l")
o=lname1.count("o")+lname2.count("o")
v=lname1.count("v")+lname2.count("v")
total_of_love=l+o+v+e
total=int(str(total_of_true)+str(total_of_love))
if total<10 or total>90:
    print(f"Your score is {total}, you go together like coke and mentos.")
elif total>=40 and total<=50:
    print(f"Your score is {total}, you are alright together.")
else:
    print(f"Your score is {total}.")

