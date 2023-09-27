import sys
import random
import os
from dataclasses import dataclass
import re

DEV_MODE = False

@dataclass
class WordList:
    """
    A data class to represent a list of words and its length.

    :param storage: A list of words.
    :param length: The length of the list.
    """
    storage: list
    length: int

    def add_new_word(self, new_word):
        """
        Add a new word to the word list and update the length.

        :param new_word: The new word to add.
        """
        self.storage.append(new_word)
        self.length += 1

    def mark_word_done(self, word):
        """
        Remove a word from the word list and update the length.

        :param word: The word to remove.
        """
        self.storage.remove(word)
        self.length -= 1

    def to_string(self):
        """
        Print the storage and length of the word list.
        """
        print("Storage: {}".format(self.storage))
        print("Length: {}".format(self.length))


@dataclass
class SecretWord:
    """
    A data class to represent a secret word and its letter map.

    :param string_value: The secret word as a string.
    :param word_map: A dictionary mapping letters to their counts in the word.
    """
    string_value: str
    word_map: dict

    def to_string(self):
        """
        Print the value and word map of the secret word.
        """
        print("Value: {}".format(self.string_value))
        print("Map: {}".format(self.word_map))

    def make_word_map(self):
        """
        Create a word map by counting the frequency of each letter in the word.
        """
        self.word_map = {}
        for char in self.string_value:
            self.word_map[char] = self.word_map.get(char, 0) + 1

    def is_letter_exist(self, letter):
        """
        Check if a letter exists in the word map and is not used up.

        :param letter: The letter to check.
        :return: True if the letter exists and is not used up, False otherwise.
        """
        return letter in self.word_map and self.word_map[letter] != 0

    def mark_letter_used(self, letter: str):
        """
        Mark a letter as used in the word map.

        :param letter: The letter to mark as used.
        """
        if self.word_map[letter] > 0:
            self.word_map[letter] -= 1

    def set_value(self, string_value):
        """
        Set the value of the secret word and create its word map.

        :param string_value: The new value for the secret word.
        """
        self.string_value = string_value
        self.make_word_map()


@dataclass
class UserAttempts:
    """
    A data class to represent user attempts in the Wordle game.

    :param letters_used: A set of letters used in guesses.
    :param word_dict: A dictionary mapping guessed words to their hints.
    :param num_attempt: The number of guess attempts.
    """
    letters_used: tuple
    word_dict: dict
    num_attempt: int

    def update(self, word, hint):
        """
        Update the user's attempts with a new guessed word and its hint.

        :param word: The guessed word.
        :param hint: The hint for the guessed word.
        """
        self.word_dict[word] = hint
        self.letters_used = self.letters_used | set(word)

    def print_attempts(self):
        """
        Print the user's attempts, number of guesses, and letters used.
        """
        print("Num of guesses: {} of 6".format(self.num_attempt))
        for word in self.word_dict:
            print(word)
            print(self.word_dict[word])
        print("Letters used: {}\n".format(self.letters_used))


def load_word_list(file_name: str) -> list:
    """
    Load a list of words from a file.

    :param file_name: The name of the file to load words from.
    :return: A list of words read from the file.
    """
    word_list = []
    path = "../data"
    file_path = os.path.join(path, file_name)
    try:
        file = open(file_path, "r")
        for line in file:
            word_list.append(line[:-1])
        return word_list
    except:
        print("File not found")
    return []

def select_word(word_list: WordList) -> str:
    """
    Select a random word from a word list.

    :param word_list: The list of words to choose from.
    :return: A randomly selected word.
    """
    if word_list.length != 0:
        random_index = random.randint(0, word_list.length-1)
        random_word = word_list.storage[random_index]
        return random_word
    else:
        print("Dictionary empty, no words found")
        print("Terminating game...")
        exit(0)
        return ""

def show_commands() -> None:
    """
    Print the available game commands.
    """
    print("Commands:")
    print("\tnew: Start a new game")
    print("\tguess <word>: Make a guess")
    print("\tcheat: Show the secret word")
    print("\thelp: This help message")
    print("\tquit: End the program")

def default_setup() -> tuple:
    """
    Set up the Wordle game with default word list and a secret word.

    :return: A tuple containing the secret word, word list, and user attempts.
    """
    dev_file_name = "wordle-dev.txt"
    prod_file_name = "wordle.txt"
    file_name = prod_file_name
    loaded_list = load_word_list(file_name)
    word_list = WordList(loaded_list, len(loaded_list))
    secret_word = SecretWord("", {})
    secret_word.set_value(select_word(word_list))
    return (secret_word, word_list)

def new_game(secret_word: SecretWord, word_list: WordList) -> tuple:
    """
    Start a new game by selecting a new secret word from the word list.

    :param secret_word: The secret word object.
    :param word_list: The word list object.
    :return: A tuple containing the updated secret word, word list, and user attempts.
    """
    if secret_word.string_value in word_list.storage:
        word_list.mark_word_done(secret_word.string_value)
    else:
        print("Please restart the  game in production mode.")
        print("Reason: ", end='')

    selected_word = select_word(word_list)
    secret_word.set_value(selected_word)
    user_attempt = UserAttempts(set(), dict(), 0)
    return (secret_word, word_list, user_attempt)


def check_inplace_match(
    guess_word: str, 
    secret_word: SecretWord, 
    hint_arr: list) -> tuple:
    """
    Check for letters in the guessed word that match the secret word in place.

    :param guess_word: The guessed word.
    :param secret_word: The secret word object.
    :param hint_arr: The hint array to update.
    :return: A tuple containing the updated secret word and hint array.
    """

    for i, guess_letter in enumerate(guess_word):
        if guess_letter == list(secret_word.string_value)[i]:
            hint_arr.append('^')
            secret_word.mark_letter_used(guess_letter)
            if DEV_MODE:
                print("[DEV_MODE] Word Map: {}".format(secret_word.word_map))
                print("[DEV_MODE] Hint: {}".format(hint_arr))
        else:
            hint_arr.append('_')
    return (secret_word, hint_arr)


