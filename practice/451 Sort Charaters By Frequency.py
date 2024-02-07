from collections import defaultdict, Counter


class Solution:
    def create_frequency_letter(
        self, word_frequency: dict[str, int]
    ) -> dict[int, list[str]]:
        frequency_letter = defaultdict(list)
        for letter, frequency in word_frequency.items():
            frequency_letter[frequency].append(letter)
        return frequency_letter

    def create_result(self, frequency_letters: dict[int, list[str]]) -> str:
        result = ""
        # Can sort if since the size is constant
        # for frequency in sorted(frequency_letters.keys(), reverse=True):
        for frequency in range(sum(frequency_letters.keys()), 0, -1):
            if frequency in frequency_letters:
                for letter in frequency_letters[frequency]:
                    result += letter * frequency
        return result

    def frequencySort(self, s: str) -> str:
        word_frequency = Counter(s)
        frequency_letters = self.create_frequency_letter(word_frequency)
        return self.create_result(frequency_letters)


def main():
    answer = Solution()
    assert answer.frequencySort("") == ""
    assert answer.frequencySort("tree") == "eetr"
    assert answer.frequencySort("cccaaa") == "cccaaa"
    assert answer.frequencySort("Aabb") == "bbAa"
    print("All test cases passed.")


if __name__ == "__main__":
    main()
