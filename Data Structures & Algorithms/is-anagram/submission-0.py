class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if len(s) != len(t):
            return False
            
        s = ''.join(sort(s.lower()))
        t = ''.join(sort(t.lower()))

        if s==t:
            return True
        else:
            return False
        