class Solution(object):
    def findLongestChain(self, pairs):
        """
        :type pairs: List[List[int]]
        :rtype: int
        """
        # Sort pairs by the second element
        pairs.sort(key=lambda x: x[1])
        
        # Initialize variables to keep track of the current chain
        max_length = 1
        current_end = pairs[0][1]
        
        # Iterate through pairs to find the maximum chain length
        for pair in pairs[1:]:
            if pair[0] > current_end:
                # If the current pair can extend the chain, update the end
                max_length += 1
                current_end = pair[1]
        
        # Return the maximum chain length
        return max_length
