import itertools as it

l = ['a', 'b', 'c', 'd']

perms = it.permutations(l, r = 2)
perms_list = list(perms)
print('Permutations list:', perms_list)

combs = it.combinations(l, r = 3)
combs_list = list(combs)
print('Combinations list:', combs_list)

l1 = [1,2]
prod = it.product(l, l1 , repeat = 1)
prod_list = list(prod)
print('Product list:', prod_list)

# trying out the statistics module now

import statistics as st

l = [1, 2, 2, 3, 3, 4, 4, 4, 5, 6, 6, 7]
print('Mean:', st.mean(l))
print('Median:', st.median(l))
print('Mode:', st.mode(l))