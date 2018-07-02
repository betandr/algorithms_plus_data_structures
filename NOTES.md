# Notes

# Structures

## Linked List
```
add_head(item)
add_tail(item)
remove_head()
remove_tail()
```

## Stack
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

### RPN calculation:
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

## Queues
```
enqueue(item)
dequeue() => item /remove
peek() => item
```

## Binary Trees
Sorted hierarchy of data.
Starts with root node.
Each child is a tree.
0, 1, or 2 children. Left child, Right child.
Left child: less than parent
Right child: greater than parent
Left-most child is lowest value overall, right-most is highest value overall
### Adding (recursive):
Empty Tree: any node added becomes root.
Smaller value: add to left of parent, keep adding to left
Larger value: add to right of parent, keep adding to right
### Finding:

### Deleting:
Find node
If leaf/terminal just remove (remove parent's reference)
If non-leaf, find the child to replace it, then:
1. (no right child) - promote left child into its place, or
2. (has a right child that has no left child) -  find node to remove, promote right child, or
3. (has a right child that has a left child) - the right child's left child will replace the removed node.
### Enumerate:
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

## Hash Tables
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

### Adding
```
array_length = 8
hash_code = hash(item)
index = hash_code % array_length
array[index] = item
```
### Retrieving
```
array_length = 8
hash_code = hash(item)
index = hash_code % array_length
return array[index]
```

### Collisions
- _Open Addressing_ - Moving to next index in table. Complex to manage.
- _Chaining_ - Storing items in a linked list from array.

### Growing
Load Factor: ratio of filled hash table array locations (aka Fill Factor)

On `add(item)`:
```
if (fill_factor >= max_fill_factor):
    new_array = array_length * 2
    for (item in array):
        hash item to new array
```

# Algorithms

## Sorting
Sorted items are comparably smaller to left of collection and larger to the right.

### Techniques
- _Linear sorting_ - a single, large operation
- _Divide and conquer_ - partition into separately-sortable sets

### Performance
Reducing either or both can help performance:
- _Comparators_ - greater than/equal to/less than.
- _Swaps_ - two values in the collection are transposed

Overall performance then is dependent on the individual performance of each
comparison or swap and can be expressed as _best_, _worst_, and _average_ performance.

### Bubble Sort (Linear)
_Run through array swapping adjacent items until no more swaps needed._
- Worst case: `O(n^2)` - Not appropriate for large, unsorted collections.
- Average case: `O(n^2)` - Not appropriate for large, unsorted collections.
- Best case: `O(n)` - Efficient to sort small or nearly sorted collections.
- Space required: `O(n)` - In-place transpositions.

### Insertion Sort (Linear)
_Single pass through an array inserting current item into place in the sorted
part of the array. Everything to the left is sorted, to the right
is unsorted._
- Worst case: `O(n^2)` - Not appropriate for large, unsorted collections.
- Average case: `O(n^2)` - Not appropriate for large, unsorted collections.
- Best case: `O(n)` - Efficient to sort small or nearly sorted collections.
- Space required: `O(n)` - In-place transpositions.

### Selection Sort (Linear)
_Find next smallest item and swap it to the first unsorted position._
- Worst case: `O(n^2)` - Not appropriate for large, unsorted collections.
- Average case: `O(n^2)` - Not appropriate for large, unsorted collections but
typically better than bubble or insertion sort.
- Best case: `O(n^2)` - Fewer swaps but many more comparisons.
- Space required: `O(n)` - In-place transpositions.

### Merge Sort (Divide and conquer)
_Recursively split array into two arrays until each only has item; all are
considered sorted. Recombine together and sort each smaller item._
- Worst case: `O(n log n)` - Appropriate for large collections. Split collections can be parallelized.
- Average case: `O(n log n)` - Appropriate for large collections.
- Best case: `O(n log n)` - Appropriate for large collections. Cost is fixed, does work regardless
- Space required: `O(n)` - Assuming merge sort is implemented in-place. Extra allocations would increase memory footprint.

### Quick Sort (Divide and conquer)
_Pick a pivot point and partition the array; move all lower values to the left. Re-pivot._
- Worst case: `O(n^2)` - Absolute worst case is inversely sorted.
- Average case: `O(n log n)` - Appropriate for large collections.
- Best case: `O(n log n)` - Appropriate for large collections.
- Space required: `O(n)` - In-place transpositions. Consider recursive stack requirements.
