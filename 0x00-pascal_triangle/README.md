# Pascal's Triangle in Python

## Overview

Pascal's Triangle is a mathematical concept that produces a triangular array of binomial coefficients. Each number in the triangle is the sum of the two numbers directly above it. The triangle starts with a single 1 at the top and each row begins and ends with 1. This triangle has applications in combinatorics and probability.

This README provides a Python implementation of Pascal's Triangle, along with an explanation of the code and examples of usage.

## Implementation

The Python code for generating Pascal's Triangle is provided in the file `pascals_triangle.py`. The implementation uses a nested list to represent the triangle, where each sublist corresponds to a row of the triangle.

```python
def generate_pascals_triangle(num_rows):
    triangle = [[1] * (i + 1) for i in range(num_rows)]
    
    for i in range(2, num_rows):
        for j in range(1, i):
            triangle[i][j] = triangle[i-1][j-1] + triangle[i-1][j]
    
    return triangle
```

## Usage

To generate Pascal's Triangle and print it, you can use the following code:

```python
from pascals_triangle import generate_pascals_triangle

num_rows = 5
triangle = generate_pascals_triangle(num_rows)

for row in triangle:
    print(row)
```

Replace `num_rows` with the desired number of rows in Pascal's Triangle. The above example will print the first 5 rows of the triangle.

## Example Output

For `num_rows = 5`, the output will be:

```
[1]
[1, 1]
[1, 2, 1]
[1, 3, 3, 1]
[1, 4, 6, 4, 1]
```

## Contributing

If you'd like to contribute to this project, please fork the repository, make your changes, and submit a pull request. Contributions are welcome!

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

Special thanks to Blaise Pascal for his contribution to mathematics and the development of Pascal's Triangle.

