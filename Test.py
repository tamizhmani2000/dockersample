import urllib
import os

def strip_path_elements(path):
    start_index = 0
    end_index = 0
    for i in range(1):
        start_index = path.index("/", start_index+1)
        print(start_index)
    for k in range(2):
        end_index = path.index("/", end_index+1)
        print(end_index)
    begin_path = path[:start_index]
    end_path = path[end_index:]
    full_path = begin_path + end_path

    return full_path


url="products/v1/nm/us/products/prod200400708"

print (strip_path_elements(url))