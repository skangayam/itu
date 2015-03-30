# File: swap_numbers.py
# A simple program illustrating swapping the numbers

def main():
    print("This program illustrates swapping the numbers")
    x = eval(input("Enter value of x : "))
    y = eval(input("Enter value of y : "))
    print ("x = %d , y = %d"%(x,y))

    print("Swapping the values of x and y")
    x , y = y , x
    print ("x = %d , y = %d"%(x,y))

main()
