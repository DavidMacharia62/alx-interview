# 0x0A. Prime Game

## Description
Maria and Ben are playing a game where they take turns choosing prime numbers from a set of consecutive integers starting from 1 up to and including n, and removing those numbers and their multiples from the set. The player who cannot make a move loses the game.

This project contains a function `isWinner` that determines the winner of each game. The function takes two parameters: `x` (the number of rounds) and `nums` (an array of integers representing different values of n for each round). Assuming Maria always goes first and both players play optimally, the function returns the name of the player who won the most rounds. If the winner cannot be determined, it returns None.

## Prototype
```python
def isWinner(x, nums):
    pass
```

## Tasks
- [x] Implement the `isWinner` function according to the prototype and requirements.
- [ ] Create test cases to ensure the function works as expected.

## Algorithm
The algorithm for determining the winner involves iterating through each round, simulating the game, and keeping track of the number of wins for each player. Players select prime numbers and remove them and their multiples from the set until no prime numbers are left for one player to choose.

## Requirements
- Allowed editors: vi, vim, emacs
- All files will be interpreted/compiled on Ubuntu 20.04 LTS using python3 (version 3.4.3)
- All files should end with a new line
- The first line of all files should be exactly `#!/usr/bin/python3`
- A `README.md` file, at the root of the project folder, is mandatory
- Code should use the PEP 8 style (version 1.7.x)
- All files must be executable
- You cannot import any packages in this task

## Usage
To use the `isWinner` function, import it into your Python script and call it with the desired parameters:

```python
from prime_game import isWinner

x = 3
nums = [4, 5, 1]
print("Winner:", isWinner(x, nums))
```

## Example
```python
x = 3
nums = [4, 5, 1]
print("Winner:", isWinner(x, nums))
# Output: Ben
```

## Files
- `0-prime_game.py`: Python script containing the implementation of the `isWinner` function.
- `main.py`: Sample script demonstrating the usage of the `isWinner` function.

## Author
Carrie Ybay, Software Engineer at Holberton School

## Project Schedule
- Project starts: February 12, 2024 6:00 AM
- Project deadline: February 16, 2024 6:00 AM
- Checker release: February 13, 2024 6:00 AM
- Auto review: Launched at the deadline

## Repository Information
- GitHub repository: [alx-interview](https://github.com/username/alx-interview)
- Directory: 0x0A-primegame
