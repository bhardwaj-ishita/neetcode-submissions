class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        #so they are asking to find the anagrams and then club them
        #two actions
        #multiple times
        #finding the anagram is executed multiple times.
        #so we can create a differnt fumction out of it
        #optimized way was o(n) --> hashmap (sets)

        def findAnagram(s: str, t: str) -> bool:
            if len(s) != len(t):
                return False
            n = len(s)
            counter = [0] * 26
            for i in range(n):
                counter[ord(s[i]) - ord('a')] += 1
                counter[ord(t[i]) - ord('a')] -= 1
            
            for val in counter:
                if val != 0:
                    return False
            return True

        #now we will get true or false that if the strings in the list are anagrams
        #best i can think of is nested loops
        #and add a checklist that these are already in the list

        m = len (strs)
        x = 0
        checklist = [0] * m
        ans = []
        while x < m:
            if checklist[x] == 0:
                y = x + 1 
                group = []
                group.append(strs[x])
                checklist[x] = 1
                while y < m:
                    isAnagram = findAnagram(strs[x],strs[y])
                    if isAnagram and checklist[y] == 0:
                        group.append(strs[y])
                        checklist[y] = 1
                    y+=1

                ans.append(group)
            x+=1
        return ans


        
                    