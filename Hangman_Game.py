import random
from words import word_list

chosen_word = random.choice(word_list)
end_of_game = False
len1 = len(chosen_word)
length = len1

lives = 6

from art import logo
print(logo)

# print(chosen_word)

display = []
for i in range(length):
    display += "_"

while not end_of_game:
    guess = input("Input: ").upper()

    if guess in display:
        print(f"You've already guessed '{guess}'")

    for position in range(length):
        letter = chosen_word[position]
        
        if letter == guess:
            display[position] = letter

    if guess not in chosen_word:
        print(f"You guessed '{guess}', that's not in the word. You lose a life.")

        lives -= 1
        if lives == 0:
            end_of_game = True
            print(f"You lose, the word was '{chosen_word}'")
    print(f"{' '.join(display)}")

    if "_" not in display:
        end_of_game = True
        print(f"You Win, the word was '{chosen_word}'")
    
    from art import stages
    print(stages[lives])  

