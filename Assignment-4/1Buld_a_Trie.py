class TrieNode:
    def __init__(self):
        self.children = {}
        self.validWord = False

    # def dfs(self, prefix=""):
    #     if self.validWord:
    #         print(prefix)
    #     for char, child in self.children.items():
    #         child.dfs(prefix + char)


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.validWord = True

    def isValidWord(self, word) -> bool:
        node = self.root
        for char in word:
            if char in node.children:
                node = node.children[char]
            else:
                return False
            
        return node.validWord
    
    def remove(self, node, word):





        
    

tree = Trie()

tree.insert("apple")
print(tree.isValidWord("banana")) #expected: False
print(tree.isValidWord("app")) #expected: False
print(tree.isValidWord("apples")) #expected: False
print(tree.isValidWord("apple")) #expected: True