class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        if not strs:
            return ""
        pref = strs[0]
        for s in strs[1:]:
            while s[:len(pref)] != pref:
                pref = pref[:-1]
                if pref == "":
                    return ""
        return pref