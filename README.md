# trials: a simple library for determining the runtimes of python code
trials is a very simple library that is used to get the average runtimes of arbitrary python code.
This library eliminates the boilerplate code for getting the difference between two time objects.

In trials you can also supply a `setup` function, that can be used to setup a trial of python code.
See the example directory where I use trials to setup a list and select a random element to search for using linear search & binary search.
I'll hopefully be adding more examples of trials in the future.

## Install
The library isn't yet on pypi, but it can be installed by downloading the repository and running `$ python setup.py` or `$ pip install .`.

## Recommendation
I built this library to experiment with `functools` in python.
trials makes heavy use of partially applied functions and I strongly recommend taking a look at functools if you haven't.
Using partially applied function has lead to simpler logic in my personal experience for testing similar functions.

## Issues
Unfortunately functools doesn't allow properties like `__name__`, so you will have (even if it did your functions would likely appear as <partial> or something of the sort).
It's recommended to have a simple debug message before calling average_trial_length like in the following snippet.

```python
print "Running Binary Search"

average = average_trial_length(...)
print "Binary Search Took on Average {}!".format(average)
```
