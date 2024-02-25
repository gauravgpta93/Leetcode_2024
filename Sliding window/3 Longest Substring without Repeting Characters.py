class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        start = end = 0
        max_length = 0
        seen = set()
        while end < len(s):
            if s[end] not in seen:
                seen.add(s[end])
                end += 1
                max_length = max(max_length, end - start)
            else:
                seen.remove(s[start])
                start += 1
        return max_length


def main():
    answer = Solution()
    assert (output := answer.lengthOfLongestSubstring("abcabcbb")) == 3, f"output: {output}"
    assert (output := answer.lengthOfLongestSubstring("bbbbb")) == 1, f"output: {output}"
    assert (output := answer.lengthOfLongestSubstring("pwwkew")) == 3, f"output: {output}"
    assert (output := answer.lengthOfLongestSubstring("")) == 0, f"output: {output}"

    print("All tests passed!")

if __name__ == "__main__":
    main()