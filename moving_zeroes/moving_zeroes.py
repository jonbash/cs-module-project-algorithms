'''
Input: a List of integers
Returns: a List of integers
'''

# first pass -- I think this is as good as it gets?
def moving_zeroes(arr):
    zeroes = 0
    i = 0
    while i < len(arr):
        if arr[i] == 0:
            arr.pop(i)
            zeroes += 1
        else:
            i += 1
    arr.extend([0] * zeroes)
    return arr


if __name__ == '__main__':
    # Use the main function here to test out your implementation
    arr = [0, 3, 1, 0, -2]

    print(f"The resulting of moving_zeroes is: {moving_zeroes(arr)}")
