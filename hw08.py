import numpy

def transitionmatrix(n):
    N = 2**n
    A = numpy.matrix([[0.0]*N]*N)
    A[0,0] = 1
    for i in range(1,N):
        A[(2*i)%N,i] = 0.5
        A[(2*i+1)%N,i] = 0.5
    print A
    return A


def makelist(n,a,b):
    A = transitionmatrix(n)
    N = 2**n
    v = numpy.matrix([1./N]*N).T
    B = A**(a-n)
    for i in range(a,b+1):
        p = (B*v)[0,0]
        print('in '+str(i)+' rolls, '+str(p))
        B = A*B

makelist(4, 20, 21)