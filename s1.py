outarray=[]
def findit(array,key):
    for i in range(0,len(array)):
        if(int(array[i])==int(key)):
            outarray.append(1)
            return
    outarray.append(-1)
n=int(input("No of test cases: "))
for i in range(0,n):
    noe,key=input().split(" ")
    line=input("")
    line=line.split(" ")
    findit(line,key)
print("output: ")
for ele in outarray:
    print(ele)
