
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
    
    def removeNthFromEnd(self, head, n):
        """
        :type head: Optional[ListNode]
        :type n: int
        :rtype: Optional[ListNode]
        """
        count = 1
        temp = head
        prev = ListNode(0, head)
        
        while temp.next is not None:
            count += 1
            temp = temp.next

        if count == n:
            return head.next

        temp = head
        while temp is not None:
            if count == n:
                prev.next = temp.next
                return head
            prev = temp
            temp = temp.next
            count -= 1

    def deleteDuplicates(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        if not head:
            return None
        prev, curr = head, head.next
        while curr:
            if prev.val == curr.val:
                prev.next = curr.next
            else:
                prev = curr
            curr = curr.next
        return head

class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next      

solution = Solution()
a = solution.letterCombinations("23")
print(a)