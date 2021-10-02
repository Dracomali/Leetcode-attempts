# determines if a number is a palindrome

class Solution:
    def isPalindrome(self, x: int) -> bool:

        num = str(x)

        numbers = [num[y] for y in reversed(range(0, len(num)))]
        
        num2 = "".join(numbers)

        if num == num2:
            return True

        else:
            return False