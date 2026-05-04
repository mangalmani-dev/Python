

while(True):
    userInput = input("Enter a number between 1 and 10: ")
    if userInput.isdigit():
        userInput = int(userInput)
        if 1 <= userInput <= 10:
            print("Thank you for entering a valid number!")
            break
        else:
            print("The number must be between 1 and 10. Please try again.")
    else:
        print("That's not a valid number. Please enter a number between 1 and 10.")