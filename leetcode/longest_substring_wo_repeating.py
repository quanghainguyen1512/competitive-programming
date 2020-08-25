# https://leetcode.com/problems/longest-substring-without-repeating-characters/

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        uniques = set({})
        s_len = len(s)
        result = 0
        i, j = 0, 0
        while i < s_len and j < s_len:
            if s[j] not in uniques:
                uniques.add(s[j])
                j += 1
                result = max(result, j - i)
            else:
                uniques.remove(s[i])
                i += 1
            if result >= s_len / 2 and i >= s_len / 2:
                break

        return result