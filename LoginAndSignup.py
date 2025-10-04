import json
import os

USER_FILE = "users.json"

def load_users():
    if os.path.exists(USER_FILE):
        with open(USER_FILE, "r") as file:
            return json.load(file)
    return {}

def save_users(users):
    with open(USER_FILE, "w") as file:
        json.dump(users, file, indent=4)

def signup():
    users = load_users()
    username = input("Enter username: ")
    if username in users:
        print("⚠️ Username already exists! Try logging in.")
        return
    password = input("Enter password: ")
    users[username] = password
    save_users(users)
    print("✅ Signup successful! You can now log in.")

def login():
    users = load_users()
    username = input("Enter username: ")
    password = input("Enter password: ")
    if username in users and users[username] == password:
        print(f"🎉 Welcome, {username}! Login successful.")
    else:
        print("❌ Invalid username or password.")

def main():
    while True:
        print("\n=== LOGIN SYSTEM ===")
        print("1. Signup")
        print("2. Login")
        print("3. Exit")
        choice = input("Choose an option: ")
        
        if choice == "1":
            signup()
        elif choice == "2":
            login()
        elif choice == "3":
            print("👋 Goodbye!")
            break
        else:
            print("⚠️ Invalid choice! Please try again.")

if __name__ == "__main__":
    main()
