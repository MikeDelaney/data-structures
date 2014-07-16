
def insertion_sort(a_list):
    for i in xrange(len(a_list)):
        j = i
        while j > 0 and a_list[j-1] > a_list[j]:
            a_list[j], a_list[j-1] = a_list[j-1], a_list[j]
            j = j - 1
    return a_list
