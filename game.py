import random

# Constants for the game
ROWS = 3
COLS = 3
MAX_LINES = 3
MAX_DEPOSIT = 100

# Mapping of symbols to their corresponding values
key_value = {
    "A": 18,
    "B": 12,
    "C": 9,
    "D": 7,
    "E": 5,
}

# Mapping of symbols to their count
key_count = {
    "A": 5,
    "B": 10,
    "C": 15,
    "D": 20,
    "E": 25,
}

# Function to start the game
def main():
    balance = get_deposit()
    while True:
        balance += spin(balance)
        print(f"Balance is: {balance}")
        if balance <= 0:
            break
        if play_check() == False:
            break
    print(f"Your ending balance was {balance}")

# Function to check if user wants to continue playing
def play_check():
    while True:
        try:
            check = input("Would you like to play again? (q to quit): ").lower()

            if check == "q":
                return False
            if check in ["y", "yea"]:
                return True
            else:
                raise ValueError
        except ValueError:
            print("Try input again")

# Function to simulate a spin and calculate winnings
def spin(balance):
    lines = get_lines()
    while True:
        bet = get_bet()
        total_bet = bet * lines
        if total_bet > balance:
            print("You don't have enough money for that bet!")
        else:
            break
    print(f"Your current bet is {bet} and the number of lines you've chosen is {lines}")

    columns = get_spin(key_count, ROWS, COLS)
    print_spin(columns)
    winnings = check_winnings(key_value, bet, columns, lines)
    # Returns winnings - total_bet
    return winnings - total_bet

# Function to simulate spinning the reels and generating columns
def get_spin(key_count, rows, cols):
    keys = []
    for key, count in key_count.items():
        for _ in range(count):
            keys.append(key)
    columns = []
    for _ in range(rows):
        cycle = keys[:]
        column = []
        for _ in range(cols):
            value = random.choice(cycle)
            column.append(value)
            cycle.remove(value)
        columns.append(column)

    return columns

# Function to print the spin result
def print_spin(columns):
    for row in range(len(columns)):
        for i, column in enumerate(columns):
            if i != len(column) - 1:
                print(column[row], end=" | ")
            else:
                print(column[row], end="")
        print()

# Function to get the number of lines the player wants to bet on
def get_lines():
    while True:
        try:
            lines = int(input("How many lines would you like to bet on? (1-3): "))
            if 1 <= lines <= 3:
                break
            else:
                print("Please insert a number between 1 and 3")
        except ValueError:
            print("Please insert a number! (# format)")
    return lines

# Function to check and calculate winnings
def check_winnings(key_value, bet, columns, lines):
    winnings = 0
    winnings_list = []
    for line in range(MAX_LINES):
        symbol = columns[0][line]
        for column in columns:
            if column[line] != symbol:
                break
        else:
            winnings = bet * key_value[symbol]
            winnings_list.append(winnings)

    winnings_list = sorted(winnings_list, reverse=True)
    if winnings_list:
        match len(winnings_list):
            case 1:
                return winnings_list[0]
            case 2:
                return winnings_list[0] + winnings_list[1]
            case 3:
                return winnings_list[0] + winnings_list[1] + winnings_list[2]
    return 0

# Function to get the player's bet amount
def get_bet():
    while True:
        try:
            amount = int(input("Place a bet: "))
            if amount > 0:
                break
            else:
                print("Please insert a number greater than 0")
        except ValueError:
            print("Please insert a number! (#### format)")
    return amount

# Function to get the player's initial deposit amount
def get_deposit():
    while True:
        try:
            amount = int(input("What would you like to deposit?: "))
            if 0 <= amount <= MAX_DEPOSIT:
                break
            else:
                print("Please insert a number greater than 0 and less than 100")
        except ValueError:
            print("Please insert a number! (#### format)")

    return amount

if __name__ == "__main__":
    main()
