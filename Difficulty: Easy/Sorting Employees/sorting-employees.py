#User function Template for python3
class Solution:
    def sortRecords(self, e, s):
        a=list(zip(s,e))
        a.sort(key=lambda x:(x[0],x[1]))
        p=[x[1] for x in a]
        return p
        
            
    


#{ 
 # Driver Code Starts
if __name__ == '__main__':
    t = int(input().strip())

    for _ in range(t):
        # Read and parse the employee names
        employee = input().strip().split()

        # Read and parse the salaries
        salary = list(map(int, input().strip().split()))

        # Create Solution object and sort records
        ob = Solution()
        result = ob.sortRecords(employee, salary)

        # Print the sorted employee names
        print(" ".join(result))

# } Driver Code Ends