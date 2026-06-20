#12/01/26 12:54 AM
class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        """    
        #method 2 (brute force) O(n^2)
        #compare each value with other values
        #run a loop on starting from i = 0 then another for i+1 till n-1
        #so there are nested loops

        n = len(nums)
        i = 0
        while(i<n):
            j = i+1
            while(j<n):
                if nums[i] == nums[j]:
                    return True
                j+=1    
            i+=1    

        return False
        """

        """
        #method 2 O(nlogn)
        #i will sort the array first --> because we don't need to send the array, just need to send true or false
        #then i will travel from the first index till the last
        #if i-2 == i-1 then true else if till end nothing found then false

        n = len(nums)
        i = 1
        nums.sort()
        while (i < n):
            if nums[i-1] == nums[i]:
                return True
            i+=1

        return False
        """

        #method 3: O(n)
        #now in O(n) we used a sort method which is taking time right?
        #so how can we remove that sort method. 
        #we bascially need to store the values in a place where we can do a lookup in O(1) instead of O(logn) {which was sort}
        #that data structure is hash map basically a dict in python
        #so in python we have two ways of building a hashmap (dict or set)
        #dict stores a key value pair : now we don't want the array intact so we don't care about the index
        #in set we only care about the values. just to check if i have seen this before
        #so a set it is

        n = len(nums)
        i = 0
        jhola = set()
        while (i<n):
            if nums[i] in jhola:
                return True
            jhola.add(nums[i])
            i+=1
        
        return False
        


        


