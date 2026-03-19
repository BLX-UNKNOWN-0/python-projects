# BLX-UNKNOWN-0
# PROJECT 9 // CONTACT BOOK

import json
import os

FILE = "contacts.json"

def load():
    if os.path.exists(FILE):
        with open(FILE, "r") as f:
            return json.load(f)
    return {}

def save(contacts):
    with open(FILE, "w") as f:
        json.dump(contacts, f, indent=4)

def add(contacts):
    name  = input("Name  : ").strip()
    phone = input("Phone : ").strip()
    email = input("Email : ").strip()
    contacts[name] = {"phone": phone, "email": email}
    save(contacts)
    print(f"✅ {name} saved!")

def view(contacts):
    if not contacts:
        print("No contacts yet.")
        return
    print("\n--- Contacts ---")
    for name, info in contacts.items():
        print(f"{name} | {info['phone']} | {info['email']}")

def delete(contacts):
    name = input("Name to delete: ").strip()
    if name in contacts:
        del contacts[name]
        save(contacts)
        print(f"✅ {name} deleted!")
    else:
        print("Contact not found.")

def search(contacts):
    name = input("Search name: ").strip()
    if name in contacts:
        info = contacts[name]
        print(f"\n{name} | {info['phone']} | {info['email']}")
    else:
        print("Not found.")

def menu():
    print("...CONTACT BOOK...")
    contacts = load()

    while True:
        print("\n 1=Add  2=View  3=Delete  4=Search  0=Quit")
        choice = input("Choose: ").strip()

        if   choice == "1": add(contacts)
        elif choice == "2": view(contacts)
        elif choice == "3": delete(contacts)
        elif choice == "4": search(contacts)
        elif choice == "0": print("Bye!"); break
        else: print("Invalid choice.")

menu()