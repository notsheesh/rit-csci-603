""" 
file: tests.py
description: Verify the LinkedHashSet class implementation
"""

__author__ = "Shreesh Tripathi, st4083"

from linkedhashset import LinkedHashSet

def print_set(a_set):
    for word in a_set:  # uses the iter method
        print(word, end=" ")
    print()

def hash_function(value):
    # takes the first letter of the word
    # a = 0, b = 1 ... 
    return ord(value[0]) - ord('A')

def test_case_3():
    """
    Test Case 3: Illustrate the following helper functions
    1. Length
    2. Contains
    """
    print("\nStarting Test Case 3")
    print("Objective:")
    print("Illustrate the following helper functions")
    print("1. Length")
    print("2. Contains")

    input("> Hit enter to proceed.")
    
    theSet = LinkedHashSet(initial_num_buckets=10, hash_function=hash_function)
    # Print 
    print("Checkpoint: Print hashset")
    input("> Hit enter to proceed.")
    print(repr(theSet))
    print("Final State: ", end='')
    print_set(theSet)
    print("=======================================================")

    # Length
    print("1. Length")
    print("Before: len(theSet) = {}".format(len(theSet)))
    sentence = ['hello', 'howdy', 'how', 'are', 'you', 'doing']
    print("Adding words: {}".format(sentence))
    input("> Hit enter to proceed.")
    for i, word in enumerate(sentence):
        theSet.add(word)
        print("Add '{}' | Word Count: {} | len(theSet) = {} | ".format(
            word, i+1, len(theSet)), end='')
        print_set(theSet)
    print("Final State: ", end='')
    print_set(theSet)
    print("After: len(theSet) = {}".format(len(theSet)))
    print("=======================================================")

    # Contains
    # Remove words
    dne = ['umbrella', 'leopard', 'samurai']
    contains = ['are', 'you', 'how', ]
    words = dne + contains
    print("2. Is Contains? {}".format(words))
    input("> Hit enter to proceed.")
    for word in words:
        print("Is Contains? '{}': {}".format(word, theSet.contains(word)))
        print("Remove '{}': {} | ".format(word, theSet.remove(word)), end='')
        print_set(theSet)
        print("Is Contains? '{}': {}".format(word, theSet.contains(word)))
        print("Set: ", end='')
        print_set(theSet)
        print("=======================================================")
        input("> Hit enter to proceed.")
    print("Final State: ", end='')
    print_set(theSet)
    print("=======================================================")
    print("Test run complete.")
    print("=======================================================")
    return 

def test_case_2():
    """
    Test Case 2: Illustrate the following phenomenons
    1. Upsizing
    2. Downsizing
    """
    print("\nStarting Test Case 2")
    print("Objective:")
    print("Illustrate the following phenomenons")
    print("1. Upsizing")
    print("2. Downsizing")

    input("> Hit enter to proceed.")

    DEBUG = True

    print("=======================================================")
    theSet = LinkedHashSet(
        initial_num_buckets=2, 
        hash_function=hash_function, 
        DEBUG=DEBUG)

    print("=======================================================")
    
    print("Adding the first 10 alphabets")
    input("> Hit enter to proceed.")
    
    for offset in range(10):
        print("=======================================================")
        alphabet = chr(ord('A') + offset)
        theSet.add(alphabet)
        print(repr(theSet))
        print("=======================================================")
        input("> Hit enter to proceed.")
        

    print("Final State: ", end='')
    print_set(theSet)
    print("=======================================================")

    print("Removing all alphabets")
    input("> Hit enter to proceed.")

    for offset in range(10):
        print("=======================================================")
        alphabet = chr(ord('A') + offset)
        theSet.remove(alphabet)
        print(repr(theSet))
        print("=======================================================")
        input("> Hit enter to proceed.")
        

    print("Final State : ", end='')
    print_set(theSet)
    print("=======================================================")

    print("Test run complete.")
    print("=======================================================")
    return 

def test_case_1():
    """
    Test Case 1: Illustrate the following operations
    1. Add words
    2. Add repeated words
    3. Remove words that exist
    4. Remove words that don't exist
    """
    print("\nStarting Test Case 1")
    print("Objective:")
    print("Illustrate the following operations -- ")
    print("1. Add words")
    print("2. Add repeated words")
    print("3. Remove words that exist")
    print("4. Remove words that dont exist")

    input("> Hit enter to proceed.")
    
    theSet = LinkedHashSet(initial_num_buckets=10, hash_function=hash_function)
    # Print 
    print("Checkpoint: Print hashset")
    input("> Hit enter to proceed.")
    print(repr(theSet))
    print("Final State: ", end='')
    print_set(theSet)
    print("=======================================================")

    # Add words
    sentence = ['hello', 'howdy', 'how', 'are', 'you', 'doing']
    print("1. Add words: {}".format(sentence))
    input("> Hit enter to proceed.")

    for word in sentence:
        print("Add '{}': {} | ".format(word, theSet.add(word)), end='')
        print_set(theSet)
    print("Final State: ", end='')
    print_set(theSet)
    print("=======================================================")

    # Add repeated words
    duplicates = ['you', 'doing', 'howdy']
    print("2. Add duplicates: {}".format(duplicates))
    input("> Hit enter to proceed.")
    for word in duplicates:
        print("Add '{}': {} | ".format(word, theSet.add(word)), end='')
        print_set(theSet)
    print("Final State: ", end='')
    print_set(theSet)
    print("=======================================================")
    
    # Print 
    print("Checkpoint: Print hashset")
    input("> Hit enter to proceed.")
    print(repr(theSet))
    print_set(theSet)
    print("=======================================================")

    # Remove words
    remove = ['are', 'you', 'how']
    print("3. Remove words: {}".format(remove))
    input("> Hit enter to proceed.")
    for word in remove:
        print("Remove '{}': {} | ".format(word, theSet.remove(word)), end='')
        print_set(theSet)
    print("Final State: ", end='')
    print_set(theSet)
    print("=======================================================")

    # Remove words that dont exist 
    dne = ['umbrella', 'leopard', 'samurai']
    print("4. Remove inexistent words: {}".format(dne))
    input("> Hit enter to proceed.")
    for word in dne:
        print("Remove '{}': {} | ".format(word, theSet.remove(word)), end='')
        print_set(theSet)
    print("Final State: ", end='')
    print_set(theSet)
    print("=======================================================")
    print("Test run complete.")
    print("=======================================================")
    return

def main():
    menu = [1,2,3]
    while(True):
        print("\nSelect an option")
        if 1 in menu:
            print("1. Test Case 1")
        if 2 in menu:
            print("2. Test Case 2")
        if 3 in menu:
            print("3. Test Case 3")
        print("4. Hit enter to exit")

        x = input("Enter a number: ")

        if x and int(x) == 1:
            menu.remove(1)
            test_case_1()
        elif x and int(x) == 2:
            menu.remove(2)
            test_case_2()
        elif x and int(x) == 3:
            menu.remove(3)
            test_case_3()
        else:
            print("Terminating tests.py")
            break

if __name__ == '__main__':
    main()

