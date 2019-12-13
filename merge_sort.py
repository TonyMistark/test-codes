def merge_sort(arr):
    """
    Merge Sort
    Complexity:O(n log(n))
    """
    # Our recursive base case
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    # Perform merge_sort recursively on both halves
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    print(f"merged_sort: arr:{arr}, mid{mid}, left:{left}, right:{right}")

    # Merge each side together
    return merge(left, right, arr.copy())


def merge(left, right, merged):
    """
    Merge helper
    Complexity: O(n)
    """
    left_cursor, right_cursor = 0, 0
    while left_cursor < len(left) and right_cursor < len(right):
        # Sort each one and place into the result
        if left[left_cursor] <= right[right_cursor]:
            merged[left_cursor + right_cursor] = left[left_cursor]
            left_cursor += 1
        else:
            merged[left_cursor + right_cursor] = right[right_cursor]
            right_cursor += 1

    # Add the left overs if there's any left to the result
    for left_cursor in range(left_cursor, len(left)):
        merged[left_cursor + right_cursor] = left[left_cursor]

    # Add the left overs if there's any left to the result
    for right_cursor in range(right_cursor, len(right)):
        merged[left_cursor + right_cursor] = right[right_cursor]

    # Return result
    return merged


if __name__ == "__main__":
    my_list = [1,4,7,2,3,1,8,5]
    l = merge_sort(my_list)
    print(f"my_list: {my_list}, sorted list: {l}")
