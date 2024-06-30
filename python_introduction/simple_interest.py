# Python3 program to find simple interest
# for given principal amount, time and
# rate of interest.
 
 
def simple_interest(P,T,R):
    print('The principal =', P)
    print('The time period =', T)
    print('The rate of interest =',R)
     
    I = (P * R * T)
     
    print('The Simple Interest is:', I)
    return I
     
# Driver code
simple_interest(1000, 3, 0.05)
