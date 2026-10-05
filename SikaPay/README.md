# SikaConnect - SikaPay

SikaPay is a Python-based simulation of a mobile money app. I built this project to reverse-engineer and understand the software systems powering this financial backbone which drives daily commerce.

## Project Structure
The project is broken down into modular components:

*   **Core Logic:** To handle the maths, balance updates, and transaction history. 
*   **Separated Interfaces:**  to provide a command-line interface for terminal users and a Tkinter graphical user interface.
*   **Data Management:** to read customer and merchant data directly from external spreadsheet files.

## Key Features

*   **Transfer Money:** this featue secures peer-to-peer transfers.
*   **SikaPay:** a special service for paying registered merchants.
*   **Flexi-Bundles:** these are data bundle purchases based on the user's inputs.
*   **Secure Cash Out:** to simulate physical cash withdrawals.
*   **Wallet Management:**  for real-time transaction history tracking and security updates.

## Security and Reliability

Financial tools require absolute reliability. Thus, SikaPay demands strict PIN verification for all sensitive transactions. To ensure the application functions as intended, I implemented unit testing for the core operations. These tests automatically verify the mathematical accuracy of transfers and edge cases, ensuring the system maintains data integrity.

## How to Run the Application

1. Clone this repository to your local machine.
2. Install the necessary dependencies:
   `pip install -r requirements.txt`
3. Run the application:
   `python main.py`

By default, the application will launch the graphical interface. To run the terminal version instead, use `python main.py --cli`.