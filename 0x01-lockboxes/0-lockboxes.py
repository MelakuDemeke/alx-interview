#!/usr/bin/python3
""" Lockboxes

This module provides a function for checking if all the boxes in a list
of lockboxes can be unlocked, given that the first box is unlocked.
"""


def canUnlockAll(boxes):
    '''
    Checks if all the lockboxes can be unlocked.

    Args:
        boxes (list of lists): A list of lockboxes where each box contains
                              keys (indices) to other boxes.

    Returns:
        bool: True if all lockboxes can be unlocked, False otherwise.
    '''
    num_boxes = len(boxes)
    seen_boxes = set([0])
    unseen_boxes = set(boxes[0]).difference(set([0]))

    while len(unseen_boxes) > 0:
        box_index = unseen_boxes.pop()

        # Ensure box_index is within valid bounds
        if not (0 <= box_index < num_boxes):
            continue

        if box_index not in seen_boxes:
            unseen_boxes = unseen_boxes.union(boxes[box_index])
            seen_boxes.add(box_index)

    return num_boxes == len(seen_boxes)
