terms=int(input("Enter the number of terms: "))
first=0
second=1
for i in range(terms):
    print(first)
    next=first+second
    first=second
    second=next
    