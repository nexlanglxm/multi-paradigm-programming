# Write a program that prints a multiplication table for numbers up to 12
for i in range(1,13):
    for j in range(1,13):
        print(f"{i * j:4}", end="") 
    print()
    #the '4' specifies that each value should occupy a minimum of 4 characters, which works well for the first 999 numbers :)