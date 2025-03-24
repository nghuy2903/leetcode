from collections import deque


class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """    
        queue = deque()
        queue.append(("", 0, 0))  # (current string, open_count, close_count)
        result = []

        while queue:
            s, open_count, close_count = queue.popleft()

            if len(s) == 2 * n:
                result.append(s)
                continue

            if open_count < n:
                queue.append((s + "(", open_count + 1, close_count))

            if close_count < open_count:
                queue.append((s + ")", open_count, close_count + 1))

        return result

solution = Solution()   
n = 3

print(solution.generateParenthesis(n))
