## Valid anagram

class Solution:

    # Basic Solution
    # def isAnagram(self, s: str, t: str) -> bool:
    #     if len(s) != len(t): return False
    #     letter_count: dict[str, int] = {}
    #     for letter in s:
    #         count = letter_count.get(letter, 0) + 1
    #         letter_count[letter] = count
    #     for letter in t:
    #         count = letter_count.get(letter, 0) - 1
    #         if count < 0:
    #             return False
    #         letter_count[letter] = count
    #     return True

    # Single loop solution
    # def isAnagram(self, s: str, t: str) -> bool:
    #     if len(s) != len(t):
    #         return False
    #     letter_count: dict[str, int] = {}
    #     for i in range(len(s)):
    #         letter_count[s[i]] = letter_count.get(s[i], 0) + 1
    #         letter_count[t[i]] = letter_count.get(t[i], 0) - 1
    #     return all(count == 0 for count in letter_count.values())

    # inbuild counter library
    def isAnagram(self, s: str, t: str) -> bool:
        from collections import Counter
        return Counter(s) == Counter(t)

def main():
    assert Solution().isAnagram("", "")
    assert Solution().isAnagram("anagram", "nagaram")
    assert not Solution().isAnagram("rat", "car")
    assert not Solution().isAnagram("a", "ab")
    print('All test cases passed.')


if __name__ == '__main__':
    main()
