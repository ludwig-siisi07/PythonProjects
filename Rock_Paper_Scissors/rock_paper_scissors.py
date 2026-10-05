import tkinter as tk
import random

# --- GAME LOGIC ---
# dict to represent the rulesto avoid long conditional chains.

WIN_RULES = {
    "Rock": "Scissors",
    "Paper": "Rock",
    "Scissors": "Paper"
}

EMOJIS = {
    "Rock": "✊",
    "Paper": "✋",
    "Scissors": "✌️"
}

def get_computer_choice():
    """Returns a random choice for the computer."""
    return random.choice(list(WIN_RULES.keys()))

def determine_winner(player_choice, computer_choice):
    """Returns 'player', 'computer', or 'tie' based on the choices."""
    if player_choice == computer_choice:
        return "tie"
    elif WIN_RULES[player_choice] == computer_choice:
        return "player"
    else:
        return "computer"


# --- GUI AND STATE MANAGEMENT ---
class RockPaperScissorsApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Rock Paper Scissors")
        self.root.geometry("350x450")
        self.root.resizable(False, False)
        
        # Game State
        self.state = {
            "player": 0,
            "computer": 0,
            "ties": 0,
            "round": 0
        }
        
        self.build_ui()

    def build_ui(self):
        """Constructs the Tkinter interface."""
        # Header
        tk.Label(self.root, text="ROCK PAPER SCISSORS", font=("Helvetica", 16, "bold"), pady=10).pack()
        
        # Arena Area (You vs CPU)
        self.arena_frame = tk.Frame(self.root)
        self.arena_frame.pack(pady=10)
        
        self.player_label = tk.Label(self.arena_frame, text="You\n❓", font=("Helvetica", 14), width=10)
        self.player_label.grid(row=0, column=0)
        
        tk.Label(self.arena_frame, text="VS", font=("Helvetica", 12, "bold")).grid(row=0, column=1)
        
        self.cpu_label = tk.Label(self.arena_frame, text="CPU\n❓", font=("Helvetica", 14), width=10)
        self.cpu_label.grid(row=0, column=2)
        
        # Result Message
        self.result_label = tk.Label(self.root, text="Make your move!", font=("Helvetica", 12), fg="blue", pady=10)
        self.result_label.pack()
        
        # Scoreboard
        self.score_frame = tk.Frame(self.root)
        self.score_frame.pack(pady=10)
        
        self.score_label = tk.Label(self.score_frame, text="Round: 0\nPlayer: 0  |  CPU: 0  |  Ties: 0", font=("Helvetica", 11))
        self.score_label.pack()
        
        # Controls (Buttons)
        self.controls_frame = tk.Frame(self.root)
        self.controls_frame.pack(pady=15)
        
        for choice in EMOJIS.keys():
            btn = tk.Button(self.controls_frame, text=f"{EMOJIS[choice]} {choice}", width=12,
                            command=lambda c=choice: self.play_round(c))
            btn.pack(pady=3)
            
        # Reset Button
        tk.Button(self.root, text="Reset Game", command=self.reset_game, fg="red").pack(pady=10)

    def play_round(self, player_choice):
        """Handles the logic of a single round."""
        computer_choice = get_computer_choice()
        winner = determine_winner(player_choice, computer_choice)
        
        # Update State
        self.state["round"] += 1
        if winner == "player":
            self.state["player"] += 1
            result_text = "You win!"
        elif winner == "computer":
            self.state["computer"] += 1
            result_text = "Computer wins!"
        else:
            self.state["ties"] += 1
            result_text = "It's a tie!"
            
        self.update_display(player_choice, computer_choice, result_text)

    def update_display(self, player_choice, computer_choice, result_text):
        """Updates the GUI labels with the new state."""
        self.player_label.config(text=f"You\n{EMOJIS[player_choice]}\n{player_choice}")
        self.cpu_label.config(text=f"CPU\n{EMOJIS[computer_choice]}\n{computer_choice}")
        
        self.result_label.config(text=result_text)
        
        self.score_label.config(
            text=f"Round: {self.state['round']}\n"
                 f"Player: {self.state['player']}  |  CPU: {self.state['computer']}  |  Ties: {self.state['ties']}"
        )

    def reset_game(self):
        """Resets all state to zero and clears the display."""
        self.state = {"player": 0, "computer": 0, "ties": 0, "round": 0}
        self.player_label.config(text="You\n❓")
        self.cpu_label.config(text="CPU\n❓")
        self.result_label.config(text="Make your move!")
        self.score_label.config(text="Round: 0\nPlayer: 0  |  CPU: 0  |  Ties: 0")

if __name__ == "__main__":
    root = tk.Tk()
    app = RockPaperScissorsApp(root)
    root.mainloop()