def falling(n, k):
    """Compute the falling factorial of n to depth k.

    >>> falling(6, 3)  # 6 * 5 * 4
    120
    >>> falling(4, 3)  # 4 * 3 * 2
    24
    >>> falling(4, 1)  # 4
    4
    >>> falling(4, 0)
    1
    """
    "*** YOUR CODE HERE ***"

    # as long as k > 0, keep computing factorial and return product. some variable to keep track of product. 
    product = 1
    while k > 0:
        product *= n
        n, k = n - 1, k - 1
    return product


def divisible_by_k(n, k):
    """
    >>> a = divisible_by_k(10, 2)  # 2, 4, 6, 8, and 10 are divisible by 2
    2
    4
    6
    8
    10
    >>> a
    5
    >>> b = divisible_by_k(3, 1)  # 1, 2, and 3 are divisible by 1
    1
    2
    3
    >>> b
    3
    >>> c = divisible_by_k(6, 7)  # There are no integers up to 6 divisible by 7
    >>> c
    0
    """
    "*** YOUR CODE HERE ***"
    # counter to keep track of what number we're on and that we're less than n
    i = 1
    count = 0
    while i <= n:
        if i % k == 0:
            print(i)
            count += 1
        i += 1
    return count


def sum_digits(y):
    """Sum all the digits of y.

    >>> sum_digits(10) # 1 + 0 = 1
    1
    >>> sum_digits(4224) # 4 + 2 + 2 + 4 = 12
    12
    >>> sum_digits(1234567890)
    45
    >>> a = sum_digits(123) # make sure that you are using return rather than print
    >>> a
    6
    """
    "*** YOUR CODE HERE ***"
    # base case, if y < 10, return y. else split y into its last and remaining digits. create some variable to store values?
    sum = 0
    while y > 0:
        y, last_y = y // 10, y % 10
        sum += last_y
    return sum
    
    # if y < 10:
    #     return y
    # else:
    #     return (y % 10) + sum_digits(y // 10)

        
def double_eights(n):
    """Return true if n has two eights in a row.
    >>> double_eights(8)
    False
    >>> double_eights(88)
    True
    >>> double_eights(2882)
    True
    >>> double_eights(880088)
    True
    >>> double_eights(12345)
    False
    >>> double_eights(80808080)
    False
    """
    "*** YOUR CODE HERE ***"
    # always will return False if n < 10, so as long as n >= 10, we want to get the last and remaining digits, check that the last digits = the last digit of remaining digits = 8.
    while n >= 10:
        rest_n, last_n = n // 10, n % 10
        if rest_n % 10 == last_n == 8:
            return True
        else:
            n = n // 10
    return False