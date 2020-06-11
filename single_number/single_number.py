'''
Input: a List of integers where every int except one shows up twice
Returns: an integer
'''


# first pass
# def single_number(arr):
#     candidates = []
#     for num in arr:
#         try:
#             candidates.remove(num)
#         except ValueError:
#             candidates.append(num)
#     return candidates[0]


# second pass
def single_number(arr):
    candidates = {}
    for num in arr:
        if num in candidates.keys():
            del(candidates[num])
        else:
            candidates[num] = 1
    for single in candidates.keys():  # only contains one key
        return single


# not actually sure which one is faster...


if __name__ == '__main__':
    # Use the main function to test your implementation
    arr = [1, 1, 4, 4, 5, 5, 3, 3, 9, 0, 0]

    print(f"The odd-number-out is {single_number(arr)}")
