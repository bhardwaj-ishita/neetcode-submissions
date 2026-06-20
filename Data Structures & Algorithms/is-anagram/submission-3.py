class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        """
        #method 0 : brute force O(n^2)
        #so it's the same like duplicates. but we have two strings unlike one. and if somehow we have 2 letters same ones
        #then we need to cross of the count of those letters
        #so basically we need to store that this letter is crossed off.
        #if all the letters are crossed off then it is an anagram

        if len(s) != len(t):
            return False
        n = len(s)
        checklist = [0] * n
        i = 0
        while i < n:
            j = 0
            while j < n:
                if s[i] == t[j] and checklist[j] != 1:
                    checklist[j] = 1 #1 means crossed off
                    break
                j += 1
            i += 1

        x = 0
        while (x < n):
            if checklist[x] == 0:
                return False
            x+=1
        return True
        """


        """
        #method 1: O(nlogn) becoz sorting
        #how to identify an anagram: same letters used to make different words
        #bascially if i sort both of them then both strings will be same

        if len(s) != len(t):
            return False
        s_sorted = sorted(s)
        t_sorted = sorted(t)
        if s_sorted == t_sorted:
            return True
        return False

        """

        #method 2: O(n) bcoz dict()
        #very similar question to duplicate values
        #because we don't require the string in any way we just need to send true and false
        #so we can modify the data structure
        #and because anagrams have same length and same letters used. we just need to check if both unraveled
        #in any way, give us the same core resource
        
        if len(s) != len(t):
            return False        

        n = len(s)
        s_dict = {}
        t_dict= {}
        i = 0
        while (i<n):
            if s[i] in s_dict: 
                s_dict[s[i]] += 1
            else:
                s_dict[s[i]] = 1
            if t[i] in t_dict:
                t_dict[t[i]] += 1
            else:
                t_dict[t[i]] = 1
            i+=1
        
        if t_dict == s_dict:
            return True
        return False
        


        