def check_word(letter, letters_guessed):
    while letter in letters_guessed or letter.isalpha() == False:
        letter = input("Not valid. Pick another letter/word: ")

def hangman(word):
    lng = ""
    for i in range(len(word)):
        lng += "_"
    print("You have to guess from " + lng + " letters.")
    lives = 0
    letters_guessed = []

    # 10 is the number of lives in hangman game
    while lives <= 10:
        if lng == word:
            print("Well done you guessed the word.")
            break

        # we allow user to choose a letter/word. Then proceed to check whether this is valid given the letters guessed list
        letter = input('Choose what letter you want to guess: ')
        check_word(letter,letters_guessed)
        letters_guessed.append(letter)

        #using a loop to check whether this letter corresponds to any letters in the word
        a = 0
        for i in range(0, len(word)):
            if (len(letter) == 1) and (word[i] == str(letter)):
                lng = lng[:i] + letter + lng[i + 1:]
                a += 1
            elif len(letter) > 1 and letter != word:
                print("You guessed the wrong word.")
                lives = 11
                a -= 1
                break
            elif len(letter) > 1 and letter == word:
                lng = word
                a -= 1
                break
            else:
                continue

        #need to check whether any letters corresponded to a letter in word
        if a == 0:
            lives +=1
            print("You guessed incorrectly. One life gone.")
        elif a > 0:
            print("Well done you guessed a correct letter. Now guess from " + lng + ".")
        else:
            continue

    if lives > 10:
        print("Game over. You lose!")
    return word

hangman("happy")














