import time 
arr=[10,2,1,4,3,5,9,8,6,7]
t1=time.time()
for i in range(1,len(arr)):
    ele=arr[i]
    temp=i-1
    while(temp>=0 and arr[temp]>ele):
        arr[temp+1]=arr[temp]
        arr[temp]=ele
        temp=temp-1
t2=time.time()
print(arr)
print("time taken: ",(t2-t1)*1000,"ms")
