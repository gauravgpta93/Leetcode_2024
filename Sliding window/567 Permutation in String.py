from collections import Counter


class Solution:
    def check_counter_match(
        self, current_count: dict[str, int], subset_count: dict[str, int]
    ) -> bool:
        for key in subset_count:
            if subset_count[key] != current_count.get(key, 0):
                return False
        return True

    def checkInclusion(self, s1: str, s2: str) -> bool:
        subset_count: dict[str, int] = Counter(s1)
        hash_count: dict[str, int] = {}
        start = end = 0
        while end < len(s2):
            hash_count[s2[end]] = hash_count.get(s2[end], 0) + 1
            if self.check_counter_match(hash_count, subset_count):
                return True
            end += 1
            if end - start + 1 > len(s1):
                hash_count[s2[start]] -= 1
                start += 1
        return False

def main():
    ans = Solution()
    assert (result := ans.checkInclusion("ab", "eidbaooo")) == True, result
    assert (result := ans.checkInclusion("ab", "eidboaoo")) == False, result
    assert (result := ans.checkInclusion("adc", "dcda")) == True, result
    assert (result := ans.checkInclusion("hello", "ooolleoooleh")) == False, result
    assert (result := ans.checkInclusion("hello", "ooolleoooleh")) == False, result
    assert (result := ans.checkInclusion("h", "ooolleoooleh")) == True, result
    assert (result := ans.checkInclusion("h", "hooolleooole")) == True, result
    assert (result := ans.checkInclusion("z", "hooolleooole")) == False, result

    print("Passed all test cases!")


if __name__ == "__main__":
    main()
