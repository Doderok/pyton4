a=float(input("скорость транспортного средства: "))
b=int(input("время движения: "))
c=0
d=0
print("час     Пройденное расстояние")
print("-----------------------------")
while (c!=b):
    c=c+1
    d=c*a
    print(c,"      ",d)