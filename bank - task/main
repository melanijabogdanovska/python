from bank import Bank
from errors import *

class Menu:
    def print_menu(self):
        print("1. Register a new user")
        print("2. Create an account for an existing user")
        print("3. List all users")
        print("4. List all accounts for an existing user")
        print("5. Deposit money to a user account")
        print("6. Withdraw money from a user account")
        print("7. Exit")

    def run(self):
        bank = Bank()

        # infinite menu loop
        while True:  
            self.print_menu()
            choice = input("Choose an item from the menu: \n> ")

            try:
                if choice == "1":
                    names = input("Enter the user's names (alpha-only): ")
                    fname, lname = names.split(" ")
                    if len(names) < 4 or not fname.isalpha() or not lname.isalpha():
                        raise InvalidUserData("Invalid names")

                    egn = input("Enter the user's EGN number (len 10, digits-only): ")
                    if len(egn) != 10 or not egn.isdigit():
                        raise InvalidUserData("Invalid EGN number")

                    bank.add_user(names, egn)
                elif choice == "2":
                    egn = input("Enter the user's EGN number (len 10, digits-only): ")
                    n=len(egn)
                    if n != 10 or not egn.isdigit():
                        raise InvalidAccountData("You have entered invalid egn")
                    currency = input(" Enter currency: ")
                    type = input( "Enter a type:")
                    bank.add_account(egn, currency, type)
                elif choice == "3":
                    for u in bank.users:
                        print(u.get_print())
                elif choice == "4":
                    user_egn = input("Enter the user's EGN number (len 10, digits-only): ")
                    n=len(user_egn)
                    if n != 10 or not user_egn.isdigit():
                        raise InvalidAccountData("You have entered invalid egn")
                    for user in bank.users:
                        if user.egn == user_egn:
                            for account in user.accounts:
                                print(account)
                        break      

                elif choice == "5":
                    user_egn = input("Enter the user's EGN number (len 10, digits-only): ")
                    n=len(user_egn)
                    if n != 10 or not user_egn.isdigit():
                        raise InvalidAccountData("You have entered invalid egn")
                elif choice == "6":
                    user_egn = input("Enter the user's EGN number (len 10, digits-only): ")
                    n=len(user_egn)
                    if n != 10 or not user_egn.isdigit():
                        raise InvalidAccountData("You have entered invalid egn")
                    

                elif choice == "7":
                    print("Goodbye\n")
                    break
                else:
                    raise InvalidMenuChoice("Error: Invalid choice")
            except Exception as ex:
                print(f"Error: There was an error while executing the command:\n{str(ex)}")
            
            print()

if __name__ == '__main__':
    menu = Menu()
    menu.run()
