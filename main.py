#sudoku solver
mat = [[0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0],
[0,1,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0]]


mat  = [
[3, 0, 6, 5, 0, 8, 4, 0, 0],
[5, 2, 0, 0, 0, 0, 0, 0, 0],
[0, 8, 7, 0, 0, 0, 0, 3, 1],
[0, 0, 3, 0, 1, 0, 0, 8, 0],
[9, 0, 0, 8, 6, 3, 0, 0, 5],
[0, 5, 0, 0, 9, 0, 6, 0, 0], 
[1, 3, 0, 0, 0, 0, 2, 5, 0],
[0, 0, 0, 0, 0, 0, 0, 7, 4],
[0, 0, 5, 2, 0, 6, 3, 0, 0]
]

def printMat():
    print("--------------------------")
    for i in mat:
        for j in i:
            print(j,' ',end='')
        print()
    print("--------------------------")

def isPossible(x,y,n):
    for i in range(8):
        if mat[x][i] == n:
            return False
    for i in range(8):
        if mat[i][y] == n:
            return False

    a = (x//3)*3
    b = (y//3)*3
    for i in range(a,a+3):
        for j in range(b,b+3):
            if n == mat[i][j]:
                return False
    return True
            

printMat()
# print(isPossible(0,1,7))

# for i in range(1,10):
    # print(i,':',isPossible(3,0,i))

