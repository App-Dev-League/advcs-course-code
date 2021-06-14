#standard implementation for binary search. idk what else to put 😔😢
import math

def search(arr: list):
	lo=0
	hi=len(arr)
	while(lo<hi):
		mid=math.ceil((lo+hi)/2)
		#another way to do the line above
		#avoids integer overflow
		mid = lo + math.ceil((hi-lo/2))
		if(check(mid)):
			#do something
			lo=mid or hi=mid-1
			#the first line depends on the type of the value that you are trying 
			#to find
		else:
			#choose the other option than the one that you chose above
			lo=mid or hi=mid-1
