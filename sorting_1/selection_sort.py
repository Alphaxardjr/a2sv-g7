class Solution: 
    def selectionSort(self, arr):
        n = len(arr)
        for i in range(n):
            # Find the minimum 
            min_idx = i
            for j in range(i+1, n):
                if arr[j] < arr[min_idx]:
                    min_idx = j
            
            # Swap the found minimum
            arr[i], arr[min_idx] = arr[min_idx], arr[i]
        
        return arr
