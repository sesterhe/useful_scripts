import rstoolbox
import pandas as pd
import matplotlib.pyplot as plt
from rstoolbox.io import read_SPR
from rstoolbox.plot import plot_SPR


# In[7]:


infile = ["4hb395_overD25.txt","4hb395_over5c4.txt"]
infilecsv = []
for e in infile:
    f = pd.read_csv(e,sep='\t')
    f.to_csv(e)
    infilecsv.append(e.rsplit('.', 1)[0] + '.csv')


# In[12]:


for e in infilecsv:
    df = read_SPR(e)
    fig = plt.figure(figsize=(10, 6.7))
    ax = plt.subplot2grid((1, 1), (0, 0))
    plt.title(e)
    plot_SPR(df, ax, datacolor='black', fitcolor='red')
    plt.show()
