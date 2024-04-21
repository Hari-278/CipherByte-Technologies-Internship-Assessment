# MASTERMIND GAME
# Two players play the game against each other; let's assume Player 1 and Player 2.
# •
# Player 1 plays first by setting a multi-digit number.
# Player 2 now tries his first attempt at guessing the number.
# • If Player 2 succeeds in his first attempt (despite odds which are highly unlikely) he
# wins the game and is crowned Mastermind! If not, then Player 1 hints by revealing which digits or numbers Player 2 got correct.
# • The game continues till Player 2 eventually is able to guess the number entirely.
# •
# Now, Player 2 gets to set the number and Player 1 plays the part of guessing the number.
# • If Player 1 is able to guess the number within a lesser number of tries than Player 2 took, then Player 1 wins the game and is crowned Mastermind.
# • If not, then Player 2 wins the game.



import random

def generate_secret_number():
    return str(random.randint(1000, 9999))

def get_guess():
    while True:
        guess = input("Enter your guess (4-digit number): ")
        if len(guess) != 4 or not guess.isdigit():
            print("Invalid input! Please enter a 4-digit number.")
        else:
            return guess

def evaluate_guess(secret_number, guess):
    correct_digits = sum(1 for i in range(4) if secret_number[i] == guess[i])
    return correct_digits

def play_mastermind():
    print("Welcome to the Mastermind game!")

    # Player 1 sets the secret number
    secret_number_p1 = generate_secret_number()
    print("Player 1 has set the secret number.")

    # Player 2 guesses the number
    attempts_p2 = 0
    while True:
        guess_p2 = get_guess()
        attempts_p2 += 1
        correct_digits = evaluate_guess(secret_number_p1, guess_p2)
        print(f"Player 2 got {correct_digits} correct digit(s).")

        if correct_digits == 4:
            print("Congratulations! Player 2 is the Mastermind!")
            break

    # Player 2 sets the secret number
    secret_number_p2 = generate_secret_number()
    print("Player 2 has set the secret number.")

    # Player 1 guesses the number
    attempts_p1 = 0
    while True:
        guess_p1 = get_guess()
        attempts_p1 += 1
        correct_digits = evaluate_guess(secret_number_p2, guess_p1)
        print(f"Player 1 got {correct_digits} correct digit(s).")

        if correct_digits == 4:
            print("Congratulations! Player 1 is the Mastermind!")
            break

    # Determine the winner
    if attempts_p1 < attempts_p2:
        print("Player 1 is the overall winner!")
    elif attempts_p1 > attempts_p2:
        print("Player 2 is the overall winner!")
    else:
        print("It's a tie!")

if __name__ == "__main__":
    play_mastermind()
