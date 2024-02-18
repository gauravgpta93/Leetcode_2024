class Solution:
    def find_lower_bound(self, nums: list[int], target: int) -> int:
        left, right = 0, len(nums) - 1
        answer = 0
        while left <= right:
            middle = (left + right) // 2
            if nums[middle] == target:
                return middle
            elif nums[middle] < target:
                answer = middle
                left = middle + 1
            else:
                right = middle - 1
        return answer

    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        if not matrix or not matrix[0] or matrix[0][0] > target or matrix[-1][-1] < target:
            return False
        first_column = [row[0] for row in matrix]
        row_index = self.find_lower_bound(first_column, target)
        column_index = self.find_lower_bound(matrix[row_index], target)
        return matrix[row_index][column_index] == target

def main():
    ans = Solution()
    assert (output := ans.searchMatrix([[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], 3)) is True, output
    assert (output := ans.searchMatrix([[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], 13)) is False, output
    assert (output := ans.searchMatrix([[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], 60)) is True, output

    print("Passed all tests")


if __name__ == "__main__":
    main()
