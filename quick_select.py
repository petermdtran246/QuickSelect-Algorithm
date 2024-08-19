def partition(arr, low, high):
    """
    Partition the array around a pivot element.

    :parameter:
    --------------------------------------------
        arr (list): The input array.
        low (int): The starting index of the subarray.
        high (int): The ending index of the subarray.

    :return:
    --------------------------------------------
        The index of the pivot after partitioning
    """
    pivot = arr[high]
    i = low - 1
    # Traverse through all elements & compare each element with pivot
    for j in range(low, high):
        if arr[j] <= pivot:
            # Increment index of smaller element
            i += 1
            arr[i], arr[j] = arr[j], arr[i] #swap elements
    # Swap the pivot element with the greater element at index i+1
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1

def QuickSelect(arr, k, low = 0, high = None):
    """
    Finds the k-th smallest element in the array using the QuickSelect algorithm

    :parameter:
    --------------------------------------------------------------------------------
        arr (list): The input array.
        k (int): The position of the smallest element to find (1-based index).
        low (int):The starting index of the subarray.
        high (int): The ending index of the subarray.

    :return:
    --------------------------------------------------------------------------------
        The k-th smallest element in the array.
    """
    if high is None:
        high = len(arr) - 1
    if low == high:
        return arr[low]

    # Partition the array around a pivot element
    pivot_index = partition(arr, low, high)

    # If the pivot index matches the desired position (k-1),
    # return the pivot element
    if pivot_index == k - 1:
        return arr[pivot_index]
    # If the pivot index is greater than the desired position,
    # continue the search in the left subarray
    elif pivot_index > k - 1:
        return QuickSelect(arr, k, low, pivot_index - 1)
    # If the pivot index is less than the desired position,
    # continue the search in the right subarray
    else:
        return QuickSelect(arr, k, pivot_index + 1, high)