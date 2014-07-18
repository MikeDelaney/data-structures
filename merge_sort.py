
def merge_sort(sort_list):
    if len(sort_list) <= 1:
        return sort_list
    else:
        midpoint = len(sort_list) // 2
        left = merge_sort(sort_list[:midpoint])
        right = merge_sort(sort_list[midpoint:])
    return merge(left, right)


def merge(left, right):
    result = []
    while len(left) > 0 or len(right) > 0:
        if len(left) > 0 and len(right) > 0:
            if left[0] <= right[0]:
                result.append(left[0])
                left = left[1:]
            else:
                result.append(right[0])
                right = right[1:]
        elif len(left) > 0:
            result.append(left[0])
            left = left[1:]
        elif len(right) > 0:
            result.append(right[0])
            right = right[1:]
    return result


if __name__ == '__main__':
    import timeit
    worst_list = []
    best_list = []
    for i in [1, 5, 10, 50, 100, 500, 1000, 5000, 10000, 20000]:
        worst = timeit.timeit('merge_sort(range({}, -1, -1))'.format(i),
                              'from __main__ import merge_sort',
                              number=1)
        worst_list.append(worst)
        best = timeit.timeit('merge_sort(range({}))'.format(i),
                             'from __main__ import merge_sort',
                             number=1)
        best_list.append(best)
    print '\nBest case scenario is sorting an already sorted list'
    print 'Worst case scenario is sorting a list in reverse order'
    print '\nBest Case\t\tWorst Case'
    for i in xrange(len(best_list)):
        if len(str(best_list[i])) < 16:
            print '{0}\t\t{1}'.format(best_list[i], worst_list[i])
        else:
            print '{0}\t{1}'.format(best_list[i], worst_list[i])
