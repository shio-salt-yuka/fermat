import random
import PyQt6


def prime_test(N, k):
    # This is main function, that is connected to the Test button. You don't need to touch it.
    return fermat(N, k), miller_rabin(N, k)


def mod_exp(x, y, N):
    if y == 0:
        return 1
    z = mod_exp(x, (y // 2), N) # n-bit integer, shifting takes n(O)...?
    # if y is even
    if y % 2 == 0:
        return z ^ 2 % N
    else:
        return x * z ^ 2 % N

        # You will need to implement this function and change the return value.


def fprobability(k):
    prob = 1 / (2 ^ k)
    return 1 - prob

    # You will need to implement this function and change the return value.


def mprobability(k):
    prob = 1 / (4 ^ k)
    return 1 - prob

    # You will need to implement this function and change the return value.


def fermat(N, k): # k is usually pretty small and thus negligible
    for i in range(1, k):
        randint = random.randint(1, N-1)  # pick positive integers a1….ak < N
        if mod_exp(randint, N-1, N) == 1:
            continue
        else:
            return 'composite'
    return 'prime'

    # You will need to implement this function and change the return value, which should be
    # either 'prime' or 'composite'.
    #
    # To generate random values for a, you will most likley want to use
    # random.randint(low,hi) which gives a random integer between low and
    #  hi, inclusive.


def miller_rabin(N, k):  # k is usually pretty small and thus negligible
    for i in range(1, k):
        randint = random.randint(1, N-1)
        power = N-1
        answer = mod_exp(randint, power, N)
        if answer != 1:
            return 'composite'
        while (answer != N-1) and (power % 2 == 0):
            power = power // 2
            answer = mod_exp(randint, power, N)
            if answer != 1 and answer != N-1:
                return 'composite'
    return 'prime'

# You will need to implement this function and change the return value, which should be
# either 'prime' or 'composite'.
#
# To generate random values for a, you will most likley want to use
# random.randint(low,hi) which gives a random integer between low and
#  hi, inclusive.
