import tkinter as tk
from tkinter import messagebox
import secrets
import string

# --- CORE LOGIC ---
def generate_secure_password(length, use_upper, use_lower, use_digits, use_specials):
    pool = ""
    guaranteed = []
    
    if use_upper:
        pool += string.ascii_uppercase
        guaranteed.append(secrets.choice(string.ascii_uppercase))
    if use_lower:
        pool += string.ascii_lowercase
        guaranteed.append(secrets.choice(string.ascii_lowercase))
    if use_digits:
        pool += string.digits
        guaranteed.append(secrets.choice(string.digits))
    if use_specials:
        pool += string.punctuation
        guaranteed.append(secrets.choice(string.punctuation))
        
    if not pool:
        raise ValueError("Please select at least one character category.")
    if length < len(guaranteed):
        raise ValueError(f"Length must be at least {len(guaranteed)}.")
        
    remaining = length - len(guaranteed)
    all_chars = guaranteed + [secrets.choice(pool) for _ in range(remaining)]
    
    secrets.SystemRandom().shuffle(all_chars)
    return "".join(all_chars)

def evaluate_strength(password):
    if len(password) >= 12: return "Strong", "green"
    if len(password) >= 8: return "Medium", "orange"
    return "Weak", "red"

# --- GUI ---
class PasswordGeneratorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Secure Password Generator")
        self.root.geometry("350x450")
        
        self.length_var = tk.StringVar(value="12")
        self.upper_var = tk.BooleanVar(value=True)
        self.lower_var = tk.BooleanVar(value=True)
        self.digits_var = tk.BooleanVar(value=True)
        self.specials_var = tk.BooleanVar(value=True)
        
        self.build_ui()

    def build_ui(self):
        tk.Label(self.root, text="Password Generator", font=("Helvetica", 14, "bold")).pack(pady=10)
        
        frame = tk.Frame(self.root)
        frame.pack(pady=5)
        tk.Label(frame, text="Length:").pack(side=tk.LEFT)
        tk.Entry(frame, textvariable=self.length_var, width=5).pack(side=tk.LEFT, padx=5)
        
        tk.Checkbutton(self.root, text="Uppercase", variable=self.upper_var).pack()
        tk.Checkbutton(self.root, text="Lowercase", variable=self.lower_var).pack()
        tk.Checkbutton(self.root, text="Numbers", variable=self.digits_var).pack()
        tk.Checkbutton(self.root, text="Symbols", variable=self.specials_var).pack()
        
        tk.Button(self.root, text="Generate Password", bg="#4CAF50", fg="white", 
                  command=self.handle_generate).pack(pady=15)
        
        self.display_var = tk.StringVar()
        tk.Entry(self.root, textvariable=self.display_var, state="readonly", width=30, justify="center").pack()
        
        self.strength_label = tk.Label(self.root, text="Strength: ---")
        self.strength_label.pack(pady=5)
        
        # New Action Buttons
        btn_frame = tk.Frame(self.root)
        btn_frame.pack(pady=10)
        tk.Button(btn_frame, text="Copy", command=self.copy_password).pack(side=tk.LEFT, padx=5)
        tk.Button(btn_frame, text="Reset", command=self.reset_app, fg="red").pack(side=tk.LEFT, padx=5)

    def handle_generate(self):
        # Now uses robust try/except validation
        try:
            length_str = self.length_var.get()
            if not length_str.isdigit():
                raise ValueError("Length must be a whole number.")
                
            password = generate_secure_password(
                int(length_str), self.upper_var.get(), self.lower_var.get(), 
                self.digits_var.get(), self.specials_var.get()
            )
            
            self.display_var.set(password)
            text, color = evaluate_strength(password)
            self.strength_label.config(text=f"Strength: {text}", fg=color)
            
        except ValueError as e:
            messagebox.showerror("Error", str(e))

    def copy_password(self):
        pwd = self.display_var.get()
        if pwd:
            self.root.clipboard_clear()
            self.root.clipboard_append(pwd)
            messagebox.showinfo("Copied", "Password copied to clipboard!")

    def reset_app(self):
        self.length_var.set("12")
        self.upper_var.set(True)
        self.lower_var.set(True)
        self.digits_var.set(True)
        self.specials_var.set(True)
        self.display_var.set("")
        self.strength_label.config(text="Strength: ---", fg="black")

if __name__ == "__main__":
    root = tk.Tk()
    app = PasswordGeneratorApp(root)
    root.mainloop()