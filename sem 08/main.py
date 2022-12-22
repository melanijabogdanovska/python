from entities import Character
from errors import *

class Menu:
    def print_menu(self):
        print("1. Create a new character")
        print("2. Create an weapon fro already existing character")
        print("3. Create plus item for already existing character")
        print("4. print all characters")
        print("5. Delete the excisting character")
        print("6. Excit")
        
    def create_character(self, name, gender,role):
        char = Character(name,gender,role)
    def run(self):
        while True:
            self.print_menu()
            choice = input("chose an item from the menu: \n")
            try:
                if choice == "1":
                    name = input("Enter th echaracter name (alpha - numeric): ")
                    fname,lname =name.split(" ") 
                    if len(name) <4 or not fname.isalpha() or not lname.isalpha():
                        raise InvalidCharacterData (" Invalid name")
                    
                    
                    
                elif choice == "2":
                    pass
                elif choice == "3":
                    pass
                elif choice == "4":
                    pass
                elif choice == "5":
                    pass
                elif choice == "6":
                    pass
                elif choice =="7":
                    print("goodbye \n")
                    break
                else:
                    raise InvalidCommand("Error: Invalid choice")
            except Exception as ex:
                print(f"Error There was an error while executing the command: \n {str(ex)}")
                
            print()
            
if __name__ == '__main__':
    menu = Menu()
    menu.run()
                    
