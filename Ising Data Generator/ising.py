#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 11 16:19:41 2022

@author: Alex Panayotof
"""

# 2D Ising Model Simulation and Data Generator

# this program simulates the Ising model and generates data for a predictive neural network

# remember to choose temperature regime (line 999) and file name (line 1005)

# program initialized for 45000 data points for high temperature magnetization

# we take b to be spin-up, r to be spin-down, and J=k=1

# import

import numpy as np
    
# generate lattice (256 particles)

def lattice():
    
    xvals=[]
    
    yvals=[]
    
    points=[]
    
    for i in range(0,16):
        
        xvals.append(i)
        
    for j in range(0,16):
        
        yvals.append(j)
        
    for x in xvals:
        
        for y in yvals:
        
            points.append([x,y])
    
    lspin=[]
    
    for c in range(0,256):
            
        r=np.random.randint(100)
            
        if r<50:
                
            lspin.append('r')
                
        else:
                
            lspin.append('b')
                
    data=np.array(points)
    
    x,y=data.T
    
    # return x and y values, list of spin values
    
    return x,y,lspin

# simulate

def simulate(x,y,spin,T):
    
    energylist=[]
    
    upedge=[]
    
    downedge=[]
    
    leftedge=[]
    
    rightedge=[]
    
    for k in range(1,15): 
        
        upedge.append(k*16+15)
        
        downedge.append(k*16)
        
        leftedge.append(k)
        
        rightedge.append(240+k)
    
    # advance time
    
    for t in range(0,10000):
        
        # metropolis algorithm
        
        n,m=np.random.randint(0,16),np.random.randint(0,16)
        
        sup=0
        
        sright=0
        
        sleft=0
        
        sdown=0
        
        s=0
        
        if n==15 and m==15:
            
            if spin[15]=='b':
            
                sright=1
            
            else:
            
                sright=-1
            
            if spin[239]=='b':
            
                sleft=1
            
            else:
            
                sleft=-1
            
            if spin[240]=='b':
            
                sup=1
            
            else:
            
                sup=-1
            
            if spin[254]=='b':
            
                sdown=1
            
            else:
            
                sdown=-1
            
            if spin[255]=='b':
            
                s=-1
            
            else:
            
                s=1
                
        elif n==15 and m==0:
            
            if spin[0]=='b':
            
                sright=1
            
            else:
            
                sright=-1
            
            if spin[224]=='b':
            
                sleft=1
            
            else:
            
                sleft=-1
            
            if spin[241]=='b':
            
                sup=1
            
            else:
            
                sup=-1
            
            if spin[255]=='b':
            
                sdown=1
            
            else:
            
                sdown=-1
            
            if spin[240]=='b':
            
                s=-1
            
            else:
            
                s=1
                
        elif n==0 and m==15:
            
            if spin[31]=='b':
            
                sright=1
            
            else:
            
                sright=-1
            
            if spin[255]=='b':
            
                sleft=1
            
            else:
            
                sleft=-1
            
            if spin[0]=='b':
            
                sup=1
            
            else:
            
                sup=-1
            
            if spin[14]=='b':
            
                sdown=1
            
            else:
            
                sdown=-1
            
            if spin[15]=='b':
            
                s=-1
            
            else:
            
                s=1
                
        elif n==0 and m==0:
            
            if spin[16]=='b':
            
                sright=1
            
            else:
            
                sright=-1
            
            if spin[240]=='b':
            
                sleft=1
            
            else:
            
                sleft=-1
            
            if spin[1]=='b':
            
                sup=1
            
            else:
            
                sup=-1
            
            if spin[15]=='b':
            
                sdown=1
            
            else:
            
                sdown=-1
            
            if spin[0]=='b':
            
                s=-1
            
            else:
            
                s=1
        
        elif n==15:
            
            if spin[m]=='b':
            
                sright=1
            
            else:
            
                sright=-1
            
            if spin[224+m]=='b':
            
                sleft=1
            
            else:
            
                sleft=-1
            
            if spin[240+(m+1)]=='b':
            
                sup=1
            
            else:
            
                sup=-1
            
            if spin[240+(m-1)]=='b':
            
                sdown=1
            
            else:
            
                sdown=-1
            
            if spin[240+m]=='b':
            
                s=-1
            
            else:
            
                s=1
            
        elif m==15:
            
            if spin[(n+1)*16+15]=='b':
            
                sright=1
            
            else:
            
                sright=-1
            
            if spin[(n-1)*16+15]=='b':
            
                sleft=1
            
            else:
            
                sleft=-1
            
            if spin[n*16]=='b':
            
                sup=1
            
            else:
            
                sup=-1
            
            if spin[n*16+14]=='b':
            
                sdown=1
            
            else:
            
                sdown=-1
            
            if spin[n*16+15]=='b':
            
                s=-1
            
            else:
            
                s=1
                
        elif m==0:
            
            if spin[(n+1)*16]=='b':
            
                sright=1
            
            else:
            
                sright=-1
            
            if spin[(n-1)*16]=='b':
            
                sleft=1
            
            else:
            
                sleft=-1
            
            if spin[n*16+1]=='b':
            
                sup=1
            
            else:
            
                sup=-1
            
            if spin[n*16+15]=='b':
            
                sdown=1
            
            else:
            
                sdown=-1
            
            if spin[n*16]=='b':
            
                s=-1
            
            else:
            
                s=1
                
        elif n==0:
            
            if spin[16+m]=='b':
            
                sright=1
            
            else:
            
                sright=-1
            
            if spin[240+m]=='b':
            
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
        
            if spin[(n+1)*16+m]=='b':
            
                sright=1
            
            else:
            
                sright=-1
            
            if spin[(n-1)*16+m]=='b':
            
                sleft=1
            
            else:
            
                sleft=-1
            
            if spin[n*16+(m+1)]=='b':
            
                sup=1
            
            else:
            
                sup=-1
            
            if spin[n*16+(m-1)]=='b':
            
                sdown=1
            
            else:
            
                sdown=-1
            
            if spin[n*16+m]=='b':
            
                s=-1
            
            else:
            
                s=1
            
        e=-2*(s*(sup+sdown+sleft+sright))
        
        if e<=0:
            
            if spin[n*16+m]=='b':
        
                spin[n*16+m]='r'
            
            else:
                
                spin[n*16+m]='b'
                
        elif np.exp(-e/T)>np.random.uniform(0,1):
            
            if spin[n*16+m]=='b':
        
                spin[n*16+m]='r'
            
            else:
                
                spin[n*16+m]='b'
                
        # get sample of energy at equilibrium
                
        if t>9979:
            
            energy=0
            
            for j in range(len(spin)):
        
                if j==255:
                
                    if spin[15]=='b':
            
                        sright=1
            
                    else:
            
                        sright=-1
            
                    if spin[239]=='b':
            
                        sleft=1
            
                    else:
            
                        sleft=-1
            
                    if spin[240]=='b':
            
                        sup=1
            
                    else:
            
                        sup=-1
            
                    if spin[254]=='b':
            
                        sdown=1
            
                    else:
            
                        sdown=-1
            
                    if spin[255]=='b':
            
                        s=1
            
                    else:
            
                        s=-1
                        
                elif j==240:
            
                    if spin[0]=='b':
            
                        sright=1
            
                    else:
            
                        sright=-1
            
                    if spin[224]=='b':
            
                        sleft=1
            
                    else:
            
                        sleft=-1
            
                    if spin[241]=='b':
            
                        sup=1
            
                    else:
            
                        sup=-1
            
                    if spin[255]=='b':
            
                        sdown=1
            
                    else:
            
                        sdown=-1
            
                    if spin[240]=='b':
            
                        s=1
            
                    else:
            
                        s=-1
                
                elif j==15:
            
                    if spin[31]=='b':
            
                        sright=1
            
                    else:
            
                        sright=-1
            
                    if spin[255]=='b':
            
                        sleft=1
            
                    else:
            
                        sleft=-1
            
                    if spin[0]=='b':
            
                        sup=1
            
                    else:
            
                        sup=-1
            
                    if spin[14]=='b':
            
                        sdown=1
            
                    else:
            
                        sdown=-1
            
                    if spin[15]=='b':
            
                        s=1
            
                    else:
            
                        s=-1
                
                elif j==0:
            
                    if spin[16]=='b':
            
                        sright=1
            
                    else:
            
                        sright=-1
            
                    if spin[240]=='b':
            
                        sleft=1
            
                    else:
            
                        sleft=-1
            
                    if spin[1]=='b':
            
                        sup=1
                        
                    else:
            
                        sup=-1
            
                    if spin[15]=='b':
            
                        sdown=1
            
                    else:
            
                        sdown=-1
            
                    if spin[0]=='b':
            
                        s=1
            
                    else:
            
                        s=-1
                
                elif j in tuple(rightedge):
            
                    if spin[j-240]=='b':
            
                        sright=1
            
                    else:
            
                        sright=-1
            
                    if spin[j-16]=='b':
            
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
            
                    if spin[j+16]=='b':
            
                        sright=1
            
                    else:
            
                        sright=-1
            
                    if spin[j-16]=='b':
            
                        sleft=1
            
                    else:
            
                        sleft=-1
            
                    if spin[j-15]=='b':
            
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
            
                    if spin[j+16]=='b':
            
                        sright=1
            
                    else:
            
                        sright=-1
            
                    if spin[j-16]=='b':
            
                        sleft=1
            
                    else:
            
                        sleft=-1
            
                    if spin[j+1]=='b':
            
                        sup=1
            
                    else:
            
                        sup=-1
            
                    if spin[j+15]=='b':
            
                        sdown=1
            
                    else:
            
                        sdown=-1
            
                    if spin[j]=='b':
            
                        s=1
            
                    else:
            
                        s=-1
                
                elif j in tuple(leftedge):
            
                    if spin[j+16]=='b':
            
                        sright=1
            
                    else:
            
                        sright=-1
            
                    if spin[j+240]=='b':
            
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
        
                    if spin[j+16]=='b':
            
                        sright=1
            
                    else:
            
                        sright=-1
            
                    if spin[j-16]=='b':
            
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
    
    for i in range(0,4):
        
        for j in range(0,4):
            
            eblock=[]
        
            for n in range((i*4),(i*4)+4):
                
                for m in range((n*16)+(j*4),(n*16)+(4*j)+4):
                    
                    eblock.append(newspin[m])
                    
            entropylist.append(eblock)
            
    for w in range(0,16):
    
        l=0
        
        for v in range(0,16):
            
            if entropylist[w][v]=='b':
                
                l=l+1
                
        if l==0:
            
            blockentropy=1
            
        elif l==16:
            
            blockentropy=1
            
        else:
            
            blockentropy=16*np.log(16)-l*np.log(l)-(16-l)*np.log(16-l)
        
        entropy=entropy+blockentropy
    
    # calculate heat capacity (using equilibrium energy sample)
    
    heatcap=0
    
    emean=0
    
    evar=0
    
    for e in elist:
        
        emean=emean+e
        
    emean=(emean/20)
    
    for e in elist:
        
        evar=evar+((e-emean)**2)
        
    evar=(evar/19)
    
    heatcap=(evar/(T**2))
    
    return newenergy,magnet,heatcap,entropy
    
# main function

def main():
    
    # set temperature (uniform in desired regime)
    
    T=np.random.uniform(3.4,6.6)
    
    x,y,spin=lattice()
    
    # write spin values to data file
    
    file=open('hight.txt','a')
    
    for value in spin:
        
        if value=='b':
            
            file.write(str(1)+'\n')
            
        else:
            
            file.write(str(-1)+'\n')
    
    newspin,elist=simulate(x,y,spin,T)
    
    newenergy,magnet,heatcap,entropy=calc(newspin,T,elist)
    
    # write magnetization value to file
    
    file.write(str(format((magnet/256),'.3f'))+'\n')
    
    file.close()
    
    # show final calculations
    
    print("The magnetization of the system is",format((magnet/256),'.3f'),"ampere meters squared")
    
    print("The entropy of the system is",format((int(entropy)/256),'.3f'),"joules per kelvin")
    
    print("The energy of the system is",format((newenergy/256),'.3f'),"joules")
    
    print("The heat capacity of the system is",format((int(heatcap)/256),'.3f'),"joules per kelvin")
    
    return

# run program

for k in range(0,45000):
    
    # show step
    
    print(k)
    
    main()