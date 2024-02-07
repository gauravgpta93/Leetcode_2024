from typing import List


class Solution:
    def serialize_list(self, word_count: List[int]) -> str:
        return "[" + ",".join(str(count) for count in word_count) + "]"

    def deserialize_list(self, word_count_string: str) -> List[int]:
        return [int(count) for count in word_count_string[1:-1].split(",")]

    def encode(self, strs: List[str]) -> str:
        if not strs:
            return ""
        word_count: List[int] = [len(word) for word in strs]
        return self.serialize_list(word_count) + "".join(strs)

    def decode(self, s: str) -> List[str]:
        if s == "":
            return []
        split_index = s.find("]")
        word_count_string = s[:split_index + 1]
        word_count = self.deserialize_list(word_count_string)
        result: List[str] = []
        start_index = split_index + 1
        for count in word_count:
            result.append(s[start_index:start_index + count])
            start_index += count
        return result


def main():
    answer = Solution()
    assert answer.decode(answer.encode([])) == []
    assert answer.decode(answer.encode([""])) == [""]
    assert answer.decode(answer.encode(["hello", "world"])) == ["hello", "world"]
    assert answer.decode(answer.encode(["hello", "world", ""])) == ["hello", "world", ""]
    assert answer.decode(answer.encode(["we", "say", ":", "yes"])) == ["we", "say", ":", "yes"]

    print('All test cases passed!')


if __name__ == '__main__':
    main()