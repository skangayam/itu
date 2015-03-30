# Name: Shashi Kanth Kangayam
# Student ID: 87501

# Mid-term exam SEN963-1

# Problem:
# asks user to enter a string and find the numbers of lower case letters, upper case letters, spaces,
# and digits in the string.

# Example:
# Enter a an input string: There are 196 countries in the world. Asia has 27 countries.
# The string contains 5 digits, 2 upper-case letters, 41 lower-case letters, and 10 space characters

def main():
    print('This program computes the number of upper-case, lower-case, digits and spaces in a phrase')
    x = input("Enter a phrase: ")
    y = list(x)
    (upper,lower,digit,space) = (0,0,0,x.count(' '))
    for i in y:
        if i.isupper():
            upper += 1
        elif i.islower():
            lower += 1
        elif i.isdigit():
            digit += 1
    print("The string contains %d digits, %d upper-case letters, %d lower-case letters and %s space characters"
          %(digit,upper,lower,space))
main()
