class Solution:
    def isPalindrome(self, s: str) -> bool:
        big = "".join(letter for letter in s if letter.isalnum()).lower()
        return big == big[::-1]
