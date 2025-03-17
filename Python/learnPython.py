import math

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

solution = Solution()



s = "AB"
numRows = 1
string = solution.convert(s, numRows)
print(string)



