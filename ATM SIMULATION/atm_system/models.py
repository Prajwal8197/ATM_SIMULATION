class User:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance

    def check_balance(self):
        print("Your balance is {}.".format(self.balance))

    def withdraw_cash(self, amount):
        if amount > self.balance:
            print("You don't have enough money.")
        else:
            self.balance -= amount
            print("You have withdrawn {}.".format(amount))

    def deposit_cash(self, amount):
        self.balance += amount
        print("You have deposited {}.".format(amount))

    def transfer_money(self, to_user, amount):
        if amount > self.balance:
            print("You don't have enough money.")
        else:
            self.balance -= amount
            to_user.balance += amount
            print("You have transferred {} to {}.".format(amount, to_user.name))


class ATM:
    def __init__(self, database):
        self.database = database

    def login(self, name, face, fingerprint):
        if not self.database.is_user_registered(name):
            print("User not registered.")
            return False

        if not self.database.is_face_match(name, face):
            print("Incorrect face.")
            return False

        if not self.database.is_fingerprint_match(name, fingerprint):
            print("Incorrect fingerprint.")
            return False

        return True

    def get_user_balance(self, name):
        balance = self.database.get_user_balance(name)
        print("Your balance is {}.".format(balance))

    def withdraw_cash(self, name, amount):
        if not self.database.is_user_registered(name):
            print("User not registered.")
            return False

        balance = self.database.get_user_balance(name)
        if amount > balance:
            print("You don't have enough money.")
            return False

        self.database.withdraw_cash(name, amount)
        print("You have withdrawn {}.".format(amount))

    def deposit_cash(self, name, amount):
        if not self.database.is_user_registered(name):
            print("User not registered.")
            return False

        self.database.deposit_cash(name, amount)
        print("You have deposited {}.".format(amount))

    def transfer_money(self, from_name, to_name, amount):
        if not self.database.is_user_registered(from_name):
            print("User not registered.")
            return False

        if not self.database.is_user_registered(to_name):
            print("User not registered.")
            return False

        balance = self.database.get_user_balance(from_name)
        if amount > balance:
            print("You don't have enough money.")
            return False

        self.database.transfer_money(from_name, to_name, amount)
        print("You have transferred {} to {}.".format(amount, to_name))

