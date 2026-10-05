import tkinter as tk
from tkinter import messagebox, simpledialog

class SikaPayGUI:
    def __init__(self, root, wallet):
        self.root = root
        self.wallet = wallet
        self.root.title("SikaPay Mobile")
        self.root.geometry("350x550")
        self.root.configure(bg="#f4f4f4")
        
        title = tk.Label(root, text="SikaPay Menu", font=("Helvetica", 16, "bold"), bg="#f4f4f4", pady=20)
        title.pack()

        buttons = [
            ("1. Transfer Money", self.gui_transfer),
            ("2. SikaPay", self.gui_momopay),
            ("3. Airtime/Bundles", self.gui_airtime),
            ("4. Allow Cash Out", self.gui_cashout),
            ("6. My Wallet", self.gui_wallet)
        ]

        for text, cmd in buttons:
            btn = tk.Button(root, text=text, font=("Helvetica", 12), width=25, pady=5, command=cmd)
            btn.pack(pady=10)

    def gui_transfer(self):
        phone = simpledialog.askstring("Transfer", "Enter recipient's 059 number:")
        amount = simpledialog.askfloat("Transfer", "Enter amount to transfer:")
        if phone and amount:
            pin = simpledialog.askstring("Transfer", "Enter SikaPay PIN:", show="*")
            success, msg = self.wallet.transfer_money(phone, amount, pin)
            messagebox.showinfo("Result", msg)

    def gui_momopay(self):
        m_id = simpledialog.askstring("SikaPay", "Enter 6-digit Merchant ID:")
        amount = simpledialog.askfloat("SikaPay", "Enter amount to pay:")
        if m_id and amount:
            pin = simpledialog.askstring("SikaPay", "Enter MOMO PIN:", show="*")
            success, msg = self.wallet.momo_pay(m_id, amount, pin)
            messagebox.showinfo("Result", msg)

    def gui_airtime(self):
        amount = simpledialog.askfloat("Flexi-Bundle", "Enter amount to purchase (GHS):")
        if amount:
            success, msg = self.wallet.buy_flexi_bundle(amount)
            messagebox.showinfo("Result", msg)

    def gui_cashout(self):
        merchant, amount = self.wallet.generate_cashout_prompt()
        if merchant and messagebox.askyesno("Cash Out", f"Cashout request for GHS {amount} to {merchant}. Approve?"):
            pin = simpledialog.askstring("Cash Out", "Enter SikaPay PIN:", show="*")
            success, msg = self.wallet.cash_out(amount, merchant, pin)
            messagebox.showinfo("Result", msg)

    def gui_wallet(self):
        amt = simpledialog.askfloat("Top Up", "Enter amount to top up:")
        if amt:
            _, msg = self.wallet.top_up(amt)
            messagebox.showinfo("Result", msg)