arr = [int(x) for x in input("Enter elements of the array separated by space: ").split()]
l,r,sum=0,1,0
while(r<len(arr)):
    if arr[l]>arr[r]:
        sum+=arr[l]-arr[r]
    else:
        l=r
    r+=1
print(sum)
