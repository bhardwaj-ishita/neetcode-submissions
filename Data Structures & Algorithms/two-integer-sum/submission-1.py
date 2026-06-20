class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        #one thing clear from the question is, that there is always an answer
        #Method 1: brute force
        #that i can think of is we do nested loops
        #start form i = 0 and j = i + 1 and find all the sums. if found. return that answer

        n = len(nums)
        i = 0
        while i < n:
            j = i+1
            while j < n:
                if nums[i] + nums[j] == target:
                    return [i,j]
                j+=1
            i+=1
        