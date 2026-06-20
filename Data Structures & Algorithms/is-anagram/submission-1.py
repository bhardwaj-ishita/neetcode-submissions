class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        #method 1: O(nlogn) becoz sorting
        #how to identify an anagram: same letters used to make different words
        #bascially if i sort both of them then both strings will be same

        s_sorted = sorted(s)
        t_sorted = sorted(t)
        if s_sorted == t_sorted:
            return True
        return False

        #method 2: O(n) bcoz dict()
        #very similar question to duplicate values
        #because we don't require the string in any way we just need to send true and false
        #so we can modify the data structure
        #and because anagrams have same length and same letters used. we just need to check if both unraveled
        #in any way, give us the same core resource


        