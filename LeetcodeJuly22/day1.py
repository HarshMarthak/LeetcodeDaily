#my solution

class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        boxTypes.sort(reverse=True, key=lambda x:x[1])
        ans=0
        i=0
        while truckSize>0 and i<len(boxTypes):
            if truckSize-boxTypes[i][0]>-1:
                truckSize-=boxTypes[i][0]
                ans+=boxTypes[i][0]*boxTypes[i][1]
            else:
                ans+=truckSize*boxTypes[i][1]
                truckSize=0
            print(boxTypes[i][0],boxTypes[i][1],ans,truckSize)
            i+=1
        return ans



