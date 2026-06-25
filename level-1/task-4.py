grid=[
    [1,2,3],
    [4,5,6],
    [7,8,2]
]

seen_numbers=[grid]
all_unique=True

for row in grid:
    for num in row: 
        if num in seen_numbers:
            all_unique=False
            break

        else:
            seen_numbers.append(num)
            

if all_unique:
    print("all numbers are unique")

else:
    print("duplicate numbers found")

        
           
        