#!/usr/bin/env python
# coding: utf-8

# In[7]:


get_ipython().run_line_magic('matplotlib', 'inline')
import matplotlib
import numpy as np


# In[8]:


def f(x):
    return x ** 2 + x + 1
def df(x):
    return 2 * x + 1
x_1 = np.linspace(start = -3, stop=3,num=100)


# In[20]:



new_x = 3
previous_x = 0
step_multiplier = 0.1
precision = 0.00001
x_list = [new_x]
slope_list = [df(new_x)]


# In[21]:


for n in range(500):
    previous_x = new_x
    gradient = df(previous_x)
    new_x = previous_x - step_multiplier * gradient
    step_size = abs(new_x - previous_x)
    x_list.append(new_x)
    slope_list.append(new_x)
    if step_size < precision:
        print('Loop ran this many times:', n)
        break
print('Local minimum occurs at:', new_x)
print('Slope of df(x) value at this point is:', df(new_x))
print('f(x) value or cost at this point is:', f(new_x))


# In[30]:


plt.figure(figsize=[15, 5])

plt.subplot(1, 2, 1)
plt.xlim(-3, 3)
plt.ylim(0, 8)

plt.title('Cost Function', fontsize=17, color='red')
plt.xlabel('X', fontsize=16)
plt.ylabel('f(x)', fontsize=16)
values = np.array(x_list)
plt.scatter(x_list, f(values), color='green', s=300, alpha=0.6)
plt.plot(x_1, f(x_1), color='blue', linewidth=5)
plt.grid()
plt.subplot(1, 2, 2)
plt.title('Slope Of The Function', fontsize=17, color='red')
plt.xlabel('X', fontsize=16)
plt.ylabel('df(x)', fontsize=16)
plt.plot(x_1, df(x_1), color='skyblue', linewidth=5)
plt.scatter(x_list, slope_list, color='green', s=300, alpha=0.6)
plt.style.use('dark_background')
plt.grid()
plt.show()


# In[ ]:




