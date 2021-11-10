arr1 = [2,7,1,5,6,8,3,9]

def main(arr):
    for i in range(len(arr)-1):
        for j in range(i+1,len(arr)):
            if arr[i] > arr[j]:
                arr[i],arr[j] = arr[j],arr[i]
    return arr


if __name__ == '__main__':
    main(arr1)
    print(arr1)

            
