import random
from hangman_images import logo
from hangman_images import stages
from hangman_words import word_list

print(logo)
word=random.choice(word_list)
lives=6
game_end=False
display=[]
for i in range(len(word)):
    display+="_"
print(display)
print(stages[lives])
while(not game_end):
    guess=input("Guess a letter: ").lower()
    if guess in display:
        print(f"Already guessed \'{guess}\'. Enter something else")
    for i in range(len(word)):
        if guess==word[i]:
            display[i]=guess
    if guess not in word:
        print(f"Wrong Guess! \'{guess}\' is not in the word. You lost a life.")
        lives-=1
        if lives==0:
            game_end=True
            print(f"You Lose. The word was \'{word}\' Better Luck Next Time.")
    print(f"{' '.join(display)}")
    if '_' not in display:
        game_end=True
        print("You Win! Well Done!")  
    print(stages[lives])