q1 = print("1.bank account(money)")
q2 = print("2.send money on account")
q3 = print("3.add money on account")
q4 = print("4.leave")

a1 = int(input("please choose 1 or 2 or 3 or 4:"))

if a1 == 1:
    print("money:5000 gel")
elif a1 == 2:
 q5 = (input("enter a username:"))
 q6 = int(input("please enter a number:"))
 if q6 > 5000:
     print("not enough money")
 else:
     print(q6, "sent to",q5 )
 if a1 == 3:
     question7 = int(input("please enter a number:"))
if question7 > 10001:
    print("10000 money is max adding to account")
if question7 < 10000:
    print(question7 , "gel was added to your bank account")
if a1 == 4:
    print("u left")
else:
    print("invalid")
    