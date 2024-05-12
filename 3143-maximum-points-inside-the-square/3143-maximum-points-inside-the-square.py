class Solution:
    def maxPointsInsideSquare(self, points: List[List[int]], s: str) -> int:
        
        tag_rs = defaultdict(list)
        for (a, b), tag in zip(points, s):
            tag_rs[tag].append(max(abs(a), abs(b)))
        print(tag_rs)
        max_radius = inf   # beyond this point it is not possible to create a square
        for rads in tag_rs.values():
            rads.sort()
            if len(rads) > 1:
                max_radius = min(max_radius, rads[1])
        print(max_radius)
        return sum(max(abs(b), abs(a)) < max_radius for a, b in points)
                    