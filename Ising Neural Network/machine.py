#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 28 13:24:20 2022

@author: Alex Panayotof
"""

# 2D Ising Model Neural Network

# this program predicts the direction and general magnitude of magnetization associated with the 2D Ising model

# this is a 4-layer network with 256 input neurons, two hidden layers of 16 neurons, and 4 output neurons

# import

import numpy as np

# training function

def train(v,cvector,lrate,mrate,momentum,T):
    
    # if initial batch randomize weights and biases (normalized Xavier)
    
    if v==0:
    
        w1=[]

        b1=[]

        for q in range(0,16):
    
            w1.append([])
    
            b1.append(0)
    
        for w in w1:
    
            for p in range(0,256):
        
                w.append(np.random.uniform((-np.sqrt(6)/np.sqrt(272)),(np.sqrt(6)/np.sqrt(272))))
            
        w2=[]

        b2=[]

        for y in range(0,16):
    
            w2.append([])
    
            b2.append(0)
    
        for u in w2:
    
            for i in range(0,16):
        
                u.append(np.random.uniform((-np.sqrt(6)/np.sqrt(32)),(np.sqrt(6)/np.sqrt(32))))
                
        w3=[]

        b3=[]

        for y in range(0,4):
    
            w3.append([])
    
            b3.append(0)
    
        for u in w3:
    
            for i in range(0,16):
        
                u.append(np.random.uniform((-np.sqrt(6)/np.sqrt(20)),(np.sqrt(6)/np.sqrt(20))))
                
        # create vector of parameters
            
        for d in range(len(w1)):
        
            for f in range(len(w1[d])):
            
                cvector.append(w1[d][f])
            
        for g in range(len(b1)):
        
            cvector.append(b1[g])
        
        for h in range(len(w2)):
        
            for j in range(len(w2[h])):
            
                cvector.append(w2[h][j])
            
        for k in range(len(b2)):
        
            cvector.append(b2[k])
            
        for h in range(len(w3)):
        
            for j in range(len(w3[h])):
            
                cvector.append(w3[h][j])
            
        for k in range(len(b3)):
        
            cvector.append(b3[k])
            
        for h in range(len(cvector)):
            
            momentum.append(0)
            
    # if not initial batch, take parameters from updated vector
            
    else:
        
        w1=[]

        b1=[]

        for q in range(0,16):
    
            w1.append([])
    
            b1.append(cvector[4096+q])
    
        for w in range(len(w1)):
    
            for p in range(0+(w*256),256+(w*256)):
        
                w1[w].append(cvector[p])
            
        w2=[]

        b2=[]

        for y in range(0,16):
    
            w2.append([])
    
            b2.append(cvector[4368+y])
    
        for u in range(len(w2)):
    
            for i in range(4112+(u*16),4128+(u*16)):
        
                w2[u].append(cvector[i])
                
        w3=[]
        
        b3=[]
                
        for y in range(0,4):
    
            w3.append([])
    
            b3.append(cvector[4448+y])
    
        for u in range(len(w3)):
    
            for i in range(4384+(u*16),4400+(u*16)):
        
                w3[u].append(cvector[i])
                
    # initialize variables
    
    totalcostvalue=0
    
    meandelc=[]
    
    m=[]
    
    # randomly select data points from dataset
    
    for l in range(0,1000):
        
        # 20000 instead of recommended 45000 for testing purposes
        
        m.append(np.random.randint(0,20000))
      
    # run through batch
            
    for n in tuple(m):
        
        # show data point
        
        print(n)
        
        # initialize
        
        cost=0
        
        magnet=0
        
        delc=[]
        
        y=[]

        newinitial=[]
        
        # open and read data file
        
        if T==0:

            file=open('hight.txt','r')
            
        elif T==1:
            
            file=open('midt.txt','r')
            
        else:
            
            file=open('lowt.txt','r')

        initial=file.readlines()[(n*256)+n:((n*256)+n)+256]
        
        file.close()
        
        if T==0:

            file=open('hight.txt','r')
            
        elif T==1:
            
            file=open('midt.txt','r')
            
        else:
            
            file=open('lowt.txt','r')
            
        magnet=file.readlines()[256+(n*257)]
            
        file.close()
        
        magnet=magnet.replace('\n','')
        
        magnet=float(magnet)

        for value in initial:
    
            value=value.replace('\n','')
    
            value=int(value)
    
            newinitial.append(value)
            
        # initialize
        
        middle1=[]

        z1=[]
        
        # act on initial vector and pass through activation function
        
        for e in range(0,16):
    
            z=0
    
            z=z+b1[e]
    
            for r in range(0,256):
        
                z=z+(newinitial[r]*w1[e][r])
        
            z1.append(z)
    
        for t in range(0,16):
    
            m=0
    
            m=(1/(1+(np.exp(-z1[t]))))
    
            middle1.append(m)
            
        # initialize
            
        middle2=[]

        z2=[]
        
        # act on second vector and pass through activation function
        
        for e in range(0,16):
    
            z=0
    
            z=z+b2[e]
    
            for r in range(0,16):
        
                z=z+(middle1[r]*w2[e][r])
        
            z2.append(z)
    
        for t in range(0,16):
    
            m=0
    
            m=(1/(1+(np.exp(-z2[t]))))
    
            middle2.append(m)
            
        # initialize
    
        final=[]

        z3=[]
        
        # act on third vector and pass through activation function

        for o in range(0,4):
    
            z=0
    
            z=z+b3[o]
    
            for p in range(0,16):
        
                z=z+(middle2[p]*w3[o][p])
        
            z3.append(z)
    
        for a in range(0,4):
    
            f=0
    
            f=(1/(1+(np.exp(-z3[a]))))
    
            final.append(f)
            
        # evaluate cost of data point
            
        if (-1<=magnet<=-.5):
            
            y=[0,0,0,1]
            
        elif (-.5<=magnet<=0):
            
            y=[0,0,1,0]
            
        elif (0<=magnet<=.5):
            
            y=[0,1,0,0]
            
        else:
            
            y=[1,0,0,0]
            
        for s in range(0,4):
            
            cost=cost+((final[s]-y[s])**2)
            
        # add individual cost to batch cost
            
        totalcostvalue=totalcostvalue+cost
        
        # calculate partial to cost with respect to first weights and biases
            
        for i in range(len(w1)):
            
            factor1=0
            
            for m in range(len(w1[i])):
                
                for j in range(0,16):
                    
                    factor12=0
                    
                    for k in range(0,4):
                        
                        factor12=factor12+(w3[k][j]*((np.exp(-z3[k]))/((1+(np.exp(-z3[k])))**2))*2*(final[k]-y[k]))
                    
                    factor1=factor1+(w2[j][i]*((np.exp(-z2[j]))/((1+(np.exp(-z2[j])))**2))*factor12)
                
                delc.append(newinitial[m]*((np.exp(-z1[i]))/((1+(np.exp(-z1[i])))**2))*factor1)
                
        for i in range(len(b1)):
            
            factor1=0
            
            for j in range(0,16):
                    
                factor12=0
                    
                for k in range(0,4):
                        
                    factor12=factor12+(w3[k][j]*((np.exp(-z3[k]))/((1+(np.exp(-z3[k])))**2))*2*(final[k]-y[k]))
                    
                factor1=factor1+(w2[j][i]*((np.exp(-z2[j]))/((1+(np.exp(-z2[j])))**2))*factor12)
            
            delc.append(((np.exp(-z1[i]))/((1+(np.exp(-z1[i])))**2))*factor1)
            
        # calculate partial to cost with respect to second weights and biases
            
        for j in range(len(w2)):
            
            factor2=0
            
            for i in range(len(w2[j])):
                
                for k in range(0,4):
                    
                    factor2=factor2+(w3[k][j]*((np.exp(-z3[k]))/((1+(np.exp(-z3[k])))**2))*2*(final[k]-y[k]))
                
                delc.append(middle1[i]*((np.exp(-z2[j]))/((1+(np.exp(-z2[j])))**2))*factor2)
                
        for j in range(len(b2)):
            
            factor2=0
            
            for k in range(0,4):
                    
                    factor2=factor2+(w3[k][j]*((np.exp(-z3[k]))/((1+(np.exp(-z3[k])))**2))*2*(final[k]-y[k]))
            
            delc.append(((np.exp(-z2[j]))/((1+(np.exp(-z2[j])))**2))*factor2)
            
        # calculate partial to cost with respect to third weights and biases
            
        for k in range(len(w3)):
            
            for j in range(len(w3[k])):
                
                delc.append(middle2[j]*((np.exp(-z3[k]))/((1+(np.exp(-z3[k])))**2))*2*(final[k]-y[k]))
                
        for k in range(len(b3)):
            
            delc.append(((np.exp(-z3[k]))/((1+(np.exp(-z3[k])))**2))*2*(final[k]-y[k]))
            
        # add individual partial to batch partial
        
        meandelc.append(delc)
        
    # find average batch partial
        
    meandelcprime=[]
    
    for u in range(len(cvector)):
        
        meandelcprime.append(0)
        
    for e in range(len(meandelc)):
        
        for r in range(len(meandelc[e])):
            
            meandelcprime[r]=meandelcprime[r]+meandelc[e][r]
            
    for t in range(len(meandelcprime)):
        
        meandelcprime[t]=(meandelcprime[t]/1000)
        
    # change parameter vector according to average batch partial
        
    for y in range(len(cvector)):
        
        cvector[y]=cvector[y]-(lrate*meandelcprime[y])+(mrate*momentum[y])
        
    # generate momentum
        
    momentum=[]
    
    for s in range(len(meandelcprime)):
        
        momentum.append(-lrate*meandelcprime[s])
        
    # return parameter vector, batch cost, momentum
        
    return cvector,totalcostvalue,momentum

# analysis function
        
def analysis(T):
    
    # take parameters from trained parameter vector
    
    newtrained=[]
    
    trainedfile=open('trained.txt','r')
    
    trained=trainedfile.readlines()
    
    for parameter in trained:
        
        parameter=parameter.replace('\n','')
        
        parameter=float(parameter)
        
        newtrained.append(parameter)
    
    w1=[]

    b1=[]

    for q in range(0,16):
    
        w1.append([])
    
        b1.append(newtrained[4096+q])
    
    for w in range(len(w1)):
    
        for p in range(0+(w*256),256+(w*256)):
        
            w1[w].append(newtrained[p])
            
    w2=[]

    b2=[]

    for y in range(0,16):
    
        w2.append([])
    
        b2.append(newtrained[4368+y])
    
    for u in range(len(w2)):
    
        for i in range(4112+(u*16),4128+(u*16)):
        
            w2[u].append(newtrained[i])
                
    w3=[]
        
    b3=[]
                
    for y in range(0,4):
    
        w3.append([])
    
        b3.append(newtrained[4448+y])
    
    for u in range(len(w3)):
    
        for i in range(4384+(u*16),4400+(u*16)):
        
            w3[u].append(newtrained[i])
            
    # initialize
    
    correct=0
    
    m=[]
    
    # define temperature regime
    
    if T==0:
        
        for r in range(668,1002):
            
            m.append(r)
            
    elif T==1:
        
        for p in range(334,668):
        
            m.append(p)
            
    else:
        
        for q in range(0,334):
            
            m.append(q)
            
    # run through test data
    
    for n in tuple(m):
        
        # initialize
        
        choice=0
        
        magnet=0
        
        # run through neural network (same as train function)
        
        newtestlist=[]
        
        testfile=open('test.txt','r')
    
        testlist=testfile.readlines()[(n*256)+n:((n*256)+n)+256]
        
        testfile.close()
        
        for value in testlist:
    
            value=value.replace('\n','')
    
            value=int(value)
    
            newtestlist.append(value)
            
        testfile=open('test.txt','r')
            
        magnet=testfile.readlines()[256+(n*257)]
            
        testfile.close()
        
        magnet=magnet.replace('\n','')
        
        magnet=float(magnet)
        
        # show magnetization
        
        print(magnet)
        
        middle1=[]

        z1=[]
        
        for e in range(0,16):
    
            z=0
    
            z=z+b1[e]
    
            for r in range(0,256):
        
                z=z+(newtestlist[r]*w1[e][r])
        
            z1.append(z)
    
        for t in range(0,16):
    
            m=0
    
            m=(1/(1+(np.exp(-z1[t]))))
    
            middle1.append(m)
            
        middle2=[]

        z2=[]
        
        for e in range(0,16):
    
            z=0
    
            z=z+b2[e]
    
            for r in range(0,16):
        
                z=z+(middle1[r]*w2[e][r])
        
            z2.append(z)
    
        for t in range(0,16):
    
            m=0
    
            m=(1/(1+(np.exp(-z2[t]))))
    
            middle2.append(m)
    
        final=[]

        z3=[]

        for o in range(0,4):
    
            z=0
    
            z=z+b3[o]
    
            for p in range(0,16):
        
                z=z+(middle2[p]*w3[o][p])
        
            z3.append(z)
    
        for a in range(0,4):
    
            f=0
    
            f=(1/(1+(np.exp(-z3[a]))))
    
            final.append(f)
            
        # make guess
            
        choice=final.index(max(final))
        
        # show guess and add to correct counter if correct
        
        if choice==0:
            
            if .5<=magnet<=1:
                
                correct=correct+1
            
            print('High Positive Magnetization: m in (.5,1)')
            
        elif choice==1:
            
            if 0<=magnet<=.5:
                
                correct=correct+1
            
            print('Low Positive Magnetization: m in (0,.5)')
            
        elif choice==2:
            
            if -.5<=magnet<=0:
                
                correct=correct+1
            
            print('Low Negative Magnetization: m in (-.5,0)')
            
        else:
            
            if -1<=magnet<=-.5:
                
                correct=correct+1
            
            print('High Negative Magnetization: m in (-1,-.5)')
            
    # show accuracy results
            
    print('\nThe neural network has a '+str((correct/334)*100)+'% accuracy')
    
    return

# main function

def main():
    
    while 1!=0:
        
        # choose function
    
        command=input('Train (t), Analyze (a), or Exit (e)?\n')
        
        # train
    
        if command=='t':
            
            while 1!=0:
                
                # choose temperature regime
                
                temp=input('High (h), Medium (m), or Low (l) Temperature?\n')
            
                if temp=='h':
                
                    T=0
                    
                    break
                
                elif temp=='m':
                
                    T=1
                    
                    break
                
                elif temp=='l':
                    
                    T=2
                    
                    break
                    
                else:
                    
                    continue
                
            # initialize parameter vector, momentum, and momentum rate
            
            cvector=[]
            
            momentum=[]
            
            mrate=.9
            
            # run through epochs
    
            for v in range(0,2000):
                
                # show epoch
                
                print(v)
                
                # set learning rate
                
                if v<=10:
                
                    lrate=1
                
                    lrate=(lrate/(1+v))
                    
                else:
                    
                    lrate=.01
                    
                    lrate=(lrate/(1+v))
                    
                # training function
        
                cvector,totalcostvalue,momentum=train(v,cvector,lrate,mrate,momentum,T)
                
                # show batch cost
                
                print(totalcostvalue)
                
                # create and write to cost file
                
                costfile=open('cost.txt','a')
    
                costfile.write(str(totalcostvalue)+'\n')
                
                costfile.close()
                
            # write final parameter vector to trained file
                
            cvectorfile=open('trained.txt','w')
            
            for g in range(len(cvector)):
                
                cvectorfile.write(str(cvector[g])+'\n')
                
            cvectorfile.close()
            
        # analyze
            
        elif command=='a':
            
            while 1!=0:
                
                # choose temperature regime
                
                temp=input('High (h), Medium (m), or Low (l) Temperature?\n')
            
                if temp=='h':
                
                    T=0
                    
                    break
                
                elif temp=='m':
                
                    T=1
                    
                    break
                
                elif temp=='l':
                    
                    T=2
                    
                    break
                    
                else:
                    
                    continue
                
            # analyze function
            
            analysis(T)
            
        # exit program
            
        elif command=='e':
            
            break
            
        else:
            
            continue
    
    return

# run program

main()
