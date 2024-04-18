#Merge sorted arrays
#You are given two integer arrays nums1 and nums2, sorted in non-decreasing order, and two integers m and n, representing the number of elements in nums1 and nums2 respectively.
#Merge nums1 and nums2 into a single array sorted in non-decreasing order.
#The final sorted array should not be returned by the function, but instead be stored inside the array nums1. 
#To accommodate this, nums1 has a length of m + n, where the first m elements denote the elements that should be merged, and the last n elements are set to 0 and should be ignored. nums2 has a length of n.

class mergeArrays(object):
    def merge(nums1, m, nums2, n):
        
        #simple way replace nums1 starting at m (since m is also how many elements need merged and lists start at 0 it replaces all values past m in the list )
        nums1[m:] = nums2
        
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

#These work in LeetCode solutions however I could not get them to run by themselves.
class rElement(object): 
    def rElement(nums, val):
        j = 0
        length = len(nums)
        while j < length:
            if nums[j] == val:
                nums[j] = nums[length-1]
                length-=1
                print(nums)
            else:
                j+=1
        
        return length
    
    def rElement2(nums, val):
        for i in range(nums.count(val)):
            nums.remove(i)
            return len(nums)

class removeDupe(object):
    def rDuplicates(nums):
        
        j = 0 

        while j<len(nums)-1:
            if nums[j] == nums[j+1]:
                nums.pop(j+1)
            else:
                j= j + 1

    def rDuplicates2(nums):
	
        if len(nums) < 2:
            return len(nums)
        
        current = 0
        #can also use for next in range to iterate through a range of numbers 
        for next in range(1, len(nums)):
            if nums[next] != nums[current] :
                current += 1
                nums[current] = nums[next];            
        
        return current + 1




#Code to test the solutions/functions uncomment as needed
'''nums1 = [1,2,3,]
m = 3
nums2 = [2,5,6]
n = 3

mergeArrays.merge(nums1, m , nums2, n)
print(nums1)
mergeArrays.merge2(nums1, m , nums2, n)
print(nums1)     '''   


'''nums = [3,2,2,3]
val = [3]
print(rElement.rElement(nums, val))
print(nums)'''

