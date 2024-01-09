import random

def load_dictionary(file_path):
    with open(file_path) as f:
        words = [line.strip() for line in f]
        return words

def is_valid_guess(guess, guesses):
    return guess in guesses

def evaluate_guess(guess, word):
    str = ""

    for i in range(5):
        if guess[i] == word[i]:
            str += "\033[32m" + guess[i]
        else:
            if guess[i] in word:
                str += "\033[33m" + guess[i]
            else:
                str += "\033[0m" + guess[i]

    return str + "\033[0m"

def wordle(guesses, answers):
    print("Welcome to Wordle! You Get 6 chances to guess a 5-letter word.")
    secret_word = random.choice(answers)

    attempts = 1
    max_attempts = 6

    while attempts <= max_attempts:
        guess = input("Enter Guess #" + str(attempts) + ": ").lower()
        if not is_valid_guess(guess, guesses):
            print("Invalid guess. Please enter an English word with 5 letters.")
            continue
        if guess == secret_word:
            options = ["Congratulations! You guessed the word", secret_word, "Good Job! You guessed the word", secret_word, "Awesome you did it! You guessed the word", secret_word, "Wonderful! You guessed the word", secret_word,]

            print(random.choice(options))
            break

        attempts += 1
        feedback = evaluate_guess(guess, secret_word)
        print(feedback)

    if attempts > max_attempts:
        print("Game over. The secret word was:", secret_word)


guesses = load_dictionary("guesses.txt")
answers = load_dictionary("answers.txt")

wordle(guesses, answers)