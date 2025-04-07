import math

class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = None

class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if needle is None:
            return -1 
        
        for pos in range(0, len(haystack)):
            if(haystack[pos : pos + len(needle)] == needle) :
                return pos
        return -1
    
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        left = 0
        right = len(nums)
        while(left < right and right > 0):
            middle = (left + right) // 2
            if target == nums[middle] :
                return middle
            elif target < nums[middle]:
                right = middle
            else:
                left = middle + 1
        return left
        
    def lengthOfLastWord(self, s):
            """
            :type s: str
            :rtype: int
            """
            maxLenSubString = 0
            in_word = False
            for char in reversed(s):
                if char == " ":
                    if in_word:
                        maxLenSubString = 0  
                        break  # Stop counting once the last word ends
                else:
                    in_word = True
                    maxLenSubString += 1

            return maxLenSubString
    
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        i = len(digits) -1
        while digits[i] == 9:
            digits[i] = 0
            i -= 1
        if i == -1:
            digits.insert(0, 1)
        else:
            digits[i] += 1   
        return digits

    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        if not s:
            return ""

        def expand_around_center(left, right):
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            return s[left + 1:right]  # Return the valid palindrome substring

        longest = ""
        
        for i in range(len(s)):
            # Odd length palindrome (e.g., "aba")
            odd_palindrome = expand_around_center(i, i)
            # Even length palindrome (e.g., "abba")
            even_palindrome = expand_around_center(i, i + 1)

            # Update longest palindrome found
            longest = max(longest, odd_palindrome, even_palindrome, key=len)

        return longest           

    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows == 1 or len(s) == 1 or numRows >= len(s) :
            return s
        res = [""]*numRows
        index, step = 0, 1 #step is move up or down
        for char in s:
            res[index] += char
            if index == 0:
                step = 1
            elif index == numRows -1:
                step = -1
            index += step
        return "".join(res)
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        left, right = 0, len(height) - 1
        maxWater = 0
        while(left < right):
            water = min(height[left], height[right]) * (right - left)
            maxWater = max(water, maxWater)
            if height[left] < height[right]:
               left += 1
            else:
                right -= 1
        return maxWater
    
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        values = [
            (1000, "M"), (900, "CM"), (500, "D"), (400, "CD"),
            (100, "C"), (90, "XC"), (50, "L"), (40, "XL"),
            (10, "X"), (9, "IX"), (5, "V"), (4, "IV"), (1, "I")
        ]

        roman = ""
        
        for value, symbol in values:
            while num >= value:
                num -= value
                roman += symbol  # Append the corresponding Roman numeral

        return roman
    
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        nums.sort()  # Sort the array to use two-pointer efficiently
        res = []
        n = len(nums)

        for i in range(n - 3):  # First number
            if i > 0 and nums[i] == nums[i - 1]:  # Skip duplicates
                continue
            for j in range(i + 1, n - 2):  # Second number
                if j > i + 1 and nums[j] == nums[j - 1]:  # Skip duplicates
                    continue
                
                left, right = j + 1, n - 1  # Two-pointer technique
                while left < right:
                    total = nums[i] + nums[j] + nums[left] + nums[right]
                    if total == target:
                        res.append([nums[i], nums[j], nums[left], nums[right]])
                        # Skip duplicates
                        while left < right and nums[left] == nums[left + 1]:
                            left += 1
                        while left < right and nums[right] == nums[right - 1]:
                            right -= 1
                        left += 1
                        right -= 1
                    elif total < target:
                        left += 1
                    else:
                        right -= 1
        return res
    
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        triangle = [[1]]
    
    # Generate subsequent rows
        for i in range(1, numRows):
            prev_row = triangle[-1]  # Get the previous row
            new_row = [1]  # Every row starts with 1
            
            # Calculate middle elements
            for j in range(1, i):
                new_row.append(prev_row[j-1] + prev_row[j])
            
            new_row.append(1)  # Every row ends with 1
            triangle.append(new_row)
        
        return triangle

    def inorderTraversal(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[int]
        """
        result = []

        def inorder(node):
            if node:
                inorder(node.left)
                result.append(node.val)
                inorder(node.right)

        inorder(root)
        return result
    
    def recoverTree(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: None Do not return anything, modify root in-place instead.
        """
        self.first = self.second = self.prev = None

        def inorder(node):
            if not node:
                return
            
            inorder(node.left)

            if self.prev and node.val < self.prev.val:
                if not self.first:
                    self.first = self.prev
                self.second = node
            
            self.prev = node

            inorder(node.right)

        inorder(root)

        # Swap the values of the two incorrect nodes
        if self.first and self.second:
            self.first.val, self.second.val = self.second.val, self.first.val

    def isSymmetric(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: bool
        """
        if not root:
            return True

        queue = deque()
        queue.append((root.left, root.right))

        while queue:
            t1, t2 = queue.popleft()
            if not t1 and not t2:
                continue
            if not t1 or not t2 or t1.val != t2.val:
                return False
            
            queue.append((t1.left, t2.right))
            queue.append((t1.right, t2.left))

        return True
    
    def findWords(self, board, words):
        """
        :type board: List[List[str]]
        :type words: List[str]
        :rtype: List[str]
        """
        root = TrieNode()
        for word in words:
            node = root
            for char in word:
                if char not in node.children:
                    node.children[char] = TrieNode()
                node = node.children[char]
            node.word = word  # đánh dấu từ hoàn chỉnh

        rows, cols = len(board), len(board[0])
        result = []

        def dfs(r, c, node):
            char = board[r][c]
            if char not in node.children:
                return

            next_node = node.children[char]
            if next_node.word:
                result.append(next_node.word)
                next_node.word = None  # tránh trùng lặp

            board[r][c] = "#"  # đánh dấu đã đi qua
            for dr, dc in [(-1,0), (1,0), (0,-1), (0,1)]:
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols and board[nr][nc] != "#":
                    dfs(nr, nc, next_node)
            board[r][c] = char  # khôi phục lại ký tự sau DFS

            # Xóa nhánh đã dùng xong để tối ưu bộ nhớ
            if not next_node.children:
                node.children.pop(char)

        for r in range(rows):
            for c in range(cols):
                dfs(r, c, root)

        return result
    

        


solution = Solution()

print(solution.generate(5))





