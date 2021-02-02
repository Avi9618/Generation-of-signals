import numpy as np
import matplotlib.pyplot as plt
#unit step function CTS
x=np.arange(-2,5,0.01)
n=len(x)
y=np.zeros(n)
i=0
for i in range(0,n):
    if (x[i]>=0):
        y[i]=1
    else:
        y[i]=0

plt.subplot(8,2,1)
plt.xlabel('t')
plt.ylabel('x(t)')
plt.plot(x,y)
plt.show()

#unit step function DTS
x=np.arange(-2,5,1)
n=len(x)
y=np.zeros(n)
i=0
for i in range(0,n):
    if (x[i]>=0):
        y[i]=1
    else:
        y[i]=0

plt.subplot(8,2,2)
plt.xlabel('n')
plt.ylabel('x(n)')
plt.stem(x,y)
plt.show()
#unit ramp function CTS
x=np.arange(-2,5,1)
n=len(x)
y=np.zeros(n)
i=0
for i in range(0,n):
    if (x[i]>=0):
        y[i]=x[i]
    else:
        y[i]=0

plt.subplot(8,2,3)
plt.xlabel('t')
plt.ylabel('x(t)')
plt.plot(x,y)
plt.show()
#unit ramp function DTS
x=np.arange(-2,5,1)
n=len(x)
y=np.zeros(n)
i=0
for i in range(0,n):
    if (x[i]>=0):
        y[i]=x[i]
    else:
        y[i]=0

plt.subplot(8,2,4)
plt.xlabel('n')
plt.ylabel('x(n)')
plt.stem(x,y)
plt.show()
#unit impulse function CTS
x=np.arange(-2,5,1)
n=len(x)
y=np.zeros(n)
i=0
for i in range(0,n):
    if (x[i]==0):
        y[i]=1
    else:
        y[i]=0

plt.subplot(8,2,5)
plt.xlabel('t')
plt.ylabel('x(t)')
plt.plot(x,y)
plt.show()
#unit impulse function DTS
x=np.arange(-2,5,1)
n=len(x)
y=np.zeros(n)
i=0
for i in range(0,n):
    if (x[i]==0):
        y[i]=1
    else:
        y[i]=0

plt.subplot(8,2,6)
plt.xlabel('n')
plt.ylabel('x(n)')
plt.stem(x,y)
plt.show()
#sine function CTS
x=np.arange(0,3*np.pi,0.1)
y=np.sin(x)
plt.subplot(8,2,7)
plt.plot(x,y)
plt.xlabel('t')
plt.ylabel('x(t)')
plt.show()
#sine function DTS
x=np.arange(0,3*np.pi,0.5)
y=np.sin(x)
plt.subplot(8,2,8)
plt.stem(x,y)
plt.xlabel('n')
plt.ylabel('x(n)')
plt.show()
#complex exponential function
x=np.arange(0,5,1)
y=np.exp(x)
plt.subplot(8,2,9)
plt.plot(x,y)
plt.show()