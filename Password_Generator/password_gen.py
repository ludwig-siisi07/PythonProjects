import tkinter as tk
import secrets
import string

# --- CORE LOGIC ---
def generate_basic_password(length, use_upper, use_lower, use_digits, use_specials):
    pool = ""
    if use_upper: pool += string.ascii_uppercase
    if use_lower: pool += string.ascii_lowercase
    if use_digits: pool += string.digits
    if use_specials: pool += string.punctuation
    
    if not pool or length <= 0:
        return ""
        
    return "".join(secrets.choice(pool) for _ in range(length))

# --- GUI ---
class PasswordGeneratorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Secure Password Generator")
        self.root.geometry("350x300")
        
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

    def handle_generate(self):
        # Basic parsing without robust error handling yet
        length = int(self.length_var.get())
        password = generate_basic_password(
            length, self.upper_var.get(), self.lower_var.get(), 
            self.digits_var.get(), self.specials_var.get()
        )
        self.display_var.set(password)

if __name__ == "__main__":
    root = tk.Tk()
    app = PasswordGeneratorApp(root)
    root.mainloop()