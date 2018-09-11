import numpy as np  # Numpy is faster than generic python lists
import timeit
"""

This Program normalizes account ids by removing whitespace and leading 000's

"""
lsz = ['000123 12', 'This is a cool program ', 'sdasdas sd asdasd asda ', '0102910920192019033913910310391039']
def normalize(ids):
    normalized_list = []
    for id in ids:
        id = id.replace(' ', '')  # removes whitespace
        id = id.lstrip('0')  # removes leading 0's
        normalized_list.append(id)

    return (normalized_list)

def np_normalize(ids):
    normalized_list = np.array([])
    for id in np.array(ids):
        id = id.replace(' ', '')
        id = id.lstrip('0')  # removes leading 0's
        normalized_list = np.append(normalized_list, id)

    return (normalized_list)

if __name__ == "__main__":

    cy = timeit.timeit('normalize(lsz)', setup='from __main__ import normalize, lsz', number=1000)
    py = timeit.timeit('np_normalize(lsz)', setup='from __main__ import np_normalize, lsz', number=1000)
    print('idpy is {}x faster than lists'.format(py/cy) )
