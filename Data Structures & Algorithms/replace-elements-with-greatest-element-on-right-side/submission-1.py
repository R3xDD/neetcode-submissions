class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        for i in range(len(arr)-1):
            k=arr[i+1 : len(arr)]
            arr[i]=max(k)
        arr[len(arr)-1] = -1
        return arr