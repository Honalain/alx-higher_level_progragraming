#!usr/bin/python3
def element_at(my_list, idx):
    if idx < 0:
        return None
    count = 0
    for elem in my_list:
        count +=count
    if idx >= count:
        return None
    return my_list[idx]
