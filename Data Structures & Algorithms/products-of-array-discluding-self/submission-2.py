import math
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # This is the prefix and postfix method
        pre = 1
        post = 1
        output = [1] * len(nums)

        # calculate the prefix
        for i in range(len(nums)):
            output[i] = pre # add the prefix (up until this point)
            pre = nums[i] * pre #update the prefix
           

        for j in range(len(nums)-1, -1, -1):
            output[j] *= post # multiply the postfix (up until this point)
            post = nums[j] * post # update the postfix
            

        return output