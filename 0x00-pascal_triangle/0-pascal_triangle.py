#!/usr/bin/python3
"""A function that prints the pascal's triangle"""

def pascal_triangle(n):
    """
    Generate Pascal's Triangle up to n rows.

    Args:
    - n (int): The number of rows in Pascal's Triangle.

    Returns:
    - List of Lists: Each sublist represents a row of Pascal's Triangle.

    Returns an empty list if n <= 0.
    """
    if n <= 0:
        return []

    triangle = [[1] * (i + 1) for i in range(n)]

    for i in range(2, n):
        for j in range(1, i):
            triangle[i][j] = triangle[i-1][j-1] + triangle[i-1][j]

    return triangle

# Test the function with the provided example
if __name__ == "__main__":
    triangle = pascal_triangle(5)
    for row in triangle:
        print(row)
