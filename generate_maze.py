import maze


# Create maze using Pre-Order DFS maze creation algorithm
def create_dfs(m):
    while m.w_cells < m.total_cells:
        pass


def main():
    current_maze = maze.Maze('create')
    create_dfs(current_maze)
    while 1:
        maze.check_for_exit()
    return

if __name__ == '__main__':
    main()
