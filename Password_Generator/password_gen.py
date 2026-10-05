import tkinter as tk
import secrets
import string

# CORE LOGIC
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
        
    if not pool or length < len(guaranteed):
        return ""
        
    remaining = length - len(guaranteed)
    all_chars = guaranteed + [secrets.choice(pool) for _ in range(remaining)]
    
    secrets.SystemRandom().shuffle(all_chars)
    return "".join(all_chars)

def evaluate_strength(password):
    if len(password) >= 12: return "Strong", "green"
    if len(password) >= 8: return "Medium", "orange"
    return "Weak", "red"

#  GUI 
class PasswordGeneratorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Secure Password Generator")
        self.root.geometry("350x350")
        
        self.length_var = tk.StringVar(value="12")
        self.upper_var = tk.BooleanVar(value=True)
        self.lower_var = tk.BooleanVar(value=True)
        self.digits_var = tk.BooleanVar(value=True)
        self.specials_var = tk.BooleanVar(value=True)
        
        self.build_ui()

    def build_ui(self):
        tk.Label(self.root, text="Password Generator", font=("Helvetica", 14, "bold")).pack(pady=10)
        tk.Entry(self.root, textvariable=self.length_var, width=5).pack()
        
        tk.Checkbutton(self.root, text="Uppercase", variable=self.upper_var).pack()
        tk.Checkbutton(self.root, text="Lowercase", variable=self.lower_var).pack()
        tk.Checkbutton(self.root, text="Numbers", variable=self.digits_var).pack()
        tk.Checkbutton(self.root, text="Symbols", variable=self.specials_var).pack()
        
        tk.Button(self.root, text="Generate", command=self.handle_generate).pack(pady=10)
        
        self.display_var = tk.StringVar()
        tk.Entry(self.root, textvariable=self.display_var, state="readonly", width=30).pack()
        
        # New Strength Label
        self.strength_label = tk.Label(self.root, text="Strength: ---")
        self.strength_label.pack(pady=5)

    def handle_generate(self):
        length = int(self.length_var.get())
        password = generate_secure_password(
            length, self.upper_var.get(), self.lower_var.get(), 
            self.digits_var.get(), self.specials_var.get()
        )
        self.display_var.set(password)
        
        if password:
            text, color = evaluate_strength(password)
            self.strength_label.config(text=f"Strength: {text}", fg=color)

if __name__ == "__main__":
    root = tk.Tk()
    app = PasswordGeneratorApp(root)
    root.mainloop()