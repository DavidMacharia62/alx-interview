# Lockboxes

This Python script provides a method to determine whether all the boxes in a given set of locked boxes can be opened or not. Each box is numbered sequentially from 0 to n - 1, and each box may contain keys to other boxes. The task is to check if, starting with the first box, all the boxes can be opened by following the keys inside them.

## Method: `canUnlockAll`

### Prototype

```python
def canUnlockAll(boxes):
    pass
```

### Parameters

- `boxes`: A list of lists representing the locked boxes. Each box is a list containing positive integers representing the keys it contains.

### Returns

- `True` if all boxes can be opened, otherwise `False`.

### Example Usage

```python
boxes = [[1], [2], [3], [4], []]
print(canUnlockAll(boxes))  # Output: True

boxes = [[1, 4, 6], [2], [0, 4, 1], [5, 6, 2], [3], [4, 1], [6]]
print(canUnlockAll(boxes))  # Output: True

boxes = [[1, 4], [2], [0, 4, 1], [3], [], [4, 1], [5, 6]]
print(canUnlockAll(boxes))  # Output: False
```

### Algorithm

The method uses a breadth-first search (BFS) approach to explore the keys in each box iteratively. It maintains a set to keep track of the boxes that can be unlocked. The algorithm starts with the first box (index 0) unlocked and explores its keys. It continues this process until no more new boxes can be unlocked or until all the boxes are unlocked.

The pseudocode for the algorithm is as follows:

```plaintext
1. Initialize an empty set `unlocked_boxes` with the first box (index 0).
2. Initialize a queue with the keys of the first box.
3. While the queue is not empty:
    a. Dequeue a key from the queue.
    b. If the key corresponds to a new box that is not in `unlocked_boxes`:
        i. Add the box index to `unlocked_boxes`.
        ii. Enqueue the keys of the newly unlocked box.
4. If the length of `unlocked_boxes` is equal to the total number of boxes, return True.
5. Otherwise, return False.
```

This approach ensures that the algorithm explores all reachable boxes and checks if all boxes can be unlocked.

### Running the Example

Save the provided Python script (`main_0.py`) and the lockboxes module (`0-lockboxes.py`) in the same directory. Then, execute the script:

```bash
./main_0.py
```

The output should match the expected results mentioned in the example usage.
