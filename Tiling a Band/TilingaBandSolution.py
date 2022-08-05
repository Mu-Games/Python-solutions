import sys # Not necessary in Domjudge.
import os # Not necessary in Domjudge.


# Code to mimic the Domjudge input.
input_dir = os.path.abspath(os.path.join(os.path.dirname(__file__),'Testsets' ))
testset_numer = 1
sys.stdin = open(os.path.join(input_dir, f'Testset0{testset_numer}.txt'),'r')


# First we read the testset.
n = int(sys.stdin.readline())

# The possible tiling of a 2xn grid are given by shifted Fibonacci sequence.
def possible_tilings(n):
    if n ==0:
        return int(0)
    if n == 1:
        return int(1)
    elif n == 2:
        return int(2)
    else:
        lst = [1,2]
        for i in range(n-2):
            lst.append(lst[-1] + lst[-2])
        return int(lst[-1])
    

# The possible tilings of a band are given by the following function.
def band_tilings(n):
    if n%2==0:
        return int(possible_tilings(n) + possible_tilings(n-2) + 2)
    else:
        return int(possible_tilings(n) + possible_tilings(n-2))
    

# Finally, we print the answer of the testset.
answer = band_tilings(n)
print(answer)