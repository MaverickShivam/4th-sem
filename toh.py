def toh(n,source,dest,aux):
    if(n==1):
        print("move disk ",n," from ",source," to ",dest)
    else:
        toh(n-1,source,aux,dest)
        print("move disk ",n," from ",source," to ",dest)
        toh(n-1,aux,dest,source)
toh(3,'A','C','B')
# output:
# move disk  1  from  A  to  C                                                                                                                                                 
# move disk  2  from  A  to  B                                                                                                                                                 
# move disk  1  from  C  to  B                                                                                                                                                 
# move disk  3  from  A  to  C                                                                                                                                                 
# move disk  1  from  B  to  A                                                                                                                                                 
# move disk  2  from  B  to  C                                                                                                                                                 
# move disk  1  from  A  to  C 
