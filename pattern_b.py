import sys

def pattern(n):
    for i in range(n):
        for j in range(i+1,n+1):
            print(str(j),end=" ")
        print()


pattern(int(sys.argv[1]))
