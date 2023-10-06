from cardHolder import CardHolder


def print_menu():
    ### Print options to the user
    print("Please choose from one of the following options...")
    print("1. Deposit")
    print("2. Withdraw")
    print("3. Show Balance")
    print("4. Exit")


def deposit(cardHolder):
    try:
        deposit = float(input("How much $$ would you like to deposit: "))
        cardHolder.set_balance(cardHolder.get_balance() + deposit)
        print(f"Thank you for your $$. Your new balance is {cardHolder.get_balance()}")
    except:
        print("Invalid input")


def withdraw(cardHolder):
    try:
        deposit = float(input("How much $$ would you like to withdraw"))
        ### check if user has enough money
        if cardHolder.get_balance() < withdraw:
            print("Insufficient balance :(")
        else:
            cardHolder.set_balance(cardHolder.get_balance() - withdraw)
            print("You'r good to go! Thank you :)")
    except:
        print("Invalid input")


def check_balance(cardHolder):
    print(f"Your current balance is: {cardHolder.get_balance()}")


if __name__ == "__main__":
    current_user = CardHolder("", "", "", "", "")

    ### Create a repo of cardHolders
    list_of_cardHolders = []
    list_of_cardHolders.append(
        CardHolder("4563846583648739", 1234, "John", "Griffith", 150.31)
    )
    list_of_cardHolders.append(
        CardHolder("4563846583648739", 4353, "Ashley", "Jones", 550.31)
    )
    list_of_cardHolders.append(
        CardHolder("4563846583648739", 7666, "Frida", "Dickerson", 450.31)
    )
    list_of_cardHolders.append(
        CardHolder("4563846583648739", 3546, "Muneeb", "Harding", 250.31)
    )
    list_of_cardHolders.append(
        CardHolder("4563846583648739", 3435, "Dawn", "smith", 950.31)
    )

    ### Prompt user for debit card number
    debitCardNum = ""
    while True:
        try:
            debitCardNum = input("Please insert your debit card: ")
            ### Check against repo
            debitMatch = [
                holder
                for holder in list_of_cardHolders
                if holder.cardNum == debitCardNum
            ]
            if len(debitMatch) > 0:
                current_user = debitMatch[0]
                break
            else:
                print("Card number not recognized, Please try again")

        except:
            print("Card number not recognized, Please try again")


### Prompt fo PIN
while True:
    try:
        userPin = int(input("Please enter your pin: ").strip())
        if current_user.get_pin() == userPin:
            break
        else:
            print("Invalid Pin. Please try again.")
    except:
        print("Invalid Pin. Please try again.")


### Pint Option
print(f"Welcome {current_user.get_firstname()} :) ")
option = 0
while True:
    print_menu()
    try:
        option = int(input())
    except:
        print("Invalid input. Please try again.")

    if option == 1:
        deposit(current_user)
    elif option == 2:
        withdraw(current_user)
    elif option == 3:
        check_balance(current_user)
    else:
        option = 0
    print("Thank you. Have a nice day :) ")
