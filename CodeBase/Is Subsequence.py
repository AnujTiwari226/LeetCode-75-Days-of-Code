class Solution:

    @staticmethod
    def isSubsequence(s: str, t: str) -> bool:
        """
        initialize i and j = 0
        i will check len of s and j will be used to compare len of t
        increment value of i if s[i]==s[j] and increment value of j in each iteration
        :param s:
        :param t:
        :return:bool : True if isomorphic else False
        """
        i = j = 0
        while i < len(s) and j < len(t):
            if s[i] == t[j]:
                i += 1
            j += 1
        return len(s) == i



if __name__ == '__main__':
    """
    Given two strings s and t, return true if s is a subsequence of t, or false otherwise.

   A subsequence of a string is a new string that is formed from the original string by deleting some (can be none) 
   of the characters without disturbing he relative positions of the remaining 
   characters. (i.e., "ace" is a subsequence of "abcde" while "aec" is not).

    """

    sol = Solution
    print('input - ')
    s = input()
    t = input()
    print(sol.isSubsequence(s=s, t=t))
