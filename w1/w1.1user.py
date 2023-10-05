# Write a program that asks the user for their name and greets them with their name.
user_name = input("What is your name?")
# Modify the previous program such that only the users Alice and Bob are greeted with their names.
if user_name == "Alice" or user_name == "Bob":
    print("Hello, " + user_name + "! Nice to meet you!")
else:
    print("Sorry, you are not Alice or Bob. I have not received the correct programming to humour you at this time")