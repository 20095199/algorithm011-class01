from collections import defaultdict, deque


class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:

        size, general_dic = len(beginWord), defaultdict(list)
        for w in wordList:
            for _ in range(size):
                general_dic[w[:_]+"*"+w[_+1:]].append(w)
        # BFS
        queue = deque()
        queue.append((beginWord, 1)) 
        visited = set()
        while queue:
            word, level = queue.popleft()
            if word in visited:
                continue
            if word == endWord: 
                return level
            visited.add(word)
            for i in range(size):            
                for tmp in general_dic[word[:i]+"*"+word[i+1:]]:
                    queue.append((tmp, level+1)) 
        return 0

