class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        def backtrack(start, curr_combination):
            if len(curr_combination) == k:
                combinations.append(curr_combination[:])
                return
            for i in range(start, n + 1):
                curr_combination.append(i)
                backtrack(i + 1, curr_combination)
                curr_combination.pop()

        combinations = []
        backtrack(1, [])
        return combinations
