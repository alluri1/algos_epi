"""
Merge k sorted arrays
<3,5,7> <0,6> <0,6,28>
Approach 1 : merge sort
Approach 2 : use a min heap(size<=k) to keep current min elements from each array
             Each node in the heap is a tuple (value, array_index, element_index)
           : pop min element from min heap to add to output array
           : push the element at next index of popped element in the same array
"""

import heapq as hq


def merge_k_sorted_arrays(sorted_arrays):

    output = []

    # add min/first element from each array into the heap
    h = []
    for array_index, current_array in enumerate(sorted_arrays):
        if len(current_array) > 1:
            hq.heappush(h, (current_array[0], array_index, 0))





