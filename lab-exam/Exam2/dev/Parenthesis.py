"""
author: Shreesh Tripathi, st4083
"""

from Stack import Stack 

def is_balance(par_str):
    s = Stack()
    print("Processing: {}".format(par_str))
    for char in par_str:
        if char == "(":
            s.push(char)
        elif char == ")":
            if not s.isEmpty():
                if s.peek() == "(":
                    s.pop()
            else:
                return False
    return s.isEmpty()

def display(par_str):
    for char in par_str:
        print(char)

def test():
    test_cases = [
        "()()()()",
        "((()))",
        "(((()()()())))",
        "()()()()((()))",
        "(())))()",
        "(()(())())",
        ")))",
        ")",
        "((())))"
    ]

    for case in test_cases:
        print("\nTest Case: {}".format(case))
        print("Are symbols balanced?: {}".format(is_balance(case)))

def main():
    # test() # For the grader
    par_str = input("Please input a string: ")
    par_str = par_str.replace(' ', '') # Clean any whitespaces
    print("Are symbols balanced?: {}".format(is_balance(par_str)))

if __name__ == '__main__':
    main()

