class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        # at every index i decide whether to extend subarray or start a new subarray
        # time: O(n)
        # space: O(1)
        if len(arr) == 1:
            return 1
        
        best_arr = curr_arr = 1
        for i in range(1, len(arr)):
            if i == 1:
                curr_arr = 1 if arr[i] == arr[i-1] else 2
            elif arr[i-2] < arr[i-1] > arr[i]:
                curr_arr += 1
            elif i > 1 and arr[i-2] > arr[i-1] < arr[i]:
                curr_arr += 1
            elif arr[i] == arr[i-1]:
                curr_arr = 1
            else:
                curr_arr = 2
            
            print(f"i: {i}, curr_arr: {curr_arr}")
            best_arr = max(curr_arr, best_arr)
        
        return best_arr