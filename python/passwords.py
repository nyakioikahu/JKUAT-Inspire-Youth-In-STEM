import hashlib
import os

#File to store passwords and site names
FILENAME ="passwords.txt"

# Function to the hash the password
def hash_password(password):
    """Hash a password for storing"""
    return (hashlib.sha256(password.encode()).hexdigest())

#function to save the password
def save_password(site, password):
    """Save a password for a site"""
    hashed_password = hash_password(password)
    with open(FILENAME, "a") as file:
        file.write(f"{site}:{hashed_password}\n")
    print(f"Password for the site saved successfully")
    
# Function to get the password
def get_password(site):
    """Retrieve the password for a site"""
    if not os.path.exists(FILENAME):
        print ("No passwords saved yet")
        return
    with open(FILENAME, "r") as file:
        for line in file:
            stored_site, stored_password, stored_hash = line.strip().split(",")
            if site == stored_site:
                return stored_password
    print("No password has been found for the site{site}")        
    return None
def main():
    if not os.path.exists(FILENAME):
        with open(FILENAME, "w") as file:
            pass#Create the file if it doesnt exist
    action = input ("Enter 'save' to save a password or 'get' to retrieve a password: ")
    if action =="save":
        site = input("Enter the site name: ")
        import string
        import random
        #Generate a random password
        characters =string.ascii_letters + string.digits + string.punctuation
        password = "".join(random.choices(characters, k=10))
        if password:
            save_password(site, password)
        elif action == "get":
            site = input("Enter the site name to retrieve password: ")
            password = get_password(site)
            if password:
                print(f"The password for {site} is {password}")
            else:
                print("Invalid action")

if __name__ == "__main__":
    main()