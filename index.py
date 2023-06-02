def loop():
    word = input("\n" + "\033[1;34m" +
                 "Type a word: " + "\033[1;32m" + "\033[3;37m")

    palindrome = word[::-1]

    if (palindrome.lower() == word.lower()):
        print("\n" + "\033[1;32m" + "The word " + "\033[3;37m" +
              word + "\033[0;32m" + "\033[1;32m" + " is a palindrome!!")
    else:
        print("\n" + "\033[1;31m" + "The word " + "\033[3;37m" +
              word + "\033[0;31m" + "\033[1;31m" + " is NOT a palindrome!!")


counter = True

while counter == True:
    loop()
    choice = input(
        "\033[3;37m" + '\n0 = No\n1 = Yes\ndo you want to continue? ')
    if choice == "0":
        counter = False
