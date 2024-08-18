import random


def display_word(history, word):
    display_letters = []
    for letter in word:
        if letter in history:
            display_letters.append(letter)
        else:
            display_letters.append("_")

    return " ".join(display_letters)


def get_user_input(history):
    user_letter = input("guess a letter: ")
    if len(user_letter) > 1:
        print("you can use only one letter")
        return
    # checking that the same letter wasnt used twice
    if user_letter in history:
        print("you used this letter")
        return
    # else:
    history.append(user_letter)

    return user_letter


def play_game(word, body_parts):
    history = []
    gallows = []
    i = 0  # failed guesses count starts

    while True:
        answered_word = display_word(history, word)
        print(answered_word)
        
        user_letter = get_user_input(history)
        if user_letter is None:
            continue

        if user_letter in word:
            answered_word = display_word(history, word)
            if not "_" in answered_word:
                print("you win")
                break

        else:
            if i == len(body_parts):
                print("game over")
                break
            gallows.append(body_parts[i])
            i += 1
            print(" ".join(gallows))



body_parts = ["head", "body", "left arm", "right arm", "left leg", "right leg"]
wordslist = ['correction', 'childish', 'beach', 'python', 'assertive', 'interference', 'complete', 'share', 'credit card', 'rush', 'south']
word = random.choice(wordslist) 

play_game(word, body_parts)
