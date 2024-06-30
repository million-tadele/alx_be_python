# Python3 program to find simple interest
# for given principal amount, time and
# rate of interest.
 
 
def simple_interest(P,R,T):
    print('principal =', P)
    print('rate  =',R)
    print('time  =', T)
     
    interest = (P * R * T)
     
    print('The simple interest is:', interest)
    return interest
     
# Driver code
simple_interest(1000, 0.05, 3)
