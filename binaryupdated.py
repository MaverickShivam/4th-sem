line=input("Enter comma seperated values: ")
line=line.split(",")
number=int(input("key: "))
def binary(start,end,snumber):
    if(int(line[int((start+end)/2)])==snumber):
        index=(int((start+end)/2))
        while(index>=0 and int(line[index-1])==snumber):
            index=index-1
        print("start:",index)
        while(index<len(line) and int(line[index+1])==snumber):
            index=index+1
        print("end:",index)
        return
    else:
        if(int(line[int((start+end)/2)])<snumber):
            binary(int((start+end)/2),end,snumber)
        elif(int(line[int((start+end)/2)])>snumber):
            binary(start,int((start+end)/2),snumber)
binary(0,len(line)-1,number)

# output:
# Enter comma seperated values: 1,2,3,4,4,4,4,5,5,6                                                                                                                            
# key: 4                                                                                                                                                                       
# start: 3                                                                                                                                                                     
# end: 6
