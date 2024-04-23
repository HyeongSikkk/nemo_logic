from func_solve import nemo_logic
rows_cnt, cols_cnt = 10, 10

row_lines = [
    [2, 2],
    [2, 2],
    [2, 2],
    [2, 2],
    [8],
    
    [10],
    [10],
    [2, 4, 2],
    [4, 4],
    [8],
]

col_lines = [
    [4],
    [6],
    [7, 2],
    [10],
    [4, 1],
    
    [4, 1],
    [10],
    [7, 2],
    [6],
    [4],
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
nemo_logic(row_lines, col_lines)
