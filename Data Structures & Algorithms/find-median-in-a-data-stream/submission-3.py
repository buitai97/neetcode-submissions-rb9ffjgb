class MedianFinder:

    def __init__(self):
        self.small, self.large = [], []

    def addNum(self, num: int) -> None:
        heapq.heappush(self.small, -1 * num)
        
        #handle wrong heaps order
        if self.small and self.large and (self.small[0] * -1 > self.large[0]):
            maxSmall = -1 * heapq.heappop(self.small)
            minLarge = heapq.heappop(self.large)
            heapq.heappush(self.small, -1 * minLarge)
            heapq.heappush(self.large, maxSmall)
            print("Small >> ", self.small)
            print("Large >> ", self.large)
        
        #handle uneven length
        if len(self.small) > len(self.large) + 1:
            maxSmall = -1 * heapq.heappop(self.small) 
            heapq.heappush(self.large , maxSmall)

    def findMedian(self) -> float:

        #odd
        if (len(self.small) + len(self.large)) % 2 != 0:
            return self.small[0] * -1

        #even
        else:
            return (self.small[0] * -1 + self.large[0])/2
        
        