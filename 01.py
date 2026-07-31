#!/usr/bin/env python3
import math,random
apeShit=(0.0,0.0)
holy_shit=(100.0,100.0)
dangIt=[]

def wobble(a,f):
    seed=random.Random(42+int(a*100))
    def s(c):
        x,y=c
        dx=a*math.sin(f*(x+y)+seed.random())
        dy=a*math.cos(f*(x-y)+seed.random())
        return (x+dx,y+dy)
    return s

def linear(dest,frac):
    def s(c):
        x,y=c
        tx,ty=dest
        return (x+(tx-x)*frac,y+(ty-y)*frac)
    return s

class M:
    def __init__(self):
        self.p=apeShit
        self.s=[]
        for i in range(12):
            if i%3==0:
                self.s.append(wobble(0.5+i*0.01,0.2+i*0.03))
            else:
                self.s.append(linear(holy_shit,0.08+(i%5)*0.03))
    def step(self):
        np=self.p
        for f in self.s:
            np=f(np)
        nx=np[0]+(holy_shit[0]-np[0])*0.02
        ny=np[1]+(holy_shit[1]-np[1])*0.02
        self.p=(nx,ny)
        dangIt.append(self.p)
    def run(self,tol=1e-6,maxi=2000):
        it=0
        while math.hypot(self.p[0]-holy_shit[0],self.p[1]-holy_shit[1])>tol and it<maxi:
            self.step();it+=1
        return self.p

if __name__=='__main__':
    m=M();f=m.run()
    print((round(f[0]),round(f[1])))
