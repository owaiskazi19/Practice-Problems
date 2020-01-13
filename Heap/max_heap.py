

def heapify(startIdx, arr, n):
    largest = startIdx
    left = 2*startIdx +1
    right = 2*startIdx + 2
    if (left < n and arr[left]>arr[largest]):
        largest = left
    if (right < n and arr[right] > arr[largest]):
        largest = right
    
    if (largest != startIdx):
        swap = arr[startIdx]
        arr[startIdx] = arr[largest]
        arr[largest] = swap

        heapify(largest, arr, n)


def buildHeap(arr, n):
    startIdx = int((n/2)) - 1
    for i in range(startIdx, -1, -1):
        heapify(i, arr, n)

def printHeap(arr,n):
    for i in range(n):
        print arr[i], 



if __name__ == '__main__': 
      
    # Binary Tree Representation 
    # of input array 
    # 1 
    #         /     \ 
    # 3         5 
    #     / \     / \ 
    # 4     6 13 10 
    # / \ / \ 
    # 9 8 15 17 
    arr = [ 1, 3, 5, 4, 6, 13,  
             10, 9, 8, 15, 17 ]; 
  
    n = len(arr); 
  
    buildHeap(arr, n); 
  
    printHeap(arr, n); 

    # T: O(NlogN)
    