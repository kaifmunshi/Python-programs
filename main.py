hrs = input("Enter Hours:")
rate=input('enter rate')
h = float(hrs)
c=float(rate)

if(h>40):
    ans=h*c
    overtime=(h-40)*c*(0.5)
    print(overtime)