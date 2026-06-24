class Solution:
    def takeCharacters(self, s: str, k: int) -> int:
        if len(s) <= 1 or k == 1:
            return -1
        return len(s[k:len(s)-k])    