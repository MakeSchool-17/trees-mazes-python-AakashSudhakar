import maze
import random


# Create maze using Pre-Order DFS maze creation algorithm
def create_dfs(m):
    """ Maze creation algorithm utilizing pre-order depth-first tree traversal. """
    # choose a cell index at random from the grid to be current cell
    current_cell = random.randint
    visited_cells, backtrack_stack = 1, list()  # Sets visited cells to one and creates backtrack stack

    while m.w_cells < m.total_cells:            # While visited cells is less than total cells
    #     get unvisited neighbors using cell_neighbors
        if m.cell_neighbors(cell) >= 1:         # If at least one neighbor
    #         choose random neighbor to be new cell
    #         knock down wall between it and current cell using connect_cells
    #         push current cell to stack
    #         set current cell to new cell
            visited_cells += 1                  # Increments visited cells by one
        else:
    #         pop from stack to current cell
            pass
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
