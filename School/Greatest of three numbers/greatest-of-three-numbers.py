#User function Template for python3

class Solution:
    def greatestOfThree(self,a,b,c):
        if(a>b):
            if(a>c):
                return a
            else:
                return c
        else:
            if(b>c):
                return b
            else:
                return c


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__=='__main__':
    t=int(input())
    for _ in range(t):
        A,B,C=map(int,input().strip().split(' '))
        ob=Solution()
        print(ob.greatestOfThree(A,B,C))   
# } Driver Code Ends