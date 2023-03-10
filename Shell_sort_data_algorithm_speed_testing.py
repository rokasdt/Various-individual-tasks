import random
import timeit

def shell_sort(arr):
    """Original sequence of distances"""
    n = len(arr)
    gap = n // 2

    while gap > 0:
        for i in range(gap, n):
            temp = arr[i]
            j = i
            while j >= gap and arr[j - gap] > temp:
                arr[j] = arr[j - gap]
                j -= gap
            arr[j] = temp
        gap //= 2

    return arr

def shell_sort_sedgewick(arr):
    """Sedgewick sequences of distances"""
    n = len(arr)
    sedgewick = []
    h = 1
    while h < n:
        sedgewick.append(h)
        h = (9 * h) + 1

    while len(sedgewick) > 0:
        h = sedgewick.pop()
        for i in range(h, n):
            temp = arr[i]
            j = i
            while j >= h and arr[j - h] > temp:
                arr[j] = arr[j - h]
                j -= h
            arr[j] = temp
    return arr

def test_sort(sort_func, data_type, num_sets=5, num_tests=10):
    """Test sorting speed for a given sorting function and data type"""
    data_sizes = [10, 100, 1000, 10000, 100000]

    for size in data_sizes:
        print(f'Testing {sort_func.__name__} with {size} {data_type} data')
        for i in range(num_sets):
            if data_type == 'random':
                test_data = [random.randint(0, 1000000) for _ in range(size)]
            elif data_type == 'almost sorted':
                test_data = [x for x in range(size)]
                random.shuffle(test_data)

            times = []
            for j in range(num_tests):
                start = timeit.default_timer()
                sort_func(test_data)
                end = timeit.default_timer()
                times.append(end - start)

            avg_time = sum(times) / num_tests
            print(f'Set {i+1}: Average time taken = {avg_time:.6f} seconds')
            print(f'Individual times: {times}\n')

# Test sorting speed for original sequence of distances
test_sort(shell_sort, 'random')
test_sort(shell_sort, 'almost sorted')

# Test sorting speed for Sedgewick sequences of distances
test_sort(shell_sort_sedgewick, 'random')
test_sort(shell_sort_sedgewick, 'almost sorted')
