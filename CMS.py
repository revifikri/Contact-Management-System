import re
from os import system

class contact_book: 
    # Create class that can return name, phone number and email
    def __init__(self, name=None, phone_num=None, email=None) -> None: 
        # None: we don't need to input some value for every command
        self.name = name
        self.phone_num = phone_num
        self.email = email
        
    def write_file(self): 
        # Create or append some input to the file "contact list"
        text = f'''Name            : {self.name.capitalize()}\
        \nPhone number    : {self.phone_num}\nEmail           : {self.email}\n\n'''
        with open("contact list.txt", "a") as file:
            file.write(text) 
    
    def read_file(): 
        # Display a list of all contacts
        with open("contact list.txt", "r") as file:
            print("List of All Contacts\n")
            print(file.read()) 
    
    def search_file(User): 
        # Search the specific contact using regular expression
        text = ""
        with open("contact list.txt", "r") as file:
            for word in file.read():
                text += word
                
        pattern = "Name\s+: " + User.capitalize() + "\s+Phone number\s+: \d+\sEmail\s+: \S+\s+"
        matches = re.search(pattern, text)
        if matches:
            print(matches.group()) 
        else:
            print('Contact not found\n') 
          
    def delete_file(User): 
        # Search the specific contact 
        text = ""
        with open("contact list.txt", "r") as file:
            for word in file.read():
                text += word
                
        pattern = "Name\s+: " + User.capitalize() + "\s+Phone number\s+: \d+\sEmail\s+: \S+\s+"
        matches = re.search(pattern, text)
        
        if matches:
            print(matches.group())
            choice = input("Do you want to delete this contact?(y/n) : ")
            if choice == "y":
                # If the user want to delete the contact we will replace the specific contact with ""
                new_text = text.replace(matches.group(), "")
                with open("contact list.txt", "w") as file:
                    # Rewrite the entire contact 
                    file.write(new_text)
                print("Contact has been successfully deleted")
            else: pass 
        else :
            print('Contact not found\n')
           
    def edit_file(User):
        # Search the specific contact
        text = ""
        with open("contact list.txt", "r") as file:
            for word in file.read():
                text += word
                
        pattern = "Name\s+: " + User.capitalize() + "\s+Phone number\s+: \d+\sEmail\s+: \S+\s+"
        matches = re.search(pattern, text)
        if matches:
            print(matches.group())
            choice = input("Do you want to edit this contact?(y/n) : ")
            
            if choice == "y":
                # If the user want to edit the contact we will replace the specific contact with the new one
                Name = input("\nEnter the new name : ")
                Phone_num = input("Enter the new phone number : ")
                Email = input("Enter the new email : ")
                
                new_text = text.replace(matches.group(), "Name            : " + Name.capitalize() +
                            "\nPhone number    : " + Phone_num +
                            "\nEmail           : " + Email + "\n\n")
                with open("contact list.txt", "w") as file:
                    # Rewrite the entire contact
                    file.write(new_text)
                print("Contact has been successfully edited")
            else: pass
        else: 
            print('Contact not found')
            
def run_program():
    while 1:
        # Menu 
        system('cls')
        print('Welcome to Contact Management System\n\n'+
            '1) Add New Contact\n'+
            '2) List All Contacts\n'+
            '3) Search Contact\n'+
            '4) Delete Contact\n'+
            '5) Edit Contact\n'+
            '0) Exit\n')
        choice = input("Enter your choice : ")
        
        # Create Contact
        if choice == "1":
            choice = 'y'
            while choice.lower() == "y":
                system('cls')
                Name = input("\nInput your name : ")
                Phone_num = input("Input your phone number : ")
                Email = input("Input your email : ")
                contact = contact_book(Name, Phone_num, Email)
                contact.write_file()
                choice = input("\nDo you have the next data?(y/n) : ")
            print("\nContact has been success fully created")
            system("pause")

        # Read contact
        elif choice == "2":
            system('cls')
            contact_book.read_file()
            system("pause")

        # Search from contact
        elif choice == "3":
            choice = 'y'
            while choice == 'y':
                system('cls')
                user = input("\nEnter the name : ")
                print("\nContact\n") 
                contact_book.search_file(user)
                choice = input('Do you want to search another contact? (y/n) : ')
            system("pause")

        # Delete contact
        elif choice == "4":
            choice = 'y'
            while choice == 'y':
                system('cls')
                user = input("\nEnter the name : ")
                print("\nContact\n")
                contact_book.delete_file(user)
                choice = input('\nDo you want to delete another contact? (y/n) : ')
            system("pause")
        
        # Edit contact
        elif choice == '5':
            choice = 'y'
            while choice == 'y':
                system('cls')
                user = input("\nEnter the name : ")
                print("\nContact\n")
                contact_book.edit_file(user)
                choice = input('\nDo you want to edit another contact? (y/n) : ')
            system("pause")
            
        # Quit from program
        elif choice == "0":
            system('cls')
            print("\t\t\tThank you for using CMS")
            break 
        else:
            pass
        
run_program()