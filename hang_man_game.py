from words import word_list
import random


def main():
    print(f"Let's play Hangman Game")
    print(f"You have to guess letters for given word and you only have 6 lifes :")
    choosed_word = random.choice(word_list)
    
    display=[]
    live=0
    print(choosed_word)
    for i in range(len(choosed_word)):# for letter in choosed_word: display+='_'
        display += '_'
    print(display)
    
    game_over = False
    while not game_over:

        guess_letter = input(f"Guess a letter : ").upper()

        for position in range(len(choosed_word)):
            letter=choosed_word[position]

            if letter.upper()==guess_letter:
                display[position]=guess_letter
        
        if guess_letter not in choosed_word.upper():
            live +=1
            if live == 6:
                game_over = True
                print("You lost")
        print(live)
        
        if '_' not in display:
            game_over = True
            print("You win")

        print(display)
        wrong_guess(live)
                



def wrong_guess(wrong_letter):
    if(wrong_letter==0):
        print("_ _ _ _ _")
        print("|       |")
        print("|        ")
        print("|        ")
        print("|        ")
        print("|        ")
        print("_ _ _ _ _")
    if(wrong_letter==1):
        print("_ _ _ _ _")
        print("|       |")
        print("|       O")
        print("|        ")
        print("|        ")
        print("|        ")
        print("_ _ _ _ _")
    if(wrong_letter==2):
        print("_ _ _ _ _")
        print("|       |")
        print("|       O")
        print("|       |")
        print("|        ")
        print("|        ")
        print("_ _ _ _ _")
    if(wrong_letter==3):
        print("_ _ _ _ _")
        print("|       |")
        print("|       O")
        print("|      /|")
        print("|        ")
        print("|        ")
        print("_ _ _ _ _")
    if(wrong_letter==4):
        print("_ _ _ _ _")
        print("|       |")
        print("|       O")
        print("|      /|\\")
        print("|        ")
        print("|        ")
        print("_ _ _ _ _")
    if(wrong_letter==5):
        print("_ _ _ _ _")
        print("|       |")
        print("|       O")
        print("|      /|\\")
        print("|      / ")
        print("|        ")
        print("_ _ _ _ _")
    if(wrong_letter==6):
        print("_ _ _ _ _")
        print("|       |")
        print("|       O")
        print("|      /|\\")
        print("|      / \\")
        print("|        ")
        print("_ _ _ _ _")
    

if __name__=='__main__':
    main()