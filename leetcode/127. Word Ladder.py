class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0

        l = len(beginWord)
        all_words = defaultdict(list)
        for word in wordList:
            for i in range(l):
                all_words[word[:i] + "*" + word[i + 1:]].append(word)

        q = deque()
        visited = set()

        q.append((beginWord, 1))
        visited.add(beginWord)

        while q:
            curr_word, curr_lev = q.popleft()

            for i in range(l):
                mid_word = curr_word[:i] + "*" + curr_word[i + 1:]
                for word in all_words[mid_word]:
                    if word == endWord:
                        return curr_lev + 1
                    if word not in visited:
                        visited.add(word)
                        q.append((word, curr_lev + 1))
        return 0