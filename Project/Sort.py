import time
#swap function
def swap(arr, i, j):
    arr[i], arr[j] = arr[j], arr[i]

# partition function 
def partition(arr, low, high):
    pivot = arr[high]
    i = low - 1

    for j in range(low, high):
        if arr[j] < pivot:
            i += 1
            swap(arr, i, j)

    swap(arr, i + 1, high)
    return i + 1

#Quick Sort implementation
def quickSort(arr, low, high):
    if low < high:
        pi = partition(arr, low, high)
        quickSort(arr, low, pi - 1)
        quickSort(arr, pi + 1, high)

# Bubble sort implementation
def bubbleSort(arr):
    n = len(arr)
    for i in range(n-1):
        swapped = False
        for j in range(n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True
        if not swapped:
            break 
        
# main program 

lst_input = input("Enter numbers separated by spaces: ").split()
numbers = [int(num) for num in lst_input]

choice = int(input("Choose sorting algorithm:\n1. Quick Sort\n2. Bubble Sort\nEnter choice (1 or 2): "))

start_time = time.time()

if choice == 1:
    quickSort(numbers, 0, len(numbers) - 1)
    print("Sorted array using Quick Sort:", numbers)
elif choice == 2:
    bubbleSort(numbers)
    print("Sorted array using Bubble Sort:", numbers)
else:
    print("Invalid choice!")
    exit()

end_time = time.time()
print(f"Time taken to sort: {end_time - start_time} seconds")
