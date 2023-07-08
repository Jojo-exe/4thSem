# task1
def countNum(lst, c=0):
    if not lst:
        return c
    elif isinstance(lst[0], (int, float)):
        return countNum(lst[1:], c+1)
    else:
        return countNum(lst[1:], c)

lst = ['a', 1, 'b', 3, 5, 'c', 7, 9]
num_count = countNum(lst)
print("Task1 :")
print("The number of numeric values in the list is:",num_count)



# Task2
def divisible_by_13(lst, res=[]):
    if not lst:
        return res
    elif lst[0] % 13 == 0:
        return divisible_by_13(lst[1:], res)
    else:
        res.append(lst[0])
        return divisible_by_13(lst[1:], res)
lst = [13, 5,18,20, 26, 39, 52, 91, 104]
updated_lst = divisible_by_13(lst)
print("task2:")
print(f"The updated list after deleting values divisible by 13 is:",updated_lst)





# Task3

def NotContains(lst, val_list, res=[]):
    if not lst:
        return res
    elif lst[0] not in val_list:
        res.append(lst[0])
    return NotContains(lst[1:], val_list, res)
lst = [1, 2, 3, 2, 4, 5, 4, 6]
val_list = [2, 4]
new_lst =NotContains(lst, val_list)
print("Task3:")
print("Result:",new_lst)




