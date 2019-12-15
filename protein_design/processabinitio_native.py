import numpy as np
import matplotlib.pyplot as plt
import sys

file=open(sys.argv[1])
file2 = open(sys.argv[2])
f=file.readlines()
f2 = file2.readlines()
#print(f)
x = [float(line.split()[1]) for line in f]
y = [float(line.split()[0]) for line in f]
x2 =  [float(line.split()[1]) for line in f2]
y2 = [float(line.split()[0]) for line in f2]
#print(x)
plt.scatter(x,y,color='blue')
plt.scatter(x2,y2,color='red')
plt.ylabel('SCORE')
plt.xlabel('RMSD')
axes = plt.gca()
axes.set_xlim([0,15])
axes.set_ylim([-150,-80])
plt.title(sys.argv[1])
plt.savefig('abinitio'+sys.argv[1].split(".")[0]+'.png')
plt.show()
