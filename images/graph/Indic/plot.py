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

def loadData(name):
    data = loadtxt(name)
    return data[:,0], data[:,1]
x1, y1 = loadData('./x1')
#x2, y2 = loadData('./x2')
x5, y5 = loadData('./x5')
x10, y10 = loadData('./x10')
x_hema, y_hema = loadData('./hema')
xc, yc = loadData('./cross')


def CText(x,y,text, bbox):
    annotate(text, xy=(x, y),
             xycoords='data',
             horizontalalignment='center',
             verticalalignment='center', bbox=bbox)
             
props = dict(boxstyle='round', facecolor='w', ec='w', alpha=0.85)
figure(0)
semilogy(x1,y1,'or',# x2, y2, 'og',
         x5, y5, 'ob', x10, y10, 'om',
     x_hema, y_hema, '^c', xc, yc, 'vk')

xlabel(r'Кут')
ylabel(r'Сигнал')
#ylim((0.955,1))
#xlim((0,2000))
legend([r'$\times1$',
        r'$\times5$',
        r'$\times10$',
        r'$pHEMA$',
        r'Пучок без зразка'])

grid(True)
savefig('plot.pdf', format='pdf')
show(block=False)

figure(1)
ax = subplot(111)
plot(x1,y1,'or',# x2, y2, 'og',
         x5, y5, 'ob', x10, y10, 'om',
     x_hema, y_hema, '^c')
yl=ax.get_ylim()
print yl
plot([1]*2,yl, '-g')#, alpha=0.5)
plot([2]*2,yl, '-g')#, alpha=0.5)

ax.set_xscale('log', basex=10)
ax.set_yscale('log', basex=10)
ax.set_xlim((10**-1,10**2))



xlabel(r'Кут')
ylabel(r'Сигнал')
#ylim((0.955,1))
#xlim((0,2000))
legend([r'$\times1$',
        r'$\times5$',
        r'$\times10$',
        r'$pHEMA$'], loc='lower left')

grid(True)
savefig('plot2.pdf', format='pdf')
show(block=True)
