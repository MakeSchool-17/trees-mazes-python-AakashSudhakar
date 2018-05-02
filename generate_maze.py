import maze
from random import choice, randint

# Create maze using Pre-Order DFS maze creation algorithm

# ======================================= PSEUDOCODE =======================================
"""
create a stack for backtracking
choose a cell index at random from the grid to be current cell
set visited cells to 1

while visited cells < total cells
    get unvisited neighbors using cell_neighbors
    if at least one neighbor
        choose random neighbor to be new cell
        knock down wall between it and current cell using connect_cells
        push current cell to stack
        set current cell to new cell
        add 1 to visited cells
    else
        pop from stack to current cell
    call refresh_maze_view to update visualization

set state to 'solve'
"""
# /====================================== PSEUDOCODE =======================================


def create_dfs(m):
    """ Maze creation algorithm utilizing pre-order depth-first tree traversal. """
    # curr = choice(m.total_cells)            # Chooses cell index at random from grid to be current cell
    curr = randint(0, m.total_cells - 1)    # Chooses cell index at random from grid to be current cell
    visited, backtrack_stack = 1, list()    # Sets visited cells to one and creates backtrack stack

    while visited < m.total_cells:            # While visited cells is less than total cells
    #     get unvisited neighbors using cell_neighbors
        neighbors = m.cell_neighbors(curr)      # Gets unvisited neighbors using cell_neighbors()
        if len(neighbors) >= 1:         # If at least one neighbor
            new_cell_i = randint(0, len(neighbors) - 1)
            cell, compass_index = neighbors[new_cell_i]
            m.connect_cells(curr, cell, compass_index)
            backtrack_stack.append(curr)
            curr = cell
            visited += 1                  # Increments visited cells by one
        else:
    #         pop from stack to current cell
            curr = backtrack_stack.pop()
        m.refresh_maze_view()                   # Call refresh_maze_view() to update visualization

    # set state to 'solve'
    m.state = "solve"


def main():
    current_maze = maze.Maze('create')
    create_dfs(current_maze)
    while 1:
        maze.check_for_exit()
    return

if __name__ == '__main__':
    main()
