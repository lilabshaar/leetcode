# Problem : Given an integer x, return true if x is a palindrome, and false otherwise.

class Solution(object):
    def isPalindrome(self, x):
        x = str(x)
        return x == x[::-1]
