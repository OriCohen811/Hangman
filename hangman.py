def open_screen():
    """print the open screen with welcome, draw, num of mistakes"""
    OPEN_SCREEN = "Welcome to Ori's game!"
    HANGMAN_ASCII_ART = ("""\n
     _    _
    | |  | |
    | |__| | __ _ _ __   __ _ _ __ ___   __ _ _ __
    |  __  |/ _` | '_ \ / _` | '_ ` _ \ / _` | '_  |
    | |  | | (_| | | | | (_| | | | | | | (_| | | | |
    |_|  |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                         __/ |
                        |___/\n""")  # the draw
    print(OPEN_SCREEN, HANGMAN_ASCII_ART, 'Max Mistakes = 6')


def choose_word():
    """Open file with words, choose a word according to index number."""
    import os

    file_path = input('Enter words file: ').strip('"').replace('\\', '/')
    while not os.path.isfile(file_path):
        print('Invalid file path. Try again.')
        file_path = input("Enter words file: ").strip('"').replace('\\', '/')

    index_input = input('Enter word location: ')
    while not index_input.isdigit() or int(index_input) <= 0:
        print('Accept only a positive number!')
        index_input = input('Enter word location: ')
    index = int(index_input)

    with open(file_path, 'r') as f:
        words = f.read().split()

    if not words:
        print("The file is empty.")
        return None

    word = words[(index - 1) % len(words)]
    return word


def guess_letter(old_letters_guessed):
    """if the letter that the player guess new and valid, the letter add to the list-old_letters_guessed
    :if not he return a massage with X and his previous guesses and False
    :len(letter_guessed) != 1 - can input just one character
    :not letter_guessed.isalpha() - the letter is in alphabet and not num or sign
    :letter_guessed in old_letters_guessed - check if the letter new"""
    letterpsser = " -> "
    letter_guessed = input("Guess a letter:")
    letter_guessed = letter_guessed.lower()
    while len(letter_guessed) != 1 or not letter_guessed.isalpha() or (letter_guessed in old_letters_guessed):
        # checked that haven't more than one letter, checked that the letter is in english, if the letter guessed before
        old_letters_guessed.sort()  # sort according a-b-c
        print('X \nError try again', '\nletters guessed', letterpsser.join(old_letters_guessed))
        letter_guessed = input("Guess a letter:")
    if letter_guessed not in old_letters_guessed:  # if the letter is new
        old_letters_guessed.append(letter_guessed)  # add to list of letters
        return letter_guessed


def count_mistakes(letter_list, word):
    """check how many letters not in the secret word and this is the mistakes"""
    mistake = 0  # starting from 0
    for letter in letter_list:  # the letters that guessed
        if letter not in word:  # check every letter
            mistake += 1
    return mistake


def mistakes_draws(num_mistake=0):
    """print the draw for every quantity of mistakes"""
    mistake_0 = ("""x-------x\n""")
    mistake_1 = ("""x-------x
|
|
|
|
|\n""")
    mistake_2 = ("""x-------x
|       |
|       0
|
|
|\n""")
    mistake_3 = ("""x-------x
|       |
|       0
|       |
|
|\n""")
    mistake_4 = ("""x-------x
|       |
|       0
|      /|\\
|
|\n""")
    mistake_5 = ("""x-------x
|       |
|       0
|      /|\\
|      /
|\n""")
    mistake_6 = ("""x-------x
|       |
|       0
|      /|\\
|      / \\
|\n
GAME OVER!!!""")
    draw_to_mistakes = {0: mistake_0, 1:mistake_1, 2: mistake_2, 3: mistake_3, 4: mistake_4, 5: mistake_5, 6: mistake_6}
    return draw_to_mistakes[num_mistake]


def show_hidden_word(secret_word, old_letters_guessed):
    """show the letters that were guessed, if the letter guessed yet - show '_' instead the letter"""
    secret = ' _ '  # letter that not guessed
    show_word = []  # need create list for the letters in secret word and sign
    for letter in secret_word:
        if letter not in old_letters_guessed:  # if the letter not guessed yet
            show_word.extend(secret)  # add '_' instead the letter
        else:
            show_word.extend(letter + ' ')
    show = "".join(show_word)  # make a str from the letter in the list
    return show


def draw_and_hidden_word(draw, word):
    print(draw)  # hangman draw
    print(word)  # word situation


def check_win(hidden_word, secret_word):
    """check if the player win
    :hidden_word = the word situation
    :secret_word = the original word
    :the action on the word is to calibrate the words"""
    hidden_word = hidden_word.replace(' ', '').lower()
    secret_word = secret_word.replace(' ', '').lower()
    hidden_word.lower()
    secret_word.lower()
    if hidden_word == secret_word:
        return True


def main():
    open_screen()
    SECRET_WORD = choose_word()  
    if SECRET_WORD == None :
        print("Problem occurred\n")
        return
    old_letters_guessed = []  
    mistakes = count_mistakes(old_letters_guessed, SECRET_WORD)
    print(mistakes_draws())
    print(show_hidden_word(SECRET_WORD, old_letters_guessed))
    while mistakes < 6:
        guess_letter(old_letters_guessed)
        mistakes = count_mistakes(old_letters_guessed, SECRET_WORD)
        draw = mistakes_draws(mistakes)  
        secret_word_situation = show_hidden_word(SECRET_WORD, old_letters_guessed) 
        if SECRET_WORD == secret_word_situation.replace(" ", ''):
            print(SECRET_WORD)
            print('WINNER!!!!!')
            return
        draw_and_hidden_word(draw, secret_word_situation) 
        print(mistakes)
    if mistakes == 6 :
        print(SECRET_WORD)
        print('\n\nOhh... Such a bad luck :( \nSee you next time!!\n')


if __name__ == "__main__":
    while True: 
        main()
