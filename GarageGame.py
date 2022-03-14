from typing import List

dir_r = [1, -1, 0, 0]
dir_c = [0, 0, 1, -1]

N = int(input())
arr_input = [[int(x) for x in input().split()] for y in range(N*3)]
arr = [[] for y in range(N*3)]
for idx, row in enumerate(arr_input):
    arr[(N*3-1)-idx] = row

cur_score= 0
max_r, min_r, max_c, min_c = 0, 0, 0, 0
result = 0

def DFS(arr : List[List[int]], score : int):
    global cur_score, max_r, min_r, max_c, min_c
    def BFS(r:int, c:int) -> int:
        print(f'----------- BFS : {r}, {c} -----------')
        global cur_score, max_r, min_r, max_c, min_c
        cur_score += 1
        max_r = max(max_r, r)
        min_r = min(min_r, r)
        max_c = max(max_c, c)
        min_c = min(min_c, c)
        print(f'score : {cur_score}')
        print(f'max_r : {max_r}, min_r : {min_r}, max_c : {max_c}, min_c : {min_c},')
        vis_map[r][c] = 1
        cur_color = arr[r][c]
        arr[r][c] = -1
        for d in range(4):
            nxt_r = r + dir_r[d]
            nxt_c = c + dir_c[d]
            if 0 <= nxt_c and nxt_c < N and 0 <= nxt_r and nxt_r < N and vis_map[nxt_r][nxt_c] == 0:
                if cur_color == arr[nxt_r][nxt_c]:
                    BFS(nxt_r, nxt_c)

    vis_map = [[0 for _ in range(N)] for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if vis_map[i][j] == 0:
                print(f'############################ DFS : {i}, {j} ############################')
                cur_score = 0
                max_r, min_r, max_c, min_c = i, i, j, j
                BFS(i, j)
                total_score = cur_score + (max_r - min_r + 1)*(max_c - min_c + 1)
                print(f'total_socre : {total_score}')
                # -------- 같은색 지우고 빈칸 채우기 -------- #
                for c in range(N):
                    cnt = 0
                    # start_r
                    # for r in range(N * 3):
                    #     if arr[r][c] == -1:
                            # cnt +=


                for row in arr:
                    print(row)




DFS(arr, 0)

# depth 3까지
# 1. n*n 그리드에서 1칸을 선택한다.
# 2. 해당 칸 주변에 같은 색인 칸을 찾는다.
# 3. 같은 색 칸 수, 작은 직사각형 크기를 구한다.
# 4. 빈칸을 채운다.
