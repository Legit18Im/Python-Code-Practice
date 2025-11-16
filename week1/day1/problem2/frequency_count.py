str = 'programming'
count= {}
for char in str:
    if char in count:
        count[char] += 1

    else:
        count[char] = 1




print(f"the count of {char} is {count}")        

     