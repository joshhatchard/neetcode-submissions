class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # one pass solution
        # store all values in a hash map
        # find the number thats the different between target and current
        prevMap = {}

        for i, n in enumerate(nums):
            diff = target - n
            if diff in prevMap:
                return [prevMap[diff], i]
            prevMap[n] = i
        
                