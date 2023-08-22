class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        # Initialize a list to store character counts
        char_count = [0] * 26  # Assuming only lowercase English letters
        
        # Populate the character counts
        for char in s:
            char_count[ord(char) - ord('a')] += 1
        
        # Iterate through the string to find the first unique character
        for i, char in enumerate(s):
            if char_count[ord(char) - ord('a')] == 1:
                return i
        
        # If no unique character is found, return -1
        return -1
