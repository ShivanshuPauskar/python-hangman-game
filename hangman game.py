import random

def display_hangman(turns_left):
    stages = [
        """
           ------
           |    |
           |    O
           |   /|\\
           |   / \\
           |
        """,
        """
           ------
           |    |
           |    O
           |   /|\\
           |   / 
           |
        """,
        """
           ------
           |    |
           |    O
           |   /|\\
           |   
           |
        """,
        """
           ------
           |    |
           |    O
           |   /|
           |   
           |
        """,
        """
           ------
           |    |
           |    O
           |    |
           |   
           |
        """,
        """
           ------
           |    |
           |    O
           |    
           |   
           |
        """,
        """
           ------
           |    |
           |    
           |    
           |   
           |
        """,
                """
           ------
           |    
           |    
           |    
           |   
           |
        """
    ]
    index = 7 - turns_left
    index = min(index, len(stages)-1)
    print(stages[index])

def main():
    print("🎮 THE HANGMAN GAME")
    print("INSTRUCTIONS:")
    print("1. You get 7 guesses.")
    print("2. You can only guess alphabets.\n")

    word_list = ['rainbow', 'computer', 'science', 'programming', 'python',
                 'mathematics', 'alphabets', 'player', 'condition',
                 'reverse', 'water', 'board', 'laptop', 'hangman', 'fool']
    word = random.choice(word_list)
    word_display = ["-" for _ in word]
    guessed_letters = []
    turns = 7

    print("Your word is:")
    print(" ".join(word_display))

    while turns > 0 and "-" in word_display:
        guess = input("Enter your guess: ").lower()

        if not guess.isalpha() or len(guess) != 1:
            print("❗ INVALID INPUT. Please enter a single alphabet letter.\n")
            continue

        if guess in guessed_letters:
            print("⚠️ You already guessed that letter!\n")
            continue

        guessed_letters.append(guess)

        if guess in word:
            print("✅ Good guess!")
            for idx, letter in enumerate(word):
                if letter == guess:
                    word_display[idx] = guess
        else:
            turns -= 1
            print(f"❌ Wrong guess. {turns} turns left.")
            display_hangman(turns)

        print("Current word:", " ".join(word_display), "\n")

    if "-" not in word_display:
        print("🎉 YOU WIN! The word was:", word)
    else:
        print("💀 YOU LOSE! The word was:", word)

if __name__ == "__main__":
    main()
