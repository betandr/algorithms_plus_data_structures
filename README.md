# Python Algorithms + Data Structures

_"Algorithms + Data Structures = Programs"_ - Niklaus Wirth

A collection of _VERY NAIVE AND NOT PRODUCTION_ algorithms and data structures
implemented in Python just to help me learn Python.

## Structures

- [Node Chain](structures/node_chain.py)
- [Linked List](structures/linked_list.py)
- [Stack](structures/stack,py)
- [Queue](structures/queue.py)
- [Binary Tree](structures/binary_tree.py)
- [Hash Table](structures/hash_table.py)
- [AVL Tree](structures/avl_tree.py) (balancing functions not completed)

## Algorithms

### Sorting
- [Bubble Sort](algorithms/sorting.py#L2)
- [Insertion Sort](algorithms/sorting.py#L18)
- [Selection Sort](algorithms/sorting.py#L30)
- [Merge Sort](algorithms/sorting.py#L41)
- [Quick Sort](algorithms/sorting.py#L86)
- [Naïve String Searching](algorithms/string_search.py#L8)
- [Boyer-Moore-Horspool String Searching](algorithms/string_search.py#L18)
- [Dijkstra's shortest path](algorithms/dijkstra.py#L47)
- [Binary Search](algorithms/binary_search.py)

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

## Notes

### Structures

#### Linked List
```
add_head(item)
add_tail(item)
remove_head()
remove_tail()
```

#### Stack
```
push(item)
pop() => item/remove
peek() => item
```

Stack can be implemented with a linked list. This means no size limit or initial allocation as in an array, although memory is allocated on every push so could be less performant than an array-backed stack.

An array-backed stack would need re-allocation of arrays to contain the stack items but this would be done every n pushes to the stack, where n is the frequency that the array should be re-allocated rather than on every push.

Stack implementation: C# push, peek, pop (pop returns value). C++ push, top, pop (pop does not return value but removes it).

Reverse Polish (Postfix) Notation: 5 6 7 * + 1 -
Infix Notation: 5 + 6 * 7 - 1

##### RPN calculation:
```
for each token:
  if token is integer:
    push token
  else if token is operator
    right side value = pop from stack
    left side value = pop from stack
    evaluate left operator right
    push result
```

#### Queues
```
enqueue(item)
dequeue() => item /remove
peek() => item
```

#### Binary Trees
Sorted hierarchy of data.
Starts with root node.
Each child is a tree.
0, 1, or 2 children. Left child, Right child.
Left child: less than parent
Right child: greater than parent
Left-most child is lowest value overall, right-most is highest value overall
##### Adding (recursive):
Empty Tree: any node added becomes root.
Smaller value: add to left of parent, keep adding to left
Larger value: add to right of parent, keep adding to right
##### Finding:

##### Deleting:
Find node
If leaf/terminal just remove (remove parent's reference)
If non-leaf, find the child to replace it, then:
1. (no right child) - promote left child into its place, or
2. (has a right child that has no left child) -  find node to remove, promote right child, or
3. (has a right child that has a left child) - the right child's left child will replace the removed node.
##### Enumerate:
Basic - process node, visit left, visit right
Order: pre-order, in-order, post-order.
```
# pre-order
visit(node)
  if (node == null)
    return
  process(node.value)
  visit(node.left)
  visit(node.right)
```

```
# in order (process items in sort-order)
visit(node)
  if(node == null)
    return
  visit(node.left)
  process(node.value)
  visit(node.right)
```

```
# post-order
visit(node)
  if(node == null)
    return
  visit(node.left)
  visit(node.right)
  process(node.value)
```

in-order used to process items in _sort order_.
post-order used as a _children first_ dependency graph when children must be processed before their parent.
pre-order used as a _parents first_ dependency graph when parents must be processed before their children.

#### Hash Tables
_Associative array_ - key/value pairs, index any comparable type, not just integer
```
index = get_index(jane.name)
_array[index] = jane
```
Hashing - fixed-sized result from an input. Every string and length returns hash of the same length and type.
Four properties:
- _Stability_ - (invariant) always same value  
- _Uniformity_ - (ideal) hash value uniformly distributed through available space. _1 million values in 4 billion should generally return uniques but some collisions may occur with some algorithms_ 32-bit gives us 4 billion values and there are more than 4 billion strings available.
- _Efficiency_ - (ideal) cost of generating has balanced with application needs
- _Security_ - (ideal) cost of finding data that produces a given has is prohibitive

| Algorithm | Stable | Uniform | Efficient | Secure |
|-----------|:------:|:-------:|:---------:|:------:|
| Additive  |   ✓    |    ✗    |     ✓     |   ✗    |
| Folding   |   ✓    |    ✓    |     ✓     |   ✗    |
| CRC32     |   ✓    |    ✓    |     ✓     |   ✗    |
| MD5       |   ✓    |    ✓    |     ✗     |   ✗    |
| SHA-2     |   ✓    |    ✓    |     ✗     |   ✓    |

##### Adding
```
array_length = 8
hash_code = hash(item)
index = hash_code % array_length
array[index] = item
```
##### Retrieving
```
array_length = 8
hash_code = hash(item)
index = hash_code % array_length
return array[index]
```

##### Collisions
- _Open Addressing_ - Moving to next index in table. Complex to manage.
- _Chaining_ - Storing items in a linked list from array.

##### Growing
Load Factor: ratio of filled hash table array locations (aka Fill Factor)

On `add(item)`:
```
if (fill_factor >= max_fill_factor):
    new_array = array_length * 2
    for (item in array):
        hash item to new array
```

#### Set
Has methods:
- `add(item) # Adds item if not already present`
- `add_range(items)`
- `count() # AKA Cardinality`
- `contains(item)`
- `union(set)`
- `intersection(set)`
- `difference(set)`
- `symmetric_difference(set)`

##### Union
Returns a set that contains all of the unique items in two other sets.
```
{1, 2, 3} ∪ {3, 4, 5} = {1, 2, 3, 4, 5}
```

##### Intersection
Returns a set that contains all of the intersecting members of two other sets.
```
{1, 2, 3} ∩ {3, 4, 5} = {3}
```

##### Difference
Returns a set that contains members of one set that are not members of a second set.
```
{1, 2, 3} ∖ {3, 4, 5} = {1, 2}
```

##### Symmetric Difference
Returns a set that contains members of two sets that are not in the other set.
```
{1, 2, 3} △ {3, 4, 5} = {1, 2, 4, 5}
```

#### AVL Trees
Self-balancing binary tree invented by Adelson-Velsky and Landis (1962)
- Follows all constraints of binary tree
- Search and enumeration identical to binary trees
- Insertion and deletion differ only in running the balance algorithm

AVL trees:
- Self-balancing
- Height
- Balance Factor
- Right/Left heavy

##### Unbalanced tree
Left height: 0
Right height: 3
```
(1)
  \
  (2)
    \
    (3)
      \
      (4)
```
Finding `4` has O(n) performance as linked-list. Example could be loading dictionary in
alphabetical order would produce unbalanced tree.

##### Balanced tree
Left height: 2
Right height: 1
```
       (3)
      /   \
    (2)    (4)
   /
(1)
```
Finding `4` has O(log n) performance as tree.

Balancing algorithm: _Height of left and right tree can differ by maximum of 1_

##### Insertion
1. Added as binary tree; lesser added to left, greater or equal to the right
2. Balancing algorithm runs for every parent node.

##### Deletion
1. The node to delete is found
2. Child nodes are removed as in binary tree
2. Balancing algorithm runs for every parent node.

##### Balancing
- Balancing is done with _Node Rotation_.
- Rotation occurs at the point of insertion and deletion and is repeated up the parents to the root node.
- Rotation changes the physical structure of the tree within the constraints of a binary tree.

##### Node rotation algorithms
- Right rotation
- Left rotation
- Right-Left rotation
- Left-Right rotation

###### Right-heavy tree
```
if right child is left-heavy
   left-right rotation
else
  left rotation
```

###### Left-heavy tree
```
if left child is right-heavy
  right-left rotation
else
  right rotation
```

##### Right rotation
```
temp = node
node = temp.left
temp.left = node.right
node.right = temp
```

##### Left rotation
```
temp = node
node = temp.right
temp.right = node.left
node.left = temp
```

##### Right-left rotation
```
left-rotate the left child
right-rotate the updated tree
```

##### Left-right rotation
```
right-rotate the right child
left rotate the updated tree
```

### Algorithms

#### Sorting
Sorted items are comparably smaller to left of collection and larger to the right.

##### Techniques
- _Linear sorting_ - a single, large operation
- _Divide and conquer_ - partition into separately-sortable sets

##### Performance
Reducing either or both can help performance:
- _Comparators_ - greater than/equal to/less than (less cost if system has fast logic)
- _Swaps_ - two values in the collection are transposed (less cost if system has fast i/o)

Overall performance then is dependent on the individual performance of each
comparison or swap and can be expressed as _best_, _worst_, and _average_ performance.

##### Bubble Sort (Linear)
_Run through array swapping adjacent items until no more swaps needed._
###### Performance
- Worst case: `O(n^2)` - Not appropriate for large, unsorted collections.
- Average case: `O(n^2)` - Not appropriate for large, unsorted collections.
- Best case: `O(n)` - Efficient to sort small or nearly sorted collections.
- Space required: `O(n)` - In-place transpositions.

##### Insertion Sort (Linear)
_Single pass through an array inserting current item into place in the sorted
part of the array. Everything to the left is sorted, to the right
is unsorted._
###### Performance
- Worst case: `O(n^2)` - Not appropriate for large, unsorted collections.
- Average case: `O(n^2)` - Not appropriate for large, unsorted collections.
- Best case: `O(n)` - Efficient to sort small or nearly sorted collections.
- Space required: `O(n)` - In-place transpositions.

##### Selection Sort (Linear)
_Find next smallest item and swap it to the first unsorted position._
###### Performance
- Worst case: `O(n^2)` - Not appropriate for large, unsorted collections.
- Average case: `O(n^2)` - Not appropriate for large, unsorted collections but
typically better than bubble or insertion sort.
- Best case: `O(n^2)` - Fewer swaps but many more comparisons.
- Space required: `O(n)` - In-place transpositions.

##### Merge Sort (Divide and conquer)
_Recursively split array into two arrays until each only has item; all are
considered sorted. Recombine together and sort each smaller item._
###### Performance
- Worst case: `O(n log n)` - Appropriate for large collections. Split collections can be parallelized.
- Average case: `O(n log n)` - Appropriate for large collections.
- Best case: `O(n log n)` - Appropriate for large collections. Cost is fixed, does work regardless
- Space required: `O(n)` - Assuming merge sort is implemented in-place. Extra allocations would increase memory footprint.

##### Quick Sort (Divide and conquer)
_Pick a pivot point and partition the array; move all lower values to the left. Re-pivot._
###### Performance
- Worst case: `O(n^2)` - Absolute worst case is inversely sorted.
- Average case: `O(n log n)` - Appropriate for large collections.
- Best case: `O(n log n)` - Appropriate for large collections.
- Space required: `O(n)` - In-place transpositions. Consider recursive stack requirements.

#### String Searching

##### Naïve algorithm
_Does not need any preprocessing. Useful when search and find strings are small._
```
for start_index in string_to_search
    match_count = 0
    while string_to_search[start_index + match_count] == string_to_find[match_count]
        match_count += 1
        if length of string_to_find == match_count
            return match at start_index of match_count length
```
- Worst case: `O(nm)`
- Average case: `O(n+m)` - Where `n` is the length of the search string and `m` is
the length of the string to find.

##### Boyer-Moore-Horspool algorithm
_Attempts to minimise cost of search by skipping as many characters as possible._
###### Stage 1
- Preprocesses the string to build a _bad match_ table that contains the length to shift when
a bad match occurs.
- Boyer-Moore algorithm creates a second _good suffix_ table.
###### Stage 2
- String to find is searched from the last character to the first.
- The _bad match table_ is used to skip characters when a mismatch occurs.

###### Bad Match Table algorithm
1. Store the length of the search string as the default shift length
2. For each character in the search string
  - Set the shift index for the current character value

###### Performance
Performance improves with longer search strings (the larger the pattern the more
characters skipped). Appropriate as a general purpose search algorithm.
- Worst case: `O(nm)` - With bad scenarios such as single characters.
- Best case: `O(n/m)` - Where `n` is the length of the search string and `m` is
the length of the string to find.
