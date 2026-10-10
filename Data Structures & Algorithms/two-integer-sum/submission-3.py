class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        s_nums = sorted(nums)
        i = 0
        j = len(s_nums) - 1
        while (s_nums[i] + s_nums[j]) != target :
            sum = s_nums[i] + s_nums[j]
            if sum > target:
                j -= 1
            else:
                i += 1
        return [i,j]
