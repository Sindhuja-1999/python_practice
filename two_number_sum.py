def twoNumberSum(array, targetSum):
    arr=list(set(array))
    outarray=[]
    for i in range(len(arr)):
        num=arr[i]
        for j in arr:
            if num==j:
                continue
            else:
                su=j+num
                if su==targetSum:
                    outarray.append(j)
                    outarray.append(num)				
    return list(set(outarray))
print(twoNumberSum(list(map(int,input().split())),int(input())))