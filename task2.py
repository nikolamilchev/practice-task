def Fibonachi_nubmer(n):
    if n<0:
        st='Exeption'
    a=0
    b=1
    if n==1:
        st='0'
    if n>1:
        st='0 1'
    for i in range(n-2):
        c=a+b
        st=st+' '+str(c)
        a=b
        b=c
    print(st)



if __name__=="__main__":
    Fibonachi_nubmer(int(input()))