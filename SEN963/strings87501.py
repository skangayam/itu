# File: strings87501.py
# Program to manipulate strings

def main():
    phrase = input("Enter a phrase: ")
    print("Entered phrase is: %s"%phrase)
    print("---------")

    print("Printing the phrase as a title")
    print(phrase.title())

    print("---------")

    print("Replacing the spaces in the phrase with a hyphen")
    print(phrase.replace(' ','-'))

    print("---------")

    print("Splitting the string into a list with the space as a delimiter")
    list = phrase.split(' ')
    print (list)

    print("---------")

    print("Printing the original phrase in the reverse order of words")
    newPhrase = '';
    for x in reversed(range(len(list))):
        newPhrase = newPhrase + ' ' +list[x];

    print(newPhrase.lstrip())

main()