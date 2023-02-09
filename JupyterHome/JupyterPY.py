#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Дана функция f(x) = 5*x**2 + 10*x - 30

# 1. Определить корни

# 2. Найти интервалы, на которых функция возрастает

# 3. Найти интервалы, на которых функция убывает

# 4. Построить график

# 5. Вычислить вершину

# 6. Определить промежутки, на котором f > 0

# 7. Определить промежутки, на котором f < 0


# In[2]:


import numpy as np
import matplotlib.pyplot as plt


# In[3]:


a, b, c = 5, 10, -30


# In[4]:


def func(x):
    return a*x**2 + b*x + c


# In[16]:


limit = 5
step = 0.01


# In[5]:


x = np.arange(-limit, limit, step)


# In[9]:


def take_roots(a, b, c) -> tuple:
    discr = (b**2 - 4*a*c)
    if discr > 0:
        x1 = (-b + discr**0.5)/(2*a)
        x2 = (-b - discr**0.5)/(2*a)
        return round(x1, 2), round(x2, 2)
    elif discr == 0:
        x = -b/(2*a)
        return (round(x, 2), )
    else:
        return (None, )


# In[7]:


roots = take_roots(a, b, c)
print(roots)


# In[11]:


min_y = min(func(x))
min_x = take_roots(a, b, c - min_y)[0]
print(min_x, min_y)


# In[19]:


x_down_pos = np.arange(-limit, min(roots), step)
x_down_neg = np.arange(min(roots), min_x, step)
x_up_neg = np.arange(min_x, max(roots), step)
x_up_pos = np.arange(max(roots), limit, step)


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[25]:


plt.rcParams['lines.linestyle'] = '-'
plt.plot(x_down_pos, func(x_down_pos), 'b', label = 'Убывание больше 0')
plt.plot(x_up_pos, func(x_up_pos), 'r', label = 'Возрастание больше 0')

plt.rcParams['lines.linestyle'] = '-.'
plt.plot(x_down_neg, func(x_down_neg), 'b', label = 'Убывание меньше 0')
plt.plot(x_up_neg, func(x_up_neg), 'r', label = 'Возрастание меньше 0')

if len(roots) == 2:
    plt.plot(roots[0], 0, 'yo', label = f'Корни ({roots[0]}, {roots[1]})')
    plt.plot(roots[1], 0, 'yo')
else:
    if roots[0] != None:
        plt.plot(roots[0], 0, 'yo', label = f'Корни ({roots[0]}, {roots[1]})')
        
plt.plot(min_x, min_y, 'gx', label = f'Экстремум функции ({min_x}, {min_y})')
plt.legend()
plt.grid()


# In[ ]:




