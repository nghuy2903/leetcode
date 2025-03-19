
class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if not digits:
            return []

        # Mapping of digits to corresponding letters
        digit_to_letters = {
            '2': "abc",
            '3': "def",
            '4': "ghi",
            '5': "jkl",
            '6': "mno",
            '7': "pqrs",
            '8': "tuv",
            '9': "wxyz"
        }

        # Initialize a queue with an empty string (starting point)
        queue = [""]
        
        # Process each digit in the input
        for digit in digits:
            if digit not in digit_to_letters:
                continue  # Skip invalid digits

            letters = digit_to_letters[digit]
            new_queue = []  # Temporary list to store new combinations
            
            # Generate new combinations by appending each letter
            for prefix in queue:
                for letter in letters:
                    new_queue.append(prefix + letter)

            # Update queue with the new combinations
            queue = new_queue

        return queue
       

solution = Solution()
a = solution.letterCombinations("23")
print(a)