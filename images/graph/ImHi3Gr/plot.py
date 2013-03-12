# -*- coding: utf-8 -*-
"""
Spyder Editor

This temporary script file is located here:
/home/kronosua/.spyder2/.temp.py
"""
from pylab import *

rc('text', usetex=True)
rcParams['text.usetex']=True
rcParams['text.latex.unicode']=True
rc('text.latex',preamble="""\usepackage[ukrainian]{babel}
\usepackage{amsmath}
\usepackage[warn]{mathtext}""")
rcParams['mathtext.fontset']='custom'
rcParams['mathtext.it']= 'serif:italic'
rc('lines', linewidth=2)
rcParams['font.size']=17

def figsize(wcm,hcm): figure(figsize=(wcm/2.54,hcm/2.54))
#figsize(13,9)

def loadData(name, cols=[0,1]):
    data = loadtxt(name)
    return data[:,0], data[:,1]

data = loadtxt('./ImHi3')
x, y1, y2 = data[:,0], data[:,1], data[:,2]


def CText(x,y,text, bbox):
    annotate(text, xy=(x, y),
             xycoords='data',
             horizontalalignment='center',
             verticalalignment='center', bbox=bbox)
rc('lines', markersize=7)      

ax = subplot(111)
props = dict(boxstyle='round', facecolor='w', ec='w', alpha=0.85)
plot(x, y1, 'og', x, y2, 'vb')

xlabel(r'Концентрація, $\times 10^ {20} ~cm^{-3}$')

'''TODO: розмірність'''

ylabel(r'$Im(\chi^{(3)}) \times 10^{-13} ~esu$')
ax.set_xticks(arange(-2,20,2))

legend([r'$0<I <150 ~\text{МВт}/cm^2$',
        r'$1250<I<1500 ~\text{МВт}/cm^2$'],
        loc='upper left')
ylim((-5,25))
xlim((-2,20))
grid(True)
savefig('plot.pdf', format='pdf')
show(block=True)

