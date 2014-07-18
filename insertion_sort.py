
def insertion_sort(sort_list):
    for i in xrange(len(sort_list)):
        j = i
        while j > 0 and sort_list[j-1] > sort_list[j]:
            sort_list[j], sort_list[j-1] = sort_list[j-1], sort_list[j]
            j = j - 1
    return sort_list


if __name__ == '__main__':
    import timeit
    worst_list = []
    best_list = []
    for i in [1, 5, 10, 50, 100, 500, 1000, 5000, 10000]:
        worst = timeit.timeit('insertion_sort(range({}, -1, -1))'.format(i),
                              'from __main__ import insertion_sort',
                              number=1)
        worst_list.append(worst)
        best = timeit.timeit('insertion_sort(range({}))'.format(i),
                             'from __main__ import insertion_sort',
                             number=1)
        best_list.append(best)
    print '\nBest case scenario is sorting an already sorted list'
    print 'Worst case scenario is sorting a list in reverse order'
    print '\nBest Case\t\tWorst Case'
    for i in xrange(len(best_list)):
        print '{0}\t{1}'.format(best_list[i], worst_list[i])
