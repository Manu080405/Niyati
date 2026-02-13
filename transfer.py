from accounts import AccountValidation
from balance import BalanceManagement
from transaction import Transaction
from notification import Notification
from fraud import FraudDetection

class FundTransfer:
    @staticmethod
    def transfer(sender, receiver, amount):
        s_acc = AccountValidation.get_account(sender)
        r_acc = AccountValidation.get_account(receiver)

        if not s_acc or not r_acc:
            print("Invalid sender or receiver")
            return

        if float(s_acc["balance"]) < amount:
            print("Insufficient balance")
            return

        FraudDetection.check(amount)

        BalanceManagement.update_balance(sender,
            float(s_acc["balance"]) - amount)

        BalanceManagement.update_balance(receiver,
            float(r_acc["balance"]) + amount)

        Transaction(sender, amount, "TRANSFER_DEBIT").save()
        Transaction(receiver, amount, "TRANSFER_CREDIT").save()

        Notification.send(sender, f"Transferred {amount} to {receiver}")
        Notification.send(receiver, f"Received {amount} from {sender}")
