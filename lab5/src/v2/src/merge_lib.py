"""
Merge Sort

A Python script for implementation of the Merge Sort algorithm 

author: Shreesh Tripathi, st4083
"""

def merge(left_lst: list, right_lst: list):
    """
    Merges two sorted lists into a single sorted list.

    :param left_lst: The left sorted list.
    :param right_lst: The right sorted list.

    :return: A merged sorted list.
    """
    merged_lst = []
    left, right = 0, 0
    while left < len(left_lst) and right < len(right_lst):
        if left_lst[left] < right_lst[right]: 
            merged_lst.append(left_lst[left])
            left += 1
        else: 
            merged_lst.append(right_lst[right])
            right += 1

    while left < len(left_lst):
        merged_lst.append(left_lst[left])    
        left += 1
    
    while right < len(right_lst):
        merged_lst.append(right_lst[right])    
        right += 1
    
    return merged_lst

def merge_sort(lst: list):
    """
    Sorts a list using the merge sort algorithm.

    :param lst: The list to be sorted.

    :return: A sorted list.
    """
    if len(lst) < 2: 
        return lst

    left_lst, right_lst = lst[:len(lst)//2], lst[len(lst)//2:]
    return merge(merge_sort(left_lst), merge_sort(right_lst))

def main():
    return

if __name__ == '__main__':
    main()