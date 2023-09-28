'''• Write a program that asks the user for a number n and gives them the possibility to choose between
computing the sum and computing the product of 1,. . . ,n.'''
# i will use functions to separate out the code and help it look more organized in case i need it again 
def compute_sum(n):
    return sum(range(1,n + 1))

def compute_product(n):
    result = 1
    for i in range(1,n + 1):
        result *= i
    return result

def main():
    try:
        n = int(input("Enter a number n: "))
        choice = input("Choose 'sum' or 'product':").lower()

        if choice == 'sum':
            result = compute_sum(n)
            print(f"The sum of numbers from 1 to {n} is {result}")

        elif choice == 'product':
            result = compute_product(n)
            print(f"The product of numbers from 1 to {n} is {result}")
        else:
            print("Invalid choice. Please choose 'sum' or 'product'.")

    except ValueError:
        print("Invalid input. Please enter a valid number.")
    
if __name__ == "__main__":
    main()