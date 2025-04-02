# 1825622 Nyarko Prince Edwin

def find_max(arr):

    if not arr:
        return "An array with numbers is needed"
    else:
        max_ele = arr[0]
        for element in arr:
            if element > max_ele:
                max_ele = element
        return max_ele


def count_element(arr, target):
    
    if not arr:
        return "An array with numbers is needed"
    else:
        count_x = 0
        for x in arr:
            if x == target:
                count_x += 1
        return count_x


def sorted(arr):
    """
    Check if the given array is sorted in non-decreasing order.

    Args:
        arr (list): A list of numbers.

    Returns:
        bool: True if the array is sorted, False otherwise.

    Time Complexity: O(n), where n is the number of elements in the array.
    """
    for i in range(len(arr) - 1):
        if arr[i] > arr[i + 1]:
            return False
    return True


def main():
    """
    Main function to demonstrate the functionality of the above functions.
    """
    arr = [1.2, 3, 1, 2, 3, 4, 5, 7, 8, 9, 10, 4, 2, 1, 0]
    try_cout = count_element(arr, 1)
    try_find = find_max(arr)
    try_sort = sorted(arr)
    print(try_find)
    print(try_cout)
    print(try_sort)


if __name__ == "__main__":
    main()