import numpy as np
import sys
import _pickle

import matplotlib.pyplot as plt

import thinkplot
import thinkstats2
from thinkstats2 import Cdf, Pmf


history = _pickle.load(open(sys.argv[1], "rb"))

print(len(history))
print(len(history[history[:,0,50] == 100, :, 50]))
print(len(history[history[:,0,50] > 50, :, 50]))
print(len(history[history[:,0,50] < 50, :, 50]))



# thinkplot.plot(history[:10,3,:50].T)
# thinkplot.show()

thinkplot.plot(np.sum(history[:,3,:], axis=0).T)
thinkplot.show()
