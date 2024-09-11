num1 = input("enter number one:")
num2 = input("enter number two:")

result = num1 > num2
road = input("choose the way left or right:")
print(type(result))
if road == "right":
    print("you went right, you saw a rock")
elif road == "left":
    print("you went left and saw nothing")
else:
    print("invalid choice!")