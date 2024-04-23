from func_solve import nemo_logic
from func_device import RemoteControl
rows_cnt, cols_cnt = 30, 30

row_lines = [
    [15],
    [6, 6, 2, 3, 2],
    [6, 1, 6, 3, 3, 3],
    [6, 1, 6, 11],
    [6, 1, 6, 9],
    
    [6, 1, 6, 9],
    [1, 1, 13],
    [1, 4, 1, 4, 1, 13],
    [1, 1, 13],
    [6, 1, 6, 9],
    
    [6, 1, 6, 9],
    [6, 1, 6, 11],
    [6, 1, 6, 3, 3, 3],
    [6, 6, 2, 3, 2],
    [15],
    
    [15],
    [4, 3, 4, 6, 6],
    [2, 7, 2, 4, 1, 1, 1, 4],
    [1, 3, 3, 1, 3, 1, 1, 1, 3],
    [4, 3, 4, 2, 1, 1, 1, 2],
    
    [2, 5, 2, 15],
    [2, 7, 2, 1, 1, 1, 1, 1],
    [2, 7, 2, 1, 11, 1],
    [2, 7, 2, 1, 1, 1, 1, 1],
    [2, 5, 2, 15],
    
    [4, 3, 4, 2, 1, 1, 1, 2],
    [1, 3, 3, 1, 3, 1, 1, 1, 3],
    [2, 7, 2, 4, 1, 1, 1, 4],
    [4, 3, 4, 6, 6],
    [15],
]

col_lines = [
    [15],
    [6, 6, 4, 3, 4],
    [6, 1, 6, 2, 7, 2],
    [6, 1, 6, 1, 3, 3, 1],
    [6, 1, 6, 4, 3, 4],
    
    [6, 1, 6, 2, 5, 2],
    [1, 1, 2, 7, 2],
    [1, 4, 1, 4, 1, 2, 7, 2],
    [1, 1, 2, 7, 2],
    [6, 1, 6, 2, 5, 2],
    
    [6, 1, 6, 4, 3, 4],
    [6, 1, 6, 1, 3, 3, 1],
    [6, 1, 6, 2 ,7, 2],
    [6, 6, 4, 3, 4],
    [15],
    
    [15],
    [2, 3, 2, 6, 6],
    [3, 3, 3, 4, 1, 1, 1, 4],
    [11, 3, 1, 1, 1, 3],
    [9, 2, 1, 1, 1, 2],
    
    [9, 15],
    [13, 1, 1, 1, 1, 1],
    [13, 1, 11, 1],
    [13, 1, 1, 1, 1, 1],
    [9, 15],
    
    [9, 2, 1, 1, 1, 2],
    [11, 3, 1, 1, 1, 3],
    [3, 3, 3, 4, 1, 1, 1, 4],
    [2, 3, 2, 6, 6],
    [15],
]

if len(row_lines) != rows_cnt :
    raise KeyError('row cnt error')

if len(col_lines) != cols_cnt :
    raise KeyError('col cnt error')
row_total = 0
for row_line in row_lines :
    for row in row_line :
        row_total += row

col_total = 0
for col_line in col_lines :
    for col in col_line :
        col_total += col
if row_total != col_total :
    print(row_total - col_total)
    raise KeyError('input error')

print("풀이 시작")
board = nemo_logic(row_lines, col_lines)

device = RemoteControl()
device.right()
for row_line in board :
    for c in row_line :
        if c == 0 :
            device.not_check()
        elif c== 1 :
            device.check()
        device.right()
    device.down()