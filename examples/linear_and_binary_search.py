from functools import partial
import random

from trials import average_trial_length

def binary_search(a, value):
    low = 0
    high = len(a) - 1
    while low <= high:
        # much better that's actually the mid...
        mid = (low + high) / 2
        guess = a[mid]
        if guess == value:
            return mid
        if guess > value:
            high = mid - 1
        else:
            low = mid + 1
    return -1

def linear_search(a, value):
    for (index, current_value) in enumerate(a):
        if(current_value == value):
            return index
    return -1

if __name__ == '__main__':
    def setup_search(n):
        # create random sorted array
        a = sorted([random.uniform(0, 1) for _ in range(n)])
        # get a value to search for in the array
        random_value = random.choice(a)
        return {'a':a, 'value':random_value}

    n = int(1e4)
    trials = 10

    setup_search_partial = partial(setup_search, n)

    print "Running Linear Search {} Times".format(trials)
    average_linear = average_trial_length(linear_search, trials, setup_search_partial)
    print "Linear Search Ran an Average of {} Seconds".format(average_linear)

    print "Running Binary Search {} Times".format(trials)
    average_binary = average_trial_length(binary_search, trials, setup_search_partial)
    print "Binary Search Ran an Average of {} Seconds".format(average_binary)
