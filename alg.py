

import random


def bubble_sort(a):
    n = len(a)
    unordered = True
    while unordered:
        unordered = False
        for j in range (n-1):
            if a[j]>a[j+1]:
                a[j], a[j+1] = a[j+1], a[j]
                unordered = True
    n -=1


#vstavkami
def selection_sort(a):
    for i in range (len(a)-1):
        imin = i
        for j in range (i +1, len(a)):
            if a [j]<a[imin]:
                imin = j
        a[i], a[imin] = a[imin], a[i]

#viborom
def insertion_sort(a):
    for i in range(1, len(a)):
        tmp = a[i]
        j = i - 1
        while j >=0 and a[j]>tmp:
            a[j+1]=a[j]
            j-=1
            a[j+1]=tmp




def quick_sort(nums):

   if len(nums) <= 1:
       return nums
   else:
       q = random.choice(nums)
       s_nums = []
       m_nums = []
       e_nums = []
       for n in nums:
           if n < q:
               s_nums.append(n)
           elif n > q:
               m_nums.append(n)
           else:
               e_nums.append(n)
       return quick_sort(s_nums) + e_nums + quick_sort(m_nums)
