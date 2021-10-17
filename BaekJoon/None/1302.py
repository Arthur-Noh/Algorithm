n = int(input())
book_list = []
unique_list=[]

for _ in range(n):
    book_list.append(input())

for x in book_list:
    if x not in unique_list:
        unique_list.append(x)

count =[book_list.count(x) for x in unique_list]
idx = []

for i in range(len(count)):
    if count[i]==max(count):
        idx.append(i)

print(sorted([unique_list[i] for i in idx])[0])
