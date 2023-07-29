#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec 16 12:18:31 2021

@author: alexpanayotof
"""

import numpy
import matplotlib.pyplot
from PIL import Image
p=100
alpha=1.5
beta=1
tlist=[]
plist=[]
for t in range(1,10000):
    b=numpy.random.normal(loc=500000*alpha,scale=27889000000*beta,size=1)
    s=1000000-b
    if b>s:
        p=p+(p/100)
    elif s>b:
        p=p-(p/100)
    else:
        p=p
    tlist.append(t)
    plist.append(p)
    x=numpy.array(tlist)
    y=numpy.array(plist)
matplotlib.pyplot.plot(x,y,color='black')
matplotlib.pyplot.savefig('stockplot.png')
im=Image.open('stockplot.png')
w,h=im.size
colors=im.getcolors(w*h)
colordict={x[1]:x[0] for x in colors}
black=colordict.get((0,0,0,255))
boxdim=((numpy.log(black))/(numpy.log(360)))
print(boxdim)