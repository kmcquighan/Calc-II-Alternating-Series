# -*- coding: utf-8 -*-
"""
Copyright Kelly McQuighan 2016

These tools can be used to visualize different improper integrals.
"""

import matplotlib
from matplotlib import pyplot as plt
import numpy as np
from numpy import *
from matplotlib.ticker import MaxNLocator
colors = ['#A90000', '#D06728', '#D9A621', '#008040', '#0080FF', '#7B00F1']

def proof(f,n):     

    n=int(n)
    nmax = 20
    func = eval("lambda n: " + f)
        
    fig = plt.figure(figsize=(20, 6))
       
    ax1 = fig.add_subplot(1,2,1)
    ax2 = fig.add_subplot(1,2,2)
    plt.tight_layout(pad=0.4, w_pad=0.5, h_pad=1.0)
      
    ns = np.linspace(1,n,n)
    an = func(ns)
    ax1.set_xlim([0,1.05*nmax])
    ax2.set_xlim([0,1.05*nmax])
    ax1.xaxis.set_major_locator(MaxNLocator(integer=True))
    ax2.xaxis.set_major_locator(MaxNLocator(integer=True))
    
    ax1.plot(ns[0],an[0],color = 'b', marker='o',markersize=13)
    sn_usr = np.zeros(n)
    sn_usr[0] = an[0]
    hl = np.min([0.1, 0.6*an[0]])
    #lw = np.min([5,50*hl])
    ax1.arrow(1, 0, 0, an[0]-hl, head_width=0.1, head_length=hl,linewidth=5, fc=colors[5], ec=colors[5])
    ax2.arrow(.8, 0, 0, sn_usr[0]-hl, head_width=0.1, head_length=hl,linewidth=5, fc=colors[5], ec=colors[5])

    for i in range(1,n):
        ax1.plot(ns[i],(-1.)**(i)*an[i],color = 'b', marker='o',markersize=13)
        hl = np.min([0.1, 0.6*an[i]])
        #lw = np.min([5,50*hl])
        sn_usr[i] = sn_usr[i-1]+(-1)**i*an[i]
        if np.mod(i,2) == 0:
            ax1.arrow(i+1, 0, 0, an[i]-hl, head_width=0.1, head_length=hl,linewidth=5, fc=colors[5], ec=colors[5])
            ax2.arrow(i+.8, sn_usr[i-1], 0, an[i]-hl, head_width=0.1, head_length=hl,linewidth=5, fc=colors[5], ec=colors[5])
        else:
            ax1.arrow(i+1, 0, 0, -1*(an[i]-hl), head_width=0.1, head_length=hl,linewidth=5, fc=colors[1], ec=colors[1])
            ax2.arrow(i+.8, sn_usr[i-1], 0, -1*(an[i]-hl), head_width=0.1, head_length=hl,linewidth=5, fc=colors[1], ec=colors[1])
            
    ax1.set_ylim([-1.1*an[0],1.1*an[0]])
    ax1.plot(np.linspace(0,21,100), np.zeros((100,1)),'k-')
    ax2.set_ylim([0,1.1*an[0]])
    ax2.plot(ns,sn_usr,color=colors[0], linestyle='', marker='o',markersize=13)
    ax2.plot(ns[n-1],sn_usr[n-1],color=colors[3], marker='o',markersize=13)
    
    ax1.set_xlabel('n', fontsize=36)
    ax1.set_title(r'$(-1)^{k+1}a_n$', fontsize=36, y=1.1)
    ax2.set_xlabel('n', fontsize=36)
    ax2.set_title(r'$s_n=\sum_{k=1}^n (-1)^{k+1} a_n$',fontsize=36, y=1.1)
    
    plt.tight_layout(pad=0.4, w_pad=0.5, h_pad=1.0)
    plt.suptitle(r'$a_n$ = '+f, fontsize=36, y=1.0)
    matplotlib.rc('xtick', labelsize=20) 
    matplotlib.rc('ytick', labelsize=20)
