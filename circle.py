class Circle:
    def __init__(self, R, X, Y, Vx, Vy):
        self.x=float(X)
        self.y=float(Y)
        self.R=float(R)
        self.Vx=float(Vx)
        self.Vy=float(Vy)

    def move(self,t):
        self.x+=t*self.Vx
        self.y+=t*self.Vy

    def check(self,other):
        d = (self.x - other.x) * (self.x - other.x) + (self.y - other.y) * (self.y - other.y)
        r = (self.R + other.R) * (self.R + other.R)
        if (d < r):
            return 1
        return 0

    def change_v(self,vx,vy):
        self.Vx=vx
        self.Vy=vy

print("количество кругов:")
N=int(input())
print("время:")
T=float(input())
print("шаг по времени:")
t=float(input())
print("круги:")
C=[]
for i in range(N):
    a=input().split()
    c=Circle(a[0], a[1], a[2], a[3], a[4])
    C.append(c)
k=0
while T>0:
    for i in range(N):
        for j in range(i + 1, N):
            if C[i].check(C[j]):
                Vxx=C[i].Vx
                Vyy=C[i].Vy
                C[i].change_v(C[j].Vx,C[j].Vy)
                C[j].change_v(Vxx,Vxx)
                k += 1
    for i in range(N):
        C[i].move(t)
    T-=t

print(k)


