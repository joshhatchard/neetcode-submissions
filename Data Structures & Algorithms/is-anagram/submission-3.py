from collections import Counter

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sFreq = {}
        tFreq = {}

        for c1, c2 in zip(s, t):
            sFreq[c1] = sFreq.get(c1, 0) + 1
            tFreq[c2] = tFreq.get(c2, 0) + 1

        return sFreq == tFreq and len(s) == len(t)