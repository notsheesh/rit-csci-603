"""
CSCI-603 Lab 2: Ciphers

A program that encodes/decodes a message by applying a set of transformation operations.
The transformation operations are:
    shift - Sa[,n] changes letter at index a by moving it n letters fwd in the alphabet. A negative
        value for n shifts the letter backward in the alphabet.
    rotate - R[n] rotates the string n positions to the right. A negative value for n rotates the string
        to the left.
    duplicate - Da[,n] follows character at index a with n copies of itself.
    trade - Ta,b swap the places of the a-th and b-th characters.
    affine - Aa,b applies the affine cipher algorithm y = (ax + b) mod 26 using a and b as keys.

All indices numbers (the subscript parameters) are 0-based.

author: Shreesh Tripathi, st4083
"""

import sys 

# Helper functions
# Shift letter by offset
def _shift_letter(letter: str, offset: int = 1) -> str: 
    letter_ord_base = ord(letter) - ord('A')
    letter_ord_base_shifted = (letter_ord_base + offset) % 26 
    letter_ord_actual = letter_ord_base_shifted + ord('A')
    shifted_letter = chr(letter_ord_actual)
    return shifted_letter

# Rotate message once
def _rotate_once(message: str) -> str:
    return message[-1] + message[:len(message)-1]

# Duplicate letter once
def _duplicate_letter(message: str, letter_index: int) -> str: 
    left_side = message[:letter_index]
    right_side = message[letter_index+1:]
    letter = message[letter_index]
    return left_side + letter + letter + right_side

def _remove_duplicate_letter(message:str, letter_index: int) -> str:
    return message[:letter_index] + message[letter_index+1:]

# Main operation functions
# Shift letter in message by offset
def shift(message: str, letter_index: int, offset: int = 1) -> str:
    letter = message[letter_index]
    shifted_letter = _shift_letter(letter, offset)
    return message[:letter_index] + shifted_letter + message[letter_index+1:]

# Rotate message k times
def rotate(message: str, k_times: int = 1) -> str:
    for _ in range(k_times % len(message)):
        message = _rotate_once(message)
    return message

# Duplicate letter k times
def duplicate(message: str, letter_index: int, k_times: int = 1) -> str: 
    for _ in range(k_times):
        message = _duplicate_letter(message, letter_index)
    return message

# Remove duplicate letter k times
def remove_duplicate(message:str, letter_index: int, k_times: int = 1) -> str:
    for _ in range(k_times):
        message = _remove_duplicate_letter(message, letter_index)
    return message

# Trade letter at index i and j where i < j always
def trade_ij(message: str, index_i: int, index_j: int) -> str:
    letter_i = message[index_i]
    letter_j = message[index_j]

    left = message[:index_i]
    middle = message[index_i+1:index_j]
    right = message[index_j+1:]

    traded_message = left + letter_j + middle + letter_i + right
    return traded_message

def sanitize(ops_dict: dict) -> dict: 
    # Normalize parameters (R -> R1 and S/Da R/Da,1)
    for op in ops_dict:
        if op == 'S' or op == 'D':
            if not ',' in ops_dict[op]:
                ops_dict[op] += ',1'

        if op == 'R' and len(ops_dict[op]) == 0:
            ops_dict[op] = '1'

    # Convert Xij to X[i,j]
    for op in ops_dict:
        if op == 'R':
            ops_dict[op] = int(ops_dict[op])

        else: # For S, R, D, T
            params = ops_dict[op].split(',')
            ops_dict[op] = [int(params[0]), int(params[1])]
    return ops_dict


def parse(operations: str, isDecode: bool = False) -> dict:
    
    # Seperate all operations 
    operations = operations.split(';') 

    # Reverse operations if 'decode'
    if isDecode: 
        operations.reverse() 
    
    # Make dictionary
    # {OPERATION: 'PARAMS'}
    ops_dict = {}
    for op in operations:
        ops_dict[op[0]] = op[1:]

    ops_dict = sanitize(ops_dict)

    # Mode = Decode, negate frequency parameters
    if isDecode: 
        for op in ops_dict:
            if op == 'S':
                ops_dict[op] = [ops_dict[op][0], ops_dict[op][1] * -1]

            if op == 'R':
                ops_dict[op] *= -1

    return ops_dict

def encrypt(message: str, operations: str) -> str:

    ops_dict = parse(operations, False)

    for op in ops_dict: 
        if op == 'R':
            message = rotate(message, ops_dict[op])

        if op == 'T':
            message = trade_ij(message, ops_dict[op][0], ops_dict[op][1])

        if op == 'D':
            message = duplicate(message, ops_dict[op][0], ops_dict[op][1])

        if op == 'S':
            message = shift(message, ops_dict[op][0], ops_dict[op][1])

    return message

def decrypt(message: str, operations: str) -> str: 

    ops_dict = parse(operations, True)

    for op in ops_dict:     
        if op == 'R':
            message = rotate(message, ops_dict[op])

        if op == 'T':
            message = trade_ij(message, ops_dict[op][0], ops_dict[op][1])

        if op == 'D':
            message = duplicate(message, ops_dict[op][0], ops_dict[op][1])

        if op == 'S':
            message = shift(message, ops_dict[op][0], ops_dict[op][1])

    return message

def affine_encrypt(message: str, a: int, b: int) -> str:
    encrypted_message = ""
    for letter in message:
        letter_i = ord(letter) - ord('A')
        encrypted_letter = (a * letter_i + b) % 26
        encrypted_message += encrypted_letter
    return encrypted_message


def affine_decrypt(message: str, a:int, b: int) -> str:
    decrypted_message = ""
#    for letter in message: 
#        letter_i
    return

# Ciphers main function 
def ciphers() -> None:
    print("Welcome to Ciphers!\n")

    while True:

        # Input option
        while True: 
            option = input("What do you want to do; (E)ncrypt, (D)ecrypt or (Q)uit?: ").upper()

            if not option in ['E', 'D', 'Q']:
                print("\nPlease enter a valid option.")
            else:
                break

        # Quit session 
        if option == 'Q':
            print("\nGoodbye!")
            break

        # Take message input
        message = input("Enter the message: ").upper()

        # Which operation to perform
        operations = input("Enter the encrypting transformation operations: ").upper()

        # Encode or Decode
        if option == 'E':
            output_message = encrypt(message, operations)
        
        if option == 'D':
            output_message = decrypt(message, operations)

        print("Generating output ...")

        print(output_message)


def checkpoint(user_input: str) -> None:
    if sys.argv[0]:
        print("[LOG: User input -> {}]".format(user_input))

def main() -> None:
    """
    The main loop responsible for getting the input details from the user
    and printing in the standard output the results
    of encrypting or decrypting the message applying the transformations
    :return: None

    """
    ciphers()

 
if __name__ == '__main__':
    main()
