#main function that prints the menu and asks the user for input
def main():
    while input != 3:
        print("Menu")
        print("-" * 13)
        print("1. Encode", "2. Decode", "3. Quit", sep="\n")
        print("\n")
        option = int(input("Please enter an option: "))
        #enocdes the inputted password, by adding 3 to each digit
        if option == 1:
            password = input("Please enter your password to encode:")
            print("Your password has been encoded and stored!")
            print("\n")
            newpassword = ""
            for digit in password:
                newdigit = int(digit)+3
                newpassword = newpassword + str(newdigit)
        #where the decode function needed to be added
        elif option == 2:
            pass
        elif option == 3:
            break
if __name__ == "__main__":
    main()



