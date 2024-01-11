# N-Queens Problem Solver

The N-Queens puzzle is a classic problem in computer science and combinatorics. The challenge is to place N non-attacking queens on an N×N chessboard. This README provides information on a Python program that solves the N-Queens problem.

## Usage

To use the program, run the following command:

```bash
python nqueens.py N
```

Replace `N` with an integer greater than or equal to 4.

### Examples

```bash
python nqueens.py 4
```

## Error Handling

The program includes error handling to ensure the correct usage.

1. If the user provides the wrong number of arguments, the program prints an error message and exits with status 1.

   Example:
   ```bash
   Usage: nqueens N
   ```

2. If the provided argument is not an integer, the program prints an error message and exits with status 1.

   Example:
   ```bash
   N must be a number
   ```

3. If the provided integer is less than 4, the program prints an error message and exits with status 1.

   Example:
   ```bash
   N must be at least 4
   ```

## Output

The program prints every possible solution to the N-Queens problem, with one solution per line. The format follows the example below:

Example:
```
. Q . .
. . . Q
Q . . .
. . Q .
```

In the output, a queen is represented by the letter "Q," and empty squares are represented by periods (".").

## Algorithm: Backtracking

The solution to the N-Queens problem is found using a backtracking algorithm. Backtracking is a systematic way to find all possible solutions to a problem by trying out different possibilities and undoing those that do not satisfy the problem constraints.

## Import Restrictions

The program adheres to the specified requirements and only imports the `sys` module.

## License

This program is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
