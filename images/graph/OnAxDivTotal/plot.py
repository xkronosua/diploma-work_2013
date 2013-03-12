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
x1, y1 = loadData('./x1')
x2, y2 = loadData('./x2')
x5, y5 = loadData('./x5')
x10, y10 = loadData('./x10')
x20, y20 = loadData('./x20')
x_hema, y_hema = loadData('./hema')



def CText(x,y,text, bbox):
    annotate(text, xy=(x, y),
             xycoords='data',
             horizontalalignment='center',
             verticalalignment='center', bbox=bbox)
             
props = dict(boxstyle='round', facecolor='w', ec='w', alpha=0.85)
plot(x1,y1,'-r', x2, y2, '-g', x5, y5, '-b', x10, y10, '-m',
     x20, y20, '-c', x_hema, y_hema, '--k')

CText(x1[len(x1)/4], y1[len(x1)/4], r'$\times1$', bbox=props)
CText(x2[len(x2)/4], y2[len(x2)/4], r'$\times2$', bbox=props)
CText(x5[len(x5)/2], y5[len(x5)/2], r'$\times5$', bbox=props)
CText(x10[len(x10)/2], y10[len(x10)/2], r'$\times10$', bbox=props)
CText(x20[len(x20)/3], y20[len(x20)/3], r'$\times20$', bbox=props)

annotate(r'$pHEMA$', xy=(x_hema[-70], y_hema[-70]),  xycoords='data',
                xytext=(0.6, 0.8), textcoords='axes fraction',
                arrowprops=dict(arrowstyle="->")
                )
xlabel(r'Інтенсивність, $\frac{\text{МВт}}{\text{см}^2}$')
ylabel(r'???, \%')

ylim((0.94,1.02))
xlim((0,2000))
grid(True)
savefig('plot.pdf', format='pdf')
show(block=True)

