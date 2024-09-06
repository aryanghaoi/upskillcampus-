import encryption
import database

def add_password(service_name, password):
    encrypted_password = encryption.encrypt_password(password)
    database.save_password(service_name, encrypted_password)
    print(f"Password for {service_name} saved successfully!")

def retrieve_password(service_name):
    encrypted_password = database.get_password(service_name)
    if encrypted_password:
        decrypted_password = encryption.decrypt_password(encrypted_password)
        print(f"Password for {service_name}: {decrypted_password}")
    else:
        print(f"No password found for {service_name}.")

def update_password(service_name, new_password):
    encrypted_password = encryption.encrypt_password(new_password)
    database.update_password(service_name, encrypted_password)
    print(f"Password for {service_name} updated successfully!")

def delete_password(service_name):
    database.delete_password(service_name)
    print(f"Password for {service_name} deleted.")
