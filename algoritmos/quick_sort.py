


list = [4,7,3,5,8,1,2]

def merge_sort(list):
    if len(list) == 1:
        return list
    
    
    down_list = list[(len(list)//2):]
    up_list = list[:(len(list)//2)] 
    sorted_left = merge_sort(down_list)
    sorted_right = merge_sort(up_list)

    return merge(sorted_left,sorted_right)


def merge(left_list,right_list):
    sorted_list = []
    while len(left_list) > 0 and len(right_list) > 0:
        print(sorted_list)
        
        if left_list[0] > right_list[0]:
            sorted_list.append(right_list[0])
            right_list.pop(0)
        else:
            sorted_list.append(left_list[0])
            left_list.pop(0)
            
            
    print(sorted_list)
        
merge_sort(list)