class Solution:

    def encode(self, strs: List[str]) -> str:
        if len(strs) > 0:
            word = " ".join(strs)
        else:
            word = ""
        return word

    def decode(self, s: str) -> List[str]:
        if len(s) > 0:
            str_list = s.split(" ")
        else:
            return []
        return str_list


