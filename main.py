print("hello")

print("git"*3)

import numpy as np
A = np.arange(25,512,10)
A = iter(A)
print(A)

for i in A:
<<<<<<< HEAD
    print(f"{i} : meto-victim :{i**2}")
=======
    print(f"{i**2} : meta victims of day are {i}")
>>>>>>> meto
