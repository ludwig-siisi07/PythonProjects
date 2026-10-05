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
            return {} 

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

    def momo_pay(self, merchant_id, amount, pin):
        if not self.verify_pin(pin):
            return False, "Invalid PIN."
        if merchant_id not in self.merchants:
            return False, "Merchant not found."
            
        e_levy = amount * 0.01
        total_deduction = amount + e_levy
        
        if self.balance < total_deduction:
            return False, "Insufficient funds."
            
        self.balance -= total_deduction
        merchant = self.merchants[merchant_id]
        self.record_tx("MOMO Pay", amount, e_levy, "Success", merchant)
        return True, (f"GHS {amount:.1f} has been paid successfully to {merchant}, "
                      f"with E-levy charge of GHS {e_levy:.1f}. New balance: GHS {self.balance:.1f}")

    def buy_flexi_bundle(self, amount):
        if self.balance < amount:
            return False, "Insufficient funds."
            
        self.balance -= amount
        data_mb = (amount / 0.01786) + (amount * 0.05) 
        
        self.record_tx("Flexi-Bundle", amount, 0.0, "Success", "Self")
        return True, f"{data_mb:.1f} MB Data Bundle successfully purchased.\nNew balance: GHS {self.balance:.1f}"

    def generate_cashout_prompt(self):
        if not self.merchants:
            return None, 0
        merchant = random.choice(list(self.merchants.values()))
        amount = random.randint(10, 500)
        return merchant, amount

    def cash_out(self, amount, merchant, pin):
        if not self.verify_pin(pin):
            return False, "Invalid PIN."
            
        fee = amount * 0.05
        if self.balance < (amount + fee):
            return False, "Insufficient funds."
            
        self.balance -= (amount + fee)
        self.record_tx("Cash out", amount, fee, "Success", merchant)
        return True, (f"Cash Out made for GHS {amount:.2f} to {merchant}. "
                      f"CashOut Fee GHS{fee:.2f} was charged automatically from your wallet.\n"
                      f"Current Balance: GHS{self.balance:.2f}")

    def top_up(self, amount):
        self.balance += amount
        self.record_tx("Account Topup", amount, 0.0, "Success", "Owner")
        return True, f"Balance top up is successful. New balance: GHS {self.balance:.1f}"

    def change_pin(self, old_pin, new_pin):
        if not self.verify_pin(old_pin):
            return False, "Incorrect current PIN."
        self.pin = new_pin
        return True, "MOMO Pin successfully changed!"