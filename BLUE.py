#!/usr/bin/env python
# coding: utf-8

# In[275]:


import matplotlib.pyplot as plt
import numpy as np
import math


# In[282]:


A = 8 # przyjęta amplituda
si= 2 # przyjęty poziom szumów
N= 100 # liczba próbek syngału 
f= 20# częstotiliwośc syngnału 
w=si*np.random.rand(1,N)# zaszumiony sygnał 


# In[283]:


war=np.var(w)


# In[284]:


Od_war=1/war
I=np.eye(N)


s=np.zeros(N)
x=np.zeros(N)

for i in range(N):
        s[i]=np.array(np.sin(2*3.14*f*i+0.3))
        

for i in range(N):        
    x=np.array(A*s+w)



# In[285]:


def Blue():
    r=x.flatten() 
    y=((s*Od_war)*I)
    z=y[0,:]

    g=np.reshape(np.transpose(r),(100,1))
    h=np.reshape(np.transpose(s),(100,1))

    li=np.dot(z,g)
    mi=np.dot(z,h)    
    wyn=li/mi
    return wyn


# In[286]:


print(Blue())


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




