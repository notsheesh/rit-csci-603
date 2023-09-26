# Constants for brute evaluation
CORRECT_INDEX = '^'
IS_EXIST = '*'
NOT_EXIST = '#'
NUM_LETTERS = 5

def brute_evaluate(guess: str, secret: str) -> str:
    global CORRECT_INDEX, IS_EXIST, NOT_EXIST, NUM_LETTERS

    hint_arr = ['_' for _ in range(NUM_LETTERS)]
    guess_arr = list(guess)
    secret_arr = list(secret)

    for i in range(NUM_LETTERS):
        if hint_arr[i] != '_':
            if guess_arr[i] in secret_arr:
                if guess_arr[i] == secret_arr[i]:
                    hint_arr[i] = CORRECT_INDEX
                    secret_arr[i] = None  # To avoid redundancy
                else:
                    hint_arr[i] = IS_EXIST
                    index_used = secret_arr.index(guess_arr[i])
                    secret_arr[index_used] = None
            else:
                hint_arr[i] = NOT_EXIST

    return ''.join(hint_arr)