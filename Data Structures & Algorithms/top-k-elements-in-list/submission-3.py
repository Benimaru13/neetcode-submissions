class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #Using bucket sort and getting clever wtih the implementation
        map = {}
        freq = [[] for i in range(len(nums)+1)] 

        for num in nums:
            map[num] = 1 + map.get(num, 0)

        result = []
        for n, count in map.items():
            freq[count].append(n)

        for i in range(len(freq)-1, 0, -1):
            for num in freq[i]:
                result.append(num)

            if len(result) == k:
                return result


        
        