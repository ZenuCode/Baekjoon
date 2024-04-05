class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        arr = []
        cars = zip(position, speed)
        for pos, speed in sorted(cars, reverse=True):
            arr.append((target - pos) / speed)
            if len(arr) > 1 and arr[-1] <= arr[-2]:
                    arr.pop()
        return len(arr)