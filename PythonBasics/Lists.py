"""
* Lists - used to store multiple items in a single variable

Internally, a list is represented as an array; the largest costs come from growing beyond the current allocation size
(because everything must move), or from inserting or deleting somewhere near the beginning (because everything after that must move).
If you need to add/remove at both ends, consider using a collections.deque instead.

Operations and Time complexity-

O(1) --> Append, Pop last, get item, set item, get length
O(n) --> Copy, Pop mid, Insert, Delete, Iterate, Delete Slice, x in S, min(s), max(s)
O(k) where k < n --> get slice, Extend
O(K + N) --> Set Slice
O(kn) --> Multiply
O(nlogn) --> Sort

"""

nums = [1, 2, 3]
ex = [9, 9, 9]
nums.index(1)  # returns index
nums.append(1)  # appends 1
nums.insert(0,10)  # inserts 10 at 0th index
nums.remove(3)  # removes all instances of 3
nums.copy()  # returns copy of the list
nums.count(1)  # returns no.of times '1' is present in the list
nums.extend(ex)  # ...
nums.pop()  # pops last element [which element to pop can also be given as optional argument]
nums.pop(4)  # O(1)
nums.pop(2)  # O(n)
nums.remove(4)  # O(1)
nums.reverse()  # reverses original list (nums in this case)
nums.sort()  # sorts list [does NOT return sorted list]
# Python's default sort uses Tim Sort, which is a combination of both merge sort and insertion sort.

