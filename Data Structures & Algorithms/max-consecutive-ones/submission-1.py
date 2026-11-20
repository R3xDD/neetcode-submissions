class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        array = []
        k= 0
        for i in range(len(nums)):
            if nums[i] == 1:
                k +=1
            else : 
                k=0
            array.append(k) 
        return max(array)
