class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        nums.sort()
        
        sum = 0
        for index in range(0, len(nums), 2):
            sum += nums[index]
            
        return sum