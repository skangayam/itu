# File: calculate87501.py
# This program calculates the square root of the given numbers

import  math
def main():
    print("This program prints the square root of the numbers")
    x = eval(input("Enter value of start : "))
    y = eval(input("Enter value of end : "))
    print ("start = %d , end = %d"%(x,y))

    print ("Number \t Square root")
    for i in range(x,y+1):
        sqrt = math.sqrt(i)
        print ("%d \t %f"%(i,sqrt))

main()