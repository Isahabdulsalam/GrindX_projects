# Write a program to check if a number is even or odd.

def odd_or_even(number):
    if number % 2 == 0:
        print(f'{number} is even')
    else:
        print(f'{number} is odd')


num = int(input("Enter number: "))
odd_or_even(num)
