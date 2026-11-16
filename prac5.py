#Prac No. 4
#Breadth-First-Search (BFS) Algorithm

from collections import deque

start = (1,2,3,
         4,5,6,
         0,7,8)

goal = (1,2,3,
        4,5,6,
        7,8,0)

def bfs(start):
    queue = deque([start])
    visited = {start}
    parent = {start : None}

    while queue: 
        state = queue.popleft()

        if state == goal:
            path = []

            while state is not None:
                path.append(state)
                state = parent[state]
            path.reverse()

            print("Solution found!")

            for s in path:
                print(s[0:3])
                print(s[3:6])
                print(s[6:9])
                print()
            return 

        zero = state.index(0)

        for move in [-3, 3, -1, 1]:
            new_pos = zero + move
            if 0 <= new_pos < 9: 
                if move == -1 and zero % 3 == 0:
                    continue
                if move == 1 and zero % 3 == 2:
                    continue
                new_state = list(state)

                new_state[zero], new_state[new_pos] = new_state[new_pos], new_state[zero]

                new_state = tuple(new_state)

                if new_state not in visited: 
                    visited.add(new_state)
                    parent[new_state] = state
                    queue.append(new_state)

    print("No solution exists!!")

bfs(start)

