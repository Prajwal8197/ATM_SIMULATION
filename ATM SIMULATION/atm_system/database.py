import os
import psycopg2
import face_recognition
import fingerprint


class ATMDatabase:

    def __init__(self):
        self.connection = psycopg2.connect(
            host=os.environ["DATABASE_HOST"],
            port=os.environ["DATABASE_PORT"],
            database=os.environ["DATABASE_NAME"],
            user=os.environ["DATABASE_USERNAME"],
            password=os.environ["DATABASE_PASSWORD"],
        )
        self.cursor = self.connection.cursor()

    def is_user_registered(self, name):
        sql = """
        SELECT EXISTS (
            SELECT 1 FROM users WHERE name = %s
        )
        """
        self.cursor.execute(sql, (name,))
        return self.cursor.fetchone()[0]

    def is_face_match(self, name, face):
        sql = """
        SELECT EXISTS (
            SELECT 1 FROM users WHERE name = %s AND face = %s
        )
        """
        self.cursor.execute(sql, (name, face))
        return self.cursor.fetchone()[0]

    def is_fingerprint_match(self, name, fingerprint):
        sql = """
        SELECT EXISTS (
            SELECT 1 FROM users WHERE name = %s AND fingerprint = %s
        )
        """
        self.cursor.execute(sql, (name, fingerprint))
        return self.cursor.fetchone()[0]

    def get_user_balance(self, name):
        sql = """
        SELECT balance FROM users WHERE name = %s
        """
        self.cursor.execute(sql, (name,))
        return self.cursor.fetchone()[0]

    def withdraw_cash(self, name, amount):
        sql = """
        UPDATE users SET balance = balance - %s WHERE name = %s
        """
        self.cursor.execute(sql, (amount, name))
        self.connection.commit()

    def deposit_cash(self, name, amount):
        sql = """
        UPDATE users SET balance = balance + %s WHERE name = %s
        """
        self.cursor.execute(sql, (amount, name))
        self.connection.commit()

    def transfer_money(self, from_name, to_name, amount):
        sql = """
        UPDATE users SET balance = balance - %s WHERE name = %s
        UPDATE users SET balance = balance + %s WHERE name = %s
        """
        self.cursor.execute(sql, (amount, from_name, amount, to_name))
        self.connection.commit()

    def send_otp(self, name, phone_number):
        sql = """
        INSERT INTO otps (name, phone_number, otp) VALUES (%s, %s, %s)
        """
        otp = face_recognition.generate_otp()
        self.cursor.execute(sql, (name, phone_number, otp))
        self.connection.commit()

    def is_otp_valid(self, name, otp):
        sql = """
        SELECT EXISTS (
            SELECT 1 FROM otps WHERE name = %s AND otp = %s
        )
        """
        self.cursor.execute(sql, (name, otp))
        return self.cursor.fetchone()[0]

    def close(self):
        self.cursor.close()
        self.connection.close()

