class Solution:

    @staticmethod
    def isIsomorphic(s: str, t: str) -> bool:
        """
        Created two dict sdict and tdict while will keep checking whether stings are isomorphic or not
        in sdict - keys : char in string s
                    values : char in string t
        in tdict - keys : char in string t
                    values : char in string s
        td-c
        :param s:
        :param t:
        :return:bool : True if isomorphic else False
        """
        sdict = {}
        tdict = {}
        n = len(s)
        for i in range(n):
            if s[i] in sdict.keys() and t[i] != sdict.get(s[i]):
                return False
            if t[i] in tdict.keys() and s[i] != tdict.get(t[i]):
                return False

            sdict[s[i]] = t[i]
            tdict[t[i]] = s[i]
        return True


if __name__ == '__main__':
    """
    Given two strings s and t, determine if they are isomorphic.
    
    Two strings s and t are isomorphic if the characters in s can be replaced to get t.
    
    All occurrences of a character must be replaced with another character
    while preserving the order of characters. No two characters may map to the same character, 
    but a character may map to itself.

    """

    sol = Solution
    print('input - ')
    s = input()
    t = input()
    print(sol.isIsomorphic(s=s, t=t))
