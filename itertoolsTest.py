def naive_tuple_grouper(inputs, n):
    num_groups = len(inputs) // n
    return [tuple(inputs[i*n:(i+1)*n]) for i in range(num_groups)]

def naive_arr_grouper(inputs, n):
    num_groups = len(inputs) // n
    return [list(inputs[i*n:(i+1)*n]) for i in range(num_groups)]

nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]

new_nums = naive_tuple_grouper(nums, 2)
new_arr_nums = naive_arr_grouper(nums, 2)
print(tuple(nums))
print(new_arr_nums)
print(new_nums)


print(tuple(nums))

