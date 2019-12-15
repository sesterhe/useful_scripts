import numpy as np
import matplotlib.pyplot as plt
import sys

file=open(sys.argv[1])
f=file.readlines()
#print(f)
x = [float(line.split()[1]) for line in f]
y = [float(line.split()[0]) for line in f] 
#print(x)
plt.scatter(x,y)
plt.ylabel('SCORE')
plt.xlabel('RMSD')
axes = plt.gca()
axes.set_xlim([0,15])
axes.set_ylim([-180,-100])
plt.title(sys.argv[1])
plt.savefig('abinitio.png') 
plt.show()
