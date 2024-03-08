import sys
a = int(sys.stdin.readline())
for i in range(a):
    str1, str2 = sys.stdin.readline().split()
    cnt = 0
    string1 = ""
    string2 = ""
    for k in range(26):
        string1 += str(str1.count(chr(95+k)))
        string2 += str(str2.count(chr(95+k)))
    if string1 == string2:
        print("Possible")
    else: 
        print("Impossible")