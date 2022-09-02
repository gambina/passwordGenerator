# 16 characters
# Uppercase
# Lowercase
# Number
# Special character
# There needs to be at least 1 for each

import string
import random
import numpy as np

lower = string.ascii_lowercase
upper = string.ascii_uppercase
nums = string.digits
special = string.punctuation

chance = np.random.dirichlet(np.ones(4), size=1)
print(chance[0, 0]*16)
print(chance[0, 1]*16)
print(chance[0, 2]*16)
print(chance[0, 3]*16)
print(chance[0, 0]+chance[0, 1]+chance[0, 2]+chance[0, 3])

# how many lowercase
lca = random.randint(1, 13)
print('lca', lca)
if lca == 13:
    uca = 1
    nca = 1
    pca = 1
else:
    uca = random.randint(1, 14-lca)
print('uca', uca)
if lca + uca == 14:
    nca = 1
    pca = 1
else:
    nca = random.randint(1, 14-lca-uca)
pca = 16-lca-uca-nca


print('nca', nca)
print('pca', pca)


# lower[random.randint(0, len(lower)-1)]

# print(len(lower)-1)
# print(len(upper)-1)
# print(len(nums)-1)
# print(len(special)-1)
