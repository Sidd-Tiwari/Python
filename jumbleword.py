import random

# List of words to choose from
words = ["python", "java", "javascript", "ruby", "csharp", "php"]

def choose_word():
    return random.choice(words)

def jumble_word(word):
    jumbled = list(word)
    random.shuffle(jumbled)
    return ''.join(jumbled)

def play_game():
    word_to_guess = choose_word()
    jumbled_word = jumble_word(word_to_guess)
    
    print("Welcome to the Jumbled Word Game!")
    print("Here is your jumbled word:", jumbled_word)
    
    attempts = 3
    while attempts > 0:
        guess = input("\nYour guess: ").lower()
        
        if guess == word_to_guess:
            print("Congratulations! You guessed the word correctly.")
            break
        else:
            attempts -= 1
            if attempts > 0:
                print(f"Wrong guess! You have {attempts} attempts left.")
            else:
                print("Sorry, you're out of attempts. The correct word was:", word_to_guess)
                break

if __name__ == "__main__":
    play_game()
