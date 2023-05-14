"""This module contains code for an ATM system."""

import os
import sys
import database

from database import ATMDatabase
from atm_user import ATMUser

from face_recognition import face_recognition
from fingerprint import fingerprint


def main():
    # Create a database connection
    database = ATMDatabase()

    # Create a user object
    user = ATMUser()

    # Get the user's name
    name = input("Enter your name: ")

    # Get the user's face
    face = face_recognition.get_face()

    # Get the user's fingerprint
    user_fingerprint = fingerprint.get_fingerprint()

    # Check if the user is registered
    if not database.is_user_registered(name):
        print("User not registered.")
        sys.exit(1)

    # Check if the user's face matches the stored face
    if not face_recognition.compare_faces(database.get_face(name), face):
        print("Incorrect face.")
        sys.exit(1)

    # Check if the user's fingerprint matches the stored fingerprint
    """This function checks if the given fingerprint is valid."""
    def check_fingerprint(fingerprint):

        if not fingerprint.compare_fingerprints(database.get_fingerprint(name), fingerprint):
            print("Incorrect fingerprint.")
            sys.exit(1)

    # Display the main menu
    while True:
        print("1. Check balance")
        print("2. Withdraw cash")
        print("3. Deposit cash")
        print("4. Transfer money")
        print("5. Quit")

        option = int(input("Enter your option: "))

        if option == 1:
            user.check_balance()
        elif option == 2:
            user.withdraw_cash()
        elif option == 3:
            user.deposit_cash()
        elif option == 4:
            user.transfer_money()
        elif option == 5:
            break

    # Close the database connection
    database.close()


if __name__ == "__main__":
    main()
