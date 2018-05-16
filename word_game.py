"""A Mini Scrabble game, where two players are challenged to form words from letters."""
import random
import time


def build_dictionary():
    """
    Uses the "scrabble_words.txt" file to build the dictionary of valid words for the game.
    """
    alphabet = "ABCDEFGHIJKLMNOPQRSXTUVWXYZ"
    for c in alphabet:
        words[c] = set()
    try:
        with open("scrabble_words.txt", "r") as file:
            for line in file:
                if len(line.strip()) <= 10:
                    words[line.strip()[:1]].add(line.strip())
        return True
    except FileNotFoundError:
        print("File \"scrabble_words.txt\" cannot be found.")
        return False


def build_letters():
    """
    Uses the "letter_info.txt" file to build the letter bag for the game and assign point values.
    """
    try:
        with open("letter_info.txt", "r") as file:
            for line in file:
                temp = line.strip().split(" ")
                point_value = int(temp[0])
                for s in temp[1:]:
                    for i in range(int(s[1:])):
                        letter_bag.append(s[:1])
                    letter_values[s[:1]] = point_value
        return True
    except FileNotFoundError:
        print("File \"letter_info.txt\" cannot be found.")
        return False


def get_letters():
    """
    Gets ten random letters from the letter bag and returns them as a list.

    :rtype list
    :returns: ten random letters from letter_bag as a list.
    """
    letters = []
    for i in range(10):
        letters.append(random.choice(letter_bag))
    return letters


def is_valid_word(s, letters):
    """
    Validates the given word with the given letters.

    :param s: the word to be validated
    :type s: str
    :param letters: the possible letters
    :type letters: list
    :rtype: bool
    :returns: True if and only if the given string can be formed using the given letters.
    """
    temp = list(letters)
    if s == "" or s not in words[s[:1]]:
        return False
    for t in s:
        c = t.upper()
        if c not in temp:
            return False
        temp.remove(c)
    return True


def score_word(s):
    """
    Calculates the scrabble score for the given word.

    :param s: the word to be scored
    :type s: str
    :rtype: int
    :return: the scrabble score of the given word as an integer.
    """
    score = 0
    for c in s:
        score += letter_values[c]
    return score


def get_all_words(letters):
    """
    Finds all possible words that can be formed from the given letters.

    :param letters: the letters that can be used to form words
    :type letters: list
    :rtype: list
    :return: a list of all words that can be formed from the given letters.
    """
    all_words = []
    for c in letters:
        for word in words[c]:
            if is_valid_word(word, letters):
                all_words.append(word)
    return all_words


def start_game():
    """
    Executes one round of the game.
    """
    letters = get_letters()
    p1_words = []
    p2_words = []
    print("\nIn this game, you will be shown 10 letters, and you will have 15 seconds to"
          "\nenter as many words as you can that can be formed from those letters.")
    input("\nPlayer 1, when you are ready to begin, press \"Enter\".")
    start_time = time.time()
    while time.time() - start_time < 15:
        print("\nThe letters are:", "".join(letters))
        temp = input("Enter a word: ").upper()
        if is_valid_word(temp, letters) and temp not in p1_words:
            p1_words.append(temp)
    input("\nTime Up. Player 2, when you are ready to begin, press \"Enter\".")
    start_time = time.time()
    while time.time() - start_time < 15:
        print("\nThe letters are:", "".join(letters))
        temp = input("Enter a word: ").upper()
        if is_valid_word(temp, letters) and temp not in p2_words:
            p2_words.append(temp)
    print("\nTime Up.\n")
    p1_score = 0
    p2_score = 0
    for word in p1_words:
        p1_score += score_word(word)
    for word in p2_words:
        p2_score += score_word(word)
    print("***SCORES***")
    print("Player 1: ", p1_score)
    print("Player 2: ", p2_score)
    print("\n***PLAYER 1's WORDS***")
    for word in p1_words:
        print(word)
    print("\n***PLAYER 2's WORDS***")
    for word in p2_words:
        print(word)
    bar = input("\nTo see all possible words from these letters, enter \"A\", otherwise, just press \"Enter\": ")
    if bar.upper() == "A":
        computers_score = 0
        print("\n***ALL POSSIBLE WORDS WITH LETTERS \"{}\"***".format("".join(letters)))
        for word in get_all_words(letters):
            print(word)
            computers_score += score_word(word)
        print("\nThe computer's score was:", computers_score)


def run():
    """
    Runs the program and initializes all dependencies.
    """
    if not build_dictionary():
        return
    if not build_letters():
        return
    print("Welcome to Mini Scrabble.")
    while True:
        foo = input("\nTo start a game, enter \"S\", and to quit, enter \"Q\": ").upper()
        if foo == "Q":
            break
        if foo == "S":
            start_game()
        else:
            print("Invalid input.")
    print("\n***PROGRAM EXITED***")


if __name__ == "__main__":
    words = {}
    letter_bag = []
    letter_values = {}
    run()
