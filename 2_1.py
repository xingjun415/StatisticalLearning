
# coding: utf-8

# # 统计学习方法：
# ## 例2.1

# In[1]:

import numpy as np


# In[8]:

loop_times = 500
learning_rate = 1

def get_y(w, x, b):
    return np.dot(w,x) + b

def predict(x,y):
    w = np.zeros_like(x[0])
    b = 0
    for _ in range(loop_times):
        have_neg = False
        for index in range(x.shape[0]):
            if y[index] * get_y(w, x[index], b)  <= 0:
                w = w + learning_rate * y[index] * x[index]
                b = b + learning_rate * y[index]
                print("index :{0}, w : {1}, b: {2} ".format(index, w, b))
                have_neg = True
                break
    if not have_neg:
                return w, b
    return w,b        


# In[9]:

x = np.array([[3,3],[4,3],[1,1]])
y = np.array([[1], [1], [-1]])
print(x,y)
w,b = predict(x,y)
print("Result : ", w, b)  


# In[ ]:



