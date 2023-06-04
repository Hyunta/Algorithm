class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        NOT_CHECKED, CHECKING, COMPLETED = 0, 1, 2

        def has_deadlock(course) -> bool:
            if course_states[course] == CHECKING:
                return True
            elif course_states[course] == COMPLETED:
                return False

            course_states[course] = CHECKING
            for pre_course in requirements[course]:
                if has_deadlock(pre_course):
                    return True

            course_states[course] = COMPLETED
            return False

        requirements = defaultdict(list)
        for a, b in prerequisites:
            requirements[a].append(b)

        course_states = [NOT_CHECKED for _ in range(numCourses)]
        for i in range(numCourses):
            if has_deadlock(i):
                return False
        return True
