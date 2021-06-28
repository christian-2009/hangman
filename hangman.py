def check_word(letter, letters_guessed):
    while letter in letters_guessed or letter.isalpha() == False:
        letter = input("not valid. Pick another letter/word ")

def hangman(word):
    lng = ""
    for i in range(len(word)):
        lng += "_"
    print("you have to guess from " + lng + " letters")
    lives = 0
    letters_guessed = []
    nu_correct = 0
    # 10 is the number of lives in hangman game
    while lives <= 10:
        if lng == word:
            print("well done you guessed the word")
            break

        # we allow user to choose a letter/word. Then proceed to check whether this is valid given the letters guessed list
        letter = input('choose what letter you want to guess: ')
        check_word(letter,letters_guessed)
        letters_guessed.append(letter)

        #using a loop to check whether this letter corresponds to any letters in the word
        a = 0
        for i in range(0, len(word)):
            if (len(letter) == 1) and (word[i] == str(letter)):
                lng = lng[:i] + letter + lng[i + 1:]
                a += 1
            elif len(letter) > 1 and letter != word:
                print("Game over. You lose!")
                break
            elif len(letter) > 1 and letter == word:
                print('You guessed the correct word.')
                break
            else:
                continue

        #need to check whether any letters corresponded to a letter in word
        if a == 0:
            lives +=1
            print("You guessed incorrectly. One life gone")
        else:
            print("Well done you guessed a correct letter")
        print(lng)
    print("out of lives")
    return word

hangman('word')













