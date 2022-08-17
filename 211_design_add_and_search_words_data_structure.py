

# https://leetcode.com/problems/design-add-and-search-words-data-structure/discuss/2434478/Python-or-DFS-or-Clean-Trie-Implementation-or-Easy
class TrieNode:
    def __init__(self):
        self.end = False
        self.children = {}


class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:

        def insert(index, root):
            if index == len(word):
                root.end = True
                return
            if word[index] not in root.children:
                root.children[word[index]] = TrieNode()
            insert(index + 1, root.children[word[index]])

        insert(0, self.root)

    def search(self, word: str) -> bool:
        def fun(index, root):
            if index == len(word):
                if root.end:
                    return True
                return False
            if word[index] in root.children:
                return fun(index + 1, root.children[word[index]])
            else:
                if word[index] == '.':
                    for key, value in root.children.items():
                        if fun(index + 1, value):
                            return True
                return False

        return fun(0, self.root)