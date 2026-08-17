class Solution:
    def MergeSort(self,arr : List[int], temp , iL, iR ) :
        if iL >= iR : return

        pivot =  (iL + iR) //2
        self.MergeSort(arr, temp, iL, pivot)
        self.MergeSort(arr, temp, pivot + 1, iR)

        i = iL
        j = pivot + 1
        k = iL

        while i <= pivot and j <= iR :
            if arr[i] <= arr[j] :
                temp[k] = arr[i]
                i += 1
            else : 
                temp[k] = arr[j]
                j += 1
            k += 1
        while i <= pivot : 
            temp[k] = arr[i]
            i += 1
            k += 1
        while j <= iR :
            temp[k] = arr[j]
            j += 1
            k += 1
        for i in range(iL, iR + 1) :
            arr[i] = temp[i]

    

    def sortArray(self, nums: List[int]) -> List[int]:
        self.MergeSort(nums, [0] * len(nums), 0, len(nums) - 1)
        return nums