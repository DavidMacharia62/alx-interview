# Rotate 2D Matrix

## Description
This Python script provides a function `rotate_2d_matrix` to rotate an n x n 2D matrix 90 degrees clockwise in-place. The script includes a test case to demonstrate the usage of the function.

## Prototype
```python
def rotate_2d_matrix(matrix):
    """
    Rotate the given n x n 2D matrix 90 degrees clockwise.

    Parameters:
    - matrix: List[List[int]]
      The input 2D matrix to be rotated.

    Returns:
    None
    """
    # Implementation details go here
```

## Usage
The `rotate_2d_matrix` function takes a 2D matrix as input and rotates it 90 degrees clockwise in-place. The matrix should have 2 dimensions, and it is assumed not to be empty.

### Example
```python
from 0-rotate_2d_matrix import rotate_2d_matrix

if __name__ == "__main__":
    matrix = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]

    rotate_2d_matrix(matrix)
    print(matrix)
```

### Output
```
[[7, 4, 1],
 [8, 5, 2],
 [9, 6, 3]]
```

## Note
- The rotation is done in-place, meaning the original matrix is modified directly.
- The input matrix is assumed to be square (n x n).
- The script includes a shebang (`#!/usr/bin/python3`) for compatibility.

## How to Run
Execute the provided script `main_0.py` in your terminal to test the `rotate_2d_matrix` function.

```bash
./main_0.py
```

This will run the test case and print the rotated matrix.

## Author
David Macharia

Feel free to reach out with any questions or concerns.
