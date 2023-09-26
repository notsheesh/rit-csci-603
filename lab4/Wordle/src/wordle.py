import sys
import random
import os
from dataclasses import dataclass
import re

CORRECT_INDEX = '^'
IS_EXIST = '*'
NOT_EXIST = '#'

@dataclass
class WordList:
    storage: list
    length: int

    def add_new_word(self, new_word):
        self.storage.append(new_word)
        self.length += 1

    def mark_word_done(self, word):
        self.storage.remove(word)
        self.length -= 1

    def to_string(self):
        print("Storage: {}".format(self.storage))
        print("Length: {}".format(self.length))


@dataclass
class SecretWord:
    string_value: str
    word_map: dict

    def to_string(self):
        print("Value: {}".format(self.string_value))
        print("Map: {}".format(self.word_map))

    def make_word_map(self):
        self.word_map = {}
        for char in self.string_value:
            self.word_map[char] = self.word_map.get(char, 0) + 1

    def is_letter_exist(self, letter):
        return letter in self.string_value

    def mark_letter_used(self, letter: str):
        if self.word_map[letter] > 0:
            self.word_map[letter] -= 1

    def set_value(self, string_value):
        self.string_value = string_value
        self.make_word_map()
    
@dataclass
class UserAttempts:
    letter_dict: dict
    num_attempt: int
    word_dict: dict
    
    def add_letter(self, letter):
        self.letter_dict.update({letter})
    
    def add_word_hint_pair(self, word, hint):
        self.word_dict.update({word, hint})
        for letter in word: 
            self.add_letter(letter)
    
    def print_attempts(self):
        print("Num of guesses: {} of 6".format(self.num_attempt))
        for word in self.word_dict.keys():
            print(word)
            print(self.word_dict[word])
            print("Letters used: {}".format(self.letter_dict))

def load_word_list(file_name: str) -> list:
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

# select a random word from a given word list
def select_word(word_list: WordList) -> str:
    # word_list.to_string()
    if word_list.length != 0:
        random_index = random.randint(0, word_list.length-1)
        random_word = word_list.storage[random_index]
        return random_word
    else:
        print("Dictionary empty, no words found")
        return ""

def show_commands():
    print("Commands:")
    print("\tnew: Start a new game")
    print("\tguess <word>: Make a guess")
    print("\tcheat: Show the secret word")
    print("\thelp: This help message")
    print("\tquit: End the program")

# If no console input is provided 
def default_setup():
    loaded_list = load_word_list("wordle-dev.txt")
    word_list = WordList(loaded_list, len(loaded_list))
    secret_word = SecretWord("", {})
    secret_word.set_value(select_word(word_list))
    return (secret_word, word_list)

# start new game if new command is provided
def new_game(secret_word: SecretWord, word_list: WordList) -> tuple:
    word_list.mark_word_done(secret_word.string_value)
    selected_word = select_word(word_list)
    secret_word.set_value(selected_word)
    user_attempt = UserAttempts({}, 0, {})
    return (secret_word, word_list, user_attempt)

# 
def evaluate_guess(
    guess_word: str,
    secret_word: SecretWord,
    user_attempt: UserAttempts) -> None: 
    hint = []
    for i, guess_letter in enumerate(guess_word):
        if guess_letter == list(secret_word.string_value)[i]:
            hint.append(CORRECT_INDEX)
            secret_word.word_map[guess_letter] -= 1
        elif guess_letter in list(secret_word.string_value):
            hint.append(IS_EXIST)
            secret_word.word_map[guess_letter] -= 1
        else:
            hint.append(NOT_EXIST)
    user_attempt.num_attempt += 1
    user_attempt.add_word_hint_pair(guess_word, "".join(hint))
    return (user_attempt)

def is_valid_user_input(user_input: str) -> bool:
    legal_commands = [
        r'new', r'guess [A-Z]{5}', r'cheat', r'help', r'quit', r'secret'
    ]
    for command in legal_commands:
        if re.fullmatch(command, user_input):
            return True
    return False

def play_game(secret_word, word_list):
    user_attempt = UserAttempts({}, 0, {})
    while True:
        user_input = input("> ")
        if user_input == "debug":
            print(user_attempt)
            print(secret_word)
            print(word_list)
            continue
        if is_valid_user_input(user_input):
            if re.fullmatch(r'new', user_input):
                (secret_word,
                 word_list,
                user_attempt) = new_game(secret_word, word_list)

            if re.fullmatch(r'guess .{5}', user_input):
                user_input = user_input.upper()
                if re.fullmatch(r'guess [a-zA-Z]{5}', user_input):
                    guess_word = user_input.split()[-1]
                    user_attempt = evaluate_guess(
                        guess_word, secret_word.string_value, user_attempt)
                    user_attempt.print_attempts()
                else:
                    print("Illegal word.")

            if re.fullmatch(r'quit', user_input):
                return 
            
            if re.fullmatch(r'secret', user_input):
                print("Secret Word: {}".format(secret_word.string_value))
        else: 
            print("Invalid command!")

def parse_console_input(console_input: str):
    dev_secret_word = console_input.upper()
    secret_word = SecretWord("", {})
    secret_word.set_value(dev_secret_word)
    word_list = WordList([], 0)

def init_game(secret_word: SecretWord, word_list: WordList) -> None:
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
