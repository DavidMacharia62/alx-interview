#!/usr/bin/python3

def canUnlockAll(boxes):
    # Set to keep track of unlocked boxes
    unlocked_boxes = {0}

    # Queue for BFS
    keys_queue = boxes[0][:]

    # Perform BFS
    while keys_queue:
        key = keys_queue.pop(0)

        # Check if the key corresponds to a new box
        if key < len(boxes) and key not in unlocked_boxes:
            unlocked_boxes.add(key)
            keys_queue.extend(boxes[key])

    # Check if all boxes can be unlocked
    return len(unlocked_boxes) == len(boxes)

