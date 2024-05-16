
#User function Template for python3

class Solution:
    def isDigitSumPalindrome(self, n):
        t=n
        sum=0
        while(t!=0):
            a=t%10
            sum=sum+a
            t=t//10
            k=str(sum)
        if len(k)==1:
            return 1
        else:
            for i in range(len(k)//2):
                if k[i]==k[-i-1]:
                    return 1
                else:
                    return 0
                

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__=='__main__':
    t=int(input())
    for _ in range(t):
        N=int(input())
        ob=Solution()
        print(ob.isDigitSumPalindrome(N))
# } Driver Code Ends