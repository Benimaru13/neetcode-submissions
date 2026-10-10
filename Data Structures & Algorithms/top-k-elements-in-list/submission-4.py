class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        num_map = {}
        res = []
        for i in range(len(nums)):
            num_map[nums[i]] = num_map.get(nums[i], 0) + 1

        key_rev = {val: key for key, val in num_map.items()}
        counts = sorted([num for num in key_rev.keys()])

        while k >= 1:
            mode = counts.pop()
            value = key_rev[mode]
            res.append(value)
            k -= 1

        return res

            