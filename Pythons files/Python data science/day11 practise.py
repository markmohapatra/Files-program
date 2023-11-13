import math
# n=[3,6,6,7,8,11,15,16]

# mean=sum(n) / len(n)
# print('Mean :', mean)

# r1=[]

# for v in n :
#     r1=r1+[abs(mean - v)]

# print(r1)
# r1Mean=sum(r1)/len(r1)
# print('M.D :',r1Mean)

# r2=[]
# for v in r1:
#     if v<r1Mean:
#         r2=r2+[v]
# print(r2)

# def STDev(n):
#     M=sum(n)/len(n)
#     print('Mean: 'M)

#     d=list(map(lambda v : (M-v)**2, n))
#     print('Dist :'d)

#     VAR=sum(d)/len(d)
#     print('Var:', VAR)

#     STD=math.sqrt(VAR)

#     #valida values
#     V=[]
#     for i,v in enumerate(n):
#         if v <STD:
#             V=V+[n[i]]
#     #print('Valid:',V)

#     #Outliers
#     out=[]

#     for i,v in enumerate(d):
#         if v> STD:
#             out=out+[n[i]]

#     #print('Out:', out)
