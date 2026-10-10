class Solution {
    public boolean isAnagram(String s, String t) {
        for (int i = 0; i < s.length; i++) {
            if (s[i] != t[i]) {
                return false;
            }
        }
        return true;
    }
}
