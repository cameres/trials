import time
from functools import partial

def trial_length(f):
    """
    given a function w/ arbitrary python code
    return how long it takes to run the code
    """
    start = time.time()
    f()
    end = time.time()
    return end - start

def average_trial_length(f, trials, setup):
    """
    Parameters
    ----------
    f: arbitrary function of python code to run

    trials: number of times to run python code in f

    setup: function that returns keyword arguments
        to be applied to the function f. ex:
        initilaize a random array for sorting
        f would be the sorting algorithm &
        setup would intialize a random array

    Returns
    -------
    mean: mean time of the trials to run f
    """
    trial_results = []
    for trial in range(trials):
        # setup function returns all values
        # to be passed to actual segment of
        # code that is desired to be tested
        args = setup()

        # partially apply setup results to function
        # NOTE: partial functions don't have __name__
        f = partial(f, **args)

        length = trial_length(f)
        print "\t completed trial #{} in {} seconds".format(trial, length)

        trial_results.append(length)
    mean = sum(trial_results)/len(trial_results)
    return mean
