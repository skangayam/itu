# File: leapyear87501.py
# This program determines whether the entered year is a leap year or not
# Name: Shashi Kanth Kangayam
# StudentID: 87501

def leapyr(n):
    if n % 400 == 0:
        return True
    if n % 100 == 0:
        return False
    if n % 4 == 0:
        return True
    else:
        return False

def main():
    print("This program determines whether the entered year is a leap year or not")
    year = eval(input("Enter a year: "))
    if leapyr(year):
        print("This is a leap year")
    else:
        print("This is not a leap year")

main()