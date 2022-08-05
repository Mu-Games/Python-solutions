import sys # Not necessary in Domjudge.
import os # Not necessary in Domjudge.


# Code to mimic the Domjudge input.
input_dir = os.path.abspath(os.path.join(os.path.dirname(__file__),'Testsets' ))
testset_numer = 1
sys.stdin = open(os.path.join(input_dir, f'Testset0{testset_numer}.txt'),'r')


# First we read the testset.
testset = sys.stdin.readline().split()
n = int(testset[0])
lamb = int(testset[1])


# Function that calculates the value of the integral iteratively.
def analytical(n, lamb):
    output = 1
    
    for i in range(n+1):
        output = (-1)**i + i / lamb * output
        
    return output


# Print the answer of the testset.
answer = round(analytical(n, lamb) * 100)
print(answer)