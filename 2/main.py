# -*- coding: utf-8 -*-
import numpy as np
from itertools import count
n = 4000000
def fib(n):
    x = np.array([[0,1],
                  [1,1]])
    base_case = np.array([0,1])
    x_n = np.linalg.matrix_power(x,n)
    arr =  x_n@base_case
    return arr[1]

l = []
for i in count():
    if fib(i)%2==0:
        l.append(fib(i))
    if sum(l) > 4000000: 
        print(f'Series is {l} and,\nSum is {sum(l)}')
        break