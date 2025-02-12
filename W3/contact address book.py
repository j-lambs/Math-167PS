#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb  5 22:37:26 2025

@author: greglabmeier
"""

def add_contact():
   name = input("Enter name: ")
   phone = input("Enter phone number: ")
   email = input("Enter email: ")

   contacts[name] = {"phone": phone, "email": email}
   print(f"Contact {name} added successfully!")

def delete_contact():
   name = input("Enter name to delete: ")
   if name in contacts:
       del contacts[name]
       print(f"Contact {name} deleted successfully!")
   else:
       print("Contact not found.")

keep_asking = True
while keep_asking:
   print("\nContact Book Menu:")
   print("1. Add Contact")
   print("2. Delete Contact")
   print("3. Exit")

   choice = input("Choose an option: ")

   if choice == "1":
       add_contact()
   elif choice == "2":
       delete_contact()
   elif choice == "3":
       print("Exiting Contact Book. Goodbye!")
       keep_asking = False
   else:
       print("Invalid choice. Please enter a number from 1-3.")
