class Solution:
    def firstPalindrome(self, words: list[str]) -> str:
        for word in words:
            if word == word[::-1]:
                return word
        return ""


def main():
    answer = Solution()
    assert answer.firstPalindrome(["abcd", "dcba", "lls", "s", "sssll"]) == "s"
    assert answer.firstPalindrome(["abc", "car", "ada", "racecar", "cool"]) == "ada"
    assert answer.firstPalindrome(["notapalindrome", "racecar"]) == "racecar"
    print("All test cases passed.")


if __name__ == "__main__":
    main()
