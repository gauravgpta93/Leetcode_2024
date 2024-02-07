from collections import defaultdict


class Solution:

    def create_result(self, words: list[str], hash_index: dict[str | tuple[int, ...], list[int]]) -> list[list[str]]:
        result = []
        for indexes in hash_index.values():
            result.append([words[index] for index in indexes])
        return result

    # sorted hash
    # def create_word_hash(self, word: str) -> str:
    #     return "".join(sorted(word))

    # count through array only for lowercase letters
    def create_word_hash(self, word: str) -> str | tuple[int, ...]:
        letter_count: list[int] = [0] * 26
        for letter in word:
            letter_count[ord(letter) - ord('a')] += 1
        # return tuple(letter_count)
        return ",".join(str(count) for count in letter_count)

    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        hash_index: dict[str | tuple[int, ...], list[int]] = defaultdict(list)
        for index, word in enumerate(strs):
            word_hash = self.create_word_hash(word)
            hash_index[word_hash].append(index)
        return self.create_result(strs, hash_index)


def main():
    answer = Solution()
    assert answer.groupAnagrams(["bdddddddddd", "bbbbbbbbbbc"]) == [["bdddddddddd"], ["bbbbbbbbbbc"]]
    assert answer.groupAnagrams([""]) == [[""]]
    assert answer.groupAnagrams(["a"]) == [["a"]]
    assert answer.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]) == [["eat", "tea", "ate"], ["tan", "nat"],
                                                                                ["bat"]]
    print('All test cases passed.')


if __name__ == '__main__':
    main()
