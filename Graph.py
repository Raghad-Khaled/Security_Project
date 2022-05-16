from string import digits
import time
from RSA import *
import matplotlib.pyplot as plt
ntested=[659*661 ,
        3907*3911,
        90887*91019,
        986257*986543,
        7505063*7519907,
        22335757*22466603,
        493756181*493826699,
        8018018851*8064645241,
        46899999989*47519791211,
        101234567897*101601701401,
        1000123465987*1012345678901,
        24738041398529*27064032706411,
        106800081666611*109139149179199,
        1106098069699111*1111235916285193,
        99999999999899999*99999999999999997,
        160409920439929091*161111111111111111,
        1000000000000000003*1000000000000000009,
        13315146811210211749*13337777797999979999,
        123456789878987654321*134792113502441352569,
        1011235813471123581347*1012384965710123854679,
        12345678911223344556677*13579135795359753197531,
        100207100213100237100267*105120136153171190210231,
        9510321949318457733566099*9989999899883889989999899
        ]

digitsofn=[]
times=[]

for n in ntested:
   #print(n) 
   start = time.time_ns()
   #print(start) 
   reslt=Encrypt("Hi",n,6709)
   digitsofn.append(len(str(n)))
   times.append(time.time_ns()-start)


# plotting the points
plt.plot(digitsofn, times,'--bo')
 
# naming the x axis
plt.xlabel('number of degits in n (the size of n)')
# naming the y axis
plt.ylabel('time ake for encript in nano sec')
 
# giving a title to my graph
plt.title('RSA encryption time vs. Key length.')

#plt.grid(color = 'green')
#plt.xticks(digitsofn)
 
# function to show the plot
plt.show()   

print(digitsofn)
print(times)   
