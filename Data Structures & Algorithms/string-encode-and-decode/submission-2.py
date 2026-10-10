class Solution:

    def encode(self, strs: List[str]) -> str:
        if len(strs) > 1:
            word = " ".join(strs)
        else:
            word = strs[0]
        return word

    def decode(self, s: str) -> List[str]:
        str_list = []
        
        if len(s.split(" ")) <= 1:
            str_list.append(s)
        else:
            str_list = s.split(" ")
        return str_list


