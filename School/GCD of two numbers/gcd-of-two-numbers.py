
class Solution:
    def gcd(self, a : int, b : int) -> int:
        g=0
        k=min(a,b)//2
        
        if a==0:
            g=b
        elif b==0:
            g=a
        else:
            l=min(a,b)
            m=max(a,b)
            while l!=0:
                r=m%l
                m=l
                l=r
            return m
                
        



#{ 
 # Driver Code Starts

if __name__=="__main__":
    t = int(input())
    for _ in range(t):
        
        a = int(input())
        
        
        b = int(input())
        
        obj = Solution()
        res = obj.gcd(a, b)
        
        print(res)
        

# } Driver Code Ends