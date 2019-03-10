import sys, datetime
sys.setrecursionlimit(10000)

cont = 0
ativo = True

def A(m, n, s="%s"):
    
    global cont
    global ativo
    cont+=1
    if (ativo == True):
        print (cont)
        print (s % ("A(%d,%d)" % (m, n)))

    if m == 0:
        return n + 1
    if n == 0:
        return A(m - 1, 1, s)
    n2 = A(m, n - 1, s % ("A(%d,%%s)" % (m - 1)))
    return A(m - 1, n2, s)

if len (sys.argv) != 3:
    print ("Usage: python Ackermann1.py <m> <n>")
else:
    m = int(sys.argv[1])
    n = int(sys.argv[2])
    ts1 = datetime.datetime.now().timestamp()
    ack = A(m,n)
    ts2 = datetime.datetime.now().timestamp()
    tempo = ts2-ts1
    print ("---")
    print (" * Saida: A(", m, ",", n, ") = ", ack)
    print (" * No. Recursoes: ", cont)
    print (" * Tempo: ", tempo)
    print ("---")

"""
cont = 0
ativo = False
def ackermann(m,n):
       #computes the value of the Ackermann function for the input integers m and n.
       #the Ackermann function being:
       #A(m,n)=n+1               if m=0
       #      =A(m-1,1)          if m>0 and n=1
       #      =A(m-1,A(m,n-1)    if m>0 and n>0
    global cont
    global ativo
    cont+=1
    if m==0:
        if (ativo == True):
            print (n+1)
        return n+1
    elif m>0 and n==0:
        if (ativo == True):
            print ("ackermann(",m-1,",",1,")")
        return ackermann(m-1,1)
    elif m>0 and n>0:
        if (ativo == True):
            print ("Ackermann(",m-1,",","Ackermann(",m,",",n-1,")",")")
        return ackermann(m-1,ackermann(m,n-1)) 

if len (sys.argv) != 3:
    print ("Usage: python Ackermann1.py <m> <n>")
else:
    m = int(sys.argv[1])
    n = int(sys.argv[2])
    resp = ackermann(m,n)
    print ("resp=",resp)
    print ("cont=",cont)
"""
