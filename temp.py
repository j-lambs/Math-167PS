def print_current_board(board):
    for row in board:
        print(row)

def vert(a):
    for j in range(len(a)):
        for i in range(len(a)):
            print(a[i][j])

a = [[1,2,3],[4,5,6],[7,8,9]]

x = 0
typeofx = type(x)
if isinstance(x, int):
    print('hi')
if isinstance(x, str):
    print('no')