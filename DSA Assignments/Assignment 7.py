# Question 2: Given three points, check whether they lie on a straight (collinear) or not.

# Time complexity = O(1)
def CheckCollinear(points):
    #using area of triangle method.
    x1,x2,x3 = points[0][0],points[1][0],points[2][0]
    y1,y2,y3 = points[0][1],points[1][1],points[2][1]
    area = 1/2*(x1*(y2-y3) + x2*(y3-y1) + x3*(y1-y2))
    if area == 0:
        return 'Yes'
    else:
        return 'No'

# driver code
points = [(1,1), (1,4), (1,5)]
result = CheckCollinear(points)
print("Whether the given points are collinear?",result)

"""Question 3: An e-commerce site tracks the purchases made each day. The product that is purchased
the most one day is the featured product for the following day. If there is a tie for the product
purchased most frequently, those product names are ordered alphabetically ascending and
the last name in the list is chosen.[Amazon]"""

from collections import Counter
import heapq
def MostFrequentPurchase(purchases):
    count = Counter(purchases) #stores the frequency of the strings in the form of a dictionary.
    result = heapq.nlargest(1,count,key=count.get)
    return result

#driver code
purchases = ['yellowShirt', 'redHat', 'blackShirt', 'bluePants', 'redHat','pinkHat', 'blackShirt', 'yellowShirt',
'greenPants', 'greenPants', 'greenPants']
result = MostFrequentPurchase(purchases)
print(f"The most frequent purchase of the day is {result}")

"""Question 4: An almost sorted array is given to us and the task is to sort that array completely. Then,
which sorting algorithm would you prefer and why?[Salesforce] """

""" 
The answer is insertion sort.
let us take a example of an almost sorted array , [10,20,30,40,50,5]
Here time complexity depends upon the number of comparison and the number of swaps.
In above example the array is sorted until the element 50, so the number of comparison until the element 50 will be 1 and swaps until the element 50 will be zero,
as the array is already sorted.
When the element is 5, there will be n-1 number of comparisons and n-1 number of swaps.
In case of implementation, until the element 50 , it doesn't go into while loop.When the element is 5, it executes while loop n-1 number of times.

Hence, Time complexity is equal to number of comparison + number of swaps
=> (n-1) + (n-1)
=> O(n)
"""