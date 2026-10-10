class Solution {
    public boolean hasDuplicate(int[] nums) {
        Hashmap <Integer, Integer> map = new Hashmap<>();
        for (int i = 0; i < nums.length; i++) {
            if map.containsKey(nums[i]) {
                return True;
            }
            map[nums[i]] = 1;
        }
        return False;
    }
}