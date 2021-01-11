#!/usr/bin/env python
# coding: utf-8

# ## Testing different libraries for parallel processing in Python

# In[1]:


import numpy as np

# Different ways to speed up your computations using multiple cpu cores
def slow_function(n=1000):
    total = 0.0
    for i, _ in enumerate(range(n)):
        for j, _ in enumerate(range(1, n)):
            total += (i * j)
    return total

data = range(100)


# ### Option 0: sequential loop

# In[2]:


results = []
for _ in data:
    results.append(slow_function())
    
print(results[:10])


# ### Option 1: Multiprocessing
# - Advantage: native python library
# - Disadvantage: verbose

# In[3]:


import multiprocessing as mp

pool = mp.Pool(mp.cpu_count())
results = [pool.apply_async(slow_function, args=()) for row in data]

pool.close()    
pool.join() 
results = [r.get() for r in results]

print(results[:10])


# ### Option 2: Ray  
# - Advantage: one of the least verbose library I'm aware of
# - Disadvantage: NOT native python library
# 
# - More:
#     * Docs: https://docs.ray.io/en/latest/index.html
#     * Github: https://github.com/ray-project/ray (14.4k stars)
#     * Install it first: `pip install ray`.
#     * Bunch of useful tips: https://docs.ray.io/en/latest/auto_examples/tips-for-first-time.html

# In[4]:


import ray
ray.init()

@ray.remote
def paralel_slow_function(x=1000):
    return slow_function(x)

futures = [paralel_slow_function.remote() for _ in data]
print(ray.get(futures[:10])) 

#ray.shutdown()


# ### Option 4: pandarallel
# 
# - Advantage: Do not need anything else if you are doing your work on pandas
# - Disadvantage: only works with pandas
# 
# - More:
#     * Docs: 
#     * Github: https://github.com/nalepae/pandarallel (1.3K stars)
#     * Install it first: `pip install pandarallel`.
#     * Bunch of useful tips: https://github.com/nalepae/pandarallel/blob/master/docs/examples.ipynb

# In[5]:


import pandas as pd
s = pd.Series(data)
s.head()


# In[6]:


# Usual way to apply a function with Pandas. Applying the `slow_function`.
# Got the similar running time as shown above.
s.apply(lambda x: slow_function())


# In[7]:


from pandarallel import pandarallel
pandarallel.initialize(progress_bar=False) # You can specify number of cores, memory, progress_bar


# In[8]:


s.parallel_apply(lambda x: slow_function())


# ### Option 5: Dask
# 
# - Advantage: It is fast and provides parallel implementations for numpy/pandas/sklean...
# - Disadvantage: implementation is similar to native numpy/pandas/sklean but not always the same
# - More:
#     * Docs: https://docs.dask.org/en/latest/
#     * Github: https://github.com/dask/dask (7.7K stars)
#     * Install it first: `pip install dask`.
#     * Bunch of useful tips: https://mybinder.org/v2/gh/dask/dask-examples/master?urlpath=lab
# 

# In[9]:


import dask.dataframe as dd
import pandas as pd
s = pd.Series(data)
ds = dd.from_pandas(s, 12)

ds.apply(lambda x: slow_function(), meta=('float64')).head(10)

