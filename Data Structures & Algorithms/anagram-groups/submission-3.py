class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        """
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

        #Method 1: brute force O(n^2)
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

        """

        """
        #method 2: create a basic hashmap O(mnlogn)
        #bascially an identity of a word is it's characters. an anagram will have same characters
        #so the key will be the unique characters sorted. And all the anagrams will fall under it's respective key
        #as values

        #defaultdict is a good data structure here
        #will by default have a empty value

        n = len(strs)
        check = defaultdict(list)
        for val in strs:
            a = ''.join(sorted(val)) #so basically sorted(val) gives output ['a','c','t'] and we want 'act' hence joining
            check[a].append(val)

        return list(check.values())

        """

        #Method 3 : 
        #so basically whatever ways we used to identify true and false for an anagram
        #in this situation they are using those ways as keys
        #first method was sorting
        #and now this one is the 26 letter array
        #that will be used as a key for each anagram or club them together
        #we use a tuple here because it is immutable. 
        #key are supposed to be immutable
        #hence we were not able to use sorted(val) as it is a list and list are mutable

        n = len(strs)
        check = defaultdict(list)
        for val in strs:
            count = [0] * 26
            for v in val:
                count[ord(v) - ord('a')] += 1
            check[tuple(count)].append(val)

        return list(check.values())



        """
        Common Pitfalls
        Using a Mutable Key Type for the Hash Map
        When using character frequency arrays as keys, you must convert them to an immutable type (like a tuple in Python or a string in other languages). Lists and arrays are mutable and cannot be used as dictionary keys directly.

        # Wrong: using list as key
        count = [0] * 26
        res[count].append(s)  # TypeError: unhashable type 'list'

        # Correct: convert to tuple
        res[tuple(count)].append(s)
        Assuming Input Contains Only Lowercase Letters
        The frequency array approach with size 26 only works for lowercase English letters. If the input could contain uppercase letters or other characters, the solution would fail or produce incorrect groupings.

        # Wrong: will crash on uppercase
        count[ord(c) - ord('a')] += 1  # Negative index for uppercase

        # Should validate or handle: ord('A') - ord('a') = -32
        Creating a New Key Format That Has Collisions
        When converting frequency counts to strings, using a naive format like concatenation without separators can cause collisions. For example, counts [1,11] and [11,1] could produce the same string "111".

        # Wrong: potential collisions
        key = ''.join(str(c) for c in count)  # "111" for both [1,11] and [11,1]

        # Correct: use separator
        key = ','.join(str(c) for c in count)  # "1,11" vs "11,1"

        """



        
                    