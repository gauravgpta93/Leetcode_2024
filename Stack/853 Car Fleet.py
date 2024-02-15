class Solution:
    def carFleet(self, target: int, position: list[int], speed: list[int]) -> int:
        cars = sorted(zip(position, speed), reverse=True)
        # times = [(target - pos) / spd for pos, spd in cars]
        result = []
        for pos, spd in cars:
            time = (target - pos) / spd
            if not result or time > result[-1]:
                result.append(time)
        return len(result)


def main():
    target = 12
    position = [10, 8, 0, 5, 3]
    speed = [2, 4, 1, 1, 3]
    assert (
        result := Solution().carFleet(target, position, speed)
    ) == 3, f"unexpected {result=}"

    target = 10
    position = [6, 8]
    speed = [3, 2]
    assert (
        result := Solution().carFleet(target, position, speed)
    ) == 2, f"unexpected {result=}"

    print("All test cases passed!")


if __name__ == "__main__":
    main()
