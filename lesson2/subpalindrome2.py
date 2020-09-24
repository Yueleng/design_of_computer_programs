# --------------
# Dynamic Programming(DP) Version
# --------------
#
# Write a function, longest_subpalindrome_slice(text) that takes 
# a string as input and returns the i and j indices that 
# correspond to the beginning and end indices of the longest 
# palindrome in the string. 
#
# Grading Notes:
# 
# You will only be marked correct if your function runs 
# efficiently enough. We will be measuring efficency by counting
# the number of times you access each string. That count must be
# below a certain threshold to be marked correct.
#
# Please do not use regular expressions to solve this quiz!

def longest_subpalindrome_slice(text):
    "Return (i, j) such that text[i:j] is the longest palindrome in text."
    # Your code here
    n = len(text)
    strTable = [[False for x in range(n)] for y in range(n)]
    start_return = end_return = 0

    # All substrings of length 1 are palindrome
    maxLength = 1

    # Check for length greater or equal to 1.
    # k is length of substring
    # k starts from 1
    k = 1
    while k <= n:
        # Fix the starting index
        i = 0
        while i <= n - k:
            # Get the end index of substring 
            # from starting index i and total length of k
            j = i + k - 1

            if ((i == j-1 or i == j or strTable[i+1][j-1]) and text[i].upper() == text[j].upper()):
                strTable[i][j] = True
                if (k > maxLength):
                    maxLength = k
                    start_return = i
                    end_return = i + k
            i += 1
        k += 1
    return start_return, end_return
    
def test():
    L = longest_subpalindrome_slice
    assert L('racecar') == (0, 7)
    assert L('Racecar') == (0, 7)
    assert L('RacecarX') == (0, 7)
    assert L('Race carr') == (7, 9)
    assert L('') == (0, 0)
    assert L('something rac e car going') == (8,21)
    assert L('xxxxx') == (0, 5)
    assert L('Mad am I ma dam.') == (0, 15)
    return 'tests pass'

print(test())

# print(longest_subpalindrome_slice('Race carr'))