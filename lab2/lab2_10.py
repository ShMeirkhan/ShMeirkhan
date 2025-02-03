my_tuple = (1, 2, 3, 4, 5)
print(my_tuple[0])
print(my_tuple[-1])
my_tuple = (1, 2, 3, 4, 5)
new_tuple = my_tuple + (6,)
print( new_tuple)
a, b, c, d, e = my_tuple
print(a, b, c, d, e)
for item in my_tuple:
    print( item)
tuple1 = (1, 2, 3)
tuple2 = (4, 5, 6)
joined_tuple = tuple1 + tuple2
print( joined_tuple)
print(len(my_tuple))
print(my_tuple.count(2))
print( my_tuple.index(3))
