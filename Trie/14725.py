import sys
input = sys.stdin.readline

class Trie:
    def __init__(self):
        self.children = {}
   
    def insert(self, foods):
        curr = self.children
        for food in foods:
            if food not in curr:
                curr[food] = {}
            curr = curr[food]
    
    def printTrie(self, current=None, depth=0):
        if current is None:
            current = self.children
        
        for child in sorted(current):
            print("--" * depth + child)
            self.printTrie(current[child], depth + 1)


n = int(input())
trie = Trie()

for _ in range(n):
    inputs = input().split()
    k = int(inputs[0])
    foods = inputs[1:]
    trie.insert(foods)

trie.printTrie()