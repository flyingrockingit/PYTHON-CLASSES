set1 = {2,4,6,8,10,12}
set2 = {1,2,3,5,7,9,11}
#Union
set_union= set1.union(set2)
print(set_union)
#Intersection
set_intersection=set1.intersection(set2)
print (set_intersection)
#Difference
set_difference=set2.difference(set1)
print (set_difference)
#Symmetricdifference
set_symmetricdifference = set2.symmetric_difference(set1)
print (set_symmetricdifference)