from collections import deque

def bfs(x, y, field, visited):
    dx = [-1, 1, 0, 0]  # 상, 하, 좌, 우
    dy = [0, 0, -1, 1]
    n = len(field)
    m = len(field[0])
    
    queue = deque([(x, y)])
    visited[x][y] = True
    
    while queue:
        x, y = queue.popleft()
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny] and field[nx][ny] == 1:
                queue.append((nx, ny))
                visited[nx][ny] = True

def solution(field):
    n = len(field)
    m = len(field[0])
    visited = [[False] * m for _ in range(n)]
    count = 0
    
    for i in range(n):
        for j in range(m):
            if not visited[i][j] and field[i][j] == 1:
                bfs(i, j, field, visited)
                count += 1
    
    return count

# 테스트 케이스 개수 입력
t = int(input())

for _ in range(t):
    # 가로길이 M, 세로길이 N, 배추 위치 개수 K 입력
    M, N, K = map(int, input().split())
    
    # 배추 밭 초기화
    field = [[0] * M for _ in range(N)]
    
    # 배추 위치 입력 및 표시
    for _ in range(K):
        X, Y = map(int, input().split())
        field[Y][X] = 1
    
    # 최소 배추흰지렁이 수 출력
    print(solution(field))