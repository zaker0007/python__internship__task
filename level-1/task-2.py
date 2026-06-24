grid=[
    [1,2,3],
    [4,5,6],
    [7,8,9]
]
entered_number = int(input("Enter a number to search in the grid: "))
for row in grid:
    for num in row:
        if num == entered_number:
            print("found")
            break
       
    else:
        print("not found")
        break
    
            
    