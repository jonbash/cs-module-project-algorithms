'''
Input: a List of integers as well as an integer `k` representing the size of the sliding window
Returns: a List of integers
'''

# first pass
def sliding_window_max(nums, k):
    maxes = []
    candidates = nums[:k]

    i = k
    while True:
        m = max(candidates)
        maxes.append(m)
        if i >= len(nums):
            break
        candidates.append(nums[i])
        candidates.pop(0)
        i += 1

    return maxes


# I don't believe a faster implementation is possible


if __name__ == '__main__':
    # Use the main function here to test out your implementation
    arr = [1, 3, -1, -3, 5, 3, 6, 7]
    k = 3

    print(f"Output of sliding_window_max function is: {sliding_window_max(arr, k)}")
