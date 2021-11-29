# Ultimate binary search with Interpolation Search
# More about ultimate binary search - https://bit.ly/3lihXuj
# More about Interpolation Search - https://www.geeksforgeeks.org/interpolation-search/

# Same as Interpolation search(Which itself is a better binary search) but in a clean way Time-complexity - O(loglogn)

def ultimate_interpolated_binary_search(arr, x):
    low = 0
    high = len(arr) - 1
    while low <= high and arr[low] <= x <= arr[high]:
        # The interpolation part
        pos = int(low + (x - arr[low]) * (high - low) / (arr[high] - arr[low]))
        if arr[pos] == x:
            return pos
        elif arr[pos] < x:
            low = pos + 1
        else:
            high = pos - 1
    return None
