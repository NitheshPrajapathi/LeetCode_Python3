class Solution:
    #@param nums
    #return targe indices from list num
    def twoSum(self, nums, target: int):
        d={}
        #iterate and check the diff val in nums add to d
        #Simple idea if the val not in d just add with index as key<-val else directly return.
        for index,value in enumerate(nums):
            diff=target-value
            if diff in d:
                return [d[diff],index]
            d[value]=index
                

obj=Solution()
nums=[2,7,4,5,6]
print(obj.twoSum(nums, 9))