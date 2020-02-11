a,b=input("enter two numbers: ").split(" ")
a=int(a)
b=int(b)
def gcd(large,small):
    if(large%small==0):
        print("GCD: ",small)
        return
    else:
        gcd(small,large%small)
gcd(max(a,b),min(a,b))
