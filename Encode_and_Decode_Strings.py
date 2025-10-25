class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            res += str(len(s)) + 'б' + s + 'н'
        return res

    def decode(self, s: str) -> List[str]:
        res = []
        s = s.split('н')[:-1]
        for i in s:
            num, string = i.split('б')
            num = int(num)
            if num > 0:
                res.append(string)
            else:
                res.append("")
        return res
