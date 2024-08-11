class Solution:
    def finalPositionOfSnake(self, n: int, commands: List[str]) -> int:
        d = {
            "RIGHT": (0, 1),
            "LEFT" : (0, -1),
            "UP" : (-1, 0),
            "DOWN" : (1, 0)
        }
        i, j = 0, 0
        for command in commands:
            i += d[command][0]
            j += d[command][1]
        return i*n + j