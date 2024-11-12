import random

class Game:
    def __init__(self):
        self.results = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
        self.weights = [2.78, 5.56, 8.33, 11.11, 13.89, 16.67, 13.89, 11.11, 8.33, 5.56, 2.78]
        self.statistics = {i: 0 for i in range(2, 13)}
        self.number_of_throws = 0

    def welcome(self):
        print("Welcome in Catan!")
        print("Press Enter to roll the dice.")
        print("To quit the game, type 'e' and confirm.")

    def roll_dice(self):
        while True:
            continue_game = input("Press Enter to roll the dice: ")
            if continue_game.lower() == 'e':
                confirmation = input("Are you sure you want to quit the game? Type 'e' to confirm: ")
                if confirmation.lower() == 'e':
                    self.display_statistics()
                    break
            else:
                rolled_number = random.choices(self.results, weights=self.weights)[0]
                print(f"Rolled number: {rolled_number}")
                self.statistics[rolled_number] += 1
                self.number_of_throws += 1

    def display_statistics(self):
        print("\nThrowing statistics:")
        print(f"Number of throws: {self.number_of_throws}")
        for result, count in self.statistics.items():
            percentage = (count / self.number_of_throws * 100) if self.number_of_throws > 0 else 0
            print(f"Number {result}: {count} times ({percentage:.2f}%)")
        input("Press Enter to exit...")

if __name__ == "__main__":
    game = Game()
    game.welcome()
    game.roll_dice()