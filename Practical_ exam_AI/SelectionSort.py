
#12,9,15,10,25
nums = []
print("Enter elements for the List: ")
for i in range(5):
  nums.append(int(input()))

for i in range(4):
    chk = 0
    small = nums[i] 
    for j in range(i+1, 5): 
        if small > nums[j]: 
            small = nums[j] 
            chk = chk + 1   
            index = j   
    if chk != 0:    
        temp = nums[i] 
        nums[i] = small 
        nums[index] = temp 

print("\nSorted List is: ")
for i in range(5):
    print(nums[i])