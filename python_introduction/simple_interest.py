# Python3 program to find simple interest
# for given principal amount, time and
# rate of interest.
 
 
def simple_interest(p,t,r):
    print('The principal =', p)
    print('The time period =', t)
    print('The rate of interest =',r)
     
    si = (p * t * r*100)/100
     
    print('The Simple Interest is:', si)
    return si
     
# Driver code
simple_interest(1000, 3, 0.05)
