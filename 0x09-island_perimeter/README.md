# Island Perimeter

## Overview
This function, `island_perimeter(grid)`, calculates and returns the perimeter of the island described in the provided grid. The grid is represented as a list of lists of integers, where 0 represents water and 1 represents land. The function follows certain constraints such as the grid being completely surrounded by water, having only one island, and not containing any "lakes" (disconnected bodies of water within the island).

## Function Signature
```python
def island_perimeter(grid: List[List[int]]) -> int:
    pass
```

## Input
- `grid`: A list of lists of integers representing the grid. Each cell in the grid is square with a side length of 1 unit. The dimensions of the grid do not exceed 100x100.

## Output
- Returns an integer representing the perimeter of the island.

## Example
```python
grid = [
    [0, 0, 0, 0, 0, 0],
    [0, 1, 0, 0, 0, 0],
    [0, 1, 0, 0, 0, 0],
    [0, 1, 1, 1, 0, 0],
    [0, 0, 0, 0, 0, 0]
]
print(island_perimeter(grid))  # Output: 12
```

## Approach
The function iterates through each cell of the grid. For each land cell (grid[i][j] == 1), it checks the adjacent cells to determine the number of adjacent water cells. The perimeter is incremented by the count of adjacent water cells for each land cell encountered. Finally, the total perimeter is returned.

## Constraints
- The grid is rectangular with width and height not exceeding 100.
- Cells are connected horizontally or vertically, not diagonally.
- The grid is completely surrounded by water.
- There is only one island or nothing.
