import random

def roll_dice():
    
    outcomes = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
    weights = [2.78, 5.56, 8.33, 11.11, 13.89, 16.67, 13.89, 11.11, 8.33, 5.56, 2.78]
    return random.choices(outcomes, weights=weights)[0]

def display_stats(stats, num_rolls):
    print("=" * 40)
    print(" " * 12 + "Roll Statistics")
    print("=" * 40)
    print(f"Number of rolls: {num_rolls}\n")

    for outcome, count in sorted(stats.items()):
        percentage = (count / num_rolls * 100) if num_rolls > 0 else 0
        print(f"Outcome {outcome}: {count} times ({percentage:.2f}%)")

    print("=" * 40)
    input("Press Enter to exit...")

def play_game():
    print("=" * 40)
    print(" " * 12 + "Welcome in Catan!")
    print("=" * 40)

    while True:
        num_players = 0

        
        while True:
            try:
                num_players = int(input("How many players (2-6)? "))
                if 2 <= num_players <= 6:
                    break
                else:
                    print("Please enter a number between 2 and 6.")
            except ValueError:
                print("Invalid input! Please enter a number.")

        
        players = []
        for i in range(num_players):
            player_name = input(f"Enter name for player {i + 1}: ")
            players.append(player_name)

        
        stats = {i: 0 for i in range(2, 13)}  
        num_rolls = 0

        
        while True:
            for player in players:
                continue_game = input(f"{player}, press Enter to roll, or write 'e' and press Enter to exit: ")

                if continue_game.lower() == 'e':
                    confirmation = input("Are you sure you want to quit? Write 'e' and press Enter to confirm: ")
                    if confirmation.lower() == 'e':
                        display_stats(stats, num_rolls)
                        return  

                
                rolled_number = roll_dice()
                print(f"Rolled number for {player}: {rolled_number}\n")

                
                num_rolls += 1
                stats[rolled_number] += 1

if __name__ == "__main__":
    play_game()
