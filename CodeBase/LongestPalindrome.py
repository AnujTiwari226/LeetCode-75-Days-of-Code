class Solution:

    def longestPalindrome(self, s: str) -> int:
        """
        create a set which will capture only unique charcters that are in odd in numbers
        we'll keep removing even values from set using loop and add only odd char
        then in the end we'll check if there is any odd number in the set if yes then we'll subtract length of set from
        length of given string and add one as no matter how many odd number we have in string we can only take 1 odd char
        if set is empty then return len of string

        eg. in abccea
        we'll have only b and e in our set. as even values a and c will be removed
        then len of string i.e 6 - len(set) i.e 2 = 4 + 1 - for keeping only one odd result = 5
         possible sol = acbca or aceca , with one odd number

        :param s:
        :return: length of longest possible palindrome
        """
        ss = set()
        for i in s:
           if i in ss:
               ss.remove(i)
           else:
               ss.add(i)
        if len(ss) != 0:
            result = len(s) - len(ss)+1
        else:
            result = len(s)
        return result


if __name__ == '__main__':
    st = input()
    print(Solution().longestPalindrome(st))
