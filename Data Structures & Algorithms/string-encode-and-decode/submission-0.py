class Solution:

    def encode(self, strs: List[str]) -> str:
        word = " ".join(strs)
        return word

    def decode(self, s: str) -> List[str]:
        str_list = s.split(" ")
        return str_list
        

