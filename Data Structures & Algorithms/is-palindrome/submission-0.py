class Solution:
    def isPalindrome(self, s: str) -> bool:
        i = 0
        big = "".join(letter for letter in s if letter.isalnum()).lower()
        j = len(big) - 1

        while i <= j:
            if big[i] != big[j]:
                return False
            i += 1
            j -= 1
        return True
