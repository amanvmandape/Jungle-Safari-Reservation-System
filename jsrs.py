# imports
import sys
import os
import time
import pickle

# Globals
slots = []


# Functions
def book_slot():
    os.system("cls")
    dbfile = open('database','wb')

    if len(slots)<10:
        data = {}
        name = input("Enter your Full Name: ")
        phone = input("Enter your Phone-Number: ")
        age = input("Enter your Age: ")
        for property in ["name", "phone", "age"]:
            data[property] = eval(property)
        slots.append(data);
        pickle.dump(slots, dbfile)
        dbfile.close()
        print("\nSuccessfully added "+data["name"])
    else:
        print("Sorry, all Slots are Full.")
    time.sleep(1.5)

def cancel_slot():
    os.system("cls")
    dbfile = open('database','wb')

    flag = True
    if len(slots)>0:
        phone = input("Enter your Phone Number: ")
        for data in slots:
            if data["phone"] == phone:
                slots.remove(data)
                pickle.dump(slots, dbfile)
                dbfile.close()
                print("\nSuccessfully Cancelled Your Slot")
                flag = False
        if flag:
            print("\nNot found in DataBase")
    else:
        print("All Slots are Empty")
    time.sleep(1.5)

def view_slot():
    os.system("cls")
    if len(slots)>0:
        for data in slots:
            print("\n\nSeat no: ",slots.index(data)+1)
            for property in ["name", "phone", "age"]:
                print(property.title()+": "+data[property], end = "\t")
        input("\n\nPress Enter to continue...")
    else:
        print("All Slots Empty")
        time.sleep(1.5)

# Main
while(True):
    try:
        dbfile = open('database','rb')
        slots = pickle.load(dbfile)
        dbfile.close()
    except EOFError as e:
        dbfile.close()

    print("\nWelcome to Jungle Safari Reservation System")
    print("\nWhat would you like to Do?")
    print("1) Book Slot")
    print("2) Cancel Slot")
    print("3) View Slot Status")
    print("4) Exit")
    user_choice = input("\nEnter your choice(1-3): ")
    if user_choice == "1":
        book_slot()
    elif user_choice == "2":
        cancel_slot()
    elif user_choice == "3":
        view_slot()
    elif user_choice == "4":
        sys.exit()
    else:
        print("\nInvalid choice entered, Please try again...")
        time.sleep(1.5)

    os.system("cls")