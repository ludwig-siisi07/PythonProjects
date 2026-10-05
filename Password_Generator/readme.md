# Secure Password Generator
i built an app that generates cryptographically secure passwords. 

## Features
- Choose password length.
- Toggle uppercase, lowercase, numbers, and special characters.
- Cryptographically secure character selection using `secrets`.
- Guarantees at least one character from every selected category is included.

## How it Works
i used the `secrets` module which taps into the OS's strongest source of randomness and ensurs that the passwords i generate cannot be easily guessed.


## How to Run It
1. Ensure Python 3.9 and above is installed on your machine.
2. Clone this repository.
3. Run the script directly from your terminal:
   ```bash
   python password_generator.py