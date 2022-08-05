import sys # Not necessary in Domjudge.
import os # Not necessary in Domjudge.


# Code to mimic the Domjudge input.
input_dir = os.path.abspath(os.path.join(os.path.dirname(__file__),'Testsets' ))
testset_numer = 1
sys.stdin = open(os.path.join(input_dir, f'Testset0{testset_numer}.txt'),'r')


# First we read the testset.
N = int(sys.stdin.readline())    

# Greatest common divisor algorithm.
def GCD(x, y):
  
   while(y):
       x, y = y, x % y
  
   return x


# Some trick to reduce memory usage. Can probably do without if you define the
# while loop in pollard in a correct way.
def exponentfactorialmodulo(a, M, N):
    for i in range(1,M+1):
        # print(a)
        a = a ** i % N
    return a


# Implementation of Pollard's algorithm.
def pollard(N):
    a = 2
    M = 2
    d = 1
    while d in [1,N]:
        a = exponentfactorialmodulo(a, M, N) % N
        d = GCD(N, a-1)
        
        M = M + 1
    return d, N // d


# Finally, we print the answer of the testset.
answer = pollard(N)
print(answer[0])
print(answer[1])