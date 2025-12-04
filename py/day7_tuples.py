# Ordered, Immutable, allows duplicate elements
single_item = (42,)
print(type(single_item))  # Output: <class 'tuple'>
print(single_item)     # Output: 42

check_tuple = (1, 2, 3, 4, 5, 5)
print(check_tuple[1])
