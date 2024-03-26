vowel = ['a', 'e', 'i', 'o', 'u']

l, c = map(int, input().split())
arr = sorted(input().split())
stack = []

def check(stack):
    c_count, v_count = 0, 0
    for i in stack:
        if i in vowel:
            v_count += 1
        else:
            c_count += 1
    
    if c_count >= 2 and v_count >= 1:
        return True
    else:
        return False

def backtrack(index):
    if len(stack) == l:
        if check(stack):
            print("".join(stack))
            return
    
    for i in range(index, c):
        stack.append(arr[i])
        backtrack(i + 1)
        stack.pop()

backtrack(0)











# words.sort() 

# def check(arr):
#     v_count, c_count = 0, 0 # 모음 개수, 자음 개수

#     for i in arr:
#         if i in vowel:
#             v_count += 1
#         else:
#             c_count += 1

#     if v_count >= 1 and c_count >= 2:
#         return True
#     else:
#         return False

# def backtracking(arr):

#     if len(arr) == L:
#         if check(arr):
#             print("".join(arr))
#             return

#     for i in range(len(arr), C):
#         if arr[-1] < words[i]:
#             arr.append(words[i])
#             backtracking(arr)
#             arr.pop()

# for i in range(C - L + 1):
#     a = [words[i]]
#     backtracking(a)