class Solution:
    # def get_max_substring_for_character(self, original_string: str, character: str, k: int) -> int:
    #     start = 0
    #     max_value = 0
    #     for index, char in enumerate(original_string):
    #         if char == character:
    #             max_value = max(max_value, index - start + 1)
    #         else:
    #             if k > 0:
    #                 k -= 1
    #                 max_value = max(max_value, index - start + 1)
    #             else:
    #                 while original_string[start] == character:
    #                     start += 1
    #                 start += 1
    #     return max_value
    #
    # def characterReplacement(self, s: str, k: int) -> int:
    #     unique_characters = set(s)
    #     max_length = 0
    #     for character in unique_characters:
    #         max_length = max(max_length, self.get_max_substring_for_character(s, character, k))
    #     return max_length

    # With a single pass
    def characterReplacement(self, s: str, k: int) -> int:
        start = 0
        max_length = 0
        max_frequency = 0
        hash = {}
        for current_index, char in enumerate(s):
            hash[char] = hash.get(char, 0) + 1
            max_frequency = max(max_frequency, hash[char])
            if (current_index - start + 1) - max_frequency <= k:
                max_length = max(max_length, current_index - start + 1)
            else:
                hash[s[start]] -= 1
                start += 1
        return max_length
def main():
    answer = Solution()
    # assert (output := answer.get_max_substring_for_character("ABAB", "A", 2)) == 4, f"output: {output}"
    assert (output := answer.characterReplacement("ABAB", 2)) == 4, f"output: {output}"
    assert (output := answer.characterReplacement("AABABBA", 1)) == 4, f"output: {output}"

    print("All tests passed!")

if __name__ == "__main__":
    main()