#12/01/26 12:54 AM
class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        
        #method 1 (brute forece)
        #i will sort the array first --> because we don't need to send the array, just need to send true or false
        #then i will travel from the first index till the last
        #if i-2 == i-1 then true else if till end nothing found then false

        n = len(nums)
        i = 1
        nums.sort()
        ans = False
        while (i < n):
            if nums[i-1] == nums[i]:
                return True
            i+=1

        return False