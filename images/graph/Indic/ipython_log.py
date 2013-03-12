# IPython log file

get_ipython().system(u'ls -F --color ')
get_ipython().system(u'ls -F --color .spyder2/')
get_ipython().system(u'cat .spyder2/history.log')
get_ipython().system(u'cat .spyder2/template.py')
get_ipython().magic(u'cd /media/3da824c2-d502-4e9a-83c6-5a2a9a28c176/home/kronosua/work/diploma-work_2013/images/graph/Indic/')
get_ipython().system(u'ls -F --color ')
a=loadtxt('x10')
from pylab import *
interp
scipy
sp
np
interp1d
from scipy import interpolate, integrate
a=a[a[:,0].argsort()]
a=loadtxt('x10')
a=a[a[:,0].argsort()]
x=a[:,0]
y=a[:,1]
t=radians(x)
yy=y*sin(t)
iu=interpolate.interp1d(t,yy)
iu(t)
t
integrate.quad(iu,t[5],t[-1])
help(integrate.quad)
integrate.quad(iu,t[5],t[-1],limits=500)
integrate.quad(iu,t[5],t[-1],limit=500)
integrate.quad(iu,t[5],t[-1],limit=100)
integrate.quad(iu,t[5],t[-1],limit=200)
integrate.quad(iu,t[5],t[-1],limit=300)
integrate.quad(iu,t[5],t[-1],limit=400)
integrate.quad(iu,t[5],t[-1],limit=500)
integrate.quad(iu,t[5],t[-1],limit=600)
iu=interpolate.interp1d(t,yy/10**10)
integrate.quad(iu,t[5],t[-1],limit=600)
integrate.quad(iu,t[5],t[-1])
integrate.quad(iu,t[5],t[-1],500)
integrate.quad(iu,t[5],t[-1],limit=500)
integrate.quad(iu,t[10],t[-1],limit=500)
integrate.quad(iu,t[5],t[-1],limit=60000)
help(integrate.quad)
integrate.quad_explain()
integrate.quad(iu,t[5],t[-1],limit=500, neval=500)
integrate.quad(iu,t[5],t[-1],limit=500, neval=500)h
help(integrate.quad)
integrate.quad(iu,t[5],t[-1],limit=500, epsrel=10**-3)
integrate.quad(iu,t[5],t[-1],limit=500, epsrel=10**-6)
integrate.quad(iu,t[5],t[-1],limit=500, epsrel=10**-5)
iu=interpolate.interp1d(t,yy)
integrate.quad(iu,t[5],t[-1],limit=500, epsrel=10**-5)
integrate.quad(iu,radians(1.8),t[-1],limit=500, epsrel=10**-5)
integrate.quad(iu,radians(1.5),t[-1],limit=500, epsrel=10**-5)
integrate.quad(iu,radians(2),t[-1],limit=500, epsrel=10**-5)
integrate.quad(iu,radians(1.5),t[-1],limit=500, epsrel=10**-5)
I0=y.max()/2./pi/dOmega
I0=y.max()/2./pi/dOmega
dOmega=659.*494.*(7.4*10**-6)**2/(23*10**-2)**2
dOmega=659.*494.*(7.4*10**-6)**2/(23*10**-2)**2
I0=y.max()/2./pi/dOmega
Iind=integrate.quad(iu,radians(1.5),t[-1],limit=500, epsrel=10**-5)
Iind
Iind=integrate.quad(iu,radians(1.5),t[-1],limit=500, epsrel=10**-5)[0]
Iind
print Iind
Iind/(I0+Iind)
dOmega
I0
I0=y.max()
Iind/(I0+Iind)
Iind/(I0+Iind)*100.
Iind
iu=interpolate.interp1d(t,yy)
yy
Iind=integrate.quad(iu,radians(1.5),radians(80), epsrel=10**-5)[0]
Iind=integrate.quad(iu,radians(1.5),radians(80), epsrel=10**-5, limit=900)[0]
Iind
print Iind
Iind=integrate.quad(iu,radians(1.5),radians(80), epsrel=10**-6, limit=900)[0]
print Iind
Iind=integrate.quad(iu,radians(1.5),radians(80), epsrel=10**-5, limit=900)[0]
iu=interpolate.interp1d(t,yy/10**10)
Iind=integrate.quad(iu,radians(1.5),radians(80), epsrel=10**-5, limit=900)[0]
Iind
Iind*10**10
print Iind*10**10
ii=integrate.quad(iu,radians(0),radians(80), epsrel=10**-5, limit=900)[0]
ii
iu=interpolate.interp1d(t,yy)
ii=integrate.quad(iu,radians(0),radians(80), epsrel=10**-5, limit=900)[0]
ii
Iind/ii
Iind=integrate.quad(iu,radians(1.5),radians(80), epsrel=10**-5, limit=900)[0]
Iind/ii
Iind/ii*100
Iind=integrate.quad(iu,radians(1.5),radians(80), epsrel=10**-6, limit=900)[0]
Iind=integrate.quad(iu,radians(1.5),radians(80), epsrel=10**-5, limit=900)[0]
help(integrate.quad)
a=loadtxt('x5')
x=a[:,0]
y=a[:,1]
t=radians(x)
yy=y*sin(t)
iu=interpolate.interp1d(t,yy)
Iind=integrate.quad(iu,radians(1.5),radians(80), epsrel=10**-5, limit=900)[0]
Iind=integrate.quad(iu,radians(1.5),radians(80), epsrel=10**-4, limit=900)[0]
Iind
I0=y.max()
Iind/(I0+Iind)*100.
ii=integrate.quad(iu,radians(0),radians(80), epsrel=10**-5, limit=900)[0]
Iind/(ii+Iind)*100.
radians(1.5)
radians(80)
Iind
852613453594.
Iind/(ii+Iind)*100.
Iind/(ii)*100.
I0=integrate.quad(iu,radians(0),radians(1.), epsrel=10**-5, limit=900)[0]
I0
Iind/(I0+Iind)*100.
I0=integrate.quad(iu,radians(0.9),radians(1.), epsrel=10**-5, limit=900)[0]
Iind/(I0+Iind)*100.
I0=integrate.quad(iu,radians(1),radians(1.), epsrel=10**-5, limit=900)[0]
I0
I0=integrate.quad(iu,radians(0.999999),radians(1.), epsrel=10**-5, limit=900)[0]
I0
I0=integrate.quad(iu,radians(0.),radians(0.1), epsrel=10**-5, limit=900)[0]
I0
Iind/(I0+Iind)*100.
I0=integrate.quad(iu,radians(0.),radians(0.01), epsrel=10**-5, limit=900)[0]
Iind/(I0+Iind)*100.
I0=integrate.quad(iu,radians(0.),radians(0.0001), epsrel=10**-5, limit=900)[0]
I0
I0=integrate.quad(iu,radians(0.),radians(0.001), epsrel=10**-5, limit=900)[0]
I0
I0=integrate.quad(iu,radians(0.),radians(0.01), epsrel=10**-5, limit=900)[0]
I0
Iind/(I0+Iind)*100.
I0=y.max()
Iind/(I0+Iind)*100.
I0=y[0:2].sum()
Iind/(I0+Iind)*100.
I0=y[0:3].sum()
Iind/(I0+Iind)*100.
def f(t): returm y[t]*sin(radians(x[t]))
def f(t): return y[t]*sin(radians(x[t]))
f(0:2)
def f(a,b): return y[a:b]*sin(radians(x[a:b]))
f(0,2)
f(0,2).sum()
I0=f(0,2).sum()
Iind/(I0+Iind)*100.
I0=f(0,3).sum()
Iind/(I0+Iind)*100.
I0=f(0,5).sum()
Iind/(I0+Iind)*100.
I0=f(0,20).sum()
Iind/(I0+Iind)*100.
Iind
Iind/(I0+Iind)*100.
I0=f(0,50).sum()
Iind/(I0+Iind)*100.
I0=f(0,3).sum()
Iind/(I0+Iind)*100.
I0=f(0,2).sum()
Iind/(I0+Iind)*100.
I0=f(0,0).sum()
Iind/(I0+Iind)*100.
I0=f(0,1).sum()
Iind/(I0+Iind)*100.
I0=f(0,2).sum()
Iind/(I0+Iind)*100.
yy
yy.max()
figure()
subplot(211)
plot(t,yy,'o')
subplot(212)
plot(t,y,'o')
show()
Iind/(I0+Iind)*100.
I0=y.max()*dOmega
I0
Iind/(I0+Iind)*100.
Iind/(I0+Iind)*100.*6.28
y.max()
I0=y.max()
Iind/2/pi/dOmega/(I0+Iind/2/pi/dOmega)*100.*6.28
Iind/2/pi/dOmega/(I0/dOmaga+Iind/2/pi/dOmega)*100.*6.28
Iind/2/pi/dOmega/(I0/dOmega+Iind/2/pi/dOmega)*100.*6.28
I0=y.max()
Iind/(I0/2/pi/dOmega+Iind)*100.*6.28
Iind/(I0*2*pi*dOmega+Iind)*100.*6.28
Iind/(I0*2*pi*dOmega+Iind)*100.
Iind
I0=dOmega
I0
y.max()*dOmega
y.max()
y.max()*dOmega/2/pi
I0=y.max()*dOmega/2/pi
Iind/(I0+Iind)*100.
a=loadtxt('x5')
a=a[a[:,0].argsort()]
x=a[:,0]
y=a[:,1]
t=radians(x)
yy=y*sin(t)
iu=interpolate.interp1d(t,yy)
Iind=integrate.quad(iu,radians(1.5),radians(80), epsrel=10**-4, limit=900)[0]
I0=y.max()*dOmega/2/pi
def scat(file, start):
    a=loadtxt(file)
    a=a[a[:,0].argsort()]
    x=a[:,0]
    y=a[:,1]
    t=radians(x)
    yy=y*sin(t)
    iu=interpolate.interp1d(t,yy)
    Iind=integrate.quad(iu,radians(start),radians(x.max()), epsrel=10**-4, limit=900)[0]
    I0=y.max()*dOmega/2/pi
    return Iind/(I0+Iind)*100.
