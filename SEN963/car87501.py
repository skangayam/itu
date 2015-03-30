# Name: Shashi Kanth Kangayam
# Student ID: 87501

# Mid-term exam SEN963-1

def calculateCommission(carSalePrice, isNew, isLuxury, tenure):
    adjustment = 0
    if tenure > 3 and tenure < 9:
        adjustment = 150
    elif tenure > 8 and tenure < 17:
        adjustment = 280
    elif tenure > 16:
        adjustment = 350

    commission = 0

    if isNew:
        if isLuxury:
            commission = (carSalePrice * (3.4 / 100)) + adjustment
        else:
            commission = (carSalePrice * (2.8 / 100)) + adjustment
    else:
        if isLuxury:
            commission = (carSalePrice * (3.5 / 100)) + adjustment
        else:
            commission = (carSalePrice * (3.2 / 100)) + adjustment

    return round(commission, 2)


def main():
    print('This program computes car sale commission for Acme Auto')
    carSalePrice = eval(input("Enter car sale price: "))
    if carSalePrice < 0 or carSalePrice > 300000.00:
        print("Invalid car price. Car price must be greater than or equal to $0 and cannot exceed $300000.00")
        return
    carType = input("Enter ‘N’ for New or ‘U’ for Used car: ")
    if carType not in ['N', 'U']:
        print("Invalid code for car type. It must be 'N' or 'U'")
        return
    carClass = input("Enter ‘E’ for Economy or ‘L’ for Luxury car: ")
    if carClass not in ['L', 'E']:
        print("Invalid code for car class. It must be 'E' or 'L'")
        return
    tenure = eval(input("Enter salesperson years of employment: "))
    if tenure < 0:
        print("Invalid input. Employment years needs to be greater than or equal to 0")
        return

    isNew = False
    if (carType == 'N'):
        isNew = True
    isLuxury = False
    if (carClass == 'L'):
        isLuxury = True
    commission = calculateCommission(carSalePrice, isNew, isLuxury, int(tenure))
    print("The sale commission is : $%s" % (commission))


main()