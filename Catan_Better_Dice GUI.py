import random
import tkinter as tk
from tkinter import messagebox, simpledialog, font

def roll_number():
    results = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
    weights = [2.78, 5.56, 8.33, 11.11, 13.89, 16.67, 13.89, 11.11, 8.33, 5.56, 2.78]
    return random.choices(results, weights=weights)[0]

class CatanGame:
    def __init__(self, master):
        self.master = master
        self.master.title("Catan Game")
        self.master.geometry("400x300")
        self.master.config(bg="#f0f0f0")
        
        self.title_font = font.Font(family="Helvetica", size=16, weight="bold")
        
        self.statistics = {i: 0 for i in range(2, 13)}
        self.num_rolls = 0
        self.players = []
        self.player_number = 0

        self.label_title = tk.Label(master, text="Welcome to Catan!", bg="#f0f0f0", font=self.title_font)
        self.label_title.pack(pady=20)
        
        self.start_button = tk.Button(
            master, text="Start Game", command=self.start_game,
            bg="#4CAF50", fg="white", font=("Helvetica", 12), relief="raised", padx=10, pady=5
        )
        self.start_button.pack(pady=10, padx=20, fill=tk.X)
        
        self.quit_button = tk.Button(
            master, text="End Game", command=self.end_game,
            bg="#f44336", fg="white", font=("Helvetica", 12), relief="raised", padx=10, pady=5,
        )
        self.quit_button.pack(pady=10, padx=20, fill=tk.X)

    def start_game(self):
        num_players = simpledialog.askinteger("Number of players", "How many players (from 2 to 6)?", minvalue=2, maxvalue=6)
        if num_players is None:
            return
        
        for i in range(num_players):
            player_name = simpledialog.askstring("Player name", f"Enter name of player {i + 1}:")
            if player_name:
                self.players.append(player_name)
        
        self.roll_dice()

    def roll_dice(self):
        if self.player_number < len(self.players):
            player = self.players[self.player_number]
            if messagebox.askyesno("Roll Dice", f"{player}, do you want to roll the dice?"):
                rolled_number = roll_number()
                self.statistics[rolled_number] += 1
                self.num_rolls += 1

                messagebox.showinfo("Roll Result", f"Rolled number for {player}: {rolled_number}")
                self.player_number += 1
                self.roll_dice()
            else:
                self.end_game()
        else:
            self.player_number = 0
            self.roll_dice()

    def end_game(self):
        if messagebox.askyesno("End Game", "Are you sure you want to end the game?"):
            self.master.quit()
            self.show_statistics()

    def show_statistics(self):
        statistics_info = "\nRoll Statistics:\n"
        statistics_info += f"Number of rolls: {self.num_rolls}\n"
        for result, count in self.statistics.items():
            percentage = (count / self.num_rolls * 100) if self.num_rolls > 0 else 0
            statistics_info += f"Number {result}: {count} times ({percentage:.2f}%)\n"
        
        messagebox.showinfo("Statistics", statistics_info)

if __name__ == "__main__":
    root = tk.Tk()
    app = CatanGame(root)
    root.mainloop()
