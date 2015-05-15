import numpy as np
import sys
f1=sys.argv[1]
a=np.genfromtxt(f1)

ave=np.mean(a)
std=np.std(a)
print ave, std
