class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        freq = [[] for n in range(len(nums) + 1)] # make the bucket for frequencies

        # hashmap of num and freq
        for num in nums:
            count[num] = count.get(num, 0) + 1

        for n,f in count.items():
            freq[f].append(n) # build up frequency buckets

        result = []
        for f in range(len(nums), 0, -1): # iterate backwards 
            for num in freq[f]: 
                if len(result) == k:
                    return result
                else:
                    result.append(num)
        
        return result

            