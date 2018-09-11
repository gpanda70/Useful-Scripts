"""

This Program normalizes account ids by removing whitespace and leading 000's

"""

def normalize(nums):
    normalized_list = []
    for num in nums:
        num = num.replace(' ', '')  # removes whitespace
        num = num.lstrip('0')  # removes leading 0's
        normalized_list.append(num)

    return (normalized_list)

if __name__ == "__main__":
    lsz = ['000123 12', 'This is a cool program ']
    print(normalize(lsz))
