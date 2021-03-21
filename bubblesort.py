#Sorting a list using bubble sort in python
a=list(input("Enter the elements of list:"))
count=0 #stores the no. of swapping
for i in range(len(a)):
  for j in range(1,len(a)):
    if a[j-1]>a[j]:
      count=+1
      a[j-1],a[j]=a[j],a[j-1]
      
print("Sorted list:\n",a)
#print the no. of swapping done
print("No. of times of swapping:",count)
