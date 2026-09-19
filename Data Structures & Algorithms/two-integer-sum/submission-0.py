class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        map = {num: i for (i, num) in enumerate(nums)}
        for i in range(len(nums)):
            comp = target - nums[i]
            if comp in map and i != map[comp]:
                return [i,map[comp]]