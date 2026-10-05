import sys
import os

def main():
    # If part 4's GUI exists and --cli isn't passed, run GUI
    if os.path.exists("sikapay/gui.py") and "--cli" not in sys.argv:
        from sikapay.gui import SikaPayGUI
        from sikapay.core import SikaPayWallet
        import tkinter as tk
        root = tk.Tk()
        app = SikaPayGUI(root, SikaPayWallet())
        root.mainloop()
    else:
        # Otherwise, run the terminal CLI
        from sikapay.cli import SikaPayCLI
        cli = SikaPayCLI()
        cli.run()

if __name__ == "__main__":
    main()