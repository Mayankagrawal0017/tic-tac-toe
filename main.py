print("hello")

print(3*3)

import random
import  numpy as np
A = np.arange(25,512,10)
A = iter(A)
print(A)
print(A.__next__())
print("And")
for i in A:
    print(i)