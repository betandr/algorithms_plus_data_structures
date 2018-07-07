# Python Algorithms + Data Structures

_"Algorithms + Data Structures = Programs"_ - Niklaus Wirth

A collection of _VERY NAIVE AND NOT PRODUCTION_ algorithms and data structures
implemented in Python.

## Structures

- [Node Chain](structures/node_chain.py)
- [Linked List](structures/linked_list.py)
- [Stack](structures/stack,py)
- [Queue](structures/queue.py)
- [Binary Tree](structures/binary_tree.py)
- [Hash Table](structures/hash_table.py)
- [AVL Tree](structures/avl_tree.py)

## Algorithms

### Sorting
- [Bubble Sort](algorithms/sorting.py)
- [Insertion Sort](algorithms/sorting.py)
- [Selection Sort](algorithms/sorting.py)
- [Merge Sort](algorithms/sorting.py)
- [Quick Sort](algorithms/sorting.py)

Running `python3 algorithms/sorting.py` executes the sorts with the same 1000
item arrays and times the result. This doesn't take into account swaps or
comparisons, for a true performance analysis, but the results are like:
```
bubble sorted in 276 milliseconds
insertion sorted in 71 milliseconds
selection sorted in 66 milliseconds
merge sorted in 5 milliseconds
quicksort sorted in 2 milliseconds
```

## Tests
```
pytest
```
