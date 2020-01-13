


def findMedian(input1, input2):

    if len(input1) > len(input2):
        return findMedian(input2, input1)
    
    n1 = len(input1)
    n2 = len(input2)
    low = 0
    high = n1

    while(low<=high):
        partitionX = low + (high-low)/2
        partitionY = (n1 + n2 + 1)/2 - partitionX

        maxLeftX = -float('inf') if partitionX == 0 else input1[partitionX-1]
        minRightX =  float('inf') if partitionX == n1 else input1[partitionX]

        maxLeftY =  -float('inf') if partitionY == 0 else input2[partitionY-1]
        minRightY =  float('inf') if partitionY == n2  else input2[partitionY]

        if maxLeftX<=minRightY and maxLeftY<=minRightX:
            if (n1 + n2) % 2 ==0:
                return max((maxLeftX, maxLeftY) + min(minRightX, minRightY))/2.0
            else:
                return max(maxLeftX,maxLeftY)
        
        elif maxLeftX>minRightY:      # Too far in the right side of partitionX
            high = partitionX - 1
        else:                           # Too far in the left side of partitionX
            low = partitionX + 1





input1 = [1, 3]
input2 = [2]

print findMedian(input1, input2)