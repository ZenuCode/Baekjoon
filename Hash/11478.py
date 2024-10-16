import sys
input = sys.stdin.readline

string = input().strip()
countSet = set()

for i in range(len(string)):
    for j in range(len(string) - i):
        countSet.add(string[j:j+i+1])

print(len(countSet))


"""
def check(i, word):
    countSet = set()
    for j in range(len(word) - i):
        countSet.add(word[j:j+i+1])
    return len(countSet)

import sys
word = sys.stdin.readline().strip()
total = 0
for i in range(len(word)): 
    total += check(i, word)
print(total)
"""

