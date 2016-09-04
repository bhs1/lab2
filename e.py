import random
import sys

def estimate():
    """
    One estimate of the constant 'e' involves generaing an infinite sequence
    of random numbers in the range (0,1). Call these values X1, X2, X3, ...
    The smallest value n such that the sum of X1 + X2 + ... + Xn > 1 gives
    an estimate for 'e'.  This function returns one such estimate.  In other
    words, it repeatedly generates numbers in the range (0,1), adding them to
    a total, and returns the number of iterations after which the total first 
    exceeds 1.0."""

def sample(n):
    """
    Return the average estimate() value over n samples.
    As n increases, this gives an increasingly more accurate estimate
    of the constant 'e'"""

print(sample(int(sys.argv[1])))


        
    
