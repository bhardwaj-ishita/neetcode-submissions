class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        """
        #one thing clear from the question is, that there is always an answer
        #Method 1: brute force O(n^2)
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

        """

        #method 2: O(n)
        #so right now in this equation nums[i] + nums[j] == target there are two variable. nums[i] and nums[j]
        #we know the target
        #so if i reverse my findings i.e. i use the equation target - nums[i] = nums[j] then i just need to find nums[j]
        #and this becomes linear then

        #also remember now that we just need to find nums[j] we need a jhola. have we seen any value which resembles target - nums[i]
        if len(nums) == 2:
            return [0,1]

        n = len(nums)
        i  = 0
        
        jhola = {}
        for i,val in enumerate(nums):
            jhola[val] = i 

        j = 0
        while j < n:
            variable = target - nums[j] 
            print(variable)
            if variable in jhola and jhola.get(variable) != j:
                return [j,jhola.get(variable)]
            j+=1
