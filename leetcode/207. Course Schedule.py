class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = defaultdict(list)
        pre_nums = [0] * numCourses
        for a, b in prerequisites:
            graph[a].append(b)
            pre_nums[b] += 1

        q = deque()
        for idx, val in enumerate(pre_nums):
            if val == 0:
                q.append(idx)

        while q:
            x = q.popleft()
            targets = graph[x]

            for t in targets:
                pre_nums[t] -= 1
                if pre_nums[t] == 0:
                    q.append(t)

        return all(pre_num == 0 for pre_num in pre_nums)
