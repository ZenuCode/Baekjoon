import sys
from collections import deque
input = sys.stdin.readline

def solution():
    n = int(input())
    for _ in range(n):
        flag = 0
        rotate = False
        direction = input().rstrip()
        arrNum = int(input())
        arr = input().strip()[1:-1].split(',')

        if arrNum:
            arr = deque(arr)
        else:
            arr = deque([])
        
        for i in direction:
            if i == 'R':
                rotate = not rotate
            else:
                if len(arr):
                    if rotate:
                        arr.pop()
                    else:
                        arr.popleft()
                else:
                    flag = 1
                    break

        if flag == 0 and not rotate:
            print("[" + ",".join(arr) + "]")
        elif flag == 0 and rotate:
            arr.reverse()
            print("[" + ",".join(arr) + "]")
        else:
            print("error")

solution() 

"""
import sys
input = sys.stdin.readline

n = int(input())

for _ in range(n):
    cmd = input()
    cmd = cmd.replace("RR", "")
    num = int(input())
    arr = list(input().strip()[1:-1].split(","))
    reverse = False
    front = 0
    back = 0

    for i in cmd:
        if i == "R":
            reverse = not reverse
        elif i == "D":
            if reverse:
                back += 1
            else:
                front += 1
    
    if front + back <= num:
        if reverse:
            arr.reverse()
            print("[" + ",".join(arr[back:num - front]) + "]")
        else:
            print("[" + ",".join(arr[front:num - back]) + "]")
    else:
        print("error")
"""