print ("Hello World")

print("one is equal to 2:", int(1==2))
print("one is equal to 1:", int(1==1))

print(f"a: {20 > 9}")
print(f"b: {5 == 6}")
print(f"c: {1 == 0}")
print(f"d: {1 == 1}")

x = 4

print(f"x<5 and x<10: {x<5 and x<10}")
print(f"x<5 and x<-4: {x<5 and x<-4}")

print(f"x<5 and x<10: {x<5 or x<10}")
print(f"x<5 and x<10: {x<5 or x<10}")

print(f"is 'matt'=='matthew'? {'matt' =='matthew'}")
                               
my_name = "Ian"
print("assignment: ",my_name)
print("equality: ",my_name == "Ian")

print("comparison:","aa" < "b")
print("comparison:", 5< 6)

bank_balance = 50 
print(f"bank balance before = {bank_balance}")

message_user = "no more money!"
if bank_balance < 100:
    money = 1000
    bank_balance += money 
    message_user = "you got paid!"
print(f"bank balance after = {bank_balance}")