scat('x5',1.5)
scat('x1',1.5)
scat('x2',1.5)
scat('hema',1.5)
scat('x1',1.5)
scat('x10',1.5)
scat('x10',2.)
scat('x10',3)
scat('x5',3)
scat('x1',3)
scat('hema',3)
scat('hema',3.)
scat('hema',2.)
scat('x1',2.)
scat('x5',2.)
scat('x10',2.)
scat('cross',2.)
dOmega
dOmega=659.*494.*(7.4*10**-6)**2/(23*10**-2)**2
dO
dOmega=659.*494.*(7.4*10**-6)**2/(23*10**-2)**2
dOmega
scat('x10',1.8)
scat('x5',1.8)
scat('x1',1.8)
scat('hema',1.8)
scat('cross',1.8)
scat('cross',1.5)
scat('HEMA',1.5)
scat('cross',1.5)
scat('hema',1.5)
scat('x1',1.5)
scat('x5',1.5)
scat('x10',1.5)
scat('x10',3.)
scat('x5',3.)
scat('x1',3.)
scat('hema',3.)
scat('cross',3.)
get_ipython().magic(u'logstate')
get_ipython().magic(u'save')
get_ipython().magic(u'logon')
get_ipython().magic(u'logstart')
get_ipython().system(u'ls -F --color ')
get_ipython().system(u'cat ipython_log.py')
quite()
