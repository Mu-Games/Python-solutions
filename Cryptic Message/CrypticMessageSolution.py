import sys # Not necessary in Domjudge.
import os # Not necessary in Domjudge.


# Given function.
def gcdExtended(a, b): 
    if a == 0 :  
        return b,0,1
             
    gcd,x1,y1 = gcdExtended(b%a, a) 
     
    x = y1 - (b//a) * x1 
    y = x1 
     
    return gcd,x,y


# Code to mimic the Domjudge input.
input_dir = os.path.abspath(os.path.join(os.path.dirname(__file__),'Testsets' ))
testset_numer = 2
sys.stdin = open(os.path.join(input_dir, f'Testset0{testset_numer}.txt'),'r')


# Read the testcase file.
n = int(sys.stdin.readline())
Wstr = sys.stdin.readline().split()
W = [0]*n
for i in range(0,n):
    W[i] = int(Wstr[i])
    
q = int(sys.stdin.readline())
r = int(sys.stdin.readline())
c = int(sys.stdin.readline())


# Determine the cryptic message.
rinv = gcdExtended(r,q) [1]

if rinv<0:
    rinv = q+rinv
    
cinv = c*rinv %q

i= n-1
answer = [0]*n

while cinv > 0:
    if W[i] <= cinv:
        cinv -= W[i]
        answer[i] = 1
    i -= 1

i = n-1
ans = ""
while i >= 0:
    ans += str(answer[n-i-1])
    i -= 1
    
    
# Return the cryptic message.
print(ans)
    