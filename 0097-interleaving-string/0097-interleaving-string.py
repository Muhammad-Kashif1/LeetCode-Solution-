class Solution(object):
    def isInterleave(self, s1, s2, s3):
        """
        :type s1: str
        :type s2: str
        :type s3: str
        :rtype: bool
        """
        len_s1, len_s2, len_s3 = len(s1), len(s2), len(s3)
        
        # If the lengths of s1 and s2 don't add up to the length of s3, it's impossible
        if len_s1 + len_s2 != len_s3:
            return False
        
        # Use a single 1D array to store the DP values
        dp = [False] * (len_s2 + 1)
        
        # Base case: an empty s1 and empty s2 can form an empty s3
        dp[0] = True
        
        # Fill the 1D DP array
        for i in range(len_s1 + 1):
            for j in range(len_s2 + 1):
                if i > 0:
                    dp[j] = dp[j] and s1[i - 1] == s3[i + j - 1]
                if j > 0:
                    dp[j] = dp[j] or (dp[j - 1] and s2[j - 1] == s3[i + j - 1])
        
        return dp[len_s2]
