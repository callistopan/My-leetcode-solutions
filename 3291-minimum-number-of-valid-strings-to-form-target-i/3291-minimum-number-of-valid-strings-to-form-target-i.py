class Trie:
    def __init__(self):
        self.children: List[Optional[Trie]] = [None] * 26
        self.isEnd: bool = False

    def insert(self, word: str) -> None:
        node = self
        for ch in word:
            idx = ord(ch) - ord("a")
            if not node.children[idx]:
                node.children[idx] = Trie()
            node = node.children[idx]
        node.isEnd = True

    def search(self, prefix: str) -> bool:
        node = self
        for ch in prefix:
            idx = ord(ch) - ord("a")
            if not node.children[idx]:
                return False
            node = node.children[idx]
        return node.isEnd

class Solution:
    def minValidStrings(self, words: List[str], target: str) -> int:
        trie = Trie()
        for w in words:
            trie.insert(w)
        n = len(target)
        @cache
        def dfs(i):
            if i == len(target):
                return 0
            ans = inf
            node = trie
            for j in range(i, n):
                idx = ord(target[j]) - ord("a")
                if not node.children[idx]:
                    break
                node = node.children[idx]
                ans = min(ans, dfs(j + 1) + 1)
            return ans
        return dfs(0) if dfs(0) != inf else -1