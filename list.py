#create sets 
set1 = {1,2,3,4,5}
set2 = {4,5,6,7,8}

#access set elements (iterate through set)
print("set 1 elements:")
for elem in set1:
    print(elem, end=" ")
    print("\nSet 2 elements: ")
for elem in set2:
    print(elem, end=" ")
    print()

# union of sets 
union_set = set1.union(set2)
print("union of set1 and set2:",union_set)

#intersection 
intersection_set = set1.intersection(set2)
print("this is the intersection of set1 and 2 :", intersection_set)

# difference of set 
difference_set = set1.difference(set2)
print(difference_set)