#Merge sorted arrays
#You are given two integer arrays nums1 and nums2, sorted in non-decreasing order, and two integers m and n, representing the number of elements in nums1 and nums2 respectively.
#Merge nums1 and nums2 into a single array sorted in non-decreasing order.
#The final sorted array should not be returned by the function, but instead be stored inside the array nums1. 
#To accommodate this, nums1 has a length of m + n, where the first m elements denote the elements that should be merged, and the last n elements are set to 0 and should be ignored. nums2 has a length of n.

class mergeArrays(object):
    def merge(nums1, m, nums2, n):
        
        #simple way replace nums1 starting at m (since m is also how many elements need merged and lists start at 0 it replaces all values past m in the list )
        nums1[m+1:] = nums2
        print(nums1)
        nums1.sort()

    def merge2(nums1, m, nums2, n):
        i = m -1
        j= n -1
        k = n+m-1
        
        while (i >= 0 and j>=0):
            if (nums1[i]>nums2[j]):
                nums1[k]= nums1[i]
                k -= 1
                i -= 1
            else:
                nums1[k] = nums2[j]
                k -=1
                j -=1

        while (j>=0):
            nums1[k] = nums2[j]
            k -=1 
            j -=1

nums1 = [1,2,3,0,0,0]
m = 3
nums2 = [2,5,6]
n = 3

mergeArrays.merge(nums1, m , nums2, n)
print(nums1)
mergeArrays.merge2(nums1, m , nums2, n)
print(nums1)        