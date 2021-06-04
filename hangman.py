#we enter in a word. for each letter

def hangman(x):
    a = 0
    b = 0
    c = 0
    print('The word is ' + str(len(x)) + ' letters long')
    while a <= 10:
        if b == len(x):
            break
        c == b
        letter = input('choose what letter you want to guess: ')
        for i in range(0,len(x)):
            if x[i] == str(letter):
                b += 1
                print('correct!')
        if c == b:
            a += 1
            print('got it wrong')
    if a > 10:
        print('Out of lives. You lose')
    else:
        print('well done you guessed the word ' + x)

hangman('hello')

