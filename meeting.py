s=[6,7,2,4,5,1,2]
f=[7,8,5,8,6,2,4]
ns=[]
nf=[]
def getmin():
    minim=13
    index=-1
    for i in range(0,len(s)):
        if(s[i]>=0 and s[i]<minim):
            minim=s[i]
            index=i
    return index
for i in range(0,len(s)):
    index=getmin()
    ns.append(s[index])
    nf.append(f[index])
    s[index]=-1
    f[index]=-1
print(ns)
print(nf)
for i in range(1,len(ns)):
    if(ns[i]<nf[i-1]):
        prevdif=nf[i-1]-ns[i-1]
        nowdif=nf[i]-ns[i]
        if(prevdif<nowdif):
            nf[i]='x'
            ns[i]='x'
        else:
            nf[i-1]='x'
            ns[i-1]='x'
print(ns)
print(nf)
si=1
for i in range(0,len(ns)):
    if(ns[i]!='x'):
        print("Meeting ",si,":",ns[i]," to ",nf[i])
        si=si+1
#Output:
#Meeting  1 : 1  to  2                                                                                                                                                        
#Meeting  2 : 2  to  4                                                                                                                                                        
#Meeting  3 : 5  to  6                                                                                                                                                        
#Meeting  4 : 6  to  7                                                                                                                                                        
#Meeting  5 : 7  to  8
