import maze
import generate_maze
import sys


# Solve maze using Pre-Order DFS algorithm, terminate with solution

def solve_dfs(m):
    # TODO: Implement solve_dfs
    pass


# Solve maze using BFS algorithm, terminate with solution
# ======================================= PSEUDOCODE =======================================
"""
create a queue
set current cell to 0
set in direction to 0b0000
set visited cells to 0
enqueue (current cell, in direction)

while current cell not goal and queue not empty
    dequeue to current cell, in direction
    visit current cell with bfs_visit_cell
    add 1 to visited cells
    call refresh_maze_view to update visualization

    get unvisited neighbors of current cell using cell_neighbors, add to queue

trace solution path and update cells with solution data using reconstruct_solution

set state to 'idle'
"""
# /====================================== PSEUDOCODE =======================================
def solve_bfs(m):
    queue, curr, in_direction, visited = list(), 0, "0b0000", 0
    queue.append((curr, in_direction))          # Enqueues current cell and direction to queue

    while curr != m.total_cells - 1 and len(queue) > 0:
        
        curr, in_direction = queue.pop(0)       # Dequeues element to current cell and in-direction

    m.state = "idle"                            # Sets state to idle


def print_solution_array(m):
    solution = m.solution_array()
    print('Solution ({} steps): {}'.format(len(solution), solution))


def main(solver='dfs'):
    current_maze = maze.Maze('create')
    generate_maze.create_dfs(current_maze)
    if solver == 'dfs':
        solve_dfs(current_maze)
    elif solver == 'bfs':
        solve_bfs(current_maze)
    while 1:
        maze.check_for_exit()
    return

if __name__ == '__main__':
    if len(sys.argv) > 1:
        main(sys.argv[1])
    else:
        main()
