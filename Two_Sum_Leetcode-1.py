class Solution:
    #@param nums
    #return targe indices from list num
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d={}
        #iterate and check the diff val in nums add to d

        for index,value in enumerate(nums):
            diff=target-value #checking for the diff
            if diff in d: #did difference encounter to d
                return d[diff],index  #return if already present
            
            d[value]=index  #Else assign the value with the index
