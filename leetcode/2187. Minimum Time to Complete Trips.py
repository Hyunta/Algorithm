class Solution:
    def minimumTime(self, time: List[int], totalTrips: int) -> int:
        lt, rt = 1, min(time) * totalTrips

        def countTrip(pt: int):
            tot = 0
            for x in time:
                tot += pt // x
            return tot

        while lt < rt:
            mid = (lt + rt) // 2
            if countTrip(mid) >= totalTrips:
                rt = mid
            else:
                lt = mid + 1
        return lt
