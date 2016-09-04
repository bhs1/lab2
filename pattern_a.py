import sys

def pattern(n):
    for i in range(n):
        for j in range(n):
            print(str(i+1),end=" ")
        print()


pattern(int(sys.argv[1]))
