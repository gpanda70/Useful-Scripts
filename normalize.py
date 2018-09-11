import numpy  # Numpy is faster than generic python lists
import timeit
"""

This Program normalizes account ids by removing whitespace and leading 000's

"""
lsz = ['000123 12', 'This is a cool program ', 'sdasdas sd asdasd asda ', '0102910920192019033913910310391039']
def normalize(nums):
    normalized_list = []
    for num in nums:
        num = num.replace(' ', '')  # removes whitespace
        num = num.lstrip('0')  # removes leading 0's
        normalized_list.append(num)

    return (normalized_list)

def np_normalize(nums):
    import numpy as np
    normalized_list = np.array([])
    for num in np.array(nums):
        num = num.replace(' ', '')
        num = num.lstrip('0')  # removes leading 0's
        normalized_list = np.append(normalized_list, num)

    return (normalized_list)

if __name__ == "__main__":

    cy = timeit.timeit('normalize(lsz)', setup='from __main__ import normalize, lsz', number=1000)
    py = timeit.timeit('np_normalize(lsz)', setup='from __main__ import np_normalize, lsz', number=1000)
    print('numpy is {}x faster than lists'.format(py/cy) )
