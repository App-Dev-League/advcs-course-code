#Standard bubble sort. Can switch the < to a > if you want to reverse the list 😇😙
def bubble_sort(arr: list):
	for i in range(len(arr)):
		for j in range(len(arr)):
			if(arr[i]<arr[j]):
				temp=arr[i]
				arr[i]=arr[j]
				arr[j]=temp
	print(arr)

