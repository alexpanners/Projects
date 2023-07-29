#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 11 16:19:41 2022

@author: Alex Panayotof
"""

# 2D Ising Model (run time: approx. 2 min 10 s)

# we take blue to be spin-up, red to be spin-down, and J=k=1

# import

import numpy as np

import matplotlib.pyplot as plt
    
# generate lattice (10000 particles)

def lattice():
    
    xvals=[]
    
    yvals=[]
    
    points=[]
    
    for i in range(0,100):
        
        xvals.append(i)
        
    for j in range(0,100):
        
        yvals.append(j)
        
    for x in xvals:
        
        for y in yvals:
        
            points.append([x,y])
    
    lspin=[]
    
    for c in range(0,10000):
            
        r=np.random.randint(100)
            
        if r<50:
                
            lspin.append('r')
                
        else:
                
            lspin.append('b')
                
    data=np.array(points)
    
    x,y=data.T
    
    # return x and y values, list of spin values (color)
    
    return x,y,lspin

# simulate

def simulate(x,y,spin,T):
    
    energylist=[]
    
    upedge=[]
    
    downedge=[]
    
    leftedge=[]
    
    rightedge=[]
    
    for k in range(1,99): 
        
        upedge.append(k*100+99)
        
        downedge.append(k*100)
        
        leftedge.append(k)
        
        rightedge.append(9900+k)
        
    # show initial lattice
    
    plt.scatter(x,y,color=spin)
    
    plt.show()
    
    # advance time
    
    for t in range(0,1000000):
        
        # metropolis algorithm
        
        n,m=np.random.randint(0,100),np.random.randint(0,100)
        
        sup=0
        
        sright=0
        
        sleft=0
        
        sdown=0
        
        s=0
        
        if n==99 and m==99:
            
            if spin[99]=='b':
            
                sright=1
            
            else:
            
                sright=-1
            
            if spin[9899]=='b':
            
                sleft=1
            
            else:
            
                sleft=-1
            
            if spin[9900]=='b':
            
                sup=1
            
            else:
            
                sup=-1
            
            if spin[9998]=='b':
            
                sdown=1
            
            else:
            
                sdown=-1
            
            if spin[9999]=='b':
            
                s=-1
            
            else:
            
                s=1
                
        elif n==99 and m==0:
            
            if spin[0]=='b':
            
                sright=1
            
            else:
            
                sright=-1
            
            if spin[9800]=='b':
            
                sleft=1
            
            else:
            
                sleft=-1
            
            if spin[9901]=='b':
            
                sup=1
            
            else:
            
                sup=-1
            
            if spin[9999]=='b':
            
                sdown=1
            
            else:
            
                sdown=-1
            
            if spin[9900]=='b':
            
                s=-1
            
            else:
            
                s=1
                
        elif n==0 and m==99:
            
            if spin[199]=='b':
            
                sright=1
            
            else:
            
                sright=-1
            
            if spin[9999]=='b':
            
                sleft=1
            
            else:
            
                sleft=-1
            
            if spin[0]=='b':
            
                sup=1
            
            else:
            
                sup=-1
            
            if spin[98]=='b':
            
                sdown=1
            
            else:
            
                sdown=-1
            
            if spin[99]=='b':
            
                s=-1
            
            else:
            
                s=1
                
        elif n==0 and m==0:
            
            if spin[100]=='b':
            
                sright=1
            
            else:
            
                sright=-1
            
            if spin[9900]=='b':
            
                sleft=1
            
            else:
            
                sleft=-1
            
            if spin[1]=='b':
            
                sup=1
            
            else:
            
                sup=-1
            
            if spin[99]=='b':
            
                sdown=1
            
            else:
            
                sdown=-1
            
            if spin[0]=='b':
            
                s=-1
            
            else:
            
                s=1
        
        elif n==99:
            
            if spin[m]=='b':
            
                sright=1
            
            else:
            
                sright=-1
            
            if spin[9800+m]=='b':
            
                sleft=1
            
            else:
            
                sleft=-1
            
            if spin[9900+(m+1)]=='b':
            
                sup=1
            
            else:
            
                sup=-1
            
            if spin[9900+(m-1)]=='b':
            
                sdown=1
            
            else:
            
                sdown=-1
            
            if spin[9900+m]=='b':
            
                s=-1
            
            else:
            
                s=1
            
        elif m==99:
            
            if spin[(n+1)*100+99]=='b':
            
                sright=1
            
            else:
            
                sright=-1
            
            if spin[(n-1)*100+99]=='b':
            
                sleft=1
            
            else:
            
                sleft=-1
            
            if spin[n*100]=='b':
            
                sup=1
            
            else:
            
                sup=-1
            
            if spin[n*100+98]=='b':
            
                sdown=1
            
            else:
            
                sdown=-1
            
            if spin[n*100+99]=='b':
            
                s=-1
            
            else:
            
                s=1
                
        elif m==0:
            
            if spin[(n+1)*100]=='b':
            
                sright=1
            
            else:
            
                sright=-1
            
            if spin[(n-1)*100]=='b':
            
                sleft=1
            
            else:
            
                sleft=-1
            
            if spin[n*100+1]=='b':
            
                sup=1
            
            else:
            
                sup=-1
            
            if spin[n*100+99]=='b':
            
                sdown=1
            
            else:
            
                sdown=-1
            
            if spin[n*100]=='b':
            
                s=-1
            
            else:
            
                s=1
                
        elif n==0:
            
            if spin[100+m]=='b':
            
                sright=1
            
            else:
            
                sright=-1
            
            if spin[9900+m]=='b':
            
                sleft=1
            
            else:
            
                sleft=-1
            
            if spin[(m+1)]=='b':
            
                sup=1
            
            else:
            
                sup=-1
            
            if spin[(m-1)]=='b':
            
                sdown=1
            
            else:
            
                sdown=-1
            
            if spin[m]=='b':
            
                s=-1
            
            else:
            
                s=1
        
        else:
        
            if spin[(n+1)*100+m]=='b':
            
                sright=1
            
            else:
            
                sright=-1
            
            if spin[(n-1)*100+m]=='b':
            
                sleft=1
            
            else:
            
                sleft=-1
            
            if spin[n*100+(m+1)]=='b':
            
                sup=1
            
            else:
            
                sup=-1
            
            if spin[n*100+(m-1)]=='b':
            
                sdown=1
            
            else:
            
                sdown=-1
            
            if spin[n*100+m]=='b':
            
                s=-1
            
            else:
            
                s=1
            
        e=-2*(s*(sup+sdown+sleft+sright))
        
        if e<=0:
            
            if spin[n*100+m]=='b':
        
                spin[n*100+m]='r'
            
            else:
                
                spin[n*100+m]='b'
                
        elif np.exp(-e/T)>np.random.uniform(0,1):
            
            if spin[n*100+m]=='b':
        
                spin[n*100+m]='r'
            
            else:
                
                spin[n*100+m]='b'
                
        # get sample of energy at equilibrium
                
        if t>997999:
            
            energy=0
            
            for j in range(len(spin)):
        
                if j==9999:
                
                    if spin[99]=='b':
            
                        sright=1
            
                    else:
            
                        sright=-1
            
                    if spin[9899]=='b':
            
                        sleft=1
            
                    else:
            
                        sleft=-1
            
                    if spin[9900]=='b':
            
                        sup=1
            
                    else:
            
                        sup=-1
            
                    if spin[9998]=='b':
            
                        sdown=1
            
                    else:
            
                        sdown=-1
            
                    if spin[9999]=='b':
            
                        s=1
            
                    else:
            
                        s=-1
                        
                elif j==9900:
            
                    if spin[0]=='b':
            
                        sright=1
            
                    else:
            
                        sright=-1
            
                    if spin[9800]=='b':
            
                        sleft=1
            
                    else:
            
                        sleft=-1
            
                    if spin[9901]=='b':
            
                        sup=1
            
                    else:
            
                        sup=-1
            
                    if spin[9999]=='b':
            
                        sdown=1
            
                    else:
            
                        sdown=-1
            
                    if spin[9900]=='b':
            
                        s=1
            
                    else:
            
                        s=-1
                
                elif j==99:
            
                    if spin[199]=='b':
            
                        sright=1
            
                    else:
            
                        sright=-1
            
                    if spin[9999]=='b':
            
                        sleft=1
            
                    else:
            
                        sleft=-1
            
                    if spin[0]=='b':
            
                        sup=1
            
                    else:
            
                        sup=-1
            
                    if spin[98]=='b':
            
                        sdown=1
            
                    else:
            
                        sdown=-1
            
                    if spin[99]=='b':
            
                        s=1
            
                    else:
            
                        s=-1
                
                elif j==0:
            
                    if spin[100]=='b':
            
                        sright=1
            
                    else:
            
                        sright=-1
            
                    if spin[9900]=='b':
            
                        sleft=1
            
                    else:
            
                        sleft=-1
            
                    if spin[1]=='b':
            
                        sup=1
                        
                    else:
            
                        sup=-1
            
                    if spin[99]=='b':
            
                        sdown=1
            
                    else:
            
                        sdown=-1
            
                    if spin[0]=='b':
            
                        s=1
            
                    else:
            
                        s=-1
                
                elif j in tuple(rightedge):
            
                    if spin[j-9900]=='b':
            
                        sright=1
            
                    else:
            
                        sright=-1
            
                    if spin[j-100]=='b':
            
                        sleft=1
            
                    else:
            
                        sleft=-1
            
                    if spin[j+1]=='b':
            
                        sup=1
            
                    else:
            
                        sup=-1
            
                    if spin[j-1]=='b':
            
                        sdown=1
            
                    else:
            
                        sdown=-1
            
                    if spin[j]=='b':
            
                        s=1
            
                    else:
            
                        s=-1
            
                elif j in tuple(upedge):
            
                    if spin[j+100]=='b':
            
                        sright=1
            
                    else:
            
                        sright=-1
            
                    if spin[j-100]=='b':
            
                        sleft=1
            
                    else:
            
                        sleft=-1
            
                    if spin[j-99]=='b':
            
                        sup=1
            
                    else:
            
                        sup=-1
            
                    if spin[j-1]=='b':
            
                        sdown=1
            
                    else:
            
                        sdown=-1
            
                    if spin[j]=='b':
            
                        s=1
            
                    else:
            
                        s=-1
                        
                elif j in tuple(downedge):
            
                    if spin[j+100]=='b':
            
                        sright=1
            
                    else:
            
                        sright=-1
            
                    if spin[j-100]=='b':
            
                        sleft=1
            
                    else:
            
                        sleft=-1
            
                    if spin[j+1]=='b':
            
                        sup=1
            
                    else:
            
                        sup=-1
            
                    if spin[j+99]=='b':
            
                        sdown=1
            
                    else:
            
                        sdown=-1
            
                    if spin[j]=='b':
            
                        s=1
            
                    else:
            
                        s=-1
                
                elif j in tuple(leftedge):
            
                    if spin[j+100]=='b':
            
                        sright=1
            
                    else:
            
                        sright=-1
            
                    if spin[j+9900]=='b':
            
                        sleft=1
            
                    else:
            
                        sleft=-1
            
                    if spin[j+1]=='b':
            
                        sup=1
            
                    else:
            
                        sup=-1
            
                    if spin[j-1]=='b':
            
                        sdown=1
            
                    else:
            
                        sdown=-1
            
                    if spin[j]=='b':
            
                        s=1
            
                    else:
            
                        s=-1
        
                else:
        
                    if spin[j+100]=='b':
            
                        sright=1
            
                    else:
            
                        sright=-1
            
                    if spin[j-100]=='b':
            
                        sleft=1
            
                    else:
            
                        sleft=-1
            
                    if spin[j+1]=='b':
            
                        sup=1
            
                    else:
            
                        sup=-1
            
                    if spin[j-1]=='b':
            
                        sdown=1
            
                    else:
            
                        sdown=-1
            
                    if spin[j]=='b':
            
                        s=1
            
                    else:
            
                        s=-1
                
                energy=energy+(-s*(sright+sleft+sup+sdown))
            
            energylist.append(energy)
            
    # show final lattice
            
    plt.scatter(x,y,color=spin)
    
    plt.show()               
    
    # return new list of spin values (color)
    
    return spin,energylist

# calculate macroscopic quantities
    
def calc(newspin,T,elist):
    
    # calculate final energy (direct counting)
    
    newenergy=0
    
    newenergy=elist[-1]
    
    # calculate magnetization (direct counting)
    
    magnet=0
    
    for spins in newspin:
        
        if spins=='b':
            
            magnet=magnet+1
            
        else:
            
            magnet=magnet-1
    
    # calculate entropy (block method)
    
    entropy=0
    
    entropylist=[]
    
    for i in range(0,10):
        
        for j in range(0,10):
            
            eblock=[]
        
            for n in range((i*10),(i*10)+10):
                
                for m in range((n*100)+(j*10),(n*100)+(10*j)+10):
                    
                    eblock.append(newspin[m])
                    
            entropylist.append(eblock)
            
    for w in range(0,100):
    
        l=0
        
        for v in range(0,100):
            
            if entropylist[w][v]=='b':
                
                l=l+1
                
        if l==0:
            
            blockentropy=1
            
        elif l==100:
            
            blockentropy=1
            
        else:
            
            blockentropy=100*np.log(100)-l*np.log(l)-(100-l)*np.log(100-l)
        
        entropy=entropy+blockentropy
    
    # calculate heat capacity (using equilibrium energy sample)
    
    heatcap=0
    
    emean=0
    
    evar=0
    
    for e in elist:
        
        emean=emean+e
        
    emean=(emean/2000)
    
    for e in elist:
        
        evar=evar+((e-emean)**2)
        
    evar=(evar/1999)
    
    heatcap=(evar/(T**2))
    
    return newenergy,magnet,heatcap,entropy
    
# main function

def main():
    
    # set temperature
    
    T=float(input("Please enter temperature:\n"))
    
    # construct system
    
    x,y,spin=lattice()
    
    # simulate
    
    newspin,elist=simulate(x,y,spin,T)
    
    # calculate
    
    newenergy,magnet,heatcap,entropy=calc(newspin,T,elist)
    
    # show final calculations
    
    print("The magnetization of the system is",(magnet/10000),"ampere meters squared")
    
    print("The entropy of the system is",(int(entropy)/10000),"joules per kelvin")
    
    print("The energy of the system is",(newenergy/10000),"joules")
    
    print("The heat capacity of the system is",(int(heatcap)/10000),"joules per kelvin")
    
    return

# run program
    
main()