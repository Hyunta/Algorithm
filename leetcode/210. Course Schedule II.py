class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        require = {i: set() for i in range(numCourses)}
        roadmap = defaultdict(set)

        for target_course, require_course in prerequisites:
            require[target_course].add(require_course)
            roadmap[require_course].add(target_course)

        res = []
        q = deque()
        for key in require:
            if not require[key]:
                q.append(key)

        while q:
            course = q.popleft()
            res.append(course)
            for target in roadmap[course]:
                require[target].remove(course)
                if not require[target]:
                    q.append(target)
        if len(res) == numCourses:
            return res
        return []
