class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        char_last_idx_dict = {}
        start, max_length = 0, 0
        for end in range(len(s)):
            if (s[end] in char_last_idx_dict) and (char_last_idx_dict[s[end]] >= start):
                start = char_last_idx_dict[s[end]] + 1
            char_last_idx_dict[s[end]] = end
            max_length = max(max_length, end-start+1)
        return max_length
