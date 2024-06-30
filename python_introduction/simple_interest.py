# Python3 program to find simple interest
# for given principal amount, time and
# rate of interest.
 
 
def simple_interest(P,T,R):
    print('principal =', P)
    print('rate  =',R)
    print('time  =', T)
     
    I = (P * R * T)
     
    print('The simple interest is:', I)
    return I
     
# Driver code
simple_interest(1000, 3, 0.05)
