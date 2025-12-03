# Approach 1 - Using Merge Sort with constant Space 
class Solution:
	def mergeKlists(self , lists:list[Optional[ListNode]]) -> Optional[ListNode]:
    	if not lists or len(lists) == 0:
      		return None  # Handle the edge cases of empty lists 
    	while len(lists) > 1:
      		mergedLists = []
        	for i in range(0 , len(lists) , 2):
        		list1 = lists[i]
				# Since we move the array pointer in two if the list 2 is of length odd then the list2 will be None 
				# So we have to handle it , without causing errors
        		list2 = lists[i+1] if (i+1) < len(lists) else None
        		mergedLists.append(self.mergeTwoLists(list1 ,list2)
				# We call the function to perform the merge operation 
      		lists = mergedLists
    	return lists[0]
	# Below is the function to merge two list , this does the merging part , this function takes Time Complextity of 
	# of O(n)
	def mergeTwoLists(self , list1 , list2):
		Dummy = ListNode()
		curr = Dummy
		while list1 and list2:
			if list1.val > list2.val:
				curr.next = list2
				list2 = list2.next 
			else:
				curr.next = list1
				list1 = list1.next 
			curr = curr.next 
		if list1:
			curr.next = list1
		if list2:
			curr.next = list2
		return Dummy.next 

# Time Complexity -> O(n * log k )
""" The reason being is that the function mergeTwoLists take O(n) time for single operation and the 
	above merged calls is called for the log k times resulting . log k * N
"""
# Space Complexity -> O(1) we do not use any extra memory in this case 

