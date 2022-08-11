bucket_list = ['germany','alaska','banff','luigis mansion','oregon']
print("original list:")
print(bucket_list)
#bucket list is in original order

print("sorted list without changing original order:")
print(sorted(bucket_list))
#prints list in sorted order without modifying the original format

print("proof that the list was not permenantly sorted:")
print(bucket_list)
#demonstrating that the original list order is preserved

bucket_list.sort()
bucket_list.reverse()
print(bucket_list)
bucket_list.reverse()
print(bucket_list)

print(f"total destinations: {len(bucket_list)}")