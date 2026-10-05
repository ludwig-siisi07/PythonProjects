from sikapay.core import SikaPayWallet

class SikaPayCLI:
    def __init__(self):
        self.wallet = SikaPayWallet()

    def run(self):
        while True:
            print("\nWelcome to SikaPay! Please select an option:")
            print("1. Transfer Money\n2. SikaPay\n3. Airtime and Bundles\n4. Allow Cash Out\n6. My Wallet\n0. Exit")
            choice = input("Enter your choice: ")
            
            if choice == '1':
                self.handle_transfer()
            elif choice == '2':
                self.handle_momopay()
            elif choice == '3':
                self.handle_airtime()
            elif choice == '4':
                self.handle_cashout()
            elif choice == '6':
                self.handle_wallet()
            elif choice == '0':
                break
            
            if input("\nDo you want to perform another operation? (yes/no): ").lower() != 'yes':
                break

    def handle_transfer(self):
        print("\nTransfer Money:\n1. SikaConnect Network\n2. Other Networks")
        input("Enter your transfer choice: ")
        phone1 = input("Enter the recipient's SikaConnect's phone number (should start with 059): ")
        phone2 = input("Verify the phone number by entering it again: ")
        
        if phone1 != phone2:
            print("Numbers do not match.")
            return
            
        amount = float(input("Enter the amount to transfer: "))
        recipient_name = self.wallet.customers.get(phone1, "Unknown")
        pin = input(f"Enter your SikaPay pin to authorize transfer to {recipient_name}: ")
        
        success, msg = self.wallet.transfer_money(phone1, amount, pin)
        print(msg)

    def handle_momopay(self):
        print("\nSikaPay/Paybill:")
        m_id = input("Enter the 6-digit Merchant ID: ")
        merchant_name = self.wallet.merchants.get(m_id, "Unknown Merchant")
        print(f"Proceed to make payment to merchant, {merchant_name}")
        amount = float(input("Enter the amount to pay: "))
        pin = input("Enter your SikaPay PIN to authorize: ")
        success, msg = self.wallet.momo_pay(m_id, amount, pin)
        print(msg)

    def handle_airtime(self):
        print("\nAirtime and Bundles:\n1. Buy Airtime\n2. Buy Bundles")
        if input("Enter your choice: ") == '2':
            print("\nBundles:\n1. GHC 5 (280 MB)\n2. GHC 10 (667 MB)\n3. GHC 100 (10 GB)\n4. Flexi-Bundle (GHS 0 - GHS 400)")
            if input("Choose your bundle type: ") == '4':
                amount = float(input("Enter amount to purchase: "))
                success, msg = self.wallet.buy_flexi_bundle(amount)
                print(msg)

    def handle_cashout(self):
        print("\nAllow CashOut:\n1. Yes\n2. No")
        if input("Enter your choice: ") == '1':
            merchant, amount = self.wallet.generate_cashout_prompt()
            if merchant:
                print(f"Cashout for GHS{amount} to {merchant}")
                pin = input("Enter your SikaPay PIN to authorize CashOut: ")
                success, msg = self.wallet.cash_out(amount, merchant, pin)
                print(msg)
            else:
                print("No merchants available for cashout.")

    def handle_wallet(self):
        print("\nMy Wallet:\n1. Top Up Balance\n2. Check Balance\n3. Change MoMo Pin\n4. Transaction History")
        choice = input("Enter your choice: ")
        
        if choice == '1':
            amt = float(input("Enter amount to top up your balance: "))
            _, msg = self.wallet.top_up(amt)
            print(msg)
        elif choice == '2':
            print(f"Current Balance: GHS {self.wallet.balance:.2f}")
        elif choice == '3':
            old = input("Enter your MoMo Pin: ")
            new = input("Enter your new 4-digit MoMo Pin: ")
            _, msg = self.wallet.change_pin(old, new)
            print(msg)
        elif choice == '4':
            print("\nTransaction History:")
            for tx in self.wallet.history:
                print("-" * 80)
                for k, v in tx.items():
                    print(f"{k} : {v}")
            print("-" * 80)