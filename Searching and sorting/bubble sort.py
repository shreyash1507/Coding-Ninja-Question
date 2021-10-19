def bubbleSort(arr) :
    length=len(arr)
    for i in range(length-1):
        
        for j in range(length-1-i):
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]



n=int(input())
for i in range(n):
    num=int(input())
    list = [int(x) for x in input().split()]
    bubbleSort(list)
    for i in range(num):
        print(list[i], end=" ")