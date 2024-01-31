# Making Change

## Overview

This Python script provides a solution for the problem of determining the fewest number of coins needed to meet a given total amount using a given set of coin values. The principle applied is that "Change comes from within."

## Problem Statement

Given a pile of coins with different values, the task is to find the fewest number of coins needed to achieve a specified total amount. The function signature is as follows:

```python
def makeChange(coins, total)
```

### Input

- `coins`: A list of integer values representing the different denominations of coins available. Each coin's value is greater than 0.
- `total`: The target amount for which we need to make change.

### Output

The function should return the fewest number of coins needed to meet the total. If the total is 0 or less, the function returns 0. If the total cannot be met by any combination of the available coins, the function returns -1.

## Example

```python
makeChange([1, 2, 25], 37)  # Output: 7
makeChange([1256, 54, 48, 16, 102], 1453)  # Output: -1
```

## Usage

You can test the provided solution using the `0-main.py` script. This script contains examples that demonstrate how the `makeChange` function works.

```python
#!/usr/bin/python3
"""
Main file for testing
"""

makeChange = __import__('0-making_change').makeChange

print(makeChange([1, 2, 25], 37))  # Output: 7
print(makeChange([1256, 54, 48, 16, 102], 1453))  # Output: -1
```

## Runtime Evaluation

The solution's runtime will be evaluated for this task, so it's important to consider the efficiency of your implementation.

## Notes

- The solution assumes an infinite number of each denomination of coin in the list.
- The script will return 0 for a total of 0 or less.
- If the total cannot be met by any combination of the available coins, the script will return -1.

Feel free to use and modify this script to solve similar problems related to making change with different coin denominations.
