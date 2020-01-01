'''
    Description: Longest Palindromic substring
    Language: Python 3.7
    Author: Suryadeep
'''
class Solution:
    def longestPalindrome(self, s):
        l = len(s)
        # If empty string is passed
        # return an empty string.
        if l == 0:
            return ''
        # Populate the empyty DP
        # matrix.
        dp = [[0 for x in range(l)] for y in range(l)]
        # All the single digit strings
        # are palindromes.
        i = 0
        while i < l:
            # Update DP table for all
            # the single digits.
            dp[i][i] = True
            # hold the coordinates for
            # palindrome string.
            palin = (i, i)
            i += 1
        # Check for 2-digit palindrome
        # substrings.
        i = 0
        while i < l - 1:
            # Check if the consecutive
            # characters are same.
            if s[i] == s[i + 1]:
                # Update the DP table.
                dp[i][i + 1] = True
                # hold the coordinates for
                # palindrome string.
                palin = (i, i + 1)
            i += 1
        # Check for all the substrings
        # that are greater than 3 in
        # length.
        k = 3
        max_len = 0
        # Iterate for 3 digit substrings
        # for all the characters.
        while k <= l:
            i = 0
            # Iterate for all the chars.
            while i < l - k + 1:
                j = i + k - 1
                # The start character and kth
                # character shold match and all
                # substring of length (k-1)
                # must be a palindrome.
                if s[i] == s[j] and dp[i + 1][j - 1]:
                    # Update rhe DP table.
                    dp[i][j] = True
                    # Check if the current palindrom
                    # substring has maximum langth.
                    if max_len <= j - i + 1:
                        # If it is maximum length then
                        # update the tuples.
                        max_len = j - i + 1
                        palin = (i, j)
                i += 1
            k += 1
        # return the Palindromic substring.
        return s[palin[0] : palin[1] + 1]
if __name__ == '__main__':
    s = Solution()
    s.longestPalindrome('cbbd')