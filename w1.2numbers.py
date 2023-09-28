'''
# Write a program that asks the user for a number n and prints the sum of the numbers 1 to n
n = int(input("Enter a positive number n: "))
# create a variable to store the sum
sum_of_numbers = 0
# calculate the sumn of numbers from 1 to n
for i in range(1,n + 1):
    sum_of_numbers += i
# print the sum
print("the sum of numbers from 1 to", n,"is:", sum_of_numbers)
'''
'''Modify the previous program such that only multiples of three or five are 
 considered in the sum, e.g. 3, 5, 6, 9, 10, 12, 15 for n=17'''
n = int(input("Enter a positive number n: "))
sum_of_multiples = 0
# calculate the sum of multiples of 3 or 5 from 1 to n
for i in range(1,n + 1):
    if i % 3 == 0 or i % 5 == 0:
        sum_of_multiples += i
    else:
        continue #skip numbers that are not multiples of 3 or 5

# print a note and the sum
print("Please be advised: \nonly multiples of 3 or 5 are being considered in this sum")
print("The sum of multiples of 3 or 5 from 1 to", n,"is:", sum_of_multiples)