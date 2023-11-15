# first_array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]

# # Define the pattern for rearranging
# pattern = [1, 2, 5, 6, 3, 4, 7, 8, 9, 10, 13, 14, 11, 12, 15, 16]

# # Create the second array by rearranging elements from the first array based on the pattern
# second_array = [first_array[i - 1] for i in pattern]

# print(second_array)

def func(num, count = 1):
    if count == num: 
        return 
    else:
        for _ in range(count):
            print("*", end='')
        print()
        func(count + 1)
        for _ in range(count):
            print("*", end='')
        print()

func(5)