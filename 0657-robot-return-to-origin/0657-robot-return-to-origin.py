class Solution:
    def judgeCircle(self, moves: str) -> bool:
        m = {'L':(0,-1),'R':(0,1),'U':(1,1),'D':(1,-1)}
        curr = [0,0]
        for mov in moves:
            curr[m[mov][0]] += m[mov][1]
        return curr[0] == 0 and curr[1] == 0
            