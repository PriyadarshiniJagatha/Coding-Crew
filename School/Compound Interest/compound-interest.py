#User function Template for python3
import math as m
class Solution:
    def getCompundInterest(self, P ,T , N , R):
        for i in range(T*N):
            I=(P*R)/(100*N)
            P=P+I
        return m.floor(P)


#{ 
 # Driver Code Starts
#Initial Template for Python 3

import math
if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        P,T,N,R = map(int,input().split())
        
        ob = Solution()
        print(ob.getCompundInterest(P,T,N,R))
# } Driver Code Ends