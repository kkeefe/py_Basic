<<<<<<< HEAD
# stuff to write as a silly test bench of py code to place in other note sections..

# use of a map function as applied to a lambda function

# make some function you want
my_func = lambda x: x ** x

# lets make a map for this function
sequence = [1, 2, 3]
my_map = list(map(my_func, sequence))
print(my_map)

# filter function, removes items from a list for which func returns false.
sequence_2 = [1,2,3]
is_odd = lambda x : ( x % 2 )
my_filter = list(filter(is_odd, sequence_2))
print(my_filter)
=======
# stuff to write as a silly test bench of py code to place in other note sections..

# use of a map function as applied to a lambda function

# make some function you want
my_func = lambda x: x ** x

# lets make a map for this function
sequence = [1, 2, 3]
my_map = list(map(my_func, sequence))
print(my_map)

# filter function, removes items from a list for which func returns false.
sequence_2 = [1,2,3]
is_odd = lambda x : ( x % 2 )
my_filter = list(filter(is_odd, sequence_2))
print(my_filter)

>>>>>>> ef1fa5f03d0dc522c35426b67da3caeb06e5339c
