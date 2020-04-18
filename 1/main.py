# -*- coding: utf-8 -*-
import numpy as np
import timeit

#pure python
def f(n):
    if n%3 == 0 or n%5 == 0:
        return n

multiples = [i for i in range(1,1000) if f(i)]
summ = sum(multiples)

#numpy
x = np.arange(1,1000)
mul = np.ma.masked_where(
        np.logical_and((x%3 != 0),(x%5 != 0)),
        x)
summed = mul.sum()
