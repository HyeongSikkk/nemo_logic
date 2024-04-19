import time
start = time.time()

rows_cnt, cols_cnt = 30, 30

row_lines = [
    [0],
    [1, 26],
    [1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 4, 5, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    
    [5, 1, 1, 1, 1, 1, 1, 4, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 3, 1, 1, 1, 1, 1, 1, 6, 1],
    [1, 1, 5, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 6],
    
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 5, 1, 1, 1, 6, 1],
    [1, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 18],
    [1, 1, 5, 1, 1],
    
    [1, 1, 1, 1, 14, 1],
    [1, 1, 1, 5, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 10],
    [1, 1, 1, 3, 1, 1, 1, 1, 1],
    [1, 1, 5, 1, 1, 1, 5, 2, 1],
    
    [1, 1, 1, 3, 1, 1, 1, 2, 1],
    [1, 1, 1, 5, 1, 1, 3, 1, 1, 1],
    [1, 1, 1, 1, 1, 5, 1, 1, 1, 1, 2],
    [1, 1, 1, 5, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 3, 1, 1, 1, 2, 1],
    
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 5, 1, 1, 1, 2],
    [1, 1, 1, 1, 1, 1, 1],
    [26, 1],
    [0],
]

col_lines = [
    [0],
    [28],
    [1, 1],
    [3, 1, 20, 1],
    [1, 1, 1, 1],
    
    [1, 3, 2, 19],
    [1, 1, 1, 1, 1],
    [6, 5, 1, 2, 1, 6, 1],
    [1, 1, 1, 1, 1, 1, 1, 1],
    [1, 12, 1, 2, 1, 1, 4],
    
    [1, 1, 1, 1, 1, 1, 1],
    [9, 1, 4, 1, 7, 1],
    [1, 1, 1, 1, 1],
    [1, 9, 1, 6, 7],
    [1, 1, 1, 1, 1],
    
    [11, 1, 1, 6, 3, 1],
    [1, 1, 1, 1, 1, 1, 1],
    [1, 11, 8, 1, 1, 1],
    [1, 1, 1, 1, 1, 1],
    [1, 1, 7, 1, 1, 3, 6, 1],
    
    [1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 7, 1, 1, 1, 8],
    [1, 3, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 8, 1],
    [1, 1, 3, 1, 1, 1, 1, 1, 1],
    
    [1, 1, 1, 1, 1, 1, 1, 1, 10],
    [1, 5, 1, 1, 1, 1, 1, 2, 1, 1],
    [1, 1, 1, 1, 1, 1],
    [28],
    [0],
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
    raise KeyError('input error')
        
# 공백을 담은 네모로직 칸 생성
board = [[0 for _ in range(cols_cnt)] for _ in range(rows_cnt)]

row_casts = {}
col_casts = {}
calced = {}
for idx, rows in enumerate(row_lines) :
    small_board = [0 for _ in range(rows_cnt)]
    small_boards = []
    def dfs(rows, sb) :
        # find last index
        for  idx, ea in enumerate(sb[::-1]) :
            if ea == 1 :
                idx = len(sb)-idx +1
                break
            elif idx+1 == len(sb) :
                idx = 0
        
        # 가능한 경우의 수 발생
        for row_idx, row in enumerate(rows) :
            if row != 0 :
                for r_idx in range(idx, len(sb)) :
                    if r_idx+row <= len(sb) :
                        sb[r_idx:r_idx+row] = [1 for _ in range(row)]
                        
                        # 마지막 row가 아닐 경우
                        if len(rows) != 1 and row_idx == 0:
                            dfs(rows[row_idx+1:], sb)
                        
                        # 마지막 row인 경우, 저장
                        elif len(rows) == 1:
                            small_boards.append([*sb])
                        sb[r_idx:r_idx+row] = [0 for _ in range(row)]
            else :
                small_boards.append(sb)

    rows_name = str(rows)
    if rows_name in calced :
        row_casts[idx] = calced[rows_name]
    else :
        dfs(rows, small_board)
        row_casts[idx] = small_boards
        calced[rows_name] = small_boards

for idx, cols in enumerate(col_lines) :
    small_board = [0 for _ in range(cols_cnt)]
    small_boards = []
    def dfs(cols, sb) :
        # find last index
        for  idx, ea in enumerate(sb[::-1]) :
            if ea == 1 :
                idx = len(sb)-idx +1
                break
            elif idx+1 == len(sb) :
                idx = 0
        
        # 가능한 경우의 수 발생
        for col_idx, col in enumerate(cols) :
            if col != 0 :
                for c_idx in range(idx, len(sb)) :
                    if c_idx+col <= len(sb) :
                        sb[c_idx:c_idx+col] = [1 for _ in range(col)]
                        
                        # 마지막 col가 아닐 경우
                        if len(cols) != 1 and col_idx == 0:
                            dfs(cols[col_idx+1:], sb)
                        
                        # 마지막 col인 경우, 저장
                        elif len(cols) == 1:
                            small_boards.append([*sb])
                        sb[c_idx:c_idx+col] = [0 for _ in range(col)]
            else :
                small_boards.append(sb)
    cols_name = str(cols)
    if cols_name in calced :
        col_casts[idx] = calced[cols_name]
    else :
        dfs(cols, small_board)
        col_casts[idx] = small_boards
        calced[cols_name] = small_boards
    
def check_board() :
    for col_number in range(cols_cnt) :
        col_line = col_lines[col_number]
        line = []
        c = 0
        for t in board :
            if t[col_number] == 1 :
                c +=1
            elif t[col_number] == 0 and c != 0 :
                line.append(c)
                c = 0
        if c != 0 :
            line.append(c)
        elif c == 0 and len(line) == 0 :
            line.append(0)
            
        if line != col_line :
            return False
    return True

def print_board(simple = True) :
    if simple :
        for idx, t in enumerate(board) :
            if idx % 5 == 0 :
                print()
            for small_idx, ea in enumerate(t) :
                print(ea, end=' ')
                if small_idx % 5 == 4 :
                    print(' ', end =' ')
            print()
    else :
        for idx, t in enumerate(board) :
            if idx % 5 == 0 :
                print()
            for small_idx, ea in enumerate(t) :
                if ea == 1 :
                    print('O', end=' ')
                elif ea == -1 :
                    print('X', end=' ')                
                else :
                    print('.', end =' ')
                    
                if small_idx % 5 == 4 :
                    print(' ', end =' ')
            print()
        
def is_can_cast(axis, key, cast) :
    # row
    if axis :
        for idx, ea in enumerate(cast) :
            board_ea = board[key][idx]
            if board_ea == 1 :
                if ea == 0 :
                    return False            
            elif board_ea == -1 :
                if ea == 1 :
                    return False

        return True
    
    # col
    else :
        for idx, ea in enumerate(cast) :
            board_ea = board[idx][key]
            if board_ea == 1 :
                if ea == 0 :
                    return False
            elif board_ea == -1 :
                if ea == 1 :
                    return False
        return True

tries = 0
print('before')
a, b = 0, 0
c, d = 1, 1
for key in row_casts :
    a += len(row_casts[key])
    c *= len(row_casts[key])
    b += len(col_casts[key])
    d *= len(col_casts[key])
print(a, b)
print(c, d)

# 기존 코드
'''
while True :
    tries += 1
    # 전부 채워져 있는 보드 생성
    tmp_board_row = [[1 for _ in range(cols_cnt)] for __ in range(rows_cnt)]
    tmp_board_col = [[1 for _ in range(cols_cnt)] for __ in range(rows_cnt)]

    # 실행 전 가능한 경우의 수
    before_row_cnt = 0
    before_col_cnt = 0
    
    # 채워져 있는 보드에서 공백 칸 분류
    for a in row_casts :
        before_row_cnt += len(row_casts[a])
        for cast in row_casts[a] :
            for idx, ea in enumerate(cast) :
                if ea == 0 :
                    tmp_board_row[a][idx] = 0
                    
    for a in col_casts :
        before_col_cnt += len(col_casts[a])
        for cast in col_casts[a] :
            for idx, ea in enumerate(cast) :
                if ea == 0 :
                    tmp_board_col[idx][a] = 0

    # 확실히 채워져 있는 블럭을 보드로 옮기기
    for row_idx in range(len(tmp_board_row)) :
        for col_idx in range(len(tmp_board_col)) :
            if tmp_board_row[row_idx][col_idx] == 1 :
                board[row_idx][col_idx] = 1
            if tmp_board_col[row_idx][col_idx] == 1 :
                board[row_idx][col_idx] = 1
    
    # 전부 막혀져 있는 보드 생성
    tmp_board_row = [[-1 for _ in range(cols_cnt)] for __ in range(rows_cnt)]
    tmp_board_col = [[-1 for _ in range(cols_cnt)] for __ in range(rows_cnt)]

    # 채워져 있는 보드에서 공백 칸 분류
    for a in row_casts :
        for cast in row_casts[a] :
            for idx, ea in enumerate(cast) :
                if ea == 1 :
                    tmp_board_row[a][idx] = 0
                    
    for a in col_casts :
        for cast in col_casts[a] :
            for idx, ea in enumerate(cast) :
                if ea == 1 :
                    tmp_board_col[idx][a] = 0

    # 확실히 채워져 있는 블럭을 보드로 옮기기
    for row_idx in range(len(tmp_board_row)) :
        for col_idx in range(len(tmp_board_col)) :
            if tmp_board_row[row_idx][col_idx] == -1 :
                board[row_idx][col_idx] = -1
            if tmp_board_col[row_idx][col_idx] == -1 :
                board[row_idx][col_idx] = -1


    # 실행 후 가능한 경우의 수
    after_row_cnt = 0
    after_col_cnt = 0
    
    for key in row_casts :
        new_list = []
        for cast in row_casts[key] :
            if is_can_cast(True, key, cast) :
                new_list.append(cast)
        after_row_cnt += len(new_list)
        row_casts[key] = new_list

    for key in col_casts :
        new_list = []
        for cast in col_casts[key] :
            if is_can_cast(False, key, cast) :
                new_list.append(cast)
        after_col_cnt += len(new_list)
        col_casts[key] = new_list
    
    if after_row_cnt == before_row_cnt and after_col_cnt == before_col_cnt :
        break
'''
# 수정 코드
def to_transport_board(tmp_borad, check) :
    if check :
        for row_idx, rows in enumerate(tmp_borad) :
            for col_idx, ea in enumerate(rows) :
                if ea == 1 :
                    board[row_idx][col_idx] = 1
    else :
        for row_idx, rows in enumerate(tmp_borad) :
            for col_idx, ea in enumerate(rows) :
                if ea == -1 :
                    board[row_idx][col_idx] = -1
while True :
    tries += 1
    # 전부 채워져 있는 보드 생성
    all_check_row = [[1 for _ in range(cols_cnt)] for __ in range(rows_cnt)]
    all_check_col = [[1 for _ in range(cols_cnt)] for __ in range(rows_cnt)]
    # 전부 막혀져 있는 보드 생성
    all_block_row = [[-1 for _ in range(cols_cnt)] for __ in range(rows_cnt)]
    all_block_col = [[-1 for _ in range(cols_cnt)] for __ in range(rows_cnt)]

    # 실행 전 가능한 경우의 수
    before_row_cnt = 0
    before_col_cnt = 0
    
    # 채워져 있는 보드에서 공백 칸 분류
    for a in row_casts :
        before_row_cnt += len(row_casts[a])
        for cast in row_casts[a] :
            for idx, ea in enumerate(cast) :
                if ea == 0 :
                    all_check_row[a][idx] = 0
                elif ea == 1 :
                    all_block_row[a][idx] = 0
                    
    for a in col_casts :
        before_col_cnt += len(col_casts[a])
        for cast in col_casts[a] :
            for idx, ea in enumerate(cast) :
                if ea == 0 :
                    all_check_col[idx][a] = 0
                elif ea == 1 :
                    all_block_col[idx][a] = 0

    # 확실히 채워져 있는 블럭을 보드로 옮기기
    to_transport_board(all_check_row, True)
    to_transport_board(all_check_col, True)
    to_transport_board(all_block_row, False)
    to_transport_board(all_block_col, False)


    # 실행 후 가능한 경우의 수
    after_row_cnt = 0
    after_col_cnt = 0
    
    for key in row_casts :
        new_list = []
        for cast in row_casts[key] :
            if is_can_cast(True, key, cast) :
                new_list.append(cast)
        after_row_cnt += len(new_list)
        row_casts[key] = new_list

    for key in col_casts :
        new_list = []
        for cast in col_casts[key] :
            if is_can_cast(False, key, cast) :
                new_list.append(cast)
        after_col_cnt += len(new_list)
        col_casts[key] = new_list
    
    if after_row_cnt == before_row_cnt and after_col_cnt == before_col_cnt :
        break
row_casts = dict(sorted(row_casts.items(), key=lambda x : len(x[1])))
col_casts = dict(sorted(col_casts.items(), key=lambda x : len(x[1])))

row_keys = list(row_casts.keys())
col_keys = list(col_casts.keys())

print('after')
a, b, c, d = 0, 0, 1, 1
for key in row_casts :
    a += len(row_casts[key])
    c *= len(row_casts[key])
    b += len(col_casts[key])
    d *= len(col_casts[key])
print(a, b)
print(c, d)

board = [[0 for _ in range(cols_cnt)] for _ in range(rows_cnt)]
def dfs_is_can_cast(axis, idx, cast) :
    # row
    if axis :
        for index in range(idx) :
            key = col_keys[index]
            if board[row_keys[idx]][key] != cast[key] :
                return False
        return True
    
    # col
    else :
        for index in range(idx+1) :
            key = row_keys[index]
            if board[key][col_keys[idx]] != cast[key] :
                return False
        return True
def dfs(axis, idx) :
    if idx == len(board) :
        print_board(False)
        end = time.time()
        print(f"elapsed time : {round(end-start, 4)}")
        exit()
    
    else :
        # row
        if axis :
            key = row_keys[idx]
            for cast in row_casts[key] :
                if dfs_is_can_cast(axis, idx, cast) :
                    before_line = [*board[key]]
                    board[key] = [*cast]
                    dfs(False, idx)
                    board[key] = [*before_line]
        
        # col
        else :
            key = col_keys[idx]
            for cast in col_casts[key] :
                if dfs_is_can_cast(axis, idx, cast) :
                    before_line = []
                    for c_idx, line in enumerate(board) :
                        before_line.append(line[key])
                        line[key] = cast[c_idx]
                    dfs(True, idx+1)
                    for c_idx, line in enumerate(board) :
                        line[key] = before_line[c_idx]
                        
dfs(True, 0)