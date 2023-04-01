#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')
data = {
    1786:627,
    1811:3800,
    1840:4400,
    1856:7200,
    1860:7027,
    1873:13932,
    1884:36308,
    1897:55000,
    1926:151000,
    1939:445000,
    1959:591000,
    1970:815000,
    1979:926000,
    1989:999000,
    2002:1011000,
    2010:1021000,
    2016:1016000,
    2021:1028000,
}
years=np.array(list(data.keys()));
people=np.array(list(data.values()));


plt.plot(years, people, label = r"Население Волгограда")
plt.grid(True)
plt.legend()
plt.show()



# In[2]:


from scipy.integrate import odeint
def dydt(y, t):
    k=0.06
    return k*y
t=years
solve=odeint(dydt,y0=1,t=t)
solve=solve.flatten()
get_ipython().run_line_magic('matplotlib', 'inline')
plt.plot(t, solve, color="red")
plt.plot(years, people, label = r"Население Волгограда")
plt.grid(True)
plt.show()


# In[29]:


def k(x):
    a = 5
    b =0.00001
    return a - b * x
def dydt2(x, t):
    return k(x) * x

t=years

solve = odeint(dydt2, y0=1, t=t)
solve = solve.flatten()

get_ipython().run_line_magic('matplotlib', 'inline')
plt.plot(t, solve, color="red")
plt.plot(years, people, label = r"Население Волгограда")
plt.grid(True)
plt.legend()
plt.show()


# In[ ]:




