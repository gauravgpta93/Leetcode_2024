class Solution:
    # def get_lower_alpha_numeric(self, word: str) -> str:
    #     return ''.join([letter.lower() for letter in word if letter.isalnum()])
    #
    # def isPalindrome(self, s: str) -> bool:
    #     word = self.get_lower_alpha_numeric(s)
    #     start_pointer, end_pointer = 0, len(word) - 1
    #     while start_pointer < end_pointer:
    #         if word[start_pointer] != word[end_pointer]:
    #             return False
    #         start_pointer += 1
    #         end_pointer -= 1
    #     return True

    # check in single loop
    def isPalindrome(self, s: str) -> bool:
        start_pointer, end_pointer = 0, len(s) - 1
        while start_pointer < end_pointer:
            if not s[start_pointer].isalnum():
                start_pointer += 1
                continue
            if not s[end_pointer].isalnum():
                end_pointer -= 1
                continue
            if s[start_pointer].lower() != s[end_pointer].lower():
                return False
            start_pointer += 1
            end_pointer -= 1
        return True


def main():
    assert Solution().isPalindrome("") == True
    assert Solution().isPalindrome(" ") == True
    assert Solution().isPalindrome("A man, a plan, a canal: Panama") == True
    assert Solution().isPalindrome("race a car") == False
    assert Solution().isPalindrome("0P") == False
    print('All test cases passed!')


if __name__ == "__main__":
    main()