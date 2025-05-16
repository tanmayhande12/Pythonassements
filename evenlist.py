a=[2,4,6,8,10,1,3,5,7,9]

even=0

odd=1

c=[odd]*len(a)
for a1 in a:
    if a1%2==0:
        if even< len(a):
            c[even]=a1
            even+=2
        else:
            
          if odd< len(a):
            c[odd]=a1
            odd+=2

print(c)
            