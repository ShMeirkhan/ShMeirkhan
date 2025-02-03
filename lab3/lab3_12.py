def histograme(nums):
    for i in range(len(nums)):
        print(nums[i]*'*')
s=[]
n=int(input())
for i in range(n):
    x=int(input())
    s.append(x)
histograme(s)