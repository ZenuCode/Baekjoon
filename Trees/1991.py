import sys
input = sys.stdin.readline

def preOrder(root): #Rt L R
    if root == ".":
        return
    print(root, end="")
    preOrder(nodes[root][0])
    preOrder(nodes[root][1])

def inOrder(root): #L Rt R
    if root == ".":
        return
    inOrder(nodes[root][0])
    print(root, end="")
    inOrder(nodes[root][1])

def postOrder(root): #L R Rt
    if root == ".":
        return
    postOrder(nodes[root][0])
    postOrder(nodes[root][1])
    print(root, end="")

n = int(input())
nodes = {}
for _ in range(n):
    a, b, c = map(str, input().split())
    nodes[a] = (b, c)

preOrder("A")
print()
inOrder("A")
print()
postOrder("A")
print()