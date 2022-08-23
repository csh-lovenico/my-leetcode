class TrieNode:
    def __init__(self):
        # sub: dict[str, TrieNode]
        self.sub = dict()
        # itself: if itself is stored
        self.itself = False

    def check_exist(self, c: chr):
        return c in self.sub.keys()

    def get_sub(self, c: chr) -> 'TrieNode':
        if not self.check_exist(c):
            self.create_sub(c)
        return self.sub[c]

    def create_sub(self, c: chr):
        self.sub[c] = TrieNode()

    def search(self, root: 'TrieNode', s: str) -> bool:
        if s == "":
            return root.itself
        c = s[0]
        if root.check_exist(c):
            return root.search(root.get_sub(c), s[1:])
        else:
            return False

    def add(self, root: 'TrieNode', s: str):
        if s == "":
            root.itself = True
            return
        c = s[0]
        root.add(root.get_sub(c), s[1:])

    def starts_with(self, root: 'TrieNode', s: str):
        if len(s) == 0:
            return len(root.sub) != 0 or root.itself
        else:
            c = s[0]
            if not root.check_exist(c):
                return False
            else:
                return root.starts_with(root.get_sub(c), s[1:])


class Trie:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        self.root.add(self.root, word)

    def search(self, word: str) -> bool:
        return self.root.search(self.root, word)

    def startsWith(self, prefix: str) -> bool:
        return self.root.starts_with(self.root, prefix)


if __name__ == '__main__':
    trie = Trie()
    trie.insert("a")
    print(trie.startsWith("a"))
