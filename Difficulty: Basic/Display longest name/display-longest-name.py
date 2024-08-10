
class Solution:
    def longest(self, n):
        c=0
        c1=0
        p=0
        for i in range(0,len(n)):
            for j in n[i]:
                c+=1
            if c>c1:
                c1=c
                p=i
            c=0  
        return n[p]


#{ 
 # Driver Code Starts
if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        names = input().split()
        obj = Solution()
        res = obj.longest(names)
        print(res)

# } Driver Code Ends