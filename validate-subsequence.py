from collections import defaultdict


def isValidSubsequence(array,sequence):

    if(len(sequence) > len(array)):
        return False
    
    array_dict = defaultdict()


    for index,value in enumerate(array):
        array_dict[value] = index
    
    valid_subsequnce = True



    for index,value in enumerate(sequence):
        if index == 0:
            continue
        else:
            if array_dict[value] > array_dict[sequence[index-1]]:
                continue
            else:
                valid_subsequnce = False
                break

    return valid_subsequnce





print(isValidSubsequence([5, 1, 22, 25, 6, -1, 8, 10],[1, 6, -1, 10, 11, 11, 11, 11]))


