class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        count = []
        for i in s:
            count.append(i)
        
        for j in t:
            if j not in count:
                return False
            count.remove(j)

        return True