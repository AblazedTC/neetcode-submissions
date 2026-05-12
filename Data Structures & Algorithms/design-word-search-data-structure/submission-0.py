class TrieNode:
    def __init__(self):
        self.endOfWord = False
        self.children = {}

class WordDictionary:

    def __init__(self):
        self.trie = TrieNode()

    def addWord(self, word: str) -> None:
        cur = self.trie
        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]
        cur.endOfWord = True

    def search(self, word: str) -> bool:

        def helper(cur, i):
            if i == len(word):
                return cur.endOfWord

            c = word[i]

            if c == '.':
                for child in cur.children.values():
                    if helper(child, i + 1):
                        return True
                return False
            else:
                if c not in cur.children:
                    return False
                return helper(cur.children[c], i + 1)

        return helper(self.trie, 0)