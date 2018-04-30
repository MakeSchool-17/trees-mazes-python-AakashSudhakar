import maze


# Create maze using Pre-Order DFS maze creation algorithm
def create_dfs(m):
    # create a stack for backtracking
    # choose a cell index at random from the grid to be current cell
    # set visited cells to 1

    # while visited cells < total cells
    while m.w_cells < m.total_cells:
    #     get unvisited neighbors using cell_neighbors
    #     if at least one neighbor
        if m.cell_neighbors(cell) >= 1:
    #         choose random neighbor to be new cell
    #         knock down wall between it and current cell using connect_cells
    #         push current cell to stack
    #         set current cell to new cell
    #         add 1 to visited cells
            pass
        else:
    #         pop from stack to current cell
            pass
    #     call refresh_maze_view to update visualization
        m.refresh_maze_view()

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
