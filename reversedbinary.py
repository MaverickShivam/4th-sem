array=[4,5,6,7,8,9,1,2,3]
key=2
def getpivot(start,end):
    if(start==end-1):
        return start
        
    else:
        if(array[int((start+end)/2)]>array[start]):
            start=int((start+end)/2)
        elif(array[int((start+end)/2)]<array[start]):
            end=int((start+end)/2)
        return getpivot(start,end)
def binarysearch(start,end,key):
    if(array[int((start+end)/2)]==key):
        print(int((start+end)/2))
    else:
        if(array[int((start+end)/2)]>key):
            end=int((start+end)/2)
        else:
            start=int((start+end)/2)
        binarysearch(start,end,key)
if(key>=array[0] and key<=array[getpivot(0,len(array))]):
    binarysearch(0,getpivot(0,len(array)),key)
else:
    binarysearch(getpivot(0,len(array)),len(array),key)
            
#output:7
