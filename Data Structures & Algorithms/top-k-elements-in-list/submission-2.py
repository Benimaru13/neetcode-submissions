class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        map = {}
        for num in nums:
            if num in map:
                map[num] += 1
            else:
                map[num] = 1
        
        k_list = [value for value in map.values()]
        k_list.sort(reverse=True)
        ans = []

        for i in range(k):
            value = k_list[i]
            for key, item in map.items():
                if item == value and key not in ans:
                    ans.append(key)

        return ans    

        