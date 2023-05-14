import unittest
from models import User, ATM


class TestUser(unittest.TestCase):

    def test_init(self):
        user = User("John Doe", 100)
        self.assertEqual(user.name, "John Doe")
        self.assertEqual(user.balance, 100)

    def test_check_balance(self):
        user = User("John Doe", 100)
        user.check_balance()
        self.assertEqual(user.balance, 100)

    def test_withdraw_cash(self):
        user = User("John Doe", 100)
        user.withdraw_cash(50)
        self.assertEqual(user.balance, 50)

    def test_deposit_cash(self):
        user = User("John Doe", 100)
        user.deposit_cash(50)
        self.assertEqual(user.balance, 150)

    def test_transfer_money(self):
        user1 = User("John Doe", 100)
        user2 = User("Jane Doe", 0)
        user1.transfer_money(user2, 50)
        self.assertEqual(user1.balance, 50)
        self.assertEqual(user2.balance, 50)


class TestATM(unittest.TestCase):

    def test_login(self):
        atm = ATM()
        user = User("John Doe", 100)
        atm.login(user.name, user.face, user.fingerprint)
        self.assertEqual(atm.is_logged_in(), True)

    def test_get_user_balance(self):
        atm = ATM()
        user = User("John Doe", 100)
        atm.get_user_balance(user.name)
        self.assertEqual(atm.get_user_balance(user.name), 100)

    def test_withdraw_cash(self):
        atm = ATM()
        user = User("John Doe", 100)
        atm.withdraw_cash(user.name, 50)
        self.assertEqual(atm.get_user_balance(user.name), 50)

    def test_deposit_cash(self):
        atm = ATM()
        user = User("John Doe", 100)
        atm.deposit_cash(user.name, 50)
        self.assertEqual(atm.get_user_balance(user.name), 150)

    def test_transfer_money(self):
        atm = ATM()
        user1 = User("John Doe", 100)
        user2 = User("Jane Doe", 0)
        atm.transfer_money(user1.name, user2.name, 50)
        self.assertEqual(atm.get_user_balance(user1.name), 50)
        self.assertEqual(atm.get_user_balance(user2.name), 50)


if __name__ == "__main__":
    unittest.main()
