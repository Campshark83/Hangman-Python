import random
#Creates the wordlist the program uses#
def choose_word():
    word_list = ["python", "hangman", "programming", "computer", "algorithm", "decide"]
    return random.choice(word_list)

def display_word(word, guessed_letters):
    display = ""
    for letter in word:
        if letter in guessed_letters:
            display += letter
        else:
            display += "_"
    return display

def hangman():
    word_to_guess = choose_word()
    guessed_letters = []
    attempts = 6
#Start of the game#
    print("Welcome to Hangman!")

    while attempts > 0:
        print("\n" + display_word(word_to_guess, guessed_letters))
        guess = input("Guess a letter: ").lower()

        if len(guess) == 1 and guess.isalpha():
            if guess in guessed_letters:
             #If already guessed, print this#
              print("You've already guessed that letter.")
            elif guess in word_to_guess:
                guessed_letters.append(guess)
                if word_to_guess == display_word(word_to_guess, 
         #If letters are guessed, display the congrats#
                                                 
              guessed_letters):
                    print("Congratulations! You guessed the word:", word_to_guess)
                    break
            else:
                guessed_letters.append(guess)
                attempts -= 1
               #Make sure to monitor attempts#
            print("Incorrect guess. Attempts left:", attempts)
        else:
            print("Please enter a valid letter.")

    if attempts == 0:
      #If run of out attempts, display this#  
      print("Sorry, you've run out of attempts. The word was:", word_to_guess)

if __name__ == "__main__":
    hangman()
