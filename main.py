import time
from search import goal_state, bfs, dfs, print_path

start = time.time()
solution = dfs((806547231, 7))
end = time.time()

if solution is not None:
    parents = solution[0]
    expanded_nodes = solution[1]
    state = goal_state
    path = [state]
    while state != parents[state]:
        state = parents[state]
        path.append(state)

    print_path(path)
    print("Cost of the path:", len(path) - 1)
    print("Number of expanded nodes:", expanded_nodes)
    print("Depth:", len(path) - 1)
    print("Running time:", end - start)

# test case
# ---------
# solution = bfs((125340678, 3))
# solution = bfs((142658730, 0))
# solution = bfs((102754863, 7))
# solution = bfs((806547231, 7))
# ------------------------------
# solution = dfs((125340678, 3))
# solution = dfs((142658730, 0))
# solution = dfs((102754863, 7))
# solution = dfs((806547231, 7))
