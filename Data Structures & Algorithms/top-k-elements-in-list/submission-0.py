class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #no index is required
        #no array is required as it is
        #only the count and the value
        #so we can sort --> which means we can hashmap it
        #run the loop once and save it in a lookup
        #and then run the loop again to just get the top two values

        #method 1: o(nlogn)
        #just hashmap it --> key value pair
        n = len(nums)
        jhola = {}
        for i,val in enumerate(nums):
            jhola[val] = 1 + jhola.get(val,0)

        #once the values are stored. now the problem which i faced was to get the top k out in the return
        #so for that you first dump the val,count into a list as count,val
        #sort this shit descending order in terms of count
        #and then append it in a new resulting list (pop shits the biggest number that is the number at the end)
        #then return it
        #for god's sake
        sorter = []
        for num,cnt in jhola.items():
            sorter.append([cnt,num])
        sorter.sort()
        print(sorter)
        ans = []
        while len(ans) < k:
            ans.append(sorter.pop()[1])
        return ans
        



        
        