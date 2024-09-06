import manager
import database

# Initialize the database (run once)
database.init_db()

def menu():
    print("Welcome to the Password Manager")
    print("1. Add Password")
    print("2. Retrieve Password")
    print("3. Update Password")
    print("4. Delete Password")
    print("5. Exit")
    
    choice = input("Choose an option: ")
    
    if choice == '1':
        service = input("Enter the service name: ")
        password = input("Enter the password: ")
        manager.add_password(service, password)
    elif choice == '2':
        service = input("Enter the service name: ")
        manager.retrieve_password(service)
    elif choice == '3':
        service = input("Enter the service name: ")
        new_password = input("Enter the new password: ")
        manager.update_password(service, new_password)
    elif choice == '4':
        service = input("Enter the service name: ")
        manager.delete_password(service)
    elif choice == '5':
        exit()
    else:
        print("Invalid choice!")

if __name__ == "__main__":
    while True:
        menu()
