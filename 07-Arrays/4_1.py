arr = [34,7,19,4,21,8]
even = 0
index = 0
while index<len(arr):
    if arr[index]%2==0:
        even += 1 
    index +=1
print(even)