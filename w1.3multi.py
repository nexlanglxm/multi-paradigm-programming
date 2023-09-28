'''• Write a program that asks the user for a number n and gives them the possibility to choose between
computing the sum and computing the product of 1,. . . ,n.'''
# i will use functions to separate out the code and help it look more organized in case i need it again 
def main():
    try:
        n = int(input("Enter a number n: "))
        choice = input("Choose 'sum' or 'product':").lower()

        result = 0

        if choice == 'sum':



    except ValueError:
        print("This input is invalid. Please enter a valid number")