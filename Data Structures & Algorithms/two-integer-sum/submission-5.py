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
        #if there are only 2 values then return the by default answer
        #and you can't send the same indices so if a value is repeated then your answer can come wrong toh will have to make 
        #sure that i and j are not the same indices
        
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


        #one very interesting thing claude has come up with is to use a singular loop instead of looping again and again
        #so technically this can help me not write the !=j condition because we will only check if it is inside
        #and if it is inside the jhola then it is not i right now. it is j
        
        if len(nums) == 2:
            return [0,1]

        n = len(nums)
        i  = 0
        
        jhola = {}
        for i,val in enumerate(nums):
            variable = target - val #first check the variable
            if variable in jhola: #then check if it is already in the jhola
                return [j,jhola.get(variable)]
            jhola[val] = i #if it is not then add it and move forward

        #what this will do is 
