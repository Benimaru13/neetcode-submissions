class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = defaultdict(list) # create a dictionary of unique anagram counts

        for s in strs:
            count = [0] * 26 # this is the template for tracking freq
            
            for ch in s:
                count[ord(ch) - ord("a")] += 1 # track the frequency of each character 
            result[tuple(count)].append(s) # the values are lists so add the values (the valid anagrams) to the keys (the unique letter freq)

        return list(result.values()) # format the output as the input suggests

        