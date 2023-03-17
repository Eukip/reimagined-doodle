'''
Given a string s, find the length of the longest 
substring
 without repeating characters.

 

Example 1:

Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.
Example 2:

Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
Example 3:

Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.
 

Constraints:

0 <= s.length <= 5 * 104
s consists of English letters, digits, symbols and spaces.
'''


class Solution(object):
    def lengthOfLongestSubstring(self, s): # 13,5
        """
        :type s: str
        :rtype: int
        """
        char_set = set()
        max_len, start = 0, 0
        for i, c in enumerate(s):
            while c in char_set:
                char_set.remove(s[start])
                start += 1
            char_set.add(c)
            max_len = max(max_len, i - start + 1)
        return max_len
    
    def lengthOfLongestSubstringLessMemory(self, s): # 13
        """
        :type s: str
        :rtype: int
        """
        longest = 0
        sub = ""
        # if char already in substring slice the string until existing char is gone.
        # else append char to str
        for char in s:
            if char not in sub:
                sub += char
            else:
                i = sub.index(char)
                sub = sub[i+1:] + char
            
            if len(sub) > longest:
                longest = len(sub)
            print(sub)
            print(char)
        return longest       
