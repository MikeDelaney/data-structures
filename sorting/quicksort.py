# import random


def quicksort(sort_list):
    if len(sort_list) <= 1:
        return sort_list
    else:
        # choose first element as pivot for ease of time demo
        pivot = sort_list[0]
        left = quicksort([item for item in sort_list[1:] if item < pivot])
        right = quicksort([item for item in sort_list[1:] if item >= pivot])
    return left + [pivot] + right


if __name__ == '__main__':
    import timeit
    worst_list = []
    best_list = []
    for i in [1, 5, 10, 50, 100, 500, 996]:
        worst_case = range(i)
        best_case = range(i)
        # move middle value to pivot point
        best_case[0], best_case[len(best_case) // 2] = \
            best_case[len(best_case) // 2], best_case[0]
        worst = timeit.timeit('quicksort({})'.format(worst_case),
                              'from __main__ import quicksort',
                              number=1)
        worst_list.append(worst)
        best = timeit.timeit('quicksort({})'.format(best_case),
                             'from __main__ import quicksort',
                             number=1)
        best_list.append(best)
    print '\nBest case scenario occurs when pivot is the middle value'
    print 'Worst case scenario occurs when pivot is greatest or least value'
    print '\nBest Case\t\tWorst Case'
    for i in xrange(len(best_list)):
        if len(str(best_list[i])) < 16:
            print '{0}\t\t{1}'.format(best_list[i], worst_list[i])
        else:
            print '{0}\t{1}'.format(best_list[i], worst_list[i])
