# File: creditcard87501.py
# This program determines the validity of a credit card number
# Name: Shashi Kanth Kangayam
# StudentID: 87501

def getDigitSum(value):
    total = 0
    for digit in list(str(value)):
        total += int(digit)
    return total

def sumOfEvenPosition(value):
    total = 0
    for digit in list(value):
        total += getDigitSum(int(digit) * 2)
    return total

def sumOfOddPosition(value):
    total = 0
    for digit in list(value):
        total += int(digit)
    return total

def isValid(cardNumber):
    numberOfDigits = len(cardNumber)
    if numberOfDigits < 13 or numberOfDigits > 16:
        return False
    firstDigit = cardNumber[0:1]
    if  firstDigit == '4' or firstDigit == '5' or firstDigit == '6':
        return True
    else :
        firstTwoDigits = cardNumber[0:2]
        if firstTwoDigits == '37':
            return True
    return False

def main():
    cardNumber = str(eval(input("Enter a card number: ")))

    if isValid(cardNumber):
        cardType = None
        firstDigit = cardNumber[0:1]
        if  firstDigit == '4':
            cardType = 'Visa'
        elif firstDigit == '5':
            cardType = 'MasterCard'
        elif firstDigit == '6':
            cardType = 'Discover'
        else :
            firstTwoDigits = cardNumber[0:2]
            if firstTwoDigits == '37':
                cardType = 'American Express'
        reverseCardNumber = cardNumber[::-1]
        sumEven = sumOfEvenPosition(reverseCardNumber[1::2])
        sumOdd = sumOfOddPosition(reverseCardNumber[0::2])
        total = sumEven + sumOdd
        if total % 10 == 0:
            print ("This is a good %s card number"%cardType)
        else:
            print ("This an invalid %s card number"%cardType)
    else:
        print ("This an invalid card number")

main()