#Steven Kravitsky
#12586350
#Assignment 4
#Problem 7

import itertools
from collections import Counter

x = [1, 2, 3, 4]
ans = []
y = [p for p in itertools.product(x, repeat=4)]

for i in range (len(y)):
    ans.append(len(set(y[i])))

res = Counter(ans)

print res.values()
