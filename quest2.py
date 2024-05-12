from typing import List
height = [int(x) for x in input("Enter elements of the array separated by space: ").split()]
# min(L,R)-h[i]
def trappedwater(height: List[int]) ->int:
    l,r,sum=0,len(height)-1,0
    lmax,rmax =height[l],height[r]
    while(l<r):
        if lmax<rmax:
            l+=1
            lmax = max(lmax,height[l])
            sum += lmax - height[l]
        else:
            r-=1
            rmax = max(rmax,height[r])
            sum += rmax - height[r]
    return sum
print("Trapped water:", trappedwater(height))
