import pandas as pd
from datetime import datetime
import random

class SikaPayWallet:
    def __init__(self):
        self.balance = 1000.0
        self.pin = "7209"
        self.history = []
        self.customers = self._load_excel("customers.xlsx", "Phone", "Name")
        self.merchants = self._load_excel("merchants.xlsx", "ID", "Name")

    def _load_excel(self, filename, key_col, val_col):
        try:
            df = pd.read_excel(filename, dtype=str)
            return dict(zip(df[key_col], df[val_col]))
        except Exception:
            return {} # Failsafe if files are missing during testing

    def verify_pin(self, pin):
        return self.pin == pin

    def record_tx(self, tx_type, amount, charges, status, recipient):
        self.history.append({
            "Timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "Type": tx_type,
            "Amount (GHS)": f"{amount:.2f}",
            "Charges (GHS)": f"{charges:.2f}",
            "Balance After": f"{self.balance:.2f}",
            "Status": status,
            "Recipient": recipient
        })

    def transfer_money(self, phone, amount, pin):
        if not self.verify_pin(pin):
            return False, "Invalid PIN."
        if phone not in self.customers:
            return False, "Number not registered on Telestar."
            
        e_levy = amount * 0.01
        service_charge = amount * 0.004
        total_deduction = amount + e_levy + service_charge
        
        if self.balance < total_deduction:
            return False, "Insufficient funds."
            
        self.balance -= total_deduction
        recipient = self.customers[phone]
        self.record_tx("Transfer", amount, e_levy + service_charge, "Success", recipient)
        
        return True, (f"GHS {amount:.1f} has been sent successfully to {recipient}, "
                      f"with E-levy charge of GHS {e_levy:.1f} Service charge: GHS {service_charge:.1f}\n"
                      f"New balance: GHS {self.balance:.1f}")