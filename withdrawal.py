from accounts import AccountValidation
from balance import BalanceManagement
from transaction import Transaction
from notification import Notification
from fraud import FraudDetection

class Withdrawal(Transaction):
    def process(self):
        acc = AccountValidation.get_account(self.acc_no)
        if not acc:
            print("Invalid account")
            return

        if self.amount <= 0:
            print("Invalid withdrawal amount")
            return

        if float(acc["balance"]) < self.amount:
            print("Insufficient balance")
            return

        FraudDetection.check(self.amount)

        new_balance = float(acc["balance"]) - self.amount
        BalanceManagement.update_balance(self.acc_no, new_balance)

        self.save()
        Notification.send(self.acc_no,
            f"Withdrawn {self.amount}. New Balance: {new_balance}")
