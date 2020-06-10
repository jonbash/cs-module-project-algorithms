
'''
Input: an integer
Returns: an integer


'''
cookie_cache = dict()

def eating_cookies(n):
    if n < 0:
        return 0
    if n in [0, 1]:
        return 1
    try:
        return cookie_cache[str(n)]
    except KeyError:
        output = 0
        for i in range(3):
            x = n - i - 1
            x_result = eating_cookies(x)
            cookie_cache[str(x)] = x_result
            output += x_result

        return output

if __name__ == "__main__":
    # Use the main function here to test out your implementation
    num_cookies = 5

    print(f"There are {eating_cookies(num_cookies)} ways for Cookie Monster to each {num_cookies} cookies")
