#!/usr/bin/python

import itertools

# Permutations (ordered)
print list(itertools.permutations([1,2,3,4], 2))
# Output
# [(1, 2), (1, 3), (1, 4),
#  (2, 1), (2, 3), (2, 4),
#  (3, 1), (3, 2), (3, 4),
#  (4, 1), (4, 2), (4, 3)]

# Permutations with repeat
print list(itertools.product(range(2),repeat=3))
# Output:
# [(0, 0, 0), (0, 0, 1), (0, 1, 0), (0, 1, 1),
#  (1, 0, 0), (1, 0, 1), (1, 1, 0), (1, 1, 1)]


# Combinations (not ordered)
print list(itertools.combinations('123', 2))
# Output: 
# [('1', '2'), ('1', '3'), ('2', '3')]

# Cartesian product
print list(itertools.product([1,2,3], [4,5,6]))
# Output
# [(1, 4), (1, 5), (1, 6),
#  (2, 4), (2, 5), (2, 6),
#  (3, 4), (3, 5), (3, 6)]
