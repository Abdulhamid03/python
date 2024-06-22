#number = int(input("please enter a number: "))
#x = 5

#if x > number:
 #    print(x, "is greater than", number)
#else:
 #    print(x, "is less than", number)  


name = input("please enter your name: ")
age = input("enter your age:")

age_limit = 21

if name == "abdul" and float(age) >= age_limit:
    print("your are welcome to drink", name)

elif name == "don":
    print("you got no business being here", name)

else:
    print("you are not welcome here")