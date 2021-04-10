import time
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

plt.rcParams['axes.titlesize'] = 9
plt.rcParams['axes.labelsize'] = 9
plt.rcParams['xtick.labelsize'] = 8
plt.rcParams['ytick.labelsize'] = 8
plt.rcParams['legend.fontsize'] = 8
plt.rcParams['text.usetex'] = True

def new_figure(height=55):
    "Return figure with width 84mm and given height in mm."

    return plt.figure(figsize=(84/25.4, height/25.4))

def average(array): 
    avg = sum(array) / len(array) 
    return avg

def bubbleSort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]


def insertionSort(arr):

    for i in range(1, len(arr)):

        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key


def merge(arr, l, m, r):
    n1 = m - l + 1
    n2 = r - m

    # create temp arrays
    L = [0] * (n1)
    R = [0] * (n2)
    for i in range(0, n1):
        L[i] = arr[l + i]

    for j in range(0, n2):
        R[j] = arr[m + 1 + j]

    i = 0
    j = 0
    k = l

    while i < n1 and j < n2:
        if L[i] <= R[j]:
            arr[k] = L[i]
            i += 1
        else:
            arr[k] = R[j]
            j += 1
        k += 1

    while i < n1:
        arr[k] = L[i]
        i += 1
        k += 1

    while j < n2:
        arr[k] = R[j]
        j += 1
        k += 1


def mergeSort(arr, l, r):
    if l < r:

        m = l + (r - l) // 2

        mergeSort(arr, l, m)
        mergeSort(arr, m + 1, r)
        merge(arr, l, m, r)


def partition(arr, low, high):
    i = (low - 1)
    pivot = arr[high]

    for j in range(low, high):

        if arr[j] <= pivot:

            i = i + 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return (i + 1)


def quick_sort(arr, low, high):
    if low < high:
        pivot = partition(arr, low, high)
        quick_sort(arr, low, pivot - 1)
        quick_sort(arr, pivot + 1, high)


def py_sort(list):
    return list.sort()


def np_sort(list):
    return np.sort(list)


sorts = [ {
    "name": "Insertion Sort",
    "sort": lambda arr: insertionSort(arr)
}, {
    "name": "Bubble Sort",
    "sort": lambda arr: bubbleSort(arr)
},{
    "name": "Merge Sort",
    "sort": lambda arr: mergeSort(arr, 0, len(arr) - 1)
}, {
    "name": "Quick Sort",
    "sort": lambda arr: quick_sort(arr, 0, len(arr) - 1)
}, {
    "name": "Python Sort",
    "sort": lambda arr: py_sort(arr)
}, {
    "name": "Numpy Sort",
    "sort": lambda arr: np_sort(arr)
}]

array_sizes = np.array([10**i for i in range(1, 5)])



plt.xlabel('Data Size')
plt.ylabel('Time Complexity')

data_frames=list()

repetitions = 10

for sort in sorts:
    times = list()
    start_all = time.clock()
    for i in range(1, 5):
        measurements=list()
        
        for k in range(1,repetitions):
            random_array = np.random.randint(1000, size=10**i)
            start = time.clock()
            sort["sort"](random_array)
            end = time.clock()
            measurements.append(end-start)
            print(sort["name"], "Sort", 10**i, "Elements in", end - start,
              "seconds")
            
        times.append(average(measurements))

            
    end_all = time.clock()
    print(sort["name"], "Sorted Elements in", end_all - start_all, "seconds")
    
    times_df=pd.DataFrame(times,index=array_sizes)
    times_df['Mean']=times_df.mean(axis=1)
    times_df['Std']=times_df.std(axis=1)
    data_frames.append(times_df)

    
    plt.plot(array_sizes, times, label=sort["name"])
    



plt.xscale("log")
plt.yscale("log")
plt.grid()
plt.legend()
plt.figure(figsize=(84/25.4, 55/25.4))
plt.show()
plt.savefig('benchmark_plot_all.pdf')