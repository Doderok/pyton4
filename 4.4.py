d=0
a=float(input("стартовое количество: "))
b=float(input("среднее увеличение в %: "))
c=int(input("количество дней для размножения: "))
print("День    Популяция")
print("1        ",a)
while(c!=d):
    d=d+1
    a=a+(a*(1+b/100))
    print(d,"     ",a)
    