def check_outplace_match(
    guess_word: str, 
    secret_word: SecretWord, 
    hint_arr: list) -> tuple:
    """
    Check for letters in the guessed word that match the secret word but are out
    of place.

    :param guess_word: The guessed word.
    :param secret_word: The secret word object.
    :param hint_arr: The hint array to update.
    :return: A tuple containing the updated secret word and hint array.
    """
    
    for i, guess_letter in enumerate(guess_word):
        if hint_arr[i] == '_':
            if secret_word.is_letter_exist(guess_letter):
                hint_arr[i] = ('*')
                secret_word.mark_letter_used(guess_letter)
                if DEV_MODE:
                    print("[DEV_MODE] Word Map: {}".format(
                        secret_word.word_map))
                    print("[DEV_MODE] Hint: {}".format(hint_arr))
            else:
                hint_arr[i] = (' ')
                if DEV_MODE:
                    print("[DEV_MODE] Word Map: {}".format(
                        secret_word.word_map))
                    print("[DEV_MODE] Hint: {}".format(hint_arr))
    return (secret_word, hint_arr)


def evaluate_attempt(
        guess_word: str,
        secret_word: SecretWord,
        user_attempt: UserAttempts) -> None:
    """
    Evaluate a user's guess attempt and update user attempts.

    :param guess_word: The guessed word.
    :param secret_word: The secret word object.
    :param user_attempt: The user attempts object.
    :return: A tuple containing the updated user attempts.
    """
    hint_arr = []
    secret_word, hint_arr = check_inplace_match(
        guess_word, secret_word, hint_arr)

    secret_word, hint_arr = check_outplace_match(
        guess_word, secret_word, hint_arr)

    if DEV_MODE:
        print("[DEV_MODE] Word Map: {}".format(secret_word.word_map))
    secret_word.make_word_map()
    user_attempt.num_attempt += 1
    hint = "".join(hint_arr)
    user_attempt.update(guess_word, hint)
    user_attempt.print_attempts()
    return (user_attempt)


def is_valid_user_input(user_input: str) -> bool:
    """
    Check if a user input string is a valid command.

    :param user_input: The user input string.
    :return: True if the input is a valid command, False otherwise.
    """
    legal_commands = [
        r'new', r'guess\s*.*', r'cheat', r'help', r'quit'
    ]
    for command in legal_commands:
        if re.fullmatch(command, user_input):
            return True
    return False


def play_game(secret_word, word_list):
    """
    Play the Wordle game with user input and logic.

    :param secret_word: The secret word object.
    :param word_list: The word list object.
    """
    user_attempt = UserAttempts(set(), dict(), 0)
    while True:
        if user_attempt.num_attempt < 6:
            user_input = input("> ")
            if user_input == "debug":
                print(user_attempt)
                print(secret_word)
                temp = word_list.storage 
                word_list.storage = temp[0:5] + ['...']
                print(word_list)
                word_list.storage = temp
                continue

            if is_valid_user_input(user_input):
                if re.fullmatch(r'new', user_input):
                    (secret_word,
                     word_list,
                     user_attempt) = new_game(secret_word, word_list)

                if re.match(r'guess', user_input):
                    if re.fullmatch(r'guess\s*', user_input):
                        print("Invalid command!")

                    elif re.fullmatch(r'guess [a-zA-Z]{5}', user_input):
                        guess_word = user_input.upper().split()[-1]
                        user_attempt = evaluate_attempt(
                            guess_word, secret_word, user_attempt)

                        if DEV_MODE:
                            print("[DEV_MODE] Guess Word: {}".format(
                                guess_word))

                            print("[DEV_MODE] Secret Word: {}".format(
                                secret_word.string_value))

                        if guess_word == secret_word.string_value:
                            print("You won!\n")
                            (secret_word,
                             word_list,
                             user_attempt) = new_game(secret_word, word_list)

                    else:
                        print("Illegal word.")

                if re.fullmatch(r'quit', user_input):
                    print("Bye! ")
                    return

                if re.fullmatch(r'cheat', user_input):
                    print("Secret Word: {}".format(secret_word.string_value))

                if re.fullmatch(r'help', user_input):
                    show_commands()

            else:
                print("Unknown command: {}".format(user_input))
                show_commands()
        else:
            print("You lost!")
            print("The word was {}\n".format(secret_word.string_value))
            (secret_word,
             word_list,
             user_attempt) = new_game(secret_word, word_list)


def parse_console_input(console_input: str):
    """
    Parse console input to set up the Wordle game.

    :param console_input: The console input string.
    :return: A tuple containing the secret word and word list objects.
    """
    dev_secret_word = console_input.upper()
    secret_word = SecretWord("", {})
    secret_word.set_value(dev_secret_word)
    word_list = WordList([], 0)
    return (secret_word, word_list)


def init_game(secret_word: SecretWord, word_list: WordList) -> None:
    """
    Initialize the Wordle game by printing the welcome message and starting the 
    game loop.

    :param secret_word: The secret word object.
    :param word_list: The word list object.
    """
    print("Welcome to Wordle App!")
    show_commands()
    play_game(secret_word, word_list)


def main():
    if len(sys.argv) > 2:
        print("Usage: wordle [1st-secret-word]")
        return
    elif len(sys.argv) == 2:
        (secret_word, word_list) = parse_console_input(sys.argv[1])
    else:
        (secret_word, word_list) = default_setup()

    init_game(secret_word, word_list)

if __name__ == '__main__':
    main()
