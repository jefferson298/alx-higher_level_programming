#!/usr/bin/python3
# 2-replace_in_list.py
def replace_in_list(my_list, idx, element):
    if idx < 0:
        return my_list
    if idx >= len(my_list):
        return my_list
    my_list[idx] = element
    return my_list
