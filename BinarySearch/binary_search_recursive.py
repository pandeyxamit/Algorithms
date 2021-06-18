def binary_search_rec(arr, item, low, high):
    mid = low + (high - low) // 2
    guess = arr[mid]
    if guess == item:
        return "Item {} found at index {} in the array.\n".format(item, mid)
    if guess < item:
        low = mid + 1
        return binary_search_rec(arr, item, low, high)
    elif guess > item:
        high = mid - 1
        return binary_search_rec(arr, item, low, high)
    return "Item not present in the array.\n"
