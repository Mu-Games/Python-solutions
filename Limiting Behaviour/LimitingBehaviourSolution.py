import sys # Not necessary in Domjudge.
import os # Not necessary in Domjudge.


# Function returns n!.
def factorial(n):
    number = 1
    for i in range(2, n+1):
        number *= i
        
    return int(number)


# Function returns newton binomial coefficient.
def newton_binomial(n, k):
    output = factorial(n) / ( factorial(n - k) * factorial(k) )
    
    return int(output)
           

# Function that returns number of ways to distribute strings of size 2 and size
# 3 over a string of size n.
def count_strings(n):
    
    
    # Define total count.
    total_count = 0
    
    
    # 
    for a in range(0, int(n/3 + 1)):
        
        
        b = ( n - 3 * a ) / 2
        
        
        if b % 1 == 0:
            total_count += newton_binomial(int(a+b), int(a))


    return int(total_count)


#------------------------------------------------------------------------------
    

# Code to mimic the Domjudge input.
input_dir = os.path.abspath(os.path.join(os.path.dirname(__file__),'Testsets' ))
testset_numer = 1
sys.stdin = open(os.path.join(input_dir, f'Testset0{testset_numer}.txt'),'r')


# First we read the testset.
n = int(sys.stdin.readline())


# Calculate number of solution for different initial conditions.
start1end0 = count_strings(n)
start01end1 = count_strings(n-2)
start01end10 = count_strings(n-3)
start001end1 = count_strings(n-3)


total = start1end0 + start01end1 + start01end10 + start001end1

print(total)