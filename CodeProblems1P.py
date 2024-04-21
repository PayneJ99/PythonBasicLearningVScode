#Most notes are handwritten as that is the most efficient way I find to work through a problem
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

#combination sum - research   
class sumCombo:
    def combinationSum(candidates: list[int], target: int) -> list[list[int]]:
        #creates a list of size target+1 and populates them each with []
        cache = [[] for _ in range(target + 1)]
        cache[0] = [[]]
        for c in candidates:
            for i in range(target + 1):
                if i >= c:
                    for temp_ans in cache[i - c]:
                        cache[i].append(temp_ans + [c])
        return cache[-1]

#leetcode 9-Easy Palindromes
class Palindrome:
    def isPalindrome(x: int) -> bool: #palindrome without converting to string 
        
        #keep track of original value for final check
        Orig = x
        y = 0
        while x>0:

            #gives the end value and gets it ready for the next value to be added 
            y = y*10
            y = x%10 + y
            #gives next whole number
            x = round(x/10)

        if Orig == y:
            return True
        else:
            return False
    
    def isPalindrome(x: int) -> bool: #palindrome utilizing string conversion
        
        x = str(x)
        #slices the string starting at the last value and going in reverse 
        y = x[::-1]
        if x == y:
            return True
        else:
            return False
        

# leetcode 10-Hard - Regular expression matching - still working through misunderrstood how it wanted it at first    
class regexpMatch:
    def isMatch(self, s: str, p: str) -> bool:
        
        retVal = "true"
        ofsVal = 0 

        while p[0] not in [s[0], '.']:
            return False
        

        for element in range(0, len(p)):
            
            print('hit')
            if (len(p) == 1 and len(s)>1):

                if p[element] != "*":
                    print("hit")
                    return False
            
            

            
            if p[element] == "*":
                print([element-1])
                print([element+ofsVal])
                if p[element-1] == "." or s[element+ofsVal]:
                    ofsVal +=1
                    element -=1
                else: 
                    return False
        
        return True

#First attempt runtime 53ms mem 16.76mb
class rtoI:
    def romanToInt(self, s: str) -> int:
        countVal = 0
        while s != "":


            if s[0] == "I" and (("V" in s) or ("X" in s)):
                
                countVal = countVal - 1
                
            elif s[0] == "X" and (("L" in s) or ("C" in s)):
                
                countVal = countVal - 10

            elif s[0] == "C" and (("M" in s) or ("D" in s)):
                
                countVal = countVal - 100
                
            else:
                
                match s[0]:
                    case "I":
                        countVal +=1
                    case "V":
                        countVal +=5
                    case "X":
                        countVal +=10
                    case "L":
                        countVal +=50
                    case "C":
                        countVal +=100
                    case "D":
                        countVal +=500
                    case "M":
                        countVal +=1000

            
            s = s[1:]
            

        return countVal
    




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

'''candidates = [2,3,6,7]
target = 7
returnVal = sumCombo.combinationSum(candidates, target)
print("The returning values: " + str(returnVal))'''


x = 12345
y = round(x/10)
print(x)
print(y